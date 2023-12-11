




# in -> day (int) ----> app -----> "Mo"

day_number = 1

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
    case _:
        print("Unexistend day!")