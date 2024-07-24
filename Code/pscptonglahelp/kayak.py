""" kayak """
def main():
    """ main """
    n = int(input())
    info = input().split() 
    for i in range(len(info)): 
        info[i] = int(info[i]) 
    info.sort()
    sk = 2
    dk = n-1
    

main()
