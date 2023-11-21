from os import system
# IO
# types
# operation

# flow control: if / else

# DATA
m_title_1 = "Avatar 2"
m_title_2 = "Terminator 9"
m_title_3 = "Titanic Zombie"

# HW1: insert other data as variable

### MOVIE BOARD
system('cls')
print(
f"""
1. {m_title_1}:
   a. 18:00
   b. 20:00

2. {m_title_2}:
   a. 16:00
   b. 23:00

3. {m_title_3}:
   a. 18:00
"""    
)

moovie_number = input("Choose a moovie: ")

if moovie_number == '1':
    print(f'You have chosen "{m_title_1}"')
    time = input('Choose time: ')
    if time == 'a':
        print('time: 18:00, ticket cost 100')
    if time == 'b':
        print('time: 20:00, ticket cost 120')

if moovie_number == '2':
    print(f'You have chosen "{m_title_2}"')

if moovie_number == '3':
    print(f'You have chosen "{m_title_3}"')