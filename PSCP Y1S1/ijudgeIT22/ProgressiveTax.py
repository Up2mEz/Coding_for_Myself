""" ProgressiveTax """
def pro_tax():
    """ main funtion """
    income = int(input())
    max_income = income
    tax = 0
    stair = [150000,150000,200000,250000,250000,1000000,2000000]
    lenght = len(stair)
    for i in range(lenght):
        if income > stair[i] :
            tax += (stair[i]*(0.05*i))
            income -= stair[i]
        else:
            tax += income*(0.05*i)
            break
    if max_income > 4000000:
        tax += (max_income-4000000)*0.35
    print(int(tax))
pro_tax()
