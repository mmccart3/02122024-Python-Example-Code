#Challenge 2-2
from random import randint
cards = ["Diamonds", "Spade", "Club", "Heart"]

target_suite = "Club"

current_card= cards[randint(0,3)]
while current_card != target_suite:
    print(current_card)
    current_card= cards[randint(0,3)]
print(current_card)

#Challenge 3
times_table = int(input("Please enter the number of the times tables you want displayed >"))
for i in range(1,13):
    answer = i * times_table
    print(f"{i} x {times_table} = {answer}")
    
#challenge 4

for i in range (2,21):
    prime = True
    for x in range(2,i):
        if i%x == 0:
            prime = False
    if prime == True:
        print(i, "prime")
    else:
        print(i,"NOT prime")