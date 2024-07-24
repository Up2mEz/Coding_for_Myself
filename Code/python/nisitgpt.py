def read_ID2l():
    g1 = [21, 23, 25, 28]
    g2 = [22, 24, 26, 27]
    if int_ID2l in g1:
        return 1
    elif int_ID2l in g2:
        return 2
    return 0  # Default value if no condition matches=
def read_ID3():
    global id
    if id == 3 or id == 4:
        return 1
    elif id == 7:
        return 2
    return 0
def read_ID2f():
    if 50 <= int_ID2f <= 55:
        return 1
    elif int_ID2f >= 56:
        return 2
    return 0
def run():
    global int_ID2f,int_ID2l,id,semester
    ID = str(input("Enter student ID: "))
    semester = int(input("Enter semester: "))
    ID2f = ID[:2]
    ID2l = ID[8:10]
    id = int(ID[2])
    int_ID2f = int(ID2f)
    int_ID2l = int(ID2l)
    g = 0
    grade = 0
    group = 0
    if semester == 1 or semester == 2:
        semester = 1
    g = read_ID2l()
    grade = read_ID3()
    group = read_ID2f()
    fee_amounts = {
        (1, 1, 1, 1): 18000,
        (1, 1, 1, 2): 21000,
        (1, 1, 3, 1): 4500,
        (1, 1, 3, 2): 5250,
        (1, 1, 1, 1): 26000,
        (1, 1, 1, 2): 31000,
        (1, 2, 3, 1): 7000,
        (1, 2, 3, 2): 7500,
        (2, 1, 1, 1): 14600,
        (2, 1, 1, 2): 17000,
        (2, 1, 3, 1): 4500,
        (2, 1, 3, 2): 5250,
        (2, 1, 1, 1): 19000,
        (2, 1, 1, 2): 23000,
        (2, 2, 3, 1): 7000,
        (2, 2, 3, 2): 7500,
    }
    fee = fee_amounts.get((g, grade, semester, group), 0)
    if fee != 0:
        print("Registration fee: {}".format(fee))
    else:
        print("Invalid input or fee condition not found.")
run()