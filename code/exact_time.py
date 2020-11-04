#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:07:32 2019

@author: hannah
"""

from xml.dom import minidom
from datetime import date
from datetime import datetime
import sys

"""
with open(sys.argv[1], 'r') as f:
    contents = f.read()
"""
contents = sys.argv[1]
documentDate = sys.argv[2]

# parse an xml file by name
mydoc = minidom.parse(contents)
items = mydoc.getElementsByTagName('TIMEX3')

print(contents)
mylist = []
myoutput =[]
precision=[0,0,0,0,0,0,0,0]
timeline=[]
#Store Items in list

#Function to return time value from date
def dateValue(currentDate,dDate):
    
    if (currentDate[0:3] == "XXXX"):
        return 0
    
    currentDate = currentDate.replace("X", "1")
    currentDate = currentDate.replace("TNI", "")
    currentDate = currentDate.replace("SP", "04")
    current = currentDate.split('-')

    if (len(current)==1):
        if (len(currentDate)==2):
            y = int(currentDate)*100
            fdate= datetime(y,1,1)
            print(fdate) 
        elif (len(currentDate)==3):
            y = int(currentDate)*10
            fdate= datetime(y,1,1)
            print(fdate)
        elif (len(currentDate)==4):
            fdate= datetime(int(currentDate),1,1)
            print(fdate) 
    elif (len(current)==2):
        try:
            fdate = datetime(int(current[0]),int(current[1]),1)
            print(fdate)
        except ValueError:
            fdate = datetime(int(current[0]),1,1)
            print(fdate)
    elif (len(current)==3): 
        fdate = datetime.strptime(currentDate, '%Y-%m-%d')
        print(fdate)
    
    ldate = datetime.strptime(dDate, '%Y-%m-%d')
    
    delta = fdate - ldate
    print("days:")
    print(delta.days)
    return delta.days
        
    
   
#Function to return time value from duration

#Store Values in list

for elem in items:
    mylist.append(elem.attributes['value'].value)
   # if elem.attributes['value'].value not in myoutput:
   #     myoutput.append(elem.attributes['value'].value)
        #filling precision list
    if elem.attributes['type'].value == "DATE":
       if elem.attributes['value'].value =="PRESENT_REF" or elem.attributes['value'].value =="PAST_REF" or elem.attributes['value'].value =="FUTURE_REF":
           print("");
       else:
          years = dateValue(str(elem.attributes['value'].value), documentDate)
          timeline.append(years)
                



#Just to print to a file
line = contents + ' ' + documentDate + ' '
for elem in timeline:
       line += str(elem)
       line += ' '  
       
       
#Print list to file 
with open("TimeLine1.txt", "a") as myfile:   
    myfile.write(line + '\n')


    

