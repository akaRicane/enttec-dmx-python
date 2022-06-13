import os, sys
import socketio

sys.path.append(os.getcwd())
from dmxlib.DxmUniverse import DmxUniverse

# instanciate socket
sio = socketio.Client()

# instanciate universe
universe = DmxUniverse('/dev/tty.usbserial-EN305173')

# add light to universe (start dmx channel & n-channels)
universe.addLight(1, 4)

@sio.event
def connect():
    print('connection established')


@sio.on('dmx-request')
def handle_dmx_query(dmx_query):
    print(f"{dmx_query=}")
    dimmer = dmx_query['dimmer']
    red = dmx_query['r']
    green = dmx_query['g']
    blue = dmx_query['b']
    universe.setValuesOfLight(0, [dimmer, red, green, blue])
    universe.render(duration=0.1)


@sio.on('mouse')
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.event
def disconnect():
    print('closing lights')
    universe.closeSession()
    print('disconnected from server.')
    # close


sio.connect('http://localhost:3001')
sio.wait()
