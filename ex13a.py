"""
 study drills for exercise 13, 
 working with unpacking
 entering commandline argument

"""


from sys import argv


script, script_process, verbose = argv

print("This is my script:", script)
print()
print("what is the script status:", script_process)
print()
print("Enter verbose_output:", verbose)

# collecting details info about user

name = input("what is your name: " )
print()
print(f"Hi {name} welcome enter number to add below.", end=' ')

a = int(input("enter the first number : "))
b = int(input("enter second number: "))


output = a + b
print()
print(f"Hey {name} adding {a} and {b} gives {output}")



