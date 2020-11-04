# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:05:03 2020

@author: hjbec
"""



#import plotly.express as px
import pandas as pd
import sys
import datetime

f1 = sys.argv[1]



dates_list = []
horizons_list = []

df = pd.DataFrame([])
datehorizons = {}
lines = []

with open(f1, "r") as file:
    lines = file.readlines()


#set max and min dates to document dates

    
count = 0  

dictionary_horizons = {}

# find mindate and maxdate of document    
for line in lines:
  try:  
      if not "start date" in line: 
          dates = line.split("\t") #get the date from the line
          date_fine = dates[0].split("-")
          start_date = datetime.date(int(date_fine[0]), int(date_fine[1]), int(date_fine[2]))
          delta = int(dates[1]) # get the number of days from the line
          time_delta = datetime.timedelta(days = delta)
          end_date = start_date + time_delta # get the end date from the line
          count += 1 # just a counter
          
          #populate list with dates 
          for i in range (delta + 1): # for each day in the range         
              day = start_date + datetime.timedelta(days=i) 
              h = float(1/delta)           
              if day.strftime("%Y-%m-%d") in dates_list:
                  ind = dates_list.index(day.strftime("%Y-%m-%d"))
                  horizons_list[ind] =  horizons_list[ind] + h
                 
              else:
                 dates_list.append(day.strftime("%Y-%m-%d"))
                 horizons_list.append(h)
                  
  except ValueError:
      print("Error on line " + str(count))
    
print(len(dates_list))#print(len(horizons_list))

dictionary = dict(zip(dates_list, horizons_list))
dates_list.sort()

"""
the_dict = {'dates': dates_list, 'horizons': horizons_list}
df = pd.DataFrame(the_dict)
df.sort_values(by=dates_list)



df.tocsv(path_or_buf=output_file,sep="\t")
"""
output_file = "density/" + f1 
with open(output_file, "w") as f2:
    for i in dates_list:
        f2.write(i + "\t" + str(dictionary[i]) + "\n")


#fig = px.bar(dates_list, y=horizons_list)
#fig = px.bar(df, x='dates',y='horizons')
#fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
#fig.show()    