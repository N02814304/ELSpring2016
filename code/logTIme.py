import time
import csv
csvout = open('mycsv.csv', 'wb')
mywriter = csv.writer(csvout)
def logTime():
	myList = []
	for i in range(0,5):
		xdate = time.strftime("%Y/%m/%d")
		xtime = time.strftime("%H:%M:%S")
		myList.append([xdate, xtime])          	
 		time.sleep(3)
	print myList
        for row in zip(myList):
		mywriter.writerow(row)	
logTime()
csvout.close()


