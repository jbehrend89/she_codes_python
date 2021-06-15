# Q1) Write a program that reads in colours_20_simple.csv and output the colour data

import csv

colours = []

with open("colours_20_simple.csv",encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        # print(line)
        colours.append(line)

# print(colours)

for code in colours:
    print(f"{code[0]} {code[1]} {code[2]}")


