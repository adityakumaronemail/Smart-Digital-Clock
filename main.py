from sense_hat import SenseHat
import time
import datafile

sense = SenseHat()
sense.set_rotation(270)
sense.clear()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)

while True:
  
  #print location and time
  sense.show_message(str(datafile.name),0.1,yellow)
  sense.show_message(str(datafile.times),0.1,cyan)
  
  #temperature
  sense.show_message(str(datafile.tempinc),0.1,blue)
  
  #weather
  sense.show_message(str(datafile.condtn),0.1,green)
  time.sleep(5)
