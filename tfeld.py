import globalVar

def TFELD(itlam,ovrm,ifk01,ifwarn,cp0,ifzent):
	FRIST()
	globalVar.Iter1['mit']=0
	globalVar.ui['im1']=globalVar.reg['imax']-1
	globalVar.ui['nm1']=globalVar.reg['nmax']-1
	ia=2
	if ifzent==1:
		ia=1
	itl=0
	globalVar.Iter1['ifkor']=1
	trmin=1.E10
	ikor=0
	ovmax=ovrm
	globalVar.Iter1['ovrel']=globalVar.Iter1['ormin']
	globalVar.Iter1['ovrel']=1.0 """THERMIX4.FOR line 424-425"""
	globalVar.basis['tbase']=0.0
	mitb=0
	while True:
		tmx=-1.E10
		for i in range(globalVar.reg['imax']):
			for n in range(globalVar.reg['nmax']):
				if globalVar.calc['t'][i][n] > tmx:
					tmx=globalVar.calc['t'][i][n] """???"""
				
		for i in range(globalVar.reg['imax']):
			for n in range(globalVar.reg['nmax']):
				globalVar.calc['t'][i][n]=globalVar.calc['t'][i][n]-tmx

		if globalVar.trans['ifinst'] == 1:
			for i in range(globalVar.reg['imax']):
				for n in range(globalVar.reg['nmax']):
					globalVarPrint['ar'][i][n]=globalVarPrint['ar'][i][n]-tmx
				
		globalVar.basis['tbase']=globalVar.basis['tbase']+tmx

		dttm=1.E-10
		globalVar.Iter1['mit']=globalVar.Iter1['mit']+1
		mitb=mitb+1
		if mitb<50:
			break
			
	itl=itl+1
	
