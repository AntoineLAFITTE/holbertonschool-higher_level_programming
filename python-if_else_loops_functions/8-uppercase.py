#!/usr/bin/python3
def uppercase(str):
    uppercased_string = ""
    for c in str:
        if 'a' <= c <= 'z':
            uppercased_string += chr(ord(c) - 32)
        else:
            uppercased_string += c
    print("{}".format(uppercased_string))
