def uppercase(str):
    for char in str:
        # Check if character is lowercase (ASCII between 97 et 122)
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from the ASCII value
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        # Print the character without a newline, and continue the loop
        print("{}".format(upper_char), end="")
    # Print a newline after the string is printed
    print()
