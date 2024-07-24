n = int(input())
li = []
for i in range(n):
    book = str(input())
    if li.count(book)==2:
        continue
    elif book not in li:
        li.append(book)
    elif book in li:
        key = li.index(book)
        li.insert(key,book)

print("ชั้นวางหนังสือ",li)