#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    biggest_int = my_list[0]  # intialize biggest_int value inside my_list
    for num in my_list:
        if num > biggest_int:
            biggest_int = num
    return biggest_int
