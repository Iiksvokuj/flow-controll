# 1d game
# ~~~x~~W~~~

w = 4
x = 2
print()

n = 1
while n <= 10:
    if n == w:
        print("W", end = " ")
    elif n == x:
        print("x", end = " ")
    else:
        print("~", end = " ")
    n += 1


print("\n")