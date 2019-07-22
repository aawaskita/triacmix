import globalVar
from frist import FRIST
from strlam import STRLAM
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
	mxb=1
	myb=1
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
	
	"""this is a returning point from quite far statement, what a messy program"""
		while True: """ loop until -> globalVar.aflux['nit'] !=1: met"""
			globalVar.Iter['it']=100
			STRLAM(ifkxx)
			globalVar.Iter['it2']=globalVar.Iter['it2']+1
			if ifm1 == 1:
				niterm=1
			for niter in range(niterm):
				diff=1.0e10
				ifmxy=niterm-niter+1
				if globalVar.hohlr['nhlr'] != 0:
					for j in range(globalVar.hohlr['nhlr']):
						
			
			
			nita=globalVar.aflux['nit']
	"""if ifm1==1"""
	
	
