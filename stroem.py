import globalVar
from frist import FRIST
from strlam import STRLAM
from elem3a import ELEM3A
from elem3b import ELEM3B
"""
KONTROL PERHITUNGAN ITERATIF TEKANAN DAN BIDANG ALIRAN. KRITERI KONVERGENSI ADALAH PENGINGAT ALIRAN MASSA (SERIAL).
HANYA PERHITUNGAN ALIRAN LAMINAR PSEUSO. BIDANG PENCETAKAN DAPAT DIATASI KHUSUS (---> TANPA PERHITUNGAN KONSTAN BARU)
"""

def STROEM(ifm1,ifm2):
	globalVar.ite2['ifgs']=0
	globalVar.itparm['ifg01']=0
	globalVar.ui['im']=globalVar.ui['im1']+1
	globalVar.ui['nm']=globalVar.ui['nm1']+1
	globalVar.Iter1['ovrel']=1.0
	globalVar.ite2['nvit']=0
	ifsqq=globalVar.Iter['ifsq']
	ifxkk=1
	mxb=1.0
	myb=1.0
	smaxa=1.0
	nita=1
	maxit=5
	maxi=0
	
	while ifsqq >= 100:
		ifsqq=ifsqq-100
		maxi=maxi+1
		maxit=maxi
		
	ifq1=ifsqq+1
	zwepsi=2.*globalVar.Iter['epsi2']
	fuepsi=5.*globalVar.Iter['epsi2']
	zeepsi=10.*globalVar.Iter['epsi2']
	zzepsi=20.*globalVar.Iter['epsi2']
	fzepsi=50.*globalVar.Iter['epsi2']
	
	if ifm1 != 1:
		if globalVar.Iter['it'] >= 100:
			ifxkk==0 """can a fortran create a variable without declaring it first?"""
		
		"""globalVar.Iter['it']<100"""
		niterm=1 """can a fortran create a variable without declaring it first?"""
		FRIST(globalVar.ui['start'])
		globalVar.Iter['it2']=0
		globalVar.ui['ifep']=0
		globalVar.Iter['it']=100
		STRLAM(ifkxx)
		globalVar.Iter['it2']=globalVar.Iter['it2']+1
	
	
	"""this is a returning point from quite far statement, what a messy program"""
	while True: """ loop until -> globalVar.aflux['nit'] !=1: met or globalVar.Iter['it2']<=3"""
		"""The first three lines were coincidence with the previous if-block
		"""
		globalVar.Iter['it']=100
		STRLAM(ifkxx)
		globalVar.Iter['it2']=globalVar.Iter['it2']+1
		if ifm1 == 1:
			niterm=1
		for niter in range(niterm): """until initial line 111 loop"""
			diff=1.0e10
			ifmxy=niterm-niter+1
			if globalVar.hohlr['nhlr'] != 0:
				for j in range(globalVar.hohlr['nhlr']):
					"""in this sub routine, pp was never be declared and instantiated, but accidentally be involced as an argument in ELEM3A"""
					ELEM3A(j,pp,ifm2,globalVar.Iter1['ovrel'],ifmxy)
					"""diff was never be declared and instantiated, how could this variable be compared?"""
					if pp < diff:
						diff=pp
			
			for i in range(1,globalVar.ui['im1']): """until initial line 101 loop"""
				for n in range(1,globalVar.ui['nm1']): """until initial line 100 loop"""
					ifb1=globalVar.TEMP['ifb'][i][n]+1
																
					if ifb1 == 2 or ifb1 ==5:
						kk=globalVar.komptx['kom'][i][n]
						stzu=globalVar.zwang['stzuk'][kk] * globalVar.geo['fzq'][n]* globalVar.geo['dz'][i]
						globalVar.pb[0]=globalVar.drukk['p'][i][n-1]
						globalVar.pb[2]=globalVar.drukk['p'][i][n+1]
						globalVar.kb[0]=globalVar.drukk['xkr'][i][n-1]
						globalVar.kb[2]=globalVar.drukk['xkr'][i][n]
						if globalVar.TEMP['ifb'][i-1][n] != 2:
							rogo=float(globalVar.prandl['rogg'][i-1][n])
							globalVar.pb[1]=globalVar.drukk['p'][i-1][n]
							globalVar.kb[1]=globalVar.drukk['xkz'][i-1][n]
						else: """line 401"""
							globalVar.ui['kk1']=globalVar.komptx['kom'][i-1][n]
							for nv in range(globalVar.verti['nverti']):
								kkk=globalVar.verti['kkomv'][nv]
								if kkk != globalVar.ui['kk1']:
									break
								else:
									io=globalVar.verti['iover'][n][nv]-1
									rogo=float(globalVar.verti['sumrg'][n][nv]+globalVar.prandl['rogg'][io][n])
									globalVar.kb[1]=globalVar.verti['sumxk'][n][nv]+globalVar.drukk['xkz'][io][n]
									globalVar.pb[1]=globalVar.drukk['p'][io][n]
											
										
						if globalVar.globalVar.TEMP['ifb'][i+1][n] != 2: """line 405"""
							rogu=float(globalVar.prandl['rogg'][i][n])
							globalVar.pb[3]=globalVar.drukk['p'][i+1][n]
							globalVar.kb[3]=globalVar.drukk['xkz'][i][n]
						else:"""line 402"""
							globalVar.ui['kk1']=globalVar.komptx['kom'][i+1][n]
							for nv in range(globalVar.verti['nverti']):
								kkk=globalVar.verti['kkomv'][nv]
								if kkk != kk1:
									break
								else:
									io=globalVar.verti['iuver'][n][nv]+1
									rogu=float(SglobalVar.verti['sumrg'][n][nv]+globalVar.prandl['rogg'][i][n])
									globalVar.kb[3]=globalVar.verti['sumxk'][n][nv]+globalVar.drukk['xkz'][i][n]
									globalVar.pb[3]=globalVar.drukk['p'][io][n]
										
						pp=globalVar.drukk['p'][i][n]
						"""the arguments that were passed through a function, should not be stated if they were already defined in globalVar
						I don't understand from where the STROMB comes, that is why it was written in capital
						mxb & myb were called by value"""
						mxb,myb = ELEM3 (ifm2,pp,globalVar.kb,STROMB,rogo,rogu,stzu,ifmxy)
						globalVar.drukk['mr'][i][n]=mxb/2
						globalVar.drukk['mz'][i][n]=myb/2
						if ifm1 != 1:
							globalVar.drukk['p'][i][n]=globalVar.drukk['p'][i][n]+(pp-globalVar.drukk['p'][i][n])*globalVar.Iter1['ovrel']
							if globalVar.drukk['p'][i][n] < diff:
								diff=globalVar.drukk['p'][i][n]
			
			"""line 110"""
			"""IF(NVERTI.GT.0) CALL ELEM3B(DIFF,OVREL,IFM2)"""
			if globalVar.verti['nverti'] > 0:
				ELEM3B(diff,ifm2)
				
			"""IF (NKUEL.GT.0) CALL ELEM 3C (DIFF,OVREL,IFM2)"""
			if globalVar.kuel1['nkuel'] > 0:
				ELEM3C(diff,ifm2)
				
			"""CALL KOPTE(1,-1,1,1,DRUCK,DIFF,OVREL)"""
			KOPTE(1,-1,1,1,diff)
			
			for i in range(1,im1):
				for n in range(1,nm1):
					globalVar.drukk['p'][i][n]=globalVar.drukk['p'][i][n]-diff
		
		"""line 111"""
		if niterm != 1:
			globalVar.ite2['nvit']=globalVar.ite2['nvit']+1
		
		globalVar.aflux['nit']=niterm
		niterm=1
		if globalVar.aflux['nit'] != 1:
			nita=globalVar.aflux['nit']
			"""how should I go to line 200?"""
	
	
