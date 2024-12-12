my_name = "Mark"

my_age = 59

student = False 




# print(my_name, my_age, student)

# print("My name is "+my_name+" and my age is ",my_age,"it is ",student,"that I am a student")

# print("My name is {} and my age is {}".format(my_name,my_age))

def print_func():
    global my_name, my_age, student
    print(f"My name is {my_name} and my age is {my_age} and it is {student} that I am a student")
print_func()
