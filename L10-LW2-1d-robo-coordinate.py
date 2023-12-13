# horisontal path / length
# x1 --------------R-----------------------> x2
# 0                                         n
# roboX - robot coordinate

length = 20
roboX = 5

x = 1
print("\n")
while x <= length:
    if x == roboX:
        print("R", end = "")    #\n
    else:
        print("-", end = "")    #\n
    x += 1

print("\n")