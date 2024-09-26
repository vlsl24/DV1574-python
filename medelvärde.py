
tal=0
i=0
float(tal)

tal=float(input("mata in en tal:"))

summa=tal
min=tal
max=tal
i+=1
loop=1
while (loop):
    tal= float(input("mata in ett tal"))
    if(tal==0):
        loop=0
    else:
        if(max<tal):
            max=tal
        if(min>tal):
            min=tal
        summa+=tal     
        i+=1

summa-=(max+min) 
summa=summa/(i-2)

print("medelvärde är: "+str(summa))
              

