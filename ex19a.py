"""
* The above script get personal information from user and display to the standard ouptut
* The information includes name, age, school, work and sex 
* all this are pass as commandline input

"""


#importing the require library

from sys import argv

def personal_info():

    """
    This function display personal details entered by user: such the age, name, school , sex and work type

    """
    input("Display personal information : press enter to continue...>")

    script, name, age, school, work, sex = argv
    print(f"I am {name} \nI am {age} years old.\nI graduated from the university of {school}.\nI am a {work}.\nI am a guy!")

def more_info(wage, hours):

    """
       To calculate work wage per hours

    """
    print()
    wage_hour = wage * hours

    print(f"I will be receiving {wage_hour} usd for this working for {hours} hours because I charge {wage} usd for this job", end="!!!")

personal_info()
more_info(70,24)
