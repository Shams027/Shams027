import random
from time import sleep
num=random.randint(1,3)
qwerty="1"
while qwerty=="1":
    sleep(1.5)
    print("Enter 'r' for rock, 'p' for paper and 's' for scissors")
    chosen1=input()
    if chosen1.lower()=="p":
        print("You have chosen Paper")
        sleep(1.5)
    if chosen1.lower()=="r":
        print("You have chosen Rock")
        sleep(1.5)
    if chosen1.lower()=="s":
        print("You have chosen Scissors")
        sleep(1.5)
    num=random.randint(1,3)
    if num==1 and chosen1.lower()=="r":
        print("The Computer has chosen Rock")
        sleep(1.5)
        print("DRAW!!!")
    if num==1 and chosen1.lower()=="s":
        print("The Computer has chosen Rock")
        sleep(1.5)
        print("YOU LOSE!!!")
    if num==1 and chosen1.lower()=="p":
        print("The Computer has chosen Rock")
        sleep(1.5)
        print("YOU WIN!!!")
    if num==2 and chosen1.lower()=="p":
        print("The Computer has chosen Paper")
        sleep(1.5)
        print("DRAW!!!")
    if num==2 and chosen1.lower()=="r":
        print("The Computer has chosen Paper")
        sleep(1.5)
        print("YOU LOSE!!!")
    if num==2 and chosen1.lower()=="s":
        print("The Computer has chosen Paper")
        sleep(1.5)
        print("YOU WIN!!!")
    if num==3 and chosen1.lower()=="s":
        print("The Computer has chosen Scissors")
        sleep(1.5)
        print("DRAW!!!")
    if num==3 and chosen1.lower()=="p":
        print("The Computer has chosen Scissors")
        sleep(1.5)
        print("YOU LOSE!!!")
    if num==3 and chosen1.lower()=="r":
        print("The Computer has chosen Scissors")
        sleep(1.5)
        print("YOU WIN!!!")
