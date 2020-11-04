#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:07:32 2019

@author: hannah
"""

from xml.dom import minidom
import sys

"""
with open(sys.argv[1], 'r') as f:
    contents = f.read()
"""
contents = sys.argv[1]
# parse an xml file by name
mydoc = minidom.parse(contents)
items = mydoc.getElementsByTagName('TIMEX3')


mylist = []
myoutput =[]
precision=[0,0,0,0,0,0,0,0,0]
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
        print((elem.firstChild.data.replace('\n', ' ')))
        if "CE" in elem.attributes['value'].value:
                temp = precision[8]
                precision[8]=temp+1
        elif "DE" in elem.attributes['value'].value:
                temp = precision[7]
                precision[7]=temp+1
        elif "Y" in elem.attributes['value'].value:
                temp = precision[6]
                precision[6]=temp+1
        elif "M" in elem.attributes['value'].value:
                temp = precision[5]
                precision[5]=temp+1
        elif "D" in elem.attributes['value'].value:
                temp = precision[4]
                precision[4]=temp+1
    if elem.attributes['type'].value == "DATE":  
            if elem.attributes['value'].value=="FUTURE_REF":
                temp = precision[2]
                precision[2]=temp+1
            elif elem.attributes['value'].value=="PRESENT_REF":
                temp = precision[0]
                precision[0]=temp+1
            elif elem.attributes['value'].value=="PAST_REF": 
                temp = precision[1]
                precision[1]=temp+1
            else: 
                temp = precision[3]
                precision[3]=temp+1
                

#Just to print to a file
line = contents + ' '
for elem in precision:
       line += str(elem)
       line += ' '  
       
#Print list to file 
with open("results_test", "a") as myfile:   
    myfile.write(line + '\n')


    

