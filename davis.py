import calendar
import time 

yy=int(input('enter a year:'))
mm=int(input('enter a month:'))
print (calendar.month(yy,mm))

print ('we are on ' + str(time.asctime()))