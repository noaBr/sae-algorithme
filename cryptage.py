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

def key_creation() :
	p = choice(list_prime(200))
	q = choice(list_prime(200))
	n = p*q
	phi = (p-1)*(q-1)
	test = False
	while test == False :
		e = randint(3,200)
		if pgcd_it(phi,e)==1:
			pub = e
			test = True
	return phi, pub
