def addition(num1, num2):
    sum = num1 + num2
    return sum

def switch_status(current_status):
    if current_status == True:
        current_status = False
    else:
        current_status = True
    return current_status

print(addition(22,87))
print(switch_status(False))
