# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:56:19 2023

@author: user
"""
import random
import opap

last_draw = opap.get_last_draw("joker")
b = last_draw[0]

# Numbers that don't appear often
c = [25, 44, 19, 45]

# Numbers that haven't appeared for a while
e = [11, 14, 30, 31, 36]

# Numbers that appear frequently
often_nums = [11, 13, 27, 29, 31, 32, 34, 37]

# Find numbers that are valid for prediction
valid_nums = [num for num in e if num not in often_nums and num not in b and num not in c]

if valid_nums:
    predict_model = random.choice(valid_nums)
else:
    print("No numbers for choice.")

lucky = []

while len(lucky) < 5:
    rand_num = random.randint(1, 44)
    if rand_num != predict_model and rand_num not in b and rand_num not in c and rand_num not in lucky:
        lucky.append(rand_num)

# Number for the Joker 1-20
often_tz = [1, 3, 8, 18, 6, 11, 19]
tzokeraki = random.choice(often_tz)

# Print the improved output
print("OUR TODAY LUCKY NUMBERS ARE:")
print(", ".join(map(str, lucky)))  # Join the lucky numbers with a comma
print("AND TZOKER:", tzokeraki)
print("VALUE OF THE TICKET IS 3 EUROS")
print("GOOD LUCK!!!")
