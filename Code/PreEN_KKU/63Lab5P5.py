def vowel_count(s):
    count = 0
    s = s.lower()
    vowel = ["a" , "e" , "i" , "o" , "u"]
    for i in range(len(s)):
        for j in range(len(vowel)):
            if s[i] == vowel[j] :
                count += 1
    return count

#ข้างล่างนี้ห้ามแก้
if __name__ == '__main__':
  s = input()
  r = vowel_count(s)
  print(type(s))
  print(r)
  print(r+3)
  print(type(r))