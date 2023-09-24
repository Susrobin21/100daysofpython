#with open('weather_data.csv') as dfile :
    #data = dfile.readlines()
    #print(data)

import csv
with open('weather_data.csv') as dfile :
    data = csv.reader(dfile)
    for line in data :
        print(line)
    #To print a seperate value such as temperature, use indexing like
    for temp in data :
        print(temp[1])

#instead use pandas
import pandas as pd
data = pd.read_csv('weather_data.csv')
print(data['temp'])