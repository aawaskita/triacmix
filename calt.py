import globalVar

def calt(i,n, ifk01):
	tnn=globalVar.calc['t'][i][n-1]
	tff=0.1
	if ifk01==-1:
		tff=globalVar.calc['tflu'][i][n] - globalVar.basis['tbase']-tnn
		
	b1=globalVar.Print['bu'][i][n]*tff+globalVar.calc['bu1'][i][n]
	b2=globalVar.Print['bu'][i][n]
	
	if ifk01!=-1:
		b2=0
		
	if i==1:
		return ((globalVar.calc['t'][i][n+1]-tnn)*globalVar.calc['wl'][i][n]+(globalVar.calc['t'][i+1][n]-tnn)*globalVar.calc['wi'][i][n]+b1)/(globalVar.calc['wt'][i][n]+b2) + tnn
	else:
		return ((globalVar.calc['t'][i-1][n]-tnn)*globalVar.calc['wi'][i-1][n]+(globalVar.calc['t'][i][n+1]-tnn)*globalVar.calc['wl'][i][n]+(globalVar.calc['t'][i+1][n]-tnn)*globalVar.calc['wi'][i][n]+b1)/(globalVar.calc['wt'][i][n]+b2) + tnn
