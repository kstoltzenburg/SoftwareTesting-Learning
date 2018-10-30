#!/usr/bin/env python3.6

# assign number to variable
types_of_people = 10
# Use number variable inside an formatted string variable
x = f"There are {types_of_people} types of people."

# assign string to variable
binary = "binary"
# assign string to variable 
do_not = "don't"

# Use string variables inside an formatted string variable (2.1, 2.2)
y = f"Those who know {binary} and those who {do_not}."

# Print formatted string
print(x)
# Print formatted string
print(y)

# Print formatted string in another formatted string (2.3)
print(f"I said: {x}")
# Print formatted string in another formatted string, with quotes (2.4)
print(f"I also said: '{y}'")

# assign boolean to a variable
hilarious = False
# assing variable with a string and placeholder
joke_evaluation = "Isn't that joke so funny?! {}"

# print and format string, replacing placeholder with boolean variable
print(joke_evaluation.format(hilarious))

# assign string to variable
w = "This is the left side of..."
# assign string to variable
e = "a string with a right side."

# print both strings
print(w + e)

# --- study drill
# 2. find all the places where a string is put inside a string. 
#    There are four places.
# 4. explain why adding the two string w and e with + makes a 
#    longer string
#    - The plus sign is used for string concatenation in python
#    adding one string to the other
