# Printing, Printing : doing complicated formatting

# creating a place holder to pass string of variable
formatter = "{} {} {}"

# passing values into the empty spaces created in the formatter
print(formatter.format(1,2,3,4))
print(formatter.format("one",  "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "twinkle twinkle twinkle ",
    "little stars",
    "How I wonder what you, Like a diamond in the sky"
))
