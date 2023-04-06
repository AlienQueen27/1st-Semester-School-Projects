# December 2020
dark_chess_pieces = ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
white_chess_pieces = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]

def initializing():
    global dictionary_of_board
    global key_list
    global value_list
    dictionary_of_board = {}

    for x in range(8, 0, -1):
        for y in ["a","b","c","d","e","f","g","h"]:
            dictionary_of_board[y + str(x)] = "  "

    i = 0
    for square in dictionary_of_board:
        if "8" in square or "7" in square:
            dictionary_of_board[square] = dark_chess_pieces[i]
            i += 1
        if "2" in square or "1" in square:
            dictionary_of_board[square] = white_chess_pieces[i - 16]
            i += 1

    key_list = list(dictionary_of_board.keys())
    value_list = list(dictionary_of_board.values())

def possible_moves(a):
    coord = list(key_list[value_list.index(a)])
    possibilities1 = []

    if a in ["P1","P2","P3","P4","P5","P6","P7","P8"]:
        if coord[0]+str(int(coord[1])-1) in dictionary_of_board:
            possibilities1 = [coord[0]+str(int(coord[1])-1)]
    elif a in ["p1","p2","p3","p4","p5","p6","p7","p8"]:
        if coord[0]+str(int(coord[1])+1) in dictionary_of_board:
            possibilities1 = [coord[0]+str(int(coord[1])+1)]

    elif a in ["B1", "B2"]:
        i = 1
        while ((chr(ord(coord[0]) + i) + str(int(coord[1]) - i)) in dictionary_of_board) and not (
                dictionary_of_board[(chr(ord(coord[0]) + i) + str(int(coord[1]) - i))] in dark_chess_pieces):
            possibilities1.append(chr(ord(coord[0]) + i) + str(int(coord[1]) - i))
            if dictionary_of_board[(chr(ord(coord[0]) + i) + str(int(coord[1]) - i))] != "  ":
                break
            i += 1
        i = 1
        while ((chr(ord(coord[0]) - i) + str(int(coord[1]) - i)) in dictionary_of_board) and not (
                dictionary_of_board[(chr(ord(coord[0]) - i) + str(int(coord[1]) - i))] in dark_chess_pieces):
            possibilities1.append(chr(ord(coord[0]) - i) + str(int(coord[1]) - i))
            if dictionary_of_board[(chr(ord(coord[0]) - i) + str(int(coord[1]) - i))] != "  ":
                break
            i += 1
    elif a in ["b1", "b2"]:
        i = 1
        while ((chr(ord(coord[0]) + i) + str(int(coord[1]) + i)) in dictionary_of_board) and not (
                dictionary_of_board[(chr(ord(coord[0]) + i) + str(int(coord[1]) + i))] in white_chess_pieces):
            possibilities1.append(chr(ord(coord[0]) + i) + str(int(coord[1]) + i))
            if dictionary_of_board[(chr(ord(coord[0]) + i) + str(int(coord[1]) + i))] != "  ":
                break
            i += 1
        i = 1
        while ((chr(ord(coord[0]) - i) + str(int(coord[1]) + i)) in dictionary_of_board) and not (
                dictionary_of_board[(chr(ord(coord[0]) - i) + str(int(coord[1]) + i))] in white_chess_pieces):
            possibilities1.append(chr(ord(coord[0]) - i) + str(int(coord[1]) + i))
            if dictionary_of_board[(chr(ord(coord[0]) - i) + str(int(coord[1]) + i))] != "  ":
                break
            i += 1

    elif a in ["N1","N2","n1","n2"]:
        for i in [-2,-1,1,2]:
            for j in [-2,-1,1,2]:
                if abs(i) == abs(j):
                    continue
                if (chr(ord(coord[0]) + i) + str(int(coord[1]) + j)) in dictionary_of_board:
                    possibilities1.append(chr(ord(coord[0]) + i) + str(int(coord[1]) + j))
        for k in [-1,1]:
            for l in [-1,1]:
                if ((chr(ord(coord[0]) + k) + str(int(coord[1]) + l)) in dictionary_of_board) and (dictionary_of_board[chr(ord(coord[0]) + k) + str(int(coord[1]) + l)] == "  "):
                    possibilities1.append(chr(ord(coord[0]) + k) + str(int(coord[1]) + l))

    elif a in ["R1","R2","r1","r2","QU","qu"]:
        i = 1
        while (coord[0] + str(int(coord[1]) + i) in dictionary_of_board) and (((a in white_chess_pieces) and not(dictionary_of_board[coord[0] + str(int(coord[1]) + i)] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[coord[0] + str(int(coord[1]) + i)] in dark_chess_pieces))):
            possibilities1.append(coord[0] + str(int(coord[1]) + i))
            if dictionary_of_board[coord[0] + str(int(coord[1]) + i)] != "  ":
                break
            i += 1
        i = -1
        while (coord[0] + str(int(coord[1]) + i) in dictionary_of_board) and (((a in white_chess_pieces) and not(dictionary_of_board[coord[0] + str(int(coord[1]) + i)] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[coord[0] + str(int(coord[1]) + i)] in dark_chess_pieces))):
            possibilities1.append(coord[0] + str(int(coord[1]) + i))
            if dictionary_of_board[coord[0] + str(int(coord[1]) + i)] != "  ":
                break
            i -= 1
        i = 1
        while ((chr(ord(coord[0]) + i) + coord[1]) in dictionary_of_board) and (((a in white_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) + i) + coord[1]] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) + i) + coord[1]] in dark_chess_pieces))):
            possibilities1.append(chr(ord(coord[0]) + i) + coord[1])
            if dictionary_of_board[chr(ord(coord[0]) + i) + coord[1]] != "  ":
                break
            i += 1
        i = -1
        while ((chr(ord(coord[0]) + i) + coord[1]) in dictionary_of_board) and (((a in white_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) + i) + coord[1]] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) + i) + coord[1]] in dark_chess_pieces))):
            possibilities1.append(chr(ord(coord[0]) + i) + coord[1])
            if dictionary_of_board[chr(ord(coord[0]) + i) + coord[1]] != "  ":
                break
            i -= 1

        if a in ["QU","qu"]:
            i = 1
            while ((chr(ord(coord[0]) + i) + str(int(coord[1]) - i)) in dictionary_of_board) and (((a in white_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) + i) + str(int(coord[1]) - i)] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) + i) + str(int(coord[1]) - i)] in dark_chess_pieces))):
                possibilities1.append(chr(ord(coord[0]) + i) + str(int(coord[1]) - i))
                if dictionary_of_board[chr(ord(coord[0]) + i) + str(int(coord[1]) - i)] != "  ":
                    break
                i += 1
            i = 1
            while ((chr(ord(coord[0]) - i) + str(int(coord[1]) - i)) in dictionary_of_board) and (((a in white_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) - i) + str(int(coord[1]) - i)] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) - i) + str(int(coord[1]) - i)] in dark_chess_pieces))):
                possibilities1.append(chr(ord(coord[0]) - i) + str(int(coord[1]) - i))
                if dictionary_of_board[chr(ord(coord[0]) - i) + str(int(coord[1]) - i)] != "  ":
                    break
                i += 1
            i = 1
            while ((chr(ord(coord[0]) + i) + str(int(coord[1]) + i)) in dictionary_of_board) and (((a in white_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) + i) + str(int(coord[1]) + i)] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) + i) + str(int(coord[1]) + i)] in dark_chess_pieces))):
                possibilities1.append(chr(ord(coord[0]) + i) + str(int(coord[1]) + i))
                if dictionary_of_board[chr(ord(coord[0]) + i) + str(int(coord[1]) + i)] != "  ":
                    break
                i += 1
            i = 1
            while ((chr(ord(coord[0]) - i) + str(int(coord[1]) + i)) in dictionary_of_board) and (((a in white_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) - i) + str(int(coord[1]) + i)] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[chr(ord(coord[0]) - i) + str(int(coord[1]) + i)] in dark_chess_pieces))):
                possibilities1.append(chr(ord(coord[0]) - i) + str(int(coord[1]) + i))
                if dictionary_of_board[chr(ord(coord[0]) - i) + str(int(coord[1]) + i)] != "  ":
                    break
                i += 1

    elif a in ["KI","ki"]:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if chr(ord(coord[0]) + i) + str(int(coord[1]) + j) in dictionary_of_board:
                    possibilities1.append(chr(ord(coord[0]) + i) + str(int(coord[1]) + j))

    possibilities2 = []
    for m in possibilities1:
        if (dictionary_of_board[m] in ["KI","ki"]):
            continue
        elif ((a in white_chess_pieces) and not(dictionary_of_board[m] in white_chess_pieces)) or (
                (a in dark_chess_pieces) and not(dictionary_of_board[m] in dark_chess_pieces)):
            possibilities2.append(m)

    return possibilities2

def moving(a,b):
    global dictionary_of_board
    global key_list
    global value_list
    if b in possible_moves(a):
        dictionary_of_board[key_list[value_list.index(a)]] = "  "
        dictionary_of_board[b] = a

        key_list = list(dictionary_of_board.keys())
        value_list = list(dictionary_of_board.values())

        return "OK"
    else:
        return "FAILED"

def printing():
    print("-" * 25)
    for key in dictionary_of_board:
        if not ("h" in key):
            print("" , dictionary_of_board[key], end="")
        else:
            print("",dictionary_of_board[key])
    print("-" * 25)

file = open("chess.txt", "r")
input_list = [line.split() for line in file.readlines()]
file.close()
initializing()

for i in input_list:
    print(">", end=" ")
    for j in i:
        print(f"{j}", end=" ")
    print()
    if i[0] == "initialize":
        initializing()
        printing()
    elif i[0] == "move":
        print(moving(i[1],i[2]))
    elif i[0] == "showmoves":
        for k in sorted(possible_moves(i[1])):
            print(k,end=" ")
        if possible_moves(i[1]) == []:
            print("FAILED",end="")
        print()
    elif i[0] == "print":
        printing()
    elif i[0] == "exit":
        exit()
