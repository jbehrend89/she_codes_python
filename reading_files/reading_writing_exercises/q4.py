# Q4) Using the same colour csv files, write a program that outputs the number of times each of the following
# colours appear in the English Name:
# ● red
# ● green
# ● blue

import csv

colours = []

with open("colours_20.csv",encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        # print(line)
        colours.append(line)

# print(colours)

