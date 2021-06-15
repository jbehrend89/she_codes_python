# Q3) Write a program that reads in colours_20.csv and output the colour data in order English, Hex then RGB.

import csv

colours = []

with open("colours_20.csv",encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        # print(line)
        colours.append(line)

# print(colours)

i = 1
while i < len(colours):
    print(f"{colours[i][4]}, Hex: {colours[i][2]}, RGB: {colours[i][1]}")
    i = i + 1


