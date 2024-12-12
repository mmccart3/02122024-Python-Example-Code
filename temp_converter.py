def multiply_by_9_over_5(celsius):
    print("Function 1!")
    return celsius*9/5

def get_fahrenheit(celsius):
    print("Function 2")
    return multiply_by_9_over_5(celsius) + 32

print(f"The temperature is {get_fahrenheit(20)}F.")