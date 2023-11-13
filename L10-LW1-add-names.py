# loop + branching


people = ""
count = 0
while True:
    count += 1
    name = input(str(count) + ") enter someone's name >> ")  #str <"John"> <"Mary">
    if name == "":
        break
    people += name

    if count % 3 == 0:
        people += "\n"
    else:
        people += " "


print()
print(people)

# "John Marry Peter\nJack Jane Victoria\nBob "


# HW1:

#
#-----------------------------------------
#|John         |Marry        |Peter      |   
#|Tatyana      |Victoria     |Bob        |
#|Jack         |Silvia       |           |
#-----------------------------------------