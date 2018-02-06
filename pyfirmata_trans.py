import pyfirmata
from os import system 

DELAY = 2 # A 2 seconds delay

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/tty.usbmodem1421' # hardcoded
print ('Opening Port')

# Creates a new board 
board = pyfirmata.Arduino(PORT)
print ('Board Connected')

pin = board.get_pin('d:11:p')

def control (brightness):
	pin.write(brightness)
