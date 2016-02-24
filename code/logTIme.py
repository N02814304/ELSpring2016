# I wrote the date and time as a single string to a csv file, 'mycsv'. The time was recorded 5 fives every three seconds.
# After writing the data to the csv file, I opened up sqlite and created a database using the data in the csv file. 
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


