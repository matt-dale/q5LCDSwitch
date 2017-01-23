# q5LCDSwitch
testing Python for use with the Q5 switch

Only tested with the Raspberry Pi 3 with Raspbian Lite OS.  

While the library "works", the timing of the Python sleep() function isn't as accurate as neccessary to repeatedly send commands.
So commands to change colors work fine, but the "writeAString" methods don't always work well.  

The Pi 3 clock has a ring, which makes the Q5 to not respond or respond incorrectly.  
The ring needs to be filtered out with a resistor/capacitor (RC) filter. 

The font supplied in q5Font.py was created experimentally. There are a few letters that don't look great, but for a proof of concept, it gets the point across.
