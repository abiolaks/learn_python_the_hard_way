"""
* Understanding the use of commandline argument and input

* Let's call it prompting and passing

* Let's begin and enjoy the ride

"""


# import the argv module from the sys package

from sys import argv

# variables to hold the commandline argument
script, user_name = argv

# diplaying a simple commandline prompt using the greater than
prompt = '>>> '


print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask. you a few questions:")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
        Alright, so you said {likes} about liking me.
        You live in {lives}. Not sure where that is.
        And you have a {computer} computer. Nice.
        """)
