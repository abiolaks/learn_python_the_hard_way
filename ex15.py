"""
* Reading Files

* The aim of this program is to understand how to read file content

* The solution will such that the user can specify the file to open
"""


from sys import argv

# declaring variables to hold command line args
# filename hold the name of the filename pass at cmd
script, filename = argv

# open the file for and grant read access
txt = open(filename)

print(f"Here's your file {filename}:")

# displaying the content of the file to  the sysout
print(txt.read())

