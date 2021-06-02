##a,b=map(int,input().split())
##print(a%b)



##a,b=map(int,input().split())
##print(a>b)




##a=input()
##b=input()
##print(ord('a')+ord('b'))





##r=int(input())
##perimeter =3.14*r*2
##area=3.14*r*r
##diameter=r*2
##print('perimeter:',perimeter,'area:',area,'diameter:',diameter)
##



##l=int(input())
##b=int(input())
##a=l*l+b*b
##print('area:',l*b)
##print('perimeter:',2*(l+b))
##print('diagnol:',a**(1/2))


 
##a=int(input())
##if not a%2:
##                print('even')
##else:
##                print('odd')



##a=int(input())
##if a>0:
##                print('positive')
##elif a==0:
##                print('zero')
##else:
##                print('negative')
##





##num=int(input())
##for i in range(num,-1,-1):
##                print(i,end=' ')




##num=int(input())
##while True:
##               if num==0:
##                               break
##               print(num,end=' ')
##               num-=1
                




##num=int(input())
##s=0
##def value(num):
##                while num:
##                                
##                   r=num%10
##                   num=num//10
##                   s+=r
##                   if s==0:
##                                   break
##print(s)



##a,b,c=map(int,input().split())
##if b<c:
##                x=b
##                y=c+1
##                d=1
##elif b>c:
##                x=c
##                y=b-1
##                d=-1
##for i in range(1,c+1):
##                if (a*i)%3==0:
##                                continue
##                print(a,'X',i,'=',a*i)
##
                                                



##num=int(input())
##ecount=0
##ocount=0
##x=0
##y=0
##while num:
##     r=num%10
##     num=num//10
##     if r%2==0:
##          x=x*10+r
##     else:
##          y=y*10+r
##print(x,'',y)          
##if ecount%2==0 and ocount%2!=0:
##     print('even   odd')
##elif ecount%2==0 and ocount%2==0:
##     print('even')
##elif ecount%2!=0 and ocount%2!=0:
##     print('odd')
##else:
##     print('mixed')



##num,s,re=map(int,input().split())
##count=0
##x=0
##while num:
##     r=num%10
##     num=num//10
##     if r==s:
##          r=re
##     elif r%s==0:
##          r=(r//s)
##     x=x+r*pow(10,count)
##     count+=1
##print(x)




##a,b,c,d=map(int,input().split())
##d=int(input())
##a=0
##b=1
##print(a)
##for i in range (1,d+1):
##    c=a+b
##    a=b
##    b=c
##    print(c)
##    



##def fib(n):
##    if n==0:
##        return True
##    if n==1:
##        print(0)
##        return True
##    a,b,c=0,1,0
##      #print(a,b,end=" ")
##    i=3
##    p=1
##    while True:
##        c=a+b
##        if c==n:
##            print(p)
##        if c>n:
####            if (n-b)>=(c-n):
####                print(b)
####            if (n-b)>=(c-n):
####                print(c)
####            return False
##        a =b
##        b=c
##        p+=1
##        print(p)
##        
##    else:
##        return False
##n=int(input())
##print(fib(n))




##def mul(a,b):
##    if a==1:
##        return b
##    if a%2:
##        return b+mul(a//2,b*2)
##    else:
##        return 0+mul(a//2,b*2)
##a,b=map(int,input().split())
##print(mul(a,b))


'''
def fib(a,b,d,n):
   if d>n:
        return
    if d==1:
        print(a,end=' ')
        d+1
    if d==2:
        print(b,end=' ')
        d+1
    print(a+b,end=' ')
    fib(b,a+b,d+1,n)
    
n=int(input())
fib(0,1,1,n-2)
'''

'''
def arm(n):
    temp=n
    dc=0
    while temp:
        temp=temp//10
        dc+=1
    res=0
    temp=n
    while temp:
        r=temp%10
        temp=temp//10
        res+=r**dc
    print(dc)
    if n==res:
        return True
    return False

n=int(input())
print(arm(n))
'''
'''
import math
def per(num):
    res=1
    s=int(math.sqrt(num))
    for i in range (2,s+1):
        if num%i==0:
            res+=i+num//i
    return res==num
num=int(input())
print(per(num))
'''        


'''
def lcm(a,b):
    t=2
    res=1
    
    while a>=t and b>=t:
        
        if a%t==0 and b%t==0:
            
            a=a//t
            b=b//t
            res=res*t
        else:
            t=t+1       
    return res*a*b
            
            
            
        
        
a,b=map(int,input().split())
print(lcm(a,b))
'''

            
'''        
def lcm(a,b):
    if a<b:
        a,b=b,a
        m=a
        while True:
            if m%a==0 and m%b==0:
                return m
            else:
                m+=1
a,b=map(int,input().split())
print(lcm(a,b))
'''

'''
def gcd(a,b):
    if a>b:
        a,b=b,a
        return a
    else:
        return gcd(a,b%a)
a,b=map(int,input().split())
print(gcd(a,b))
'''


'''
from math import *
def fac(a):
    s=round(sqrt(a))
    b=2
    for i in range (2,s+1):
        if a%i==0:
            if i==a//i:
                b+=1
            else:
                b+=2
    print(b)
a=int(input())
fac(a)
'''



