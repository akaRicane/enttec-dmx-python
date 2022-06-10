import os, sys

sys.path.append(os.getcwd())
from dmxlib.DxmUniverse import DmxUniverse

# instanciate universe
universe = DmxUniverse('/dev/tty.usbserial-EN305173')

# add light to universe (start dmx channel & n-channels)
universe.addLight(1, 4)
universe.addLight(5, 4)

# set values to channels of queried light
universe.setValuesOfLight(0, [10, 0, 255, 255])
universe.setValuesOfLight(1, [255, 0, 255, 255])

# render universe
universe.render(duration=2)

# close
universe.closeSession()
