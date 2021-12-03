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