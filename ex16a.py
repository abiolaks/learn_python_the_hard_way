# Reading the file content

# import the command line argumnet module
from sys import argv


# passing argunment to the comand line : the script name and the filename
script, filename = argv


# opening file in read mode
txt = open(filename, 'r')

print(f"Here is your file {filename}:")

# displaying a simple prompt
input("...Loading ...complete. press ENter ")
# reading the content of the file
print(txt.read())

print("greats, we close the file now")
txt.close()




