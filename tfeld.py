import globalVar

def TNEU(i,n):
	dt = globalVar.Iter1['tn']-globalVar.calc['t'][i][n]
	tneu = globalVar.calc['t'][i][n]+dt*globalVar.Iter1['ovrel']
	trel = abs(dt)
	if globalVar.Iter1['trmax'] <= trel:
		globalVar.Iter1['trmax']=trel
		globalVar.Iter1['ifkor']=0
		globalVar.Iter1['itmax']=1
		globalVar.Iter1['ntmax'] = n
		globalVar.ui['t1'] = globalVar.Iter1['tn']
		globalVar.Iter1['t2']= globalVar.calc['t'][i][n]

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
	if globalVar.lamt['iflamt'] != 0:
		if globalVar.trans['ifinst'] !=1:
			if itl >= itlam:
				KONST1(0)
				itl=0
				
	globalVar.Iter1['trmax']=0.0
	if ifinst != 1:
		if globalVar.Iter1['ifrel']==0:
			for n in range(1,globalVar.ui['nm1']):
				for i in range(globalVar.ui['im1']):
					if globalVar.zus['ifber'][i][n] < 1:
						break
					else:
						k=globalVar.komp1['kom'][i][n]
						ii=i-globalVar.feld2['idiff']
						nn=n-globalVar.feld2['ndiff']
						if ii>=1 or nn>=1 or ii<=globalVar.feld2['imh'] or nn<=globalVar.feld2['nmh']: 
							if globalVar.berhet['ifbh'][ii][nn] != 0:
								if globalVar.het['nhmat1'][k][0]==globalVar.blindl['m24']:
									globalVar.setwd['dos'][k]=globalVar.blindl['dosi'][i][n]
								CALTA(ii,nn,ifkO1)
								globalVar.Iter1['tn']=globalVar.blindl['tmitl']-globalVar.basis['tbase']
						else:
							globalVar.Iter1['tn']=CALT(i,n,ifkO1) """471"""
						globalVar.calc['t'][i][n]=TNEU(i,n) """472"""
		else: """112"""
			for i in range(ia,globalVar.ui['im1']):
				for n in range(1,globalVar.ui['nm1']):
					if globalVar.zus['ifber'][i][n]>=1: 
						k=globalVar.komp1['kom'][i][n]
						ii=i-globalVar.feld2['idiff']
						nn=n-globalVar.feld2['ndiff']
						if ii>=1 or nn>=1 or ii<=globalVar.feld2['imh'] or nn<=globalVar.feld2['nmh']:
							if globalVar.berhet['ifbh'][ii][nn] != 0:
								if globalVar.het['nhmat1'][k][0] == globalVar.blindl['m24']:
									globalVar.setwd['dos'][k]=globalVar.blindl['dosi'][i][n]
								CALTA(ii,nn,ifkO1)
								globalVar.Iter1['tn']=globalVar.blindl['tmitl']-globalVar.basis['tbase']
						else: """571"""
							globalVar.Iter1['tn']=CALT(i,n,ifkO1)
						globalVar.calc['t'][i][n]=TNEU(i,n)
					else: """301"""
						
	else: """302"""		
