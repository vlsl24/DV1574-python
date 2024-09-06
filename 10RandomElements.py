import random
intList = []
n = 10
for i in range( 0, n):
 rand=  int(random.randint(0,10))
 intList.append(rand)

for i in range (0, n):
    print(intList[i])