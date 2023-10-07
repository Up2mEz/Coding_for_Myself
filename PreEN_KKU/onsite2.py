n = int(input("Number of customers: "))
meal=[]
cal=[]
for i in range(n):
    meal.append(input("Enter food, amount, cal:").split)

print("---- Meal summary ----")
for i in range(n):
    all_call = meal[i][1]*meal[i][2]
    cal.append(all_call)
    print(f"{meal[i][0]} x {meal[i][1]}"    ,cal[i])

for i in range(len(cal)):
    sum += cal[i]

avg_cal = sum/n
print(f"Avg energy take in for each person {avg_cal} kCal")