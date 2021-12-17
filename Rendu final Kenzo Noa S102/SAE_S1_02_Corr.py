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



def demopoids() :
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


def img(bin4) :
	dd = []
	for nombre in bin4 : #tableau represantant un nombre separer
		dd.append([])
		for y in range(0, len(nombre)) :#chiffre du nombre etape
			i = ""  + (nombre[y])
			dd[len(dd)-1].append([(int(i[0])+int(i[1])+int(i[3]))%2,(int(i[0])+int(i[2])+int(i[3]))%2,int(i[0]),(int(i[1])+int(i[2])+int(i[3]))%2,int(i[1]),int(i[2]),int(i[3])])
	return dd 
