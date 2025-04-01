# stone,paper,seaser game

import random
ans=input("Are you ready for the game ?".lower())
if ans=="y":
    print("Welcome to the GAME !")
    while True:
        print("===INSTRUCTIONS===\n")
        list=["Stone","Paper","Scissor"]
        print("Enter 0 for Stone\nEnter 1 for Paper\nEnter 2 for Scissor")
        result=int(input("Enter Your Choice :"))
        
        num=random.randint(0,2)
        print(f"You Choose -{list[result]} and oppenent choose -{list[num]}")
        if list[num]==list[result]:
            print("Math Draw !")
        
        elif num==0 and result==1:
            print("You Won !")
        elif num==0 and result==2:
            print("You Loss !")
        elif num==1 and result==0:
            print("You Loss !")
        
        elif num==1 and result==2:
            print("You Won !")
        elif num==2 and result==0:
            print("You Won !")
        elif num==2 and result==1:
            print("You Loss !")
        