"""
 * Performing more operations with file
 * writing a python script to copy one file to another
 * let do this

"""


# importing the require module 

from sys import argv # module for passing commandline args
from os.path import exists # this module return true if a file exists based on its name in string argument.

script, from_file, to_file = argv # args to pass to commandline

# we could do these two on onelinen how

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file) # opening file specify on commandline

indata = in_file.read() # reading the content of the file

print(f"The input file is {len(indata)} bytes long")

# this checks if the output file to write to exists
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# opening the file for write operations
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

# closing the two file opened
out_file.close()
in_file.close()
