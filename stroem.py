import globalVar
from frist import FRIST
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
		"""FRIST(start) start was accidentatlly appeared with being declare first"""
		
	"""if ifm1==1"""
