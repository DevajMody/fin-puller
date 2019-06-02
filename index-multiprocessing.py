import csv
import getter
import os, sys, time
import multiprocessing

list = []

with open("companyCodes.csv", "r") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        list.append(line[0])

def spawn(company):
	getter.getit(company)

if __name__ == '__main__':
    number_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(number_processes)
    total_tasks = len(list)
    tasks = list
    results = pool.map_async(spawn, tasks)
    pool.close()
    pool.join()
