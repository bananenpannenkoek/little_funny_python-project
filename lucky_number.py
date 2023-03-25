from random import randint
from time import sleep
input1=input("type a number between 1 and 50:\n")
number=randint(1,3)
if int(input1)==number:
    print ("you won!")
else:
    print ("you lose :(\nthe number was: ")
    print (number)
sleep(10)