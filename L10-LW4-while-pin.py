# allow user > enter PIN > true

correct_PIN = 1234


while True:
    user_PIN = int(input("Enter PIN: "))
    if user_PIN == correct_PIN:
        print("Yes!!!")
    else:
        print("Wrong!!!")