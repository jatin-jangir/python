def hcf(num1,num2):
    l=0
    for i in range(1,max(num1,num2)):
        if num1%i==0:
            if num2%i==0:
                if i>l:
                    l=i

    return l

def lcm(num1,num2):
    l=num1*num2
    i=(num1*num2)-1

    while(i>max(num1,num2)):
        if(i%num1 ==0 and i%num2==0):
             l=i
        i-=1
    return l


print(lcm(15,10))