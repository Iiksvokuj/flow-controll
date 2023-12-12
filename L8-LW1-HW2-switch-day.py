

# HW1:  rewrite this solution using if/elif.../else
# HW2:  enter day number from KB
# HW3*: as a continuation of "currency conventor"
#       rewrite a part of if/else -> match/case


# in -> day (int) ----> app -----> "Mo"

n = 1
while n <= 10:
    n += 1
    day_number = int(input("Enter day number: "))
    match day_number:
        case 1:          # day_number == 1 ?
            print("Mo")
        case 2: 
            print("Tu")
        case 3: 
            print("We")
        case 4: 
            print("Th")
        case 5: 
            print("Fr")
        case 6: 
            print("St")
        case 7: 
            print("Su")
      # case "stop":
      #     break
        case _:
            print("Unexistend day!")