# Python Basics Chapter 3:
# ========================

# 1. If Statement

# Syntax:
 
# if (condition):
#   code        # if condition is true then this code will execute

# age = int(input("Your age : "))

# if age >= 18:
#     print("You can play!!")

# print("If statement ended!!")

# 2. Pass Statement

# x = 18
# if x > 18:
#     pass

# 3. If - Else Statement

# age = int(input("Your age : "))

# if (age == 18):
#     print("Yes!! Your age is 18!!")

# elif (age > 18):
#     print("Your age is above than 18!!")
    
# else:
#     print("You age is less than 18!!")

# if (age < 14):
#     print("Your age is too low!!")

# elif (age >= 14 and age < 18):
#     print("Your age is slightly low!!")

# elif (age == 18):
#     print("Your age is fine!!")

# elif (age >= 19 and age <= 25):
#     print("Your age is slightly above!!")
    
# else:
#     print("Your age is too high!!")

# 4. Exercise - 1

# Number Guessing Game:

# Make a variable like win_num and assign any number to it.
# Ask user to guess a number.
# If user guessed correctly then print "You Win !!!!"
# If user didn't guessed correctly then:
# If user guessed lower than actual number then print "too low"
# If user guessed higher than actual number then print "too high"

# 5. Nested If - Else and Exercise - 1 Solution

# win_num = 5
# user_num = int(input("Guess a number between 1 and 100 : "))

# Option - 1:

# if user_num == win_num:
    # print("You Win !!!!")

# else:

# if user_num < win_num:
    # print("Too Low !!")

# else:
    # print("Too High !!")

# Option - 2:

# if user_num == win_num:
#     print("You Win !!!!")

# elif user_num < win_num:
#     print("Too Low !!")

# elif user_num > win_num:
#     print("Too High !!")

# else:
#     pass

# 6. And, Or Operator

# Check two or more conditions at same time

# name = "Anshul"
# age = 22

# # and operator:

# if name == "Anshul" and age == 24:
#     print("True")
 
# else:
#     print("False")

# or operator:

# if name == "Anshul" or age == 24:
#     print("True")

# else:
#     print("False")

# 7. Exercise - 2

# Watch Conjuring2:

# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 18 then
# Print "You can watch conjuring2 !!!!"
# Else print "You can't watch conjuring2 !!"

# 8. Exercise - 2 Solution

# name, age = input("Your name and age separated by space : ").split()

# if (name[0] == 'a' or name[0] == 'A') and int(age) >= 18:
#     print("You can watch conjuring2 !!!!")

# else:
#     print("You can't watch conjuring2 !!")

# 9. In Keyword

# name = "Anshul"

# if "A" in name:
#     print("A is present")

# else:
#     print("A is not present")

# 10. Check Empty or Not

# name = input("Your name : ")

# if name.strip() : 
#     print(f"Welcome {name}")

# else:
#     print("Why you didn't enter your name...")

# 11. While Loop

# 10 times

# print("Hello World")

# count = 0
# while count < 10:
#     print(f"Hello World {count}")
#     count += 1

# count = 1
# while count <= 10:
#     print(f"Hello World {count}")
# count += 1

# 12. Sum of Numbers Program using While Loop

# Sum: 1 to 10 (or any number)

# total = 0
# count = 1
# while count <= 10:
# total = total + count
# count = count + 1

# print(total)

# total = 0, count = 1
# total = 1, count = 2
# total = 3, count = 3
# total = 6, count = 4
# total = 10, count = 5 
# total = 15, count = 6
# total = 21, count = 7
# total = 28, count = 8
# total = 36, count = 9
# total = 45, count = 10
# total = 55, count = 11

# total = 1
# count = 1
# while count <= 10:
# total = total * count
# count = count + 1

# print(total)

# 13. Exercise - 3

# Sum of n natural numbers.
# Ask a user for natural number (n).
# Print total from 1 to n.

# 14. Exercise - 3 Solution

# num = int(input("Enter any number : "))

# total = 0
# count = 1
# while count <= num:
#     total += count
#     count += 1

# print(total)

 # 15. Exercise - 4

# Ask user to input a number containing more than one digit.
# Example -> 12345
# Calculate 1 + 2 + 3 + 4 + 5 and print.

# 16. Exercise - 4 Solution

# num = input("A number of more than one digit : ")

# total = 0
# count = 0
# while count < len(num):
# total += int(num[count])
# count += 1

# print(total)
  
# 17. Exercise - 5

# Ask a user for name.
# Example -> Anshul
# Print count of each characters.
# Output:
# A : 1, n : 1, s : 1, h : 1, u : 1, l : 1

