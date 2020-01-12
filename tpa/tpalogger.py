# BPM280 temperature and pressure logger
# Daniel J. Breton, 11 Jan 2020

import time
import board
# import digitalio # For use with SPI only
import busio
import adafruit_bmp280
from adafruit_circuitplayground.express import cpx

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# OR create library object using our Bus SPI port
#spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
#bmp_cs = digitalio.DigitalInOut(board.D10)
#bmp280 = adafruit_bmp280.Adafruit_BMP280_SPI(spi, bmp_cs)

# change this to match the location's pressure (hPa) at sea level
# find this number locally at
# https://forecast.weather.gov/MapClick.php?lat=43.81040000000007&lon=-72.15544999999997#.XhnlGuF7k5k
bmp280.sea_level_pressure = 1018.9  # mb = hPa

sup = time.time()  # startup time, seconds since epoch

while True:
    cpx.red_led = True  # turn on red led while collecting data
    cpx.play_tone(1000,0.10)  # beep!

    # open up a file for data storage
    fh = open("data.txt","a")  # "a" is for append
    
    #get current time
    now = time.time()

    # build output string
    str = "%d,%0.1f,%0.1f,%0.2f\n" % (now-sup, bmp280.temperature,bmp280.pressure,bmp280.altitude)
    #print(str) # debug
    
    # turn off red led to let user know it is safe to turn off power
    cpx.red_led = False

    # write output string to file
    fh.write(str)
    # close file to avoid file corruption
    fh.close()
        
    # pause inbetween measurements
    time.sleep(60)  # 60 sec = 1 min

