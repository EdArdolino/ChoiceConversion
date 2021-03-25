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

def start():
    print("\n")
    print("Choose which you would like to do:\n 1.) Convert a string from binary\n 2.) Convert a string to binary")
    response = input("Please enter 1 or 2: ")
    while response not in {"1", "2"}:
        response = input("Incorrect input, please enter 1 or 2: ")

# If statement to take binary input
    if response == ("1"):
        string_from_binary()

# If statement to take a string input
    if response == ("2"):
        string_to_binary()

# Ask user if they would like to run the program again
# Automatically converts all answers to lowercase for accessibility
    run_again()

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

# Input to run program again
def run_again():
    more_conversions = input("Would you like to run ChoiceConversion.py again? (y/n): ").lower()
    while more_conversions not in {"y", "n"}:
        more_conversions = input("Incorrect input, please enter y or n: ")

    # If the user enters yes, the program will run again, if not, the program will stop
    if more_conversions == ("y"):
        start()
    elif("n"):
        print("Thank you.")
        exit(0)