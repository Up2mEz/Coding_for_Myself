kg = int(input())
g = int(input())

sum_gold = (kg*1000)+g
amount_gold = sum_gold//1000

if sum_gold >= 10000:
    sum_gold -= amount_gold*200
    kg = sum_gold//1000
    g = sum_gold-kg*1000
    
elif sum_gold < 10000:
    sum_gold -= amount_gold*100
    kg = sum_gold//1000
    g = sum_gold-kg*1000

print(kg)
print(g)