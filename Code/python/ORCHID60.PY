arr = []
c = 0


n = int(input())
for i in range(n):
    arr.append(int(input()))

for j in range(len(arr)):
    if j == 0:
        if arr[j] > arr[j+1]:
            arr[j] = arr[j+1]
            c += 1    
    else:
        if arr[j] < arr[j-1]:
            arr[j] = arr[j-1]
            c+= 1

print("จำนวนต้นไม้ที่ต้องเปลี่ยน {} ต้น".format(c))
            


