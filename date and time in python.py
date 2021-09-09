#                    Date and Time in python 
# A date in Python is not a data type of its own, but we can import a module named 'datetime' to work with 
# dates as date objects.
#for us be able to use date and time as a module we must import(copy) it into the code
import datetime
today_date=datetime.datetime.now()
print(today_date) 

#To create a date, we can use the 'datetime()' class constructor of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
#  e.g ------date=datetime.datetime(year, month,day)
import datetime
date=datetime.datetime(2020,11,6)
print(date)

#The strftime() Method
#to change the format of the date and time to suit ur preference we use '.strftime()' function to perform dis
#'.strftime()' means string format time. to read up on more 'strftime' reference u can visit "python strftime
#  reference"
import datetime
Date=datetime.datetime(2021,11,6)
print(Date.strftime('%a'))

'''
The following are some '.strftime()' references 
*%a--Weekday, short version                                               result--Wed
*%A--Weekday, full version                                                result--Wednesday
*%w--Weekday as a number 0-6, 0 is Sunday                                 result--3
*%d--Day of month 01-31                                                   result--31
*%b--Month name, short version                                            result--Dec
*%B--Month name, full version                                             result--December
*%m--Month as a number 01-12                                              result--12
*%y--Year, short version, without century                                 result--18
*%Y--Year, full version                                                   result--2018
*%H--Hour 00-23                                                           result--17
*%I--Hour 00-12                                                           result--05
*%p--AM/PM                                                                result--PM
*%M--Minute 00-59                                                         result--41
*%S--Second 00-59                                                         result--08
*%f--Microsecond 000000-999999                                            result--548513
*%z--UTC offset                                                           result--+0100
*%Z--Timezone                                                             result--CST
*%j--Day number of year 001-366                                           result--365
*%U--Week number of year, Sunday as the first day of week, 00-53          result--52
*%W--Week number of year, Monday as the first day of week, 00-53          result--52
*%c--Local version of date and time                                       result--Mon Dec 31 17:41:00 2018
*%x--Local version of date                                                result--12/31/18
*%X--Local version of time                                                result--17:41:00
*%%--A % character                                                        result--%
'''