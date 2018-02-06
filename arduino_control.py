from db import retrieve_data
import time
from pyfirmata_trans import *

brightness = 0
db_file = "./database.db"

while(1):
	cur_min = retrieve_data(db_file, 0)
	cur_max = retrieve_data(db_file, 1)
	print ('Debug msg: MIN: [{0}], MAX: [{1}] @ Arduino ctrl'
		.format(cur_min, cur_max))

	# temp val for testing
	brightness = (cur_min + cur_max)/200
	print ('Debug msg: Brightness: [{0}]'.format(brightness))
	control(brightness)

	# refresh rate to be adjusted
	time.sleep(0.1)



# brightness = 0

# while (1):
# 	txt = audioToText()
# 	brightness = control(txt, brightness)
# 	print 'Current Brightness: ', brightness