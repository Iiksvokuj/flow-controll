

# HW1:  rewrite this solution using if/elif.../else
# HW2:  enter day number from KB
# HW3*: as a continuation of "currency conventor"
#       rewrite a part of if/else -> match/case


# in -> day (int) ----> app -----> "Mo"

n = 1
while n <= 10:
    n += 1
    day_number = int(input("Enter day number: "))
    if day_number == 1:         # day_number == 1 ?
        print("Mo")
    elif day_number == 2:
        print("Tu")
    elif day_number == 3: 
        print("We")
    elif day_number == 4: 
        print("Th")
    elif day_number == 5: 
        print("Fr")
    elif day_number == 6: 
        print("St")
    elif day_number == 7: 
        print("Su")
    else:
        print("Unexistend day!")