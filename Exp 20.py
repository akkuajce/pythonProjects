a=int(input("enter the limit:"))
f1=0
f2=1
print(("Fibonacci series:"))
print(f1)
print(f2)
i=3
while(i<=a):
    next=f1+f2
    print(next)
    f1=f2
    f2=next
    i+=1