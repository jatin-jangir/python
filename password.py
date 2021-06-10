import random
import string

len = int (input("enter length of password --- "))
d=input('enter Y if you need numbers --- ')
s=input('enter Y if you need symbols --- ')
u=input('enter Y if you need uppercase --- ')
l=input('enter Y if you need lowercase --- ')
res=''.join(random.choices(string.ascii_letters,k=len))
if(d=='y' and s!='y' and len>= 1):
    res = ''.join(random.choices(string.digits +string.ascii_letters , k = len))

if (d!='y' and s=='y' and len>=1):
    res = ''.join(random.choices(string.ascii_letters+string.punctuation , k = len))

if (d=='y' and s=='y' and len >=2):
    res = ''.join(random.choices(string.digits +string.ascii_letters+string.punctuation , k = len))


print("The generated random string : " + str(res))