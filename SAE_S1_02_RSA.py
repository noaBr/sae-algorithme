from random import *

def prime(n) :
     premier=True
     l=[]
     if n==0:
         return l
     for i in range(1,n):
         if i==1 | i==2:
             l.append(i)
         for k in range (2,i):
             if i%k==0:
                 premier=False
                 break    
             else:
                 premier=True
         if premier==True:
             l.append(i)                
     return l

def extended_gcd(a,b):
	u0=1
	u1=0
	v0=0
	v1=1
	q,r=qotrem(a,b)
	while r!=0:
		u2=u0-q*u1
		v2=v0-q*v1
		u0=u1
		v0=v1
		u1=u2
		v1=v2
		a=b
		b=r
		q,r=qotrem(a,b)
	return b,u1,v1     

def qotrem(a,b):
	q=0
	r=a
	while r>=b:
		q=q+1
		r=r-b
	return q,r

def pgcd_it(a,b):
	r=qotrem(a,b)[1]
	while r!=0:
		a=b
		b=r
		r=qotrem(a,b)[1]
	return b

def key_creation():
        p=choice(prime(200))
        q=choice(prime(200))
        n= p*q
        phi_n=(p-1)*(q-1)
        for e in prime(200) and e>2:
            if pgcd_it(phi_n,e)==1 :
                pub=e
                break
        return n,pub


