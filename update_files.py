import shutil
import time
timer = .5
while True:
	shutil.copy2('testData/bulletdata1.txt', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata2.txt', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata3.txt', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata4.txt', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata5.txt', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata6.txt', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata7.txt', 'bulletdata.json')
	time.sleep(timer)
	shutil.copy2('testData/bulletdata8.txt', 'bulletdata.json')
	time.sleep(timer)
