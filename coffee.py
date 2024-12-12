from time import sleep

def setup_global_variables():
    global coffee_is_grinding_flag
    coffee_is_grinding_flag = False
    
def press_grind_beans():
    global coffee_is_grinding_flag
    if coffee_is_grinding_flag:
        print("stopping grinding")
        sleep(0.5)
        print("grinding stopped")
        coffee_is_grinding_flag = False
    else:
        print("grinding starting")
        sleep(0.5)
        print("grinding!")
        sleep(0.5)
        print("grinding!")
        coffee_is_grinding_flag = True
        
setup_global_variables()
press_grind_beans()
press_grind_beans()

