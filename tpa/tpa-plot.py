# tpa-plot.py -- Daniel J. Breton -- 12 Jan 2020

import numpy as np
import matplotlib.pyplot as plt

# specify path to data file
path = 'C:\\Users\\rdcrldjb\\Documents\\cktPython\\jrscilg-master\\tpa\\'
fname = 'uphill_data.csv'
fpath = path+fname

# open file and store data into arrays:
# time (sec), temp (C), press (hPa) and altitude (m)
print("Opening %s..." % fpath)
time,temp,press,alt = np.loadtxt(fpath, delimiter=',', unpack=True, skiprows=1)

# fix an "oops" in the data, which starts at second 776 by mistake
time = time - 776  # subtracts 776 from all time values... so data will start at time=0

# plot the data.  
plt.plot(time/60.0, press)  # convert time into minutes to make plot easier to interpret

# label the axes
plt.xlabel('Elapsed time, min')
plt.ylabel('Pressure, hPa')

# make a title
plt.title('Air pressure during ascent of Lyme Hill, 11 Jan 2020')

# show the plot in an interactive window
plt.show()
