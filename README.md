

This is based on contributions from mutliple authors, originally based on a chart example from d3js.org. Modified primarly to accept a json file from https://github.com/skybolt/Tavi_165_Mpguino/tree/master. 

Requires editing of seral_read.py python script to pull from correct serial port at the correct speed. You will have to set up automatically calling serial_read.py (by placing 'python serial_read.py' or 'python serial_read.py &' in the appropriate startup script. Once you do, then load index.html in a browser capable of doing the incredibly insecure function of calling a remote javascript object from d3js.org (or a local copy of it) together with reading data from a local json file. Chrome refuses to do this without command-line disabling of well-functioning security safeguards, Firefox might, and Iceweasel worked well until it was updated. As long as these programs are used for the limited purpose of reading arduino data and presenting it in a browser there should be little risk. If you modify this code to read your bank data, for example, you do so at your own risk. This can work on a desktop running linux or MacOS and firefox, reading the serial output from your arduino connected via USB, but will reset your arduino on each connect. So, you may wish to use the included test data, which can be updated by calling the update_files.py python script. 

--below is original readme from raided source file --

This is a Bullet Chart example that allows the user to update the chart automatically by updating the `bulletdata2.json` file. This (online) example won't change, but if you download the file and read in conjunction with d3noob.org you will be able to impliment your own dynamic chart with it.

This is a follow on from the [example](http://bl.ocks.org/d3noob/5886992) that updated the charts with random data.
