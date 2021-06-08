with open('data.txt') as f:
    lines=f.readlines()

curr={}
for line in lines:
    par=line.split('\t')
    curr[par[0]]=par[1]

[print(item) for item in curr.keys()]
choice=input("\n\nenter the name of currency -- ")
amount=int(input("enter amount -- "))
print(f"{amount} $ is equal to {amount*float(curr[choice])}")