"""
* Working more on understanding variable 

* formatting string output using f string

* f string allow us to embed variable in String

"""


# defining a variable name 
name = 'Zed A. Shaw'

# defining a variable age
age = 35 # not a lie

# defining a variable height
height = 74 # inches

# defining a variable weight
weight = 180 #lbs

# defining variable for eye color
eyes = 'Blue'

# defining a variable for the color of teeth
teeth = 'White'

# defining a variable for the color of hair
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight

print(f"If I add {age}, {height}, and {weight} I get {total}.")

print()

print("Converting the above measurement 'inches to centimeter' and 'pounds to kilogram'")

# converting inches to centimeter: 1 inches is 2.54cm

# rounding up to nearest whole number
height_in_cm = round(height * 2.54)

weight_in_pounds = round(weight * 0.45359237)

print(f"{name} is {height_in_cm} centimeter tall.")
print(f"{name} is {weight_in_pounds} kilogram heavy.")





