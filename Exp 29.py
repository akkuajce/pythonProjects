a=int(input("Enter upper limit:"))
b=int(input("Enter lower limit:"))
lists=[]
for i in range(a,b+1):
    for j in range(1,i):
        if i*i==i:
            string=str(i)
            if int(string[0]%2==0 and int (string[i])%2==0 and int (string[3])%2==0):
                lists.append(string)
print(lists)