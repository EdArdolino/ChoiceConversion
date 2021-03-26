##
# @Author: Ed Ardolino
# @Version 3.0
# @Creation Date: 3-22-2021
##

##
#
# Python program to define all functions that ware used in ChoiceConversion.py
#
##

def start():
    print("\nChoose which you would like to do:\n 1.) Convert binary to a string\n 2.) Convert a string to binary\n")
    response = input("Please enter 1 or 2: ")
    while response not in {"1", "2"}:
        response = input("Incorrect input, please enter 1 or 2: ")

    # If statement to take binary input
    if response == ("1"):
        binary_to_string()

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
def binary_to_string():

    print("You selected: '1.) Convert binary to a string'\n")
    binary_input = input("Binary: ")
    # Conversion that takes the binary input and converts it into a string
    converted = "".join([chr(int(binary, 2)) for binary in binary_input.split(" ")])
    print("The binary conversion is: " + str(converted))
    print("The converted string has been written to a log file.")
    binary_write_to_log(binary_input + " -> " + converted + "\n")

# Input is converted and written to a file
def string_to_binary():
    print("You selected: '2.) Convert a string to binary'\n")
    string_input = input("String: ")
    # Conversion that takes the string input and converts it into binary
    converted = ' '.join(format(ord(i), '08b') for i in string_input)
    print("\nThe converted string is: " + str(converted))
    print("The converted string has been written to a log file.")
    string_write_to_log(string_input + " -> " + converted + "\n")

# Input to  ask about running the program again
def run_again():
    more_conversions = input("\nWould you like to run ChoiceConversion.py again? (y/n): ").lower()
    while more_conversions not in {"y", "n"}:
        more_conversions = input("Incorrect input, please enter y or n: ")

    # If the user enters yes, the program will run again, if not, the program will stop
    if more_conversions == ("y"):
        start()
    elif("n"):
        print("\nThank you.\n")
        exit(0)