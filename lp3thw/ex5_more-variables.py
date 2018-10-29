#!/usr/bin/env python3.6

name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
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

# ---study drill 2
# convert inches to centimeters
# multiply the inch length value by 2.54
conversion_inch_to_centimeter = 2.54
height_cm = height * conversion_inch_to_centimeter
print(f"{name}'s height of {height} inches equals {height_cm} centimeters")

# convert pounds to kilogram
# multiply the pounds weight by 0.45359237
conversion_pounds_to_kilogram = 0.45359237
weight_kg = weight * conversion_pounds_to_kilogram
weight_kg = round(weight_kg, 2)
print(f"{name}'s weight of {weight} pounds equals approximately {weight_kg} kilograms")

# Or in line, and as a one-liner
print(f"In the metric system, {weight} pounds are about {round(weight * 0.45359273, 2)} kilogram, and {height} inches are about {height * 2.54} centimeters")




