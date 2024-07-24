print("=== Membership application ===")
print()
formation = []
formation.append(input("Please enter the first name of the applicant: "))
formation.append(input("Last name: "))
formation.append(input("Your birthday (year month date): ").split())
age = 2022-int(formation[2][2])
formation.append(input("Your blessing: "))
print()
print(f"Welcome {formation[0]}, {formation[1]} ({formation[2][0]} / {formation[2][1]} / {formation[2][2]} , age {age})")
print(formation[3])


