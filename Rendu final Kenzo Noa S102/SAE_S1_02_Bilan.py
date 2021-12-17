from random import *
import numpy as np

def list_prime(n) :
	if n != 0 :
		l = [1]
		for i in range(2, n+1) :
			test = False
			for y in range(2,i) :
				if i%y == 0 :
					test = True
					break
			if test == False :
				l = l+[i] 
	return l

def qotrem(a, b):
	q = 0
	r = a 
	while r >= b:
		q = q+1
		r = r-b
	return q, r

def pgcd_it(a, b):
	r = qotrem(a, b)[1]
	while r != 0:
		a = b
		b = r
		r = qotrem(a, b)[1]
	return b

def extended_gcd(a, b):
	u0 = 1
	u1 = 0
	v0 = 0
	v1 = 1
	q, r = qotrem(a, b)
	while r != 0 :
		u2 = u0-q*u1
		v2 = v0-q*v1
		u0 = u1
		v0 = v1
		u1 = u2
		v1 = v2
		a = b
		b = r
		q, r = qotrem(a, b)
	return b, u1, v1   

def key_creation() :
	n = 0
	while n <= 10000 :
		p = 0 
		q = 0
		while p == q :
			p = choice(list_prime(1000))
			q = choice(list_prime(1000))
		n = p*q
	phi = (p-1)*(q-1)
	test = False
	while test == False :
		e = randint(3, 200)
		if pgcd_it(phi, e) == 1:
			pub = e
			test = True
	c, d, dd = extended_gcd(pub, phi)
	priv = d%phi
	return n, pub, priv

def conv_text(msg) :
	crypt = []
	crypt2 = ""
	crypt3 = []
	for i in range(0, len(msg)) :
		crypt.append(str(ord(msg[i])))
		if len(crypt[i]) < 3 :
			crypt[i] = str(0)+crypt[i]
		crypt2 = crypt2+crypt[i]
	for i in range(0, len(crypt2), 4) :
		crypt3.append(crypt2[i:i+4])
	if len(crypt3[len(crypt3)-1]) < 4 :
			for y in range(0,4-(len(crypt3[len(crypt3)-1]))) :
				crypt3[len(crypt3)-1] = crypt3[len(crypt3)-1] + str(0)
	return crypt3

def encryption(n, pub, msg) :
	msg1 = conv_text(msg)
	chiffrer = []
	for i in range(0, len(msg1)) :
		chiffrer.append(str(((int(msg1[i])**pub)%n)))
	return chiffrer

def tradbin(msg) :
	newmsg = []
	for i in range(0, len(msg)) :
		newmsg.append([])
		for y in range(0, len(msg[i])) :
			newmsg[i].append(bin(int(msg[i][y])))
	for i in range(0, len(newmsg)) :
		for y in range(0, len(newmsg[i])) :
			newmsg[i][y] = newmsg[i][y][2:]
			while len(newmsg[i][y]) < 4 :
				newmsg[i][y] = str(0) + newmsg[i][y]
	return newmsg	

def img(bin4) :
	dd = []
	for nombre in bin4 : #tableau represantant un nombre separer
		dd.append([])
		for y in range(0, len(nombre)) :#chiffre du nombre etape
			i = ""  + (nombre[y])
			dd[len(dd)-1].append([(int(i[0])+int(i[1])+int(i[3]))%2,(int(i[0])+int(i[2])+int(i[3]))%2,int(i[0]),(int(i[1])+int(i[2])+int(i[3]))%2,int(i[1]),int(i[2]),int(i[3])])
	return dd 

def noise(msg) :
	res = []
	for i in range(0, len(msg)) :
		res.append([])
		for y  in range(0, len(msg[i])) :
			vect = msg[i][y].copy()
			test = np.random.randint(0,4)
			if test > 0 :
				index = np.random.randint(0, np.size(vect))
				vect[index] = (vect[index]+1)%2
			res[len(res)-1].append(vect)
	return res

def denoise(msg) :
	ds = f72()
	for i in range(0, len(msg)) :
		for y in range(0, len(msg[i])) :
			for z in range(0, len(ds)) :
				if poids(msg[i][y], ds[z]) == 0 or poids(msg[i][y], ds[z]) == 1 :
					msg[i][y]=ds[z]
					break
	return msg

def poids(u, v) :
	dd = []
	compteur = 0
	for i in range(0, len(u)) :
		dd.append((u[i]+v[i])%2)
		if dd[i] == 1 :
			compteur = compteur+1	
	return compteur

def antecedent(msg) :
	newmsg = []
	for i in range(0, len(msg)) :
		newmsg.append([])
		for y in range(0, len(msg[i])) :
			newmsg[len(newmsg)-1].append(str(msg[i][y][2])+str(msg[i][y][4])+str(msg[i][y][5])+str(msg[i][y][6]))
	return newmsg
	
def detradbin(msg) :
	newmsg = []
	for i in range(0, len(msg)) :
		newmsg.append("")
		for y in range(0, len(msg[i])) :
			newmsg[i] = newmsg[i] + str((int(msg[i][y][0])*8)+(int(msg[i][y][1])*4)+(int(msg[i][y][2])*2)+(int(msg[i][y][3])*1))
	return newmsg

def decryption(n, priv, msg) :
	dechiffrer = []
	dechiffrer2 = ""
	dechiffrer3 = []
	dechiffrer4 = ""
	a = 0
	for i in range(0, len(msg)) :
		dechiffrer.append(str((int(msg[i])**priv)%n))
		while len(dechiffrer[i]) < 4 :
			dechiffrer[i] = str(0) + dechiffrer[i]
		dechiffrer2 = dechiffrer2 + dechiffrer[i]
	for i in range(0, len(dechiffrer2), 3) :
		dechiffrer3.append(dechiffrer2[i:i+3])
	if int(dechiffrer3[len(dechiffrer3)-1]) == 0 :
		dechiffrer3 = dechiffrer3 [:len(dechiffrer3)-1]
	while a < len(dechiffrer3) :
		dechiffrer4 = dechiffrer4 + chr(int(dechiffrer3[a]))
		a = a+1
	return dechiffrer4


def chiffrement_rsa(msg):
	n,pub,priv=key_creation()
	print("ceci est la traduction en nombre du message de Bob :",conv_text(msg))
	print("ceci est le chiffrement du message",encryption(n,pub,msg))
	print("ceci est la traduction en binaire en 4 bits :",tradbin(encryption(n,pub,msg)))
	print("ceci est la traduction en binaire sur 7 bits :",img(tradbin(encryption(n,pub,msg))))
	print("ceci est l'envoi du message avec du bruit :",noise(img(tradbin(encryption(n,pub,msg)))))
	print("ceci est le débruitage du message :",denoise(noise(img(tradbin(encryption(n,pub,msg))))))
	print("ceci est le message final :",decryption(n,priv,detradbin(antecedent(denoise(noise(img(tradbin(encryption(n,pub,msg)))))))))


