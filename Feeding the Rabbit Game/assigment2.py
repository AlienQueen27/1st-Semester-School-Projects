# November 2020

def printing(the_string):
    a = 0
    for i in range(number_of_lines):
        for j in range(number_of_columns):
            print(the_string[a], end=" ")
            a += 1
        print("")

def moving_asterisk():
    global string_list, asterisk
    string_list[asterisk] = "X"
    string_list[new_asterisk] = "*"
    asterisk = new_asterisk

def scoring():
    global point
    if string_list[new_asterisk] == "C":
        point += 10
    elif string_list[new_asterisk] == "A":
        point += 5
    elif string_list[new_asterisk] == "M":
        point -= 5
    elif string_list[new_asterisk] == "P":
        moving_asterisk()
        printing(string_list)
        print(f"Your score is: {point} \n")
        exit()
    moving_asterisk()

def moving(direction_string):
    global asterisk, new_asterisk
    for i in direction_string:
        if i == "U":
            new_asterisk = asterisk - number_of_columns
            if asterisk < number_of_columns or string_list[new_asterisk] == "W":
                continue
            else:
                scoring()
        elif i == "D":
            new_asterisk = asterisk + number_of_columns
            if asterisk >= (len(string_list) - number_of_columns) or string_list[new_asterisk] == "W":
                continue
            else:
                scoring()
        elif i == "R":
            new_asterisk = asterisk + 1
            if (asterisk % number_of_columns) == (number_of_columns - 1) or string_list[new_asterisk] == "W":
                continue
            else:
                scoring()
        elif i == "L":
            new_asterisk = asterisk - 1
            if (asterisk % number_of_columns) == 0 or string_list[new_asterisk] == "W":
                continue
            else:
                scoring()

list = input("Please enter feeding map as a list: \n")
number_of_lines = list.count("[") - 1
string_list = ((((list.replace("[","")).replace("]","")).replace(",","")).replace("'","")).split(" ")
number_of_columns = len(string_list)//number_of_lines
asterisk = string_list.index("*")

moves = input("Please enter direction of movements as a list: \n")
moves = ((((moves.replace("[","")).replace("]","")).replace(",","")).replace("'","")).replace(" ","")
point = 0

print("Your board is:")
printing(string_list)
print("Your final board is:")
moving(moves)
printing(string_list)
print(f"Your score is: {point} \n")
