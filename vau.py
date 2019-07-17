import globalVar
import math

def VAU(i,n):
	"""VAU= SQRT((MZ(I,N)/FZQ(N))**2+(MR(I,N)/FRQ(I,N))**2)/RHO(I,N)"""
	a=globalVar.drukk['mz'][i][n]/globalVar.geo['fzq'][n]
	b=globalVar.drukk['mr'][i][n]/globalVar.geo['frq'][i][n]
	c=globalVar.TEMP['rho'][i][n]
	return math.sqrt(a**2+b**2)/c
