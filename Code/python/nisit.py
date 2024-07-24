def read_ID2l():
    global g
    g1 = [21, 23, 25, 28]
    g2 = [22, 24, 26, 27]
    if int_ID2l in g1:
        g = 1
    elif int_ID2l in g2:
        g = 2
    return g

def read_ID3():
    global grade
    if ID3 == 3 or ID3 == 4:
        grade = 1
    elif ID3 == 7:
        grade = 2
    return grade

def read_ID2f():
    global group
    if 55 >= int_ID2f >=50:
        group = 1
    elif int_ID2f >= 56:
        group = 2
    return group

def run(): 
    global int_ID2f,int_ID2l,ID3   
    ID = str(input("Enter student ID: "))
    semester = int(input("Enter semester: "))
    ID2f = []
    ID3 = int(ID[2])
    ID2l = []
    for i in range(len(ID)):
        if i < 2:
            ID2f.append(ID[i])
        if  8 <= i <= 9 :
            ID2l.append(ID[i])
    int_ID2f = ''.join(ID2f)
    int_ID2l = ''.join(ID2l)
    int_ID2f = int(int_ID2f)
    int_ID2l = int(int_ID2l)
    if g == 1:
        if grade == 1:
            if semester == 1 or semester == 2:
                if group == 1:
                    fee = 18000
                else:
                    fee = 21000
            else:
                if group == 1:
                    fee = 4500
                else:
                    fee = 5250
        else:
            if semester == 1 or semester == 2:
                if group == 1:
                    fee = 26000
                else:
                    fee = 31000
            else:
                if group == 1:
                    fee = 7000
                else:
                    fee = 7500

    else:
        if grade == 1:
            if semester == 1 or semester == 2:
                if group == 1:
                    fee = 14500
                else:
                    fee = 17000
            else:
                if group == 1:
                    fee = 4500
                else:
                    fee = 5250
        else:
            if semester == 1 or semester == 2:
                if group == 1:
                    fee = 19000
                else:
                    fee = 23000
            else:
                if group == 1:
                    fee = 7000
                else:
                    fee = 7500
    print("Registration fee : {}".format(fee))

run()