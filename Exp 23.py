str=input("Enter string:")
print(str)
dict={}
for i in str:
    if i in dict:
        dict[i]=dict[i]+1
        print(dict)
    else:
        dict[i]=1
        print(dict)
for m,n in dict.items():
    print(m,n)

