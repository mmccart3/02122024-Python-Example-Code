# print(f"\t|\t|\n\t|\t|\n \t|\t|\n-------------------------\n\t|\t|\n\t|\t|\n \t|\t|\n-------------------------\n\t|\t|\n\t|\t|\n \t|\t|\n")

space1 = " "
space2 = " "
space3 = "O"
space4 = "X"
space5 = " "
space6 = "X"
space7 = "X"
space8 = " "
space9 = "O"

blank_crossline = "   |   |   "
cross_crossline = "-----------"

print(blank_crossline)
print(f" {space1} | {space2} | {space3}")
print(blank_crossline)
print(cross_crossline)
print(blank_crossline)
print(f" {space1} | {space2} | {space3}")
print(blank_crossline)
print(cross_crossline)
print(blank_crossline)
print(f" {space1} | {space2} | {space3}")

# print("     Hello You say   ".strip()+"Goodbye")

# print("the quick brown fox jumps over the lazy dog. so does the cat! i wonder? should i".capitalize())

# #Traditional way of increasing the value of a variable
# my_number = 10
# print(my_number)
# my_number = my_number + 5
# print(my_number)

# #Modern way of increasing a value stored in a variable
# my_number = 10
# print(my_number)
# my_number += 5
# print(my_number)
# my_number /= 3
# print(my_number)
# my_number *= 4
# print(my_number)
# my_number -= 1
# print(my_number)

# Month = 30

# number_of_months_till_birthday = 4
# number_of_days_till_end_of_month = 22
# number_of_days_in_birthday_month_till_birthday= 29
# total_number_of_days_till_birthday = number_of_days_till_end_of_month + (number_of_months_till_birthday*Month)+number_of_days_in_birthday_month_till_birthday
# print(total_number_of_days_till_birthday)

from random import randint

# print(randint(1,10))

dice1 =randint(1,6)
dice2 = randint(1,6)

print(dice1,dice2)

from datetime import datetime
today = datetime.now()
my_birthdate = datetime(1965,4,29)
days_since = today - my_birthdate
print(days_since.days)