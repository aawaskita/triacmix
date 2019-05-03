import globalVar

def CALT3(i,n,ifk01):
	ifprnt=0
	ITER=0 """This is the first and probably the only one variable with all capital letters due to its corresponding lowercase was already used by python"""
	iterm=ihmax
	ovrelh=1.0
	globalVar.iterh['ihmax']=1.0e-10
	ia=i+globalVar.feld2['idiff']
	na=n+globalVar.feld2['ndiff']
	tf=globalVar.calc['tflu'][ia][na]
	kO=globalVar.feld2['kkb'][i][n]
	nz=globalVar.het1['nhzon'][k0]
	wtt=globalVar.calc['wt'][ia][na]/globalVar.het2['zkug'][i][n]
	"""index starts with 0"""
	globalVar.wc[0]=globalVar.calc['wl'][ia][na-1]
	globalVar.wc[2]=globalVar.calc['wl'][ia][na]
	globalVar.wc[3]=globalVar.calc['wi'][ia][na]
	globalVar.tm[0]=(globalVar.calc['t'][ia][na-1]+globalVar.Print['ar'][ia][na-1])/2.0+globalVar.basis['tbase']
	globalVar.tm[2]=(globalVar.calc['t'][ia][na+1]+globalVar.Print['ar'][ia][na+1])/2.0+globalVar.basis['tbase']
	globalVar.tm[3]=(globalVar.calc['t'][ia+1][na]+globalVar.Print['ar'][ia+1][na])/2.0+globalVar.basis['tbase']
	
	if ia !=1:
		globalVar.wc[1]=globalVar..calc['wi'][ia-1][na]
		globalVar.tm[1]=(globalVar.calc['t'][ia-1][na]+globalVar.Print['ar'][ia-1][na])/2.0+globalVar.basis['tbase']
	
	globalVar.wc[1]=0.0
	globalVar.tm[1]=0.0
	
	arand=0.0
	for j in range(4):
		arand=arand+globalVar.wc[j]*globalVar.tn[j]/globalVar.het2['zkug'][i][n]
		
	wq1=globalVar.bheter['wqk'][i][n]/globalVar.het2['zkug'][i][n]
	if ifk01 == -1:
		wtt=wtt+wq1
		wq1=wq1*tf
		
	wq2=globalVar.bheter['wqn'][i][n]/globalVar.het2['zkug'][i][n]
