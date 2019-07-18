import os
try:
    input_path = input(r"path: ")    # absolute path to file
    base_path = os.path.normpath(input_path)
    with open(base_path) as f:
        reader = f.readlines()
except FileNotFoundError:
    print(r'you must write absolute path like: "D:\Users\Voldemort\*.txt"')


temporary_list = [r for read in reader for r in read.split()]
filtered_list = [lis.replace(':', '') for lis in temporary_list]
sorted_list = [int(sort) for sort in filtered_list]


hours = [hour for hour in range(800, 2100, 100)]
divided_hours = [[], [], [], [], [], [], [], [], [], [], [], []]
for numb in range(12):
    for element in sorted_list:
        if hours[numb + 1] > element > hours[numb]-1:
            divided_hours[numb].append(element)


visitor_hourly = [len(items) for items in divided_hours]
index_of_max = visitor_hourly.index(max(visitor_hourly))
list_copy = sorted(divided_hours[index_of_max]).copy()  # Fix me


def final(tmp_list):
    '''

    :param tmp_list: list consisting integers
    :return: concatenated with ':' list objects of str type
    '''
    tmp = []
    for item in tmp_list:
        it = str(item)
        if len(it) > 3:
            it = it[0:2]+':'+it[2:]
            tmp.append(it)
        else:
            it = it[0:1]+':'+it[1:]
            tmp.append(it)
    return tmp[0]+' '+tmp[-1]


print(final(list_copy), '\n')
