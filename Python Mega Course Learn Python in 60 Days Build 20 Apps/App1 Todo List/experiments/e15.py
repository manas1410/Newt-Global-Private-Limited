#1
import csv
import glob

myfiles = glob.glob("files15/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())


#2

with open("files15/weather.csv") as file:
    data = list(csv.reader(file))
    print(data)
city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])

#3

import shutil
shutil.make_archive("output","zip","files15")

#4

import webbrowser
user_term = input("Enter a search term: ")
webbrowser.open("http://google.com/search?q="+user_term)