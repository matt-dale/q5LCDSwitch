# a test script using the command line
import sys
from q5Class import *

spi = setupSPI(0,0)
Q5 = Q5LCDController(spi)

Q5.clearScreen()
sleep(0.25)

try:
	aString = sys.argv[1] # no spaces
	aColor = sys.argv[2]
except:
	print 'no args given'

if aColor:
	Q5.changeColor(aColor)

if aString:
	Q5.writeAString(aString)
	Q5.writeAString(aString)
	Q5.writeAString(aString)

sleep(1)
	
