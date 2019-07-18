import os
input_path = input(r" ")  # absolute path to file
base_path = os.path.normpath(input_path)

with open(base_path) as f:
    reader = f.readlines()

temporary_list = [float(r) for read in reader for r in read.split()]
sorted_list = sorted(temporary_list)


def percentile(iterable, percent):
    tmp = int(round(percent * len(iterable) + 0.5))
    if tmp > 1:
        return iterable[tmp-2]
    return iterable[0]


def median(n: list):
    '''

    :param n: is eny iterable
    :return: index of iterable that equals to median
    if it is 2 items than 1x+2x/2
    '''
    length = len(n)
    if length % 10 == 0:
        bl = (n[int(length / 2)] + n[int(length / 2 - 1)]) / 2
        return bl
    return n[int(length / 2)]


print("%.2f" % percentile(sorted_list, 0.9), '\n')
print("%.2f" % median(sorted_list), '\n')
print("%.2f" % sorted_list[-1], '\n')
print("%.2f" % sorted_list[0], '\n')    # {"%.2f"%} or {int(n*100)/100} :both non eficient
