import csv
import getter
import os, sys, time

list = []

with open("companyCodes.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        list.append(line[0])

for company in list:
	getter.getit(company)
	#time.sleep(1)