# 18. Exercise - 5 Solution

# name = input("Your name : ")

# count = 0
# while count < len(name):
# print(f"{name[count]} : {name.count(name[count])}")
# count += 1

# Name = input("Enter your name : ")
# count = 0
# while count < len(name):
# print(f"{name[count]} : {name.count(name[count])}")
# count+= 1 
# # 19. Infinite Loop

# By Mistake:

# count = 0
# while count <= 10:
# print("Hello World")


# By Intent ionally:

# while True:
#     print("Hello World")

# Boolean Values:

# True -> 1
# False -> 0

# 20. For Loop

# for i in range(10):
#     print(i)
    # print(f"Hello World {i}")

# for i in range(1, 11):
#     print(f"Hello World {i}")

# 21. For Loop Example - 1

# total = 1
# for i in range(1, 10):
#     total += i

# print(total)

# num = int(input("Number : "))

# total = 0
# for i in range(1, num+1):
# total += i

# print(total)

# 22. For Loop Example - 2

# num = input("A number of more than one digit : ")

# total = 0
# for i in range(len(num)):
#     total += int(num[i])

# print(total)

# num = input("A number of more than one digit : ")

# total = 0
# for i in range(len(num)):
#     total = total + int(num[i])

# print(total)

# Explanation -

# num = 12345

# total = 0, i = 0, int(num[i]) = 1
# total = 1, i = 1, int(num[i]) = 2
# total = 3, i = 2, int(num[i]) = 3
# total = 6, i = 3, int(num[i]) = 4
# total = 10, i = 4, int(num[i]) = 5
# total = 15, i = 5, int(num[i]) = 6

# # 23. For Loop Example - 3

# name = input("Your name : ")

# for ch in range(len(name)):
#     print(f"{name[ch]} : {name.count(name[ch])}")

# Explanation -

# name = "Anshul"

# ch = 0, name[ch] = "A", name.count(name[ch]) = 1
# ch = 1, name[ch] = "n", name.count(name[ch]) = 1
# ch = 2, name[ch] = "s", name.count(name[ch]) = 1
# ch = 3, name[ch] = "h", name.count(name[ch]) = 1
# ch = 4, name[ch] = "u", name.count(name[ch]) = 1
# ch = 5, name[ch] = "l", name.count(name[ch]) = 1

# 24. Break and Continue

# break keyword

# count = 1
# while count <= 10:
# if count == 5:
# break
# print(count)
#     count += 1

# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# continue keyword

# count = 1
# while count <= 10:
#     if count == 5:
#         count += 1
#         continue
#     print(count)
#     count += 1

# for i in range(1, 11):
# if i == 5:
# continue
#     print(i)

# 25. Exercise - 6 / Modify Number Guessing Game

# Ask the number to the user untill the correct guessed.
# Also count the number of guesses and print.

# # 26. Exercise - 6 Solution

# win_num = 5
# count = 1

# while True:
#     user_num = int(input("Guess a number between 0 and 100 : "))

#     if user_num == win_num:
#         print(f"Yeah!! You guessed the number in {count} moves")
#         break
    
#     elif user_num < win_num:
#         print(f"Too Low!!")
    
#     else:
#         print(f"Too High!!")

#     count += 1

# 27. DRY Principle of Coding

# DRY -> Don't Repeat Yourself. 

# import random

# win_num = random.randint(1, 100)

# count = 1

# while True:
#     user_num = int(input("Guess a number between 0 and 100 : "))

#     if user_num == win_num:
#         print(f"Yeah!! You guessed the number in {count} moves")
#         break

#     elif user_num < win_num:
#         print(f"Too Low!!")
    
#     else:
#         print(f"Too High!!")
    
#     count += 1

# 28. Step Argument in Range Function

# for i in range(1, 11, 1):
#     print(i)

# for i in range(0, 11, 2):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

# for i in range(2, 11, 2):
#     print(i)

# for i in range(1, 11):
    # print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(10, -1, -1):
#     print(i)

# for i in range(-1, -11, -1):
#     print(i)

# for i in range(-10, 1, 1):
    # print(i)

# 29. For Loop and Strings

# name = "Anshul"

# length = len(name)
# print(length)

# for ch in range(length):
# print(name[ch])

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

# for ch in name:
# print(ch)

# num = input("Number : ")

# total = 0
# for i in num:
#     total += int(i)

# print(total)

nums = "12345"

print(int(n1ums[0]) + int(nums[1]) + int(nums[2]) + int(nums[3]) + int(nums[4]))
