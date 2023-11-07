hp = float(input())
goal = float(input())
n = int(input())
csgo = 0

for i in range(n):
    dmg = float(input())
    hp -= dmg
    csgo = csgo+(dmg*0.03)

if hp <= 0:
    print("ดีดี้โดนัท")
elif hp > 0 and csgo >= goal:
    print("พาลอยซาชิมิ")
elif hp > 0 and csgo < goal:
    print("ตายคู่")
