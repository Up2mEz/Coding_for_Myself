""" print tree """
def tree(n = int(input()),k = int(input())):
    """ Christmas """
    max_colum = 2*n-1
    for i in range(1,n+1):
        print(" "*((max_colum-(2*i-1))//2),end="")
        print("*"*(2*i-1),end="")
        print(" "*((max_colum-(2*i-1))//2))
    for _ in range(k):
        print(" "*((max_colum-3)//2),end="")
        print("---",end="")
        print(" "*((max_colum-3)//2))
tree()
