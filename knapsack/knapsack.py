#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    max_value = (0, 0, [0, 0, 0])
    for i in range(len(items)):
        arr_values = []
        item1 = items[i]
        # item1 = item1_tuple.1
        for j in range(len(items)):
            if items[i] is not items[j]:
                item2 = items[j]
                # item2 = item2_tuple.1
                for k in range(len(items)):
                    if items[k] is not items[i] and items[k] is not items[j]:
                        item3 = items[k]
                        total_value = item1[2] + item2[2] + item3[2]
                        total_size = item1[1] + item2[1] + item3[1]
                        item = (total_size, total_value, [item1[0], item2[0], item3[0]])
                        if total_size <= capacity:
                            arr_values.append(item)
        for l in range(len(arr_values)):
            if arr_values[l][1] > max_value[1]:
                max_value = arr_values[l]
    return {'Value': max_value[1], 'Chosen': max_value[2]}



if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')