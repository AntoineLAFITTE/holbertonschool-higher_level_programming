#!/usr/bin/python3
def islower(c):
    # Get ASCII value
    ascii_value = ord(c)
    if ascii_value >= 97 and ascii_value <= 122:
        return True
    else:
        return False
