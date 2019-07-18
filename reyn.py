import globalVar
from vau import VAU
from ethag import ETHAG

def REYN(i,n):
	ifb1=globalVar.TEMP['ifb'][i][n]+1
	reyn=0 """this variable uses the same name with its function because this modul was derived from fortran"""
	if ifb1==1:
		return reyn
		
	tem1=(globalVar.TEMP['tfl'][i][n]+globalVar.TEMP['t'][i][n])/2
	tem2=(globalVar.TEMP['tfl'][i-1][n]+globalVar.TEMP['t'][i-1][n])/2
	tem3=(globalVar.TEMP['tfl'][i][n-1]+globalVar.TEMP['t'][i][n-1])/2
	tem4=(globalVar.TEMP['tfl'][i-1][n-1]+globalVar.TEMP['t'][i-1][n-1])/2
	tem=(tem1+tem2+tem3+tem4)/4
	kk=globalVar.komptx['kom'][i][n]
	globalVar.konst['epsi']=globalVar.spezi['epsil'][kk]
	et=ETHAG(tem)
	v=VAU(i,n)
	
	"""if ifb1 == 1:
		return reyn"""
	if ifb1 ==2:
		reyn = globalVar.konst['rek'] * globalVar.TEMP['rho'][i][n] * v/et/(1.-globalVar.konst['epsi']) 
		"""is there any special reason why the fractional symbol was written twice consecutively?"""
	else:
		reyn=globalVar.TEMP['rho'][i][n] * v/globalVar.konst['epsi']*globalVar.spezi['dhyd'][kk]/et/100.
		
	return reyn
