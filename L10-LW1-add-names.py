# loop + branching


people = ""
count = 0
while True:
    count += 1
    name = input(str(count) + ") enter someone's name >> ")  #str <"John"> <"Mary">

    people += f"|{name:12}"

    if count % 3 == 0:
        people += "|\n"
    else:
        people += " "
    if name == "":
        break



print()
print("-"*14*3)
print(people, end="")
print("-"*14*3)

# "John Marry Peter\nJack Jane Victoria\nBob "


# HW1:

#
#-----------------------------------------
#|John         |Marry        |Peter      |   
#|Tatyana      |Victoria     |Bob        |
#|Jack         |Silvia       |           |
#-----------------------------------------