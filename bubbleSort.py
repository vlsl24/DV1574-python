import random
intList = []
i=0
while (i <11):
    var=random.randint(0,1000)

    if var not in intList:
        intList.append(var)
        i+=1

print(intList)

def bubbleSort():
 x= intList
 print("sorting")
 sorting = 1
 iterator=0
 while(sorting):
   for i in range(0,10):
      if x[i]>x[i+1]:
         y=x[i+1]
         x[i+1]=x[i]
         x[i]=y
         iterator=0
      else:
       
         iterator+=1
      if iterator==10:
       sorting=False

 print(x)    

bubbleSort()