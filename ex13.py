"""
Understanding Parameters

And Unpacking varibles

"""

# uisng the import allow adding feature to our code from the python
# python feature set

# argv is the argument varible - it holds the argument
# it holds argument that you will pass to the python script
from sys import argv

# this unpacks argv so  that it holds all the argument.
# here it get assign to four variable
# it takes whatever is in argv upacks it and assign it ot all
# these variable on the lhs in order
script, first, second, third = argv

# printing to the sysout.
print("The script is called:", script)
print("Your first varibles is:", first)
print("Your second varibles is:", second)
print("Your third variable is:", third)
