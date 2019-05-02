import globalVar

"""A function"""
def CALT2(i,n, ifk01):
	k1=1
	wqnin = globalVar.bheter['wqn'][i][n] / globalVar.blindl['brv']
	wqkin = globalVar.bheter['wqk'][i][n]
	kO = globalVar.feld2['kkb'][i][n]
	nz = globalVar.het1['nhzon'][kO]
	
	for k in range(nz):
		globalVar.the[k] = globalVar.berhet['thet'][i][n][k]
		globalVar.tha[k] = globalVar.bheter['thalt'][i][n][k]
		
	ibl=1
	CALT2H(i,n,ifk01,wqnin,wqkin,the,tha,nz,k0,ibl)
	
	for k in range(nz):
		globalVar.berhet['thet'][i][n][k] = globalVar.the[k]
		
	globalVar.blindl['tmitl'] = globalVar.blindl['brv'] * globalVar.berhet['thet'][i][n][k1]
	
	if globalVar.blindl['blv'] != 0:
		wqnin = 0.
		for k in range(nz):
			globalVar.the[k] = globalVar.blindl['thetb'][i][n][k]
			globalVar.tha[k] = globalVar.blindl['thaltb'][i][n][k]
		
		ibl=2
		CALT2H(i,n,ifk01,wqnin,wqkin,the,tha,nz,kO,ibl)
		
		for k in range(nz):
			globalVar.blindl['thetb'][i][n][k] = globalVar.the[k]
			
		globalVar.blindl['tmitl'] = globalVar.blindl['tmitl'] + globalVar.blindl['blv'] * globalVar.blindl['thetb'][i][n][k1]
