str=input("Enter the text:")
print(str)
list=str.split()
print(list)
dict={}
for i in list:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
for m,n in dict.items():
    print(m,n)