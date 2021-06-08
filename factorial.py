#factorial code

from typing import Mapping


def factorial(num):
    if(num==0): 
        return 1;
    else:
        return num*factorial(num-1)

#find triling zeros
def FactTrailZero(num):
    count =0
    i=5
    while(num//i!=0):
        count+=int(num/i)
        i=i*5
    return count


if __name__=='__main__':
      #print(factorial(12))
      print(f'  {FactTrailZero(120)}')