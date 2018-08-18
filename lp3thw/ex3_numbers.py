# + plus
# - minus
# / slash
# * asterisk
# % percent
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal

# Floating point numbers
# https://docs.python.org/3/tutorial/floatingpoint.html

# Rewritten to use floatng point numbers by writing 1.0 instead of 1

# counting chickens ... 
print("I will now count my chickens:")

# count of hens
print("Hens", 25 + 30 / 6)  # 30.0
# count of roosters
print("Roosters", 100.0 - 25 * 3 % 4)

# ---- modulo --------------------------
# the above equates to:
# 100 - ((25 * 3) modulo 4)
# 75 modulo 4 = 3
# 4 fits 18 times in 75, leaving 3 over
# --------------------------------------

# counting eggs ...
print("Now I will count the eggs:")

# count of eggs
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)  # 6.75

# Evaluating equation ...
print("Is it true that 3 + 2 < 5 - 7?")

# evalute the whole equation
print(3 + 2 < 5 - 7)  # False

# calculate first part
print("What is 3 + 2?", 3.0 + 2)  # 5

# calculate second part
print("What is 5 - 7?", 5.0 - 7)  # -2

# compare -> result
print("Oh, that's why it's False.")

# More equations ....
print("How about some more.")

# evalute using greater-than
print("Is it greater?", 5 > -2)  # True

# evalute using greater-than-equal
print("Is it greater or equal?", 5 >= -2)  # True

# evaluate using less-than-equal
print("Is it less or equal?", 5 <= -2)  # False