'''
##class Solution:
##    def isPowerOfThree(self, n: int) -> bool:
##        p=0
##        while 3**p>=1:
##            if 3**p==n:
##                return True
##            if 3**p>n:
##                return False
##n=int(input())
##if n==0:
##            print( '1')
##s=bin(n).replace("0b", "")
##k=len(s)-1
##i=0
##while True:
##    if s[i]==s[k]:
##        break
##    if s[1
        
print(s)
     
'''

'''
num=int(input())
for i in range(1,num+1):
     for j in range(1,num+1):
          if j%2==1:
               
              if i%2==0:
                    print('0',end='')
               else:
                    print('1',end='')
          else:
              if i%2==0:
                    print('1',end='')
               else:
                    print('0',end='')
         
     print()
'''              

'''
num=int(input())
for i in range(1,num+1):
    for i in range(1,i+1):
        print('*',end='')
    print()
        
'''
  

'''
num=int(input())
for i in range(num,0,-1):
  for j in range (1,i+1):
        print('*',end='')
    print()
'''   




'''
num=int(input())
for i in range(1,num+1):
    for j in range (1,i+1):
        print(i,end='')
    print()
'''  


'''
num=int(input())
for i in range(num,0,-1):
    for j in range (1,i+1):
        print(i+1,end='')
    print()
'''    


'''
num=int(input())
for i in range(1,num+1):
    for j in range (1,i+1):
        print(j,end='')
    print()
'''
'''
num=int(input())
for i in range(num,0,-1):
    t=num
    for j in range (1,i+1):
        print(t,end='')
        t-=1
    print()
'''
'''
num=int(input())
for i in range(num,0,-1):
    if i%2==0:
       for j in range (i,0,-1):
            print(j,end='')
    else:
       for j in range(1,i+1):
            print(j,end='')
            
    print()
'''   


'''
num=int(input())
for i in range(num,0,-1):
    for s in range(num,i,-1):
       print(' ',end='')
    for j in range(1,i+1):
        print('*',end='')
    print()
'''    
        
'''   
num=int(input())
for i in range(1,num+1):
    for s in range(num,i,-1):
        print(' ',end='')
    for j in range(1,i+1):
       print(i,end='')
   print()

'''


'''
num=int(input())
for i in range(1,num+1):
    for s in range(i,num):
        print(' ',end='')
        
    
    for j in range(1,i*2):
        print(i,end='')
    print()
'''
'''
num=int(input())
for i in range(1,num+1):
    for s in range(1,num-i+1):
        print(' ',end='')
        
    
    for j in range(1,i*2):
        print(i,end='')
    print()
'''

'''
def total_marks(n,data):
    res=0
    for i in data:
        res+=i
        return res

n=int(input())
data=list(map(int,input().split())
total=total_marks(n,data)
          print(total)
'''
'''
def evenodd(n,data):
    ec,oc=0,0
    for i in data:
        if i%2==0:
            ec+=1
        else:
            oc+=1
    return ec,oc
n=int(input())
data=list(map(int,input().split()))
total=evenodd(n,data)
print(*total)
##for i in total
##print(total,end=" ")
'''
'''
import math as m
def isprime(n):
    s=int(m,sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def countprime(n,data):
    pc=0
    for i in data:
        if isprime(i):
            pc+=1
    return pc
n=int(input())
data=list(map(int,input().split()))
pc=countPrimes(n,data)
print(pc)
'''
'''
import math as m
def isprime(n):
    if num==1:
        return 0
    s=int(m.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def findPrimes(n,data):
    m=[]
    for i in data:
        if isprime(i):
            m.append(i)
    return m
n=int(input())
data=list(map(int,input().split()))
primes=findPrime(n,data)
print(*prime)
'''
'''
import math as m
def isprime(n):
    if num==1:
        return 0
    s=int(m.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def findPrimes(n,data):
    prime=[]
    nonprimes=[]
    for i in data:
        if isprime(i):
            prime.append(i)
        else:
            nonprimes.append(i)
    return prime,nonprimes
n=int(input())
data=list(map(int,input().split()))
primes,nonprimes=findPrimes(n,data)
print(*primes)
print(*nonprimes)

'''
'''
def sum(n):
    s=0
    while True:
        r=n%10
        n=n//10
        s=s+r
    return s

def sumofdigits(n,data):
    for i in range(len(data)):
        data[i]=sum(data[i])
n=int(input())
data=list(map(int,input().split()))
sumofdigits=findPrime(n,data)
print(*data)
'''


#reverse of a number in list
#count of palindromes in list

'''
import math
def reverse(n):
    s=0
    while True:
        r=n%10
        n=n//10
        s=s*10+r
    return s
def sumofdigits(n,data):
    for i in range(len(data)):
        data[i]=sum(data[i])
    return data
n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)
'''

'''
import math
def palindrome(n):
    m=n
    s=0
    while True:
        r=n%10
        n=n//10
        s=s*10+r
    return s==m
def sumofdigits(n,data):
    c=0
    for i in range(len(data)):
        if palindrome(data[i]):
            c+=1
    return c
n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)

'''















































































