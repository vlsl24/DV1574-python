import random
#sNumber gets random int that user must guess
sNumber =random.randint(0,100)
#loop that lets user play the game 5 times 
i=0
while i<5:
    # accepts input from user
    try:
        x= int(input("enter your guess: "))
        #checks if user guessed too low
        if sNumber >x:
             print("wrong")
             print("you  guessed low")
             i+=1
        #checks if user guessed correctly
        elif sNumber==x:
             print("correct you won")
             i=10
    #checks if user guessed too higt
        elif sNumber<x:
             print("wrong")
             print("you guessed high")
             i+=1
 
    except: 
        print("type numbers only")
        i+=1

    
   
if i!=10:
     print("you lost")


