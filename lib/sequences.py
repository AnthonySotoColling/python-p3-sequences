#!/usr/bin/env python3

def print_fibonacci(length):
    list = [0,1]
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print(list)
        return
    for n in range(2,length):
        list.append(list[n-1]+list[n-2])
    print(list)