Uni = {
"MU" :"Mahidol University",

"CU" : "Chulalongkorn University",

"CMU" : "Chiang Mai University",

"KU" : "Kasetsart University",

"PSU" : "Prince of Songkla University",

"KKU" : "Khon Kaen University",

"TU" : "Thammasat University",

"KMUTT" : "King Mongkut's University of Technology Thonburi",

"RU" : "Ramkhamhaeng University",

"KMITL" : "King Mongkut's Institute of Technology Ladkrabang"
}

n = str(input())
if n in Uni:
    print(Uni[n])
else:
    print("Error")