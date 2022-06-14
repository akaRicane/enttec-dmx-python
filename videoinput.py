import cv2
import socketio
import struct
import time
import pickle
import zlib

input_id = 'dev/ttys001'
sio = socketio.Client()
sio.connect('http://localhost:3001')

# @sio.event
# def connect():
#     print('connection established')

# @sio.event
# def disconnect():
#     print('disconnected from server.')

# def get_video(input_id):
#     camera = cv2.VideoCapture(input_id)
#     while True:
#         okay, frame = camera.read()
#         if not okay:
#             break

#         cv2.imshow('video', frame)
#         cv2.waitKey(1)
#     pass

# if __name__ == '__main__':
#     get_video(0)

cam = cv2.VideoCapture(0)

cam.set(3, 320)
cam.set(4, 240)

img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)


    print("{}: {}".format(img_counter, size))
    sio.emit('video', struct.pack(">L", size) + data)
    img_counter += 1

cam.release()