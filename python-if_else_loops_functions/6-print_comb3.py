#!/usr/bin/python3
for number in range(10):
    for j in range(number + 1, 10):
        if number < 8 or (number == 8 and j < 9):
            print("{:02d}".format(number * 10 + j), end=", ")
        else:
            print("{:02d}".format(number * 10 + j))
