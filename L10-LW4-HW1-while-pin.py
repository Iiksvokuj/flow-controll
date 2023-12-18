# allow user > enter PIN > true

correct_PIN = 1234
wrong       = True
attempt = 1

# HW1: stop loop after 3 WRONG attempts

while wrong and attempt <= 3:
    user_PIN = int(input("Enter PIN: "))
    if user_PIN == correct_PIN:
        print("Yes!!!")
        wrong = False
    else:
        print("Wrong!!!")
        print("Remaining attempts:", 3 - attempt)
        attempt += 1