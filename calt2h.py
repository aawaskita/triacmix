import globalVar

"""A function"""
def CALT2H(i,n,ifk01,wqnin,wqkin,the,tha,nz,kO,ibl):
	ifprnt=0
	ia=i+globalVar.feld2['idiff']
	na=n+globalVar.feld2['ndiff']
	tf=globalVar.calc['tflu'][ia][na]
	brkon = 1.
	wtt=globalVar.calc['wt'][ia][na]/globalVar.het2['zkug'][i][n]
	globalVar.wc[0]=globalVar.calc['wl'][ia][na-1]
	globalVar.wc[2]=globalVar.calc['wl'][ia][na]
	globalVar.wc[3]=globalVar.calc['wi'][ia][na]
	globalVar.tm[0]=(globalVar.calc['t'][ia][na-1]+globalVar.Print['ar'][ia][na-1])/2.0+globalVar.basis['tbase']
	globalVar.tm[2]=(globalVar.calc['t'][ia][na+1]+globalVar.Print['ar'][ia][na+1])/2.0+globalVar.basis['tbase']
	globalVar.tm[3]=(globalVar.calc['t'][ia+1][na]+globalVar.Print['ar'][ia+1][na])/2.0+globalVar.basis['tbase']
	
	if ia != 1:
		globalVar.wc[1]=globalVar.calc['wi'][ia-1][na]
		globalVar.tm[1]=(globalVar.calc['t'][ia-1][na]+globalVar.Print['ar'][ia-1][na])/2.0+globalVar.basis['tbase']
	else:
		globalVar.wc[1]=0.0
		globalVar.tm[1]=0.0
		
	arand=0.0
