# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:05:03 2020

@author: hjbec
"""



import plotly.express as px
import pandas as pd
import sys
import datetime

file = sys.argv[1]
docdate = sys.argv[2]

df = pd.DataFrame([])
datehorizons = {}
lines = []

with open(file, "r") as file:
    lines = file.readlines()


#set max and min dates to document dates
date_fine = docdate[0].split("-")
maxdate = datetime.date(int(date_fine[0]), int(date_fine[1]), int(date_fine[2]))
mindate = datetime.date(int(date_fine[0]), int(date_fine[1]), int(date_fine[2]))
    
count = 0  



# find mindate and maxdate of document    
for line in lines:
  try:  
      if not "start date" in line: 
          dates = line.split("\t")
          date_fine = dates[0].split("-")
          start_date = datetime.date(int(date_fine[0]), int(date_fine[1]), int(date_fine[2]))
          delta = int(dates[1])
          timedelta = datetime.timedelta(days = delta)
          end_date = start_date + timedelta
          if end_date > maxdate:
              maxdate = end_date
          if start_date < mindate:
              mindate = start_date        
          count += 1
          #populate dictionary with dates
          for i in range (timedelta.days + 1):
              day = mindate + timedelta(days=i)
              datehorizons.update({day:float(1/delta)})
  except ValueError:
      print("Error on line " + str(count))
    
#print(df.sample(5))

#populate dictionary with dates
difference = maxdate-mindate

dates = []
horizons = []
for key in datehorizons:
    dates.append(key)
    horizons.append(datehorizons[key])


the_dict = {'dates': dates, 'horizons': horizons}

fig = px.bar(the_dict, x='dates',y='horizons')
#fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()    