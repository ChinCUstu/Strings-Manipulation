#!/usr/bin/env python
# coding: utf-8

# #### Data Types
# 
# Strings

# In[ ]:


print("Hello"[-1])

print("123" + "345")


# ### Integer

# In[ ]:


123_456_789 + 234_567_789


# #### Float and Boolean

# In[ ]:


#float
3.1415
#boolen
true
false


# In[ ]:


num_char = len(input("What is your name?"))
# print("Your name has "+num_char+" characters.")
print(type(num_char))


# ### Type Casting

# In[ ]:


# num_char = len(input("What's your name? "))

# new_num_char = str(num_char)

# print("Your name has "+new_num_char+" characters.")

a = float(123)

print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))


# #### Data Type Exercise: Write a program that adds the digits in a 2 digit number

# In[ ]:


two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

result = first_digit + second_digit
print(result)


# ### Mathematical Operations

# In[ ]:


3 + 5
7 - 3
3 * 2
6 / 3
2 ** 3

# PEMDASLR
# P: Paranthesis
# E: Exponent
# M: Multiplication
# D: Division
# A: Addition
# S: Subtraction
# LR: Left to Right

print(3 * (3 + 3) / 3 - 3)


# ### BMI(Body Mass Index) Calculator Exercise

# In[ ]:


# Calculates the BMI of a person
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

new_height = float(height)
new_weight = int(weight)
type(new_height)
type(new_weight)
body_mass_index = new_weight / new_height ** 2
bmi_as_int = int(body_mass_index)
print(bmi_as_int)


# ### Number Manipulation and F string 

# In[ ]:


print(round(8 / 3,2))
print(8 // 3)

result = 4 / 2

result /= 2
print(result)

score = 0

# User scores a point
score += 1
print(score)


# In[ ]:


score = 0
height = 1.8
isWinning = True

#f-string
print(f"Your score is {score}, your height is {height}, you are winning is\
 you are winning is {isWinning}")


# ### Exercise Life in Weeks

# ###### Instruction: Create a program using maths and f strings that tells us how many days, weeks, months we have left if we live until 90 years old

# In[5]:


age = input("What is your current age? ")
age_as_int = int(age)

days = (365 * 90) - (365 * age_as_int)
weeks = (52 * 90) - (52 * age_as_int)
months = (12 * 90) - (12 * age_as_int)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")


# ## Tip Calculator

# In[25]:


# Program for a tip calculator
print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
bill_as_int = float(bill)
total_bill = float(bill)
split_bill = input("How many people to split the bill? ")
split_as_int = int(split_bill)
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percent_as_int = int(percentage)

new_bill = (((percent_as_int/100)  * bill_as_int) + total_bill)/split_as_int
total_bill = "{:.2f}".format(new_bill,2)

print(f"Each person should pay: {total_bill}")

