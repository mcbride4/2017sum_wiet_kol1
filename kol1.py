#Flight simulator. Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction. 
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
import random
import time

def find_tilt():
	return random.gauss(0, 1)

def correct_tilt(current_orientation, tilt_correction, maximum=0.3):
	if abs(tilt_correction - current_orientation) <= maximum:
		current_orientation += tilt_correction
		tilt_corrected = tilt_correction
	else:
		if tilt_correction > 0:
			tilt_corrected = maximum 
		else:
			tilt_corrected = -maximum
		current_orientation = current_orientation + tilt_corrected

	print "tilt correction: " + str(tilt_correction)
	print "current orientation: " + str(current_orientation)
	print "tilt corrected: " + str(tilt_corrected)
	print "\n"
	return current_orientation

orient = 0
while(True):
	tilt = find_tilt()
	orient = correct_tilt(orient, tilt)
	time.sleep(0.5)
