"""
The aim of this exercise is to utilize the power of function with file
operations.

short function will be written to execute file operations which are afore used in the previous exercise

This exercise solidify the understanding of function there usage

"""

from sys import argv # import the require library to pass commandline args

script, input_file = argv # variables to supply as commandline args: script and filename

# defining a function

def print_all(f):
    ''' function to read the contend of file specify as methods argument '''
    print(f.read())

def rewind(f):
    ''' method description goes here '''
    f.seek(0)

def print_a_line(line_count, f):
    ''' this function return the number of line in the fie '''
    print(line_count, f.readline())

current_file = open(input_file) # this open the content of the file in default mode - read mode

print("First let's print the whole file:\n")

print_all(current_file) # calling the function print_all on the file pass

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # description goes here

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) # printing the first line in the file

current_line = current_line + 1 # incrementing the line number by 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# incrementing the line_number and displaying the content of the line
current_line = current_line + 1
print_a_line(current_line, current_file)

