# types
# operators
# i/o

# os [system, path,...]
from os import system
from time import sleep

now = 20

system("cls")
# DATA INPUT
#  ┌---------┐ str
#  v         ^
e_what  = input("Event type: ") #e_what-event
# 'Meet'
e_where = input("Event location: ")
# 'online'
e_when  = input("Event tyme: ")
# '20'

period = int(e_when) - now

sleep(3)
system("cls")

# DATA OUTPUT
print("\n"*3) # + \n
print("-"*40)
print("ATTANTION !!!")  # "ATTANTION !!! + \n"
print("You have a", e_what, e_where, "in", period, "hours")