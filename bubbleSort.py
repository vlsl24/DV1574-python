import random
intList = []
n=10
r=100
i=0

while (i <n):
    var=random.randint(0,r)

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
   for i in range(0,n-1):
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