from time import sleep

stored_PIN = 9876
current_balance = 505.26

def check_sufficient_funds(amount):
    global current_balance
    if amount <= current_balance:
        return True
    else:
        return False

def check_PIN(input_PIN):
    global stored_PIN
    if input_PIN == stored_PIN:
        return True
    else:
        return False

def make_cash_withdrawal():
    global current_balance
    PIN = int(input("Please type in ypur 4 digit PIN >"))
    amount = int(input("Please input the amount of cash you wish to withdraw as a mutiple of 10 >"))
    if check_PIN(PIN) and check_sufficient_funds(amount):
        current_balance = current_balance - amount
        print("Dispensing")
        sleep(1)
        print(f"£{amount} dispensed. Please take your cash.")
        print(f"Your new balance is £{current_balance}")
    else:
        print("Either PIN incorrect or insufficient funds")
        # make_cash_withdrawal()
        

make_cash_withdrawal()