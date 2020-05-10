import numpy as np
from datetime import datetime


def binary_search(inp_array, search_value):
    length_of_array = len(inp_array)
    middle = length_of_array//2
    if inp_array[middle] == search_value:
        return "found"
    else:
        for i in range(0, middle):
            if search_value == inp_array[i] or inp_array[i*-1]:
                return "found"
    return "not found"


def linear(inp_array, search_value):
    length_of_array = len(inp_array)
    for i in range(0, length_of_array):
        if search_value == inp_array[i]:
            return "found"
    return "not found"




inp_array = np.random.randint(0, 10000000, 1000000)
search_value = np.random.randint(0, 1000000)
# inp_array.sort()

start = datetime.now()
result = binary_search(inp_array, inp_array[search_value])
print(result)
print("time taken : ", (datetime.now()-start).total_seconds())

start = datetime.now()
result = linear(inp_array, inp_array[search_value])
print(result)
print("time taken : ", (datetime.now()-start).total_seconds())
