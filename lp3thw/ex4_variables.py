# setup variables
# how many cars available?
cars = 100
# how many spaces per car?
# NOTE: This assumes available spaces are the same for all cars
# space_in_a_car = 4.0
space_in_a_car = 4
# how many drivers?
drivers = 30
# how many passengers?
passengers = 90
# given available drivers, how many cars will not be driven?
cars_not_driven = cars - drivers
# given available drivers, how many cars will be driven?
# NOTE: this will be incorrect, if we have more drivers then cars; maybe
# if drivers <= cars; cars_driven = drivers; else cars_driven = cars
cars_driven = drivers
# overall available spaces in cars for carpooling
carpool_capacity = cars_driven * space_in_a_car
# How many people per car for carpooling?
average_passengers_per_car = passengers / cars_driven

# -- Study drill
# average_passengers_per_car = car_pool_capacity / passenger
# Will give an error: "name 'car_pool_capacity' is not defined"
# I'd be using, in line 8/9, a variable that has not been defined before,
# python doesn't know what this is supposed to be
# Presumably a typo - I'm defining in line 7/8: 'carpool_capacity'
# but here, I'm trying to use it as           : 'car_pool_capacity'
# --

# print information
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# -- Study drill
# Is using 4.0 for space_in_a_car necessary?
# - frankly, I don't see it making a difference or being important.
# Am I certain? No. 4.0 being a floating point number might make it
# more exact in calculations, but I tried with different values,
# to put 2.66... people in each car, and it had the same results.
# --
