
##
# @Author: Ed Ardolino
# @Version 1.0
# @Creation Date: 3-22-2021
##

##
#
# Python converter that gives the option of converting a binary input to a string, and converting a string input into binary
#
##

# When the program is run, a string is printed asking the user to select the operation they would like to perform.
# Error checking is performed to make sure the user enters option given by the print statemnt
print("Choose which you would like to do?\n 1.) Convert a string from binary\n 2.) Convert a string to binary")
response = input("Please enter 1 or 2: ")
while response not in {"1", "2"}:
    response = input("Incorrect input, please enter 1 or 2: ")


# Function created to write the conversion to a file named 'Binary Conversion(s)'
def binary_write_to_log(string):

    with open("Binary Conversion(s).txt", "a") as file:
        file.writelines(str(string))

# Function created to write the conversion to a file named 'String Conversion(s)'
def string_write_to_log(string):

    with open("String Conversion(s).txt", "a") as file:
        file.writelines(str(string))


#def string_write_to_log(string):
    #with pd.ExcelWriter(r'C:\Users\ardolinoe\Documents\Python\ChoiceConversion\StringConversions.xlsx') as writer:
        #return

        

# If statement to take binary input
# Input is converted and written to a file
if response == ("1"):
    print("Currently in development")
    exit(0)

    print("You selected: '1.) Convert a string from binary'")
    binary_input = input("Binary: ")
    print("The binary conversion is: " + str(converted))

    # To be used later when full conversion is working
    # binary_write_to_log(converted)


# If statement to take a string input
# Input is converted and written to a file
if response == ("2"):
    print("You selected: '2.) Convert a string to binary'")
    string_input = input("String: ")
    converted = ''.join(format(ord(i), '08b') for i in string_input)
    print("The converted string is: " + str(converted))
    print("The converted string has been written to a log file.")
    string_write_to_log(string_input + " -> " + converted + "\n")
