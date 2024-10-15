def akronym(namnOefternamn,  år):
    
    namn=namnOefternamn[0]
    namn+=namnOefternamn[1]
    for i in range(len(namnOefternamn)):
        if namnOefternamn[i]==" ":
            eNamn=namnOefternamn[(i+1)]
            eNamn+=namnOefternamn[(i+2)]
            break
        
    akronym=namn+eNamn
    akronym=akronym.lower()
    nummer=str(år)[2]
    nummer+=str(år)[3]
    akronym+=nummer

    print(akronym)
    
    
fileName=input("Vilken fill vill du använda? ")

print("\nKlart\n")

file=open(fileName,"r")

i=0
loop=True
while loop:
    try:
        namn=file.readline()
        år=file.readline()
        akronym(namn,år)
        i+=2
    except:
        loop=False
              