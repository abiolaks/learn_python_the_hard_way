"""

 * Reading and Writing Files
 * Using some functions to operate on file
 * Examining and understanding the use of the functions below:
 

"""



from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.") # filename will be specify as an argument on the cmd

print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.") # enter key

input("?") # displaying a basic prompt ?

print("Opening the file...")

# this open the filename pass as cmd arg in write mode
target = open(filename, 'w')

# Erasing the file, also note opening the file in write mode also erase the content of the file.
print("Truncating the file. Goodbye!")

# This empties the file
target.truncate()

# Entering in content to the file
print("Now I'm going to ask you for three lines.")

# getting file content from the user
line1 = input("line 1: ")
line2 = input("line 2: ") 
line3 = input("line 3: ")

print("I'm going to write these to the file..")

target.write(f"{line1}\n{line2}\n{line3}\n")


print("And finally, we close it. ")
target.close()
