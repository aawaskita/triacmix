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
