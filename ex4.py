# Working variables - The art of naming things in python


# declaring a variable car to hold a value of 100

cars = 100

# declaring the a variable to hold the number of space in the car
space_in_a_car = 4.0

# a variable to hold the number of passengers in the car
passengers = 90

# a variable to hold the numbers of driver
drivers = 30

# declaring a variale to know the car avaible i.e car on ground
cars_not_driven = cars - drivers

# a variable to know the car driven
cars_driven = drivers

# a variable to know total number of driven and space in the car
carpool_capacity = cars_driven * space_in_a_car

# a variable to know the average number of passengers per car
average_passengers_per_car = passengers / cars_driven


# displaying the number of cars available
print("There are", cars, "cars available.")

# displaying the number of drivers available 
print("There are only", drivers, "drivers available.")

# displaying empty car - cars not driven
print("There will be", cars_not_driven, "empty cars today.")

# displaying pool of customer 
print("We can transport", carpool_capacity, "people today.")

# displaying the number of passenger
print("We have", passengers, "to carpool today.")

# displaying the number of passenger require per car
print("We need to put about", average_passengers_per_car, "in each car.")


