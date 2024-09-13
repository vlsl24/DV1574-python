import random

totalSum=0
#funktion som kastar och adderar ihop tärningar
def ThrowDice(x):
    sum=0
    for i in range(0,x):
        sum+=random.randint(1,6)

    print("summan av kast är: "+str(sum))
    return sum

#main loopen som styr funktionen
loop=True
while loop:
    x=input("Hur många gånger ska tärningen kastas?")

    #om användare skriver "q" kommer programmet skriva ut totalsumma och avsluta programmet
    if x=="q":
       print(totalSum)
       if totalSum % 2 ==0:
           print("jämn")
       else:
           print("udda")

       loop=False
    else:
        x=int(x)
        y=ThrowDice(x)
        totalSum +=y