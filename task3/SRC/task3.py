import os
import glob

input_directory = input(r"directoy: ")    # absolute path to files
path = glob.glob(input_directory+os.sep+'*.txt')

cashbox = []
for p in path:
    with open(p) as f:
        reader = f.readlines()
        temporary_list = [float(r) for read in reader for r in read.split()]
        cashbox.append(temporary_list)

intervals = []
for x in range(16):
    count = cashbox[0][x] + cashbox[1][x] + cashbox[2][x] + cashbox[3][x] + cashbox[4][x]
    intervals.append(count)

print(intervals.index(max(intervals))+1)    # printing interval from 1 to 16
