n=50
sum=0
f1=0
f2=1

for i in range(-1, n):
    print(sum)
    sum=f1+f2
    f2=f1
    f1=sum
