
#!/usr/bin/python

import os
import time
 
# Define Axis Channels (channel 3 to 7 can be assigned for more buttons / joysticks)
swt_channel = 23
vrx_channel = 15
vry_channel = 18
 
#Time delay, which tells how many seconds the value is read out
delay = 0.5
 

 
 
# endless loop
while True:
 
  # Determine position
  vrx_pos = (vrx_channel)
  vry_pos = (vry_channel)
 
  # SW determine
  swt_val = (swt_channel)
 
  # output
  print("VRx : {}  VRy : {}  SW : {}".format(vrx_pos,vry_pos,swt_val))
 
  # wait
  time.sleep(delay)
  
