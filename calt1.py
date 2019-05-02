import globalVar

"""A function"""
def CALT1(i,n, ifk01):
	tf=1.0
	"""indeks start from 0"""
	globalVar.tm[0]=globalVar.calc['t'][i][n-1]+globalVar.Print['ar'][i][n-1]
	globalVar.tm[2]=globalVar.calc['t'][i][n+1]+globalVar.Print['ar'][i][n+1]
	globalVar.tm(3)=globalVar.calc['t'][i+1][n]+globalVar.Print['ar'][i+1][n]
	
	if ifk01 == -1:
		tf=globalVar.calc['tflu'][i][n]-globalVar.basis['tbase']
		
	globalVar.wc[0]=globalVar.calc['wl'][i][n-1]
	globalVar.wc[2]=globalVar.calc['wl'][i][n]
	globalVar.wc[3]=globalVar.calc['wi'][i][n]
	
	if i != 1:
		globalVar.tm[1]=globalVar.calc['t'][i-1][n] + globalVar.Print['ar'][i-1][n]
		globalVar.wc[1]=globalVar.calc['wi'][i-1][n]
	else:
		globalVar.wc[1]=0.0
		globalVar.tm[1]=0.0
		
	tst=2.0 * globalVar.Print['ar'][i][n]
	globalVar.Print1['xz']=0.0
	b1=globalVar.Print['bu'][i][n] * tf + globalVar.calc['bu1'][i][n]
	b2=globalVar.Print['bu'][i][n]/2.0
	
	if ifk01 != -1:
		b2 = 0.
		
	for j in range(4):
		globalVar.Print1['xz']=globalVarPrint1['xz']+(globalVar.tm[j]-tst)*globalVar.wc[j]
		
	globalVar.Print1['xz']=globalVar.Print1['xz']+b1-b2*tst
	xn=globalVar.calc['wt'][i][n]+b2
	
	return globalVar.Print1['xz']/xn+globalVar.Print['ar'][i][n]
