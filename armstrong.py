def armstrong(num):
    temp=num
    lens =len(str(num))
    sum=0
    while num>0:
        t=num%10
        sum=sum+t**lens
        num=num//10
    if temp==sum:
        return True
    return sum

print(armstrong(153))
