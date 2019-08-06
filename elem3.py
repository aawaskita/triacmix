import globalVar

"""
ELEM3(IFM2,PB,PP,KB,STROMB,ROGO,ROGU,MXB,MYB,STZU,IFMXY) call from stroem: 4th argument was kb, declared in globalVar.py
ELEM3(IFMK,P,PP,KX,STROM,ROG2,ROG4,MX,MY,STZU,IFMXY) called by stroem: 4th argument was KX
variables that already been declared in globalVar.py will not be passing as an argument.
MX & MY were the variables that required to update. Then they will be treated as a passing by value
This policy was started at July 24, 2019
"""

"""
Is the passing paramter in Fortran by reference?
"""

def ELEM3 (ifmk,pp,STROMB,rog2,rog4,stzu,ifmxy):
	"""it was assumed that rog has already been declared as 4 elements list"""
	globalVar.rog[0]=0.0
	globalVar.rog[1]=rog2
	globalVar.rog[2]=0.0
	"""in KONVEK1.FOR, rog[3] assigned twice consecutively. 1st as rog4, 2nd as -rog4"""
	globalVar.rog[3]=-rog4
	
	globalVar.Print1['xz']=0.0
	xn=0.0
	for i in range(4):
		if globalVar.kb[i] == 1.0e30:
			break
		"""when this sub routine was called from stroem, the 2nd argument was pb
		In this sub routine, pb was declared as p
		Because pb was declared in globalVar.py as a list with 4 elements, it was ignored in a passing parameter scheme"""
		globalVar.Print1['xz']=globalVar.Print1['xz']+(globalVar.pb[i]+globalVar.rog[i])/globalVar.kb[i]
		xn=xn+1./globalVar.kb[i]
		
	globalVar.Print1['xz']=globalVar.Print1['xz']+stzu
	pp=globalVar.Print1['xz']/xn
	
	"""this 4 elements list was declared locally on elem3, hopefully, it was a real a local variable
	"""
	mp=[]
	for i in range(4):
		mp.append(0.0)
	if ifmxy==1:
		for i in range(4):
			"""In globalVar, kx is 50 elements list variables
			"""
			if globalVar.addrt['kx'][i] == 1e30:
				break
			mp[i]=(globalVar.pb[i]+globalVar.rog[i]-pp)/addrt['kx'][i]
			
		STROMB=0.
		mx=mp(0)-mp(2)
		my=mp(1)-mp(3)
	return mx,my
	
