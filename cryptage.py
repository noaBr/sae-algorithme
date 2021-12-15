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
	c, d,dd = extended_gcd(pub,phi)
	priv = d%phi
	return phi, pub

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


def decryption(n, priv,msg) :
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
	print(dechiffrer3)
	while a<len(dechiffrer3) :
		dechiffrer4 = dechiffrer4 + chr(int(dechiffrer3[a]))
		a = a+1
	return dechiffrer4



#PARTIE 2 

def f42() :
	e1 = [1,0,0,0]
	e2 = [0,1,0,0]
	e3 = [0,0,1,0]
	e4 = [0,0,0,1]
	df = []
	s = [0,1]
	for x1 in s :
		for x2 in s :
			for x3 in s :
				for x4 in s :
					d = []
					for i in range(0,4) :
						d.append((x1*e1[i])+(x2*e2[i])+(x3*e3[i])+(x4*e4[i])) 
					df.append(d)	
	return df

def f72() :
	df = f42()
	dd = []
	for i in df :
		dd.append([(i[0]+i[1]+i[3])%2,(i[0]+i[2]+i[3])%2,i[0],(i[1]+i[2]+i[3])%2,i[1],i[2],i[3]])
	return dd 



def poids() :
	dd = f72()
	for i in range(0,len(dd)-1) :
		for y in range (i+1,len(dd)) :
			compteur = 0
			dp = []
			for z in range(0,7):
				dp.append((dd[i][z] + dd[y][z])%2)
				if dp[z] ==1 :
					compteur = compteur+1
			if compteur<3 :
				return False	
	return True







