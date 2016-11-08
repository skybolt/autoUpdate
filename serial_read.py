#!/usr/bin/python
# get lines of text from serial port, save them to a file

from __future__ import print_function
import serial, io
import time

addr  = '/dev/ttyS0'  # serial port to read data from
baud  = 57600            # baud rate for serial port
fname = 'bulletdata.txt'   # log file to save data in
fmode = 'w'             # log file mode = append

while (1):
	with serial.Serial(addr,baud) as pt, open(fname,fmode) as outf:
		spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
			encoding='ascii', errors='ignore', newline='\r',line_buffering=True)
		# spb.readline()  # throw away first line; likely to start mid-sentence (incomplete)
		x = spb.readline()  # read one line of text from serial port
		#print (x,end='')    # echo line of text on-screen
		outf.write(x)       # write line of text to file
		outf.flush()        # make sure it actually gets written out
		fn = open("bulletdata.json","w")
		fn.write(x)
		fn.flush()
		fn.close()
		pt.close()

