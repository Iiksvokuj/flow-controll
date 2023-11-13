# loop + branching


people = ""

while True:
    name = input("enter someone's name >> ")  #str <"John"> <"Mary">
    if name == "":
        break
    people += name + " "


print(people)