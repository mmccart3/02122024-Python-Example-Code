def setup_variables():
    global space1, space2, space3,  space4, space5, space6, space7, space8, space9
    space1 = "O"
    space2 = " "
    space3 = "X"
    space4 = "O"
    space5 = "X"
    space6 = "O"
    space7 = "X"
    space8 = " "
    space9 = "O"

blank_crossline = "   |   |   "
cross_crossline = "-----------"

def print_grid():
    print(blank_crossline)
    print(f" {space1} | {space2} | {space3}")
    print(blank_crossline)
    print(cross_crossline)
    print(blank_crossline)
    print(f" {space4} | {space5} | {space6}")
    print(blank_crossline)
    print(cross_crossline)
    print(blank_crossline)
    print(f" {space7} | {space8} | {space9}")
    print(blank_crossline)

def check_rows():
    if space1 == "O" and space2 == "O" and space3 == "O":
        print ("Noughts have won - top row")
    elif space1 == "X" and space2 == "X" and space3 == "X":
        print("Crosses have won - top row")
    elif space4 == "O" and space5 == "O" and space6 == "O":
        print ("Noughts have won - middle row")
    elif space4 == "X" and space5 == "X" and space6 == "X":
        print("Crosses have won - middle row")
    elif space7 == "O" and space8 == "O" and space9 == "O":
        print ("Noughts have won - bottom row")
    elif space7 == "X" and space8 == "X" and space9 == "X":
        print("Crosses have won - bottom row")
    

def check_columns():
    if space1 == "O" and space4 == "O" and space7 == "O":
        print ("Noughts have won - first column")
    elif space1 == "X" and space4 == "X" and space7 == "X":
        print("Crosses have won - first column")
    elif space2 == "O" and space5 == "O" and space8 == "O":
        print ("Noughts have won - second column")
    elif space2 == "X" and space5 == "X" and space8 == "X":
        print("Crosses have won - second column")
    elif space3 == "O" and space6 == "O" and space9 == "O":
        print ("Noughts have won - third column")
    elif space3 == "X" and space6 == "X" and space9 == "X":
        print("Crosses have won - third column")

def check_diagonals():
    if space1 == "O" and space5 == "O" and space9 == "O":
        print ("Noughts have won - diagonal")
    elif space1 == "X" and space5 == "X" and space9 == "X":
        print("Crosses have won - diagonal")
    elif space3 == "O" and space5 == "O" and space7 == "O":
        print ("Noughts have won - diagonal")
    elif space3 == "X" and space5 == "X" and space7 == "X":
        print("Crosses have won - diagonal")

def check_move():
    check_rows()
    check_columns()
    check_diagonals()

setup_variables()   
print_grid()
check_move()