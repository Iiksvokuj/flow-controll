from os import system
# IO
# types
# operation

# flow control: if / else


### MOVIE BOARD
system('cls')
print(
"""
1. Avatar 2:
   a. 18:00
   b. 20:00

2. Terminator 9:
   a. 16:00
   b. 23:00

3. Titanic Zombie:
   a. 18:00
"""    
)

moovie_number = input("Choose a moovie: ")

if moovie_number == '1':
    print('You have chosen "Avatar 2"')
    time = input('Choose time: ')
    if time == 'a':
        print('time: 18:00, ticket cost 100')
    if time == 'b':
        print('time: 20:00, ticket cost 120')

if moovie_number == '2':
    print('You have chosen "Terminator 9"')

if moovie_number == '3':
    print('You have chosen "Titanic Zombie"')