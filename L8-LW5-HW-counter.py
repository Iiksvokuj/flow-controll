## while counter

# - 3 keypoints: start, step, end
# - direct / reverse
# - diagram
# - breakpoints
# - shortcuts

# HW*:
#     draw diagram for
#     while-counter

print("""- Hey daddy! Where is the 3?
- Gotta find it, sonny! Let's count from 1 to 10, or backwards?
""", end = "")
start = int(input("- C'mon from: "))
##  end   = 10
n = start
x = 3 

if start == 1:
    end = 10
    while n <= end:
        print(n)
        if n == x:
            print('Found!')
        n += 1
elif start == 10:
    end = 1
    while n >= end:
        print(n)
        if n == x:
            print('Found!')
        n -= 1
