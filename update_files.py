import shutil
import time
import os
os.chdir('/home/pi/Desktop/autoUpdate')
timer = .5
while True:
	shutil.copy2('testData/bulletdata1.json', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata2.json', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata3.json', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata4.json', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata5.json', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata6.json', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata7.json', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata8.json', 'bulletdata.json')
	time.sleep(timer)
