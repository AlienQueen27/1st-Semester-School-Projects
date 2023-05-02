import sys
letter_list = list(".ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

def to_intlist(string):
    if len(string) % n != 0:
        messageplus = [" " for i in range(n - (len(message) % n))]
        messagelist = list(message) + messageplus
    else:
        messagelist = list(message)

    return [letter_list.index(i) for i in messagelist]

def to_matrix(list1):
    wanted_matrix = []
    x = 1
    for i in range(len(list1) // n):
        small_list = []
        for j in range(n):
            small_list.append([list1[x-1]])
            x += 1
        wanted_matrix.append(small_list)
    return wanted_matrix

def to_list(matrix1):
    wanted_list = []
    for i in matrix1:
        for j in i:
            wanted_list.append(j)

    return wanted_list

def multiplying(matrix1,matrix2):
    wanted_matrix = [[0]*len(matrix2[0]) for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                wanted_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return wanted_matrix

def inverse(mainM):
    identity = [[0]*len(mainM) for i in range(len(mainM[0]))]
    for i in range(len(mainM)):
        for j in range(len(mainM[0])):
            if i == j:
                identity[i][j] = 1

    wanted_matrix = [i.copy() for i in mainM]
    wanted_matrix2 = [x.copy() for x in wanted_matrix]
    identity2 = [i.copy() for i in identity]
    for i in range(len(wanted_matrix)):
        for j in range(len(wanted_matrix[0])):
            if j >= len(wanted_matrix):
                j = j % len(wanted_matrix)
            wanted_matrix[j][i] /= wanted_matrix2[i][i]
            identity[j][i] /= wanted_matrix2[i][i]
        wanted_matrix2 = [x.copy() for x in wanted_matrix]
        identity2 = [i.copy() for i in identity]
        for k in range(i + 1,len(wanted_matrix[0]) + i):
            for l in range(i,len(wanted_matrix) + i):
                if k >= len(wanted_matrix):
                    k = k % len(wanted_matrix)
                if l >= len(wanted_matrix):
                    l = l % len(wanted_matrix)
                wanted_matrix[l][k] -= wanted_matrix2[l][i] * wanted_matrix2[i][k]
                identity[l][k] -= identity2[l][i] * wanted_matrix2[i][k]
        wanted_matrix2 = [x.copy() for x in wanted_matrix]
        identity2 = [i.copy() for i in identity]

    return identity


try:
    try:
        key_name = sys.argv[2]
        try:
            if key_name[-3:] != "txt":
                raise AssertionError
            with open(key_name, "r") as file1:
                list1 = file1.read().splitlines()
                try:
                    if list1 == []:
                        raise AssertionError
                    try:
                        key_matrix = [[int(k) for k in j] for j in [list1[i].split(",") for i in range(len(list1))]]
                        n = len(key_matrix)
                    except:
                        print("Invalid Character In Key File")
                except AssertionError:
                    print("Key File Is Empty")
        except AssertionError:
            print("Key File Could Not Be Read Error")
    except FileNotFoundError:
        print("Key File Not Found Error")

    try:
        message_name = sys.argv[3]
        try:
            if message_name[-3:] != "txt":
                raise AssertionError
            with open(message_name, "r") as file2:
                message = file2.read().upper()
                try:
                    if message == "":
                        raise AssertionError
                except AssertionError:
                    print("Input file is empty")
        except AssertionError:
            print("The Input File Could Not Be Read Error")
    except FileNotFoundError:
        print("Input File Not Found Error")
    anan = inverse(key_matrix)
    try:
        if len(sys.argv) != 5:
            raise AssertionError
        try:
            if sys.argv[1] == "enc":
                try:
                    for i in message:
                        if i not in letter_list[1:]:
                            raise AssertionError
                    result = [multiplying(key_matrix,i) for i in to_matrix(to_intlist(message))]
                    result = to_list(result)
                    result = [str(i[0]) for i in result]
                    with open(sys.argv[4], "w") as file3:
                        file3.write(",".join(result))
                except AssertionError:
                    print("Invalid Character In Input File Error")
            elif sys.argv[1] == "dec":
                try:
                    for i in message:
                        if i not in ["0","1","2","3","4","5","6","7","8","9",","]:
                            raise AssertionError
                    result = [multiplying(anan,i) for i in to_matrix([int(i) for i in message.split(",")])]
                    result = to_list(result)
                    result = [int(i[0]) for i in result]
                    result = [letter_list[i] for i in result]
                    with open(sys.argv[4], "w") as file3:
                        file3.write(("".join(result)).strip())
                except AssertionError:
                    print("Invalid Character In Input File Error")
            else:
                raise AssertionError
        except AssertionError:
            print("Undefined Parameter Error")
    except AssertionError:
        print("Parameter Number Error")
except:
    pass
