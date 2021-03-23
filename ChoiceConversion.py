import ChoiceFunctions
##
# @Author: Ed Ardolino
# @Version 2.0
# @Creation Date: 3-22-2021
##

##
#
# Python converter that gives the option of converting a binary input to a string, and converting a string input into binary
#
##

# When the program is run, a string is printed asking the user to select the operation they would like to perform.
# Error checking is performed to make sure the user enters option given by the print statement
print("\n")
print("Choose which you would like to do:\n 1.) Convert a string from binary\n 2.) Convert a string to binary")
response = input("Please enter 1 or 2: ")
while response not in {"1", "2"}:
    response = input("Incorrect input, please enter 1 or 2: ")

# If statement to take binary input
if response == ("1"):
    ChoiceFunctions.string_from_binary()

# If statement to take a string input
if response == ("2"):
    ChoiceFunctions.string_to_binary()

# Ask user if they would like to run the program again
# Automatically converts all answers to lowercase for accessibility

ChoiceFunctions.run_again()
