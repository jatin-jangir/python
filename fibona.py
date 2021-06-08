def printFibonnacci(num):
    s1=0
    s2=1
    if(num>=1):
        print(" ",s1) 
    if(num>=2):
         print(" ",s2)
    if(num>2):
        for i in range(2,num):
            t=s2+s1
            print(" ",t)
            s1=s2
            s2=t
printFibonnacci(4)