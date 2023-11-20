# INPUT monthly salary LIMIT : 2000
salary = 1000     #USD

# 2000+         - good
# 1000 .. 2000  - normal
# 999-          - bad

# x --------------x---------------X--------------------> salary   
# 0      bad     1000    norm    2000     good       + infinity

# ----> good
if salary >= 2000:
    print("good")
else:
    if salary >= 1000:
        print("normal")
    else:
        print("bad")
