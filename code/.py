# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:24:25 2020

@author: hjbec
"""



from xml.dom import minidom
from datetime import datetime as dt
from datetime import timedelta
import sys
import re

"""
with open(sys.argv[1], 'r') as f:
    contents = f.read()
"""
contents = sys.argv[1]
# parse an xml file by name
mydoc = minidom.parse(contents)
items = mydoc.getElementsByTagName('TIMEX3')
date = sys.argv[2]
date_time = dt.strptime(date, '%Y-%m-%d')
print(date_time)
date_time_string = str(date_time).split(" ")
print(date_time_string[0])

document = contents.split("-")
year = document[1].replace(".txt","")
print(year)
mylist = []
myoutput =[]
precision=[]
start_date=[]
#Store Items in list
"""
for elem in items:
    mylist.append(elem.firstChild.data.replace('\n', ' '))
    if elem.firstChild.data not in myoutput:
        myoutput.append(elem.firstChild.data.replace('\n', ' '))

"""
#Store Values in list

print("Processing... " + contents)

for elem in items:
    #print(elem)
    mylist.append(elem.attributes['value'].value)
   # if elem.attributes['value'].value not in myoutput:
   #     myoutput.append(elem.attributes['value'].value)
        #filling precision list
    if elem.attributes['type'].value == "DURATION":
        if "CE" in elem.attributes['value'].value:
            try:
                temp =  int(re.sub("[^0-9]", "", elem.attributes['value'].value ))
                precision.append(temp*36500)
                start_date.append(date_time_string[0])
            except ValueError:
                    print("CEXD skipped")
        elif "DE" in elem.attributes['value'].value:
            try:
                temp =  int(re.sub("[^0-9]", "", elem.attributes['value'].value ))
                precision.append(temp*3650)
                start_date.append(date_time_string[0])
            except ValueError:
                print("PXDE Skipped")
        elif "Y" in elem.attributes['value'].value:
             try:
                 temp =  int(re.sub("[^0-9]", "", elem.attributes['value'].value ))
                 precision.append(temp*365)
                 start_date.append(date_time_string[0])
             except ValueError:
                 print("PXY skipped")
        elif "M" in elem.attributes['value'].value:
            try:
                temp =  int(re.sub("[^0-9]", "", elem.attributes['value'].value ))
                precision.append(temp*30)
                start_date.append(date_time_string[0]) 
            except ValueError:
                print("PXM Skipped")
        elif "D" in elem.attributes['value'].value:
             try:
                temp =  int(re.sub("[^0-9]", "", elem.attributes['value'].value ))
                precision.append(temp)
                start_date.append(date_time_string[0])
             except ValueError:
                print("PXY skipped")
    if elem.attributes['type'].value == "DATE":  
     
            if elem.attributes['value'].value=="FUTURE_REF":
                precision.append(1)
                start_date.append(date_time_string[0])
          
            elif elem.attributes['value'].value=="PRESENT_REF":
                temp = 1
                precision.append(temp) # appends things like now
                start_date.append(date_time_string[0])
            elif elem.attributes['value'].value=="PAST_REF": 
                temp = 1
                precision.append(temp)
                start_date.append(date_time_string[0])
            else:
                date_referenced = elem.attributes['value'].value.split("-")
                if len(date_referenced)==3:
                    precision.append(1)
                    start_date.append(elem.attributes['value'].value)
                elif len(date_referenced)==2:
                    if "SU" in elem.attributes['value'].value:
                        precision.append(90)
                        start_date.append(str(date_referenced[0]+"-06-21"))
                    if "SP" in elem.attributes['value'].value:
                        precision.append(90)
                        start_date.append(str(date_referenced[0]+"-03-21"))
                    if "FA" in elem.attributes['value'].value:
                        precision.append(90)
                        start_date.append(str(date_referenced[0]+"-09-21"))
                    if "WI" in elem.attributes['value'].value:
                        precision.append(90)
                        start_date.append(str(date_referenced[0]+"-12-21"))
                    elif "W" in elem.attributes['value'].value:
                        temp = elem.attributes['value'].value.replace("W","")
                        day = int(temp[1])
                        start = date_time - timedelta(7*day)
                        date_new = str(start).split(" ")
                        start_date.append(date_new[0])
                        precision.append(1)
                elif len(date_referenced)==1:
                    if len(date_referenced[0]) == 4:
                        precision.append(365)
                        start_date.append(elem.attributes['value'].value+ "-01-01")
                    elif len(date_referenced[0]) == 2:
                        precision.append(365*100)
                        start_date.append(elem.attributes['value'].value+ "00-01-01")

#Just to print to a file
line = "start date \t precision \n"
for i in range(0,len(precision)):
       line += str(start_date[i]) + "\t" + str(precision[i])
       line += '\n'  
       
#Print list to file 
horizons = "horizons_new/" + year + ".txt"     
with open(horizons, "w") as myfile:   
    myfile.write(line + '\n')