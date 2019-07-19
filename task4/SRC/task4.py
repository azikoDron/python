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


def two_max_indexes(tmp_list: list):
    '''

    when sequence is important!
    find max element index in list and return tuple of one index
    if two max elements in list return tuple of both indexes
    :param tmp_list: list
    :return: tuple
    '''
    first_max_index = tmp_list.index(max(tmp_list))
    second_max_index = first_max_index + tmp_list[first_max_index + 1:].index(max(tmp_list[first_max_index + 1:])) + 1
    if tmp_list[first_max_index] == tmp_list[second_max_index]:
        return first_max_index, second_max_index
    return first_max_index,


visitor_hourly = [len(items) for items in divided_hours]    # +++++++++
for indexes in two_max_indexes(visitor_hourly):
    list_copy = sorted(divided_hours[indexes]).copy()  # Fix me
    print(final(list_copy), '\n')
