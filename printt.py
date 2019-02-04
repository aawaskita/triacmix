import globalVar

def PRINTT(zeith,zeits,dtem1,bu,ifph):
	"""
	IZH=IFIX(ZEITH), IFIX: convert real to integer
	"""
	izh=int(zeith) """hour"""
	izmin=int((zeith-izh)*60) """minutes"""
	zs=(zeith-izh)*3600 - izmin*60 """seconds"""
	if globalVar.Print['indgeo']==1:
		for n in range(globalVar.reg['nmax']):
			globalVar.reg['phi'][n]=globalVar.reg['phi'][n]*180/3.1416
			
	i1=1
	i2=i1+16
	if i2 > globalVar.reg['imax']: i2=globalVar.reg['imax']
	
	"""
	In this space, a code will writing out:
	1. bezei['bi'], reg['rad']
	2. bezei['bn']
	that I currently do not understand, whether to a file or any specific devices. But the most important clue is in variable N61
	"""
	
	"""
	In this space, there also a for loop (in range of reg['nmax']) for writing
	1. reg['phi']
	2. feld[]
	and the most important clus is still in variable N61
	"""
	
	
	
	
