import time, sys
import datetime
import board
import neopixel

pixel_pin = board.D12
num_pixels = 60

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

RED = (255, 0, 0)
RED_2 = (64, 0, 0)
RED_3 = (32, 0, 0)
OFF = (0,0,0)

#def clear (pixels):
#    for i in range(num_pixels):
 #       pixels[i] = (0,0,0)
  #      pixels.show()
    
#pixels[1] = (0,0,0)
#pixels.show()
while True:
        pixels.fill(OFF)
        pixels.show()
        now = datetime.datetime.now()
        hourPixel = ((now.hour - 12) * 5) + (now.minute // 12)
        minutePixel = now.minute 
        secPixel = now.second

        hourColor = (255,0,0)
        minuteColor = (0,0,255)
        secColor = (0,255,0)
        overlapColor = (255,0,255)

        pixels[hourPixel] = hourColor
        pixels[minutePixel] = minuteColor
        pixels[secPixel] = secColor
        pixels.show()
        time.sleep(1)
'''
        print(now.hour)
        #print((now.hour % num_pixels))
        print(hourPixel)
        print(minutePixel)
        print(secPixel)
        #time.sleep(1)
'''

'''
while(True):
    #now = datetime.datetime.now()
    #clear(pixels)
    #clock(strip,now)
    for i in range(num_pixels):
        pixels[i] = (0,0,0)
        pixels.show()
        time.sleep(1)
'''
'''
try:
    while True:
        for i in range(num_pixels):
            pixels[i] = RED
            pixels[i-1] = RED_2
            pixels[i-2] = RED_3
            pixels[i-3] = OFF
            #time.sleep(0.1)
            pixels.show()
            time.sleep(0.025)

except KeyboardInterrupt:
            pixels.fill(OFF)
            pixels.show()
            sys.exit()
'''
'''
try:
    while True:
        now = datetime.datetime.now()
        clock(pixels,now)
        time.sleep(0.5)
except KeyboardInterrupt:
            pixels.fill(OFF)
            pixels.show()
            sys.exit()
'''