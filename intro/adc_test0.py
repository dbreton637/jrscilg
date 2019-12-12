# adc_test0.py
# example reading of ADC on pin A1 of # circuit playground express
# Daniel J. Breton, 10 DEC 2019

import analogio
import digitalio
from board import *

# define adc averaging function
def avgn(n):
    L = 0.0 # initialize accumulator
    for i in range(0,n):
        L += adc.value
    return L/n  # return average

# define calibration factor K [mV/bit]:
# reference voltage = 3300 mV
# ADC resolution 16 bits
K = (3300 / 2**16) * 0.992  # theoretical value is about 0.8% too high 

# set up analog-to-digital converter instance for cpx pin A1
adc = analogio.AnalogIn(A1)

# print reference voltage and wait...
print("ADC Reference Voltage = %1.2f V" % adc.reference_voltage)
input("Hit enter to start measurements.")

while True:
    # read ADC values
    v = avgn(1000)  # 1000 recommended for mV accuracy

    # send results of measurement to serial terminal
    print(v, K*v, 100*v/2**16,"%")  # mean ADC code and measured voltage in mV
