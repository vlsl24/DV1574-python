print("skriv in 5 tal")
def listIn():
    intList=[]
    for i in range(0,5):
    
        intList.append(int(input("")))
    
    
    evenList=intList
    print(intList)
    for i in range(0,5):
        if evenList[i]%2!=0:
            evenList[i]+=1
        
        
        
    print(str(evenList))
    print("Den nya lista innehåller:")
    for i in range(0,5):
        print(evenList[i])    
        #skrivguiden.se/referenshantering/skriva-referenser/
        #//refero.inu.se/
        
listIn()