##
# @Author: Ed Ardolino
# @Version 1.0
# @Creation Date: 3-22-2021
##

##
#
# Python program to define all functions that ware used in ChoiceConversion.py
#
##

# Function created to write the conversion to a file named 'Binary Conversion(s)'
def binary_write_to_log(string):

    with open("Binary Conversion(s).txt", "a") as file:
        file.writelines(str(string))

# Function created to write the conversion to a file named 'String Conversion(s)'
def string_write_to_log(string):

    with open("String Conversion(s).txt", "a") as file:
        file.writelines(str(string))

# Input is converted and written to a file        
def string_from_binary():
    print("Currently in development")
    exit(0)

    print("You selected: '1.) Convert a string from binary'")
    binary_input = input("Binary: ")
    print("The binary conversion is: " + str(converted))

    # To be used later when full conversion is working
    #binary_write_to_log(converted)

# Input is converted and written to a file
def string_to_binary():
    print("You selected: '2.) Convert a string to binary'")
    string_input = input("String: ")
    converted = ''.join(format(ord(i), '08b') for i in string_input)
    print("The converted string is: " + str(converted))
    print("The converted string has been written to a log file.")
    string_write_to_log(string_input + " -> " + converted + "\n")

def run_again():

    more_conversions = input("Would you like to run ChoiceConversion.py again? (y/n): ").lower()
    while more_conversions not in {"y", "n"}:
        more_conversions = input("Incorrect input, please enter y or n: ")

    if more_conversions == ("y"):
        print("Work in progress.")
        exit(0)
    elif("n"):
        print("Thank you.")