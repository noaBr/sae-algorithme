from random import *

def list_prime(n) :
	if n!=0 :
		l=[1]
		for i in range(2,n+1) :
			test = False
			for y in range(2,i) :
				if i%y==0 :
					test= True
					break
			if test==False :
				l=l+[i] 
	return l

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

def key_creation() :
	n=0
	while n<=10000 :
		p = 0 
		q = 0
		while p == q :
			p = choice(list_prime(1000))
			q = choice(list_prime(1000))
		n = p*q
	phi = (p-1)*(q-1)
	test = False
	while test == False :
		e = randint(3,200)
		if pgcd_it(phi,e)==1:
			pub = e
			test = True
	c, d,dd = extended_gcd(pub,phi)
	priv = d%phi
	return n, pub, priv



def conv_text(msg) :
	crypt = []
	crypt2 = ""
	crypt3 = []
	for i in range(0,len(msg)) :
		crypt.append(str(ord(msg[i])))
		if len(crypt[i])<3 :
			crypt[i] = str(0)+crypt[i]
		crypt2=crypt2+crypt[i]
	for i in range(0,len(crypt2),4) :
		crypt3.append(crypt2[i:i+4])
	if len(crypt3[len(crypt3)-1])<4 :
			for y in range (0,4-(len(crypt3[len(crypt3)-1]))) :
				crypt3[len(crypt3)-1] = crypt3[len(crypt3)-1] + str(0)
	return crypt3


def encryption(n,pub,msg) :
	msg1 = conv_text(msg)
	chiffrer = []
	for i in range(0,len(msg1)) :
		chiffrer.append(str(((int(msg1[i])**pub)%n)))
	return chiffrer

def decryption2(n, priv,msg) :
	dechiffrer = []
	dechiffrer2 = ""
	dechiffrer3 = []
	dechiffrer4 = ""
	a = 0
	for i in range(0, len(msg)) :
		dechiffrer.append(str((int(msg[i])**priv)%n))
		while len(dechiffrer[i])<4 :
			dechiffrer[i] = str(0) + dechiffrer[i]
		dechiffrer2 = dechiffrer2 + dechiffrer[i]
	for i in range(0,len(dechiffrer2),3) :
		dechiffrer3.append(dechiffrer2[i:i+3])
	if int(dechiffrer3[len(dechiffrer3)-1])==0 :
		dechiffrer3 = dechiffrer3 [:len(dechiffrer3)-1]
	while a<len(dechiffrer3) :
		dechiffrer4 = dechiffrer4 + chr(int(dechiffrer3[a]))
		a = a+1
	return dechiffrer4

