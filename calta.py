import globalVar

def CALTA(i,n,ifkO1):
	k1=1
	"""or k1=0 to respond to line 19"""
	wqnin=globalVar.bheter['wqn'][i][n] / globalVar.blindl['brv']
	wqkin=globalVar.bheter['wqk'][i][n] / globalVar.blindl['brv']
	k0=globalVar.feld2['kkb'][i][n]
	nz=globalVar.het1['nhzon'][k0]
	
	for k in range(nz):
		globalVar.the[k] = globalVar.berhet['thet'][i][n][k]

	CALTAH(i,n,ifk01,wqnin,wqkin,globalVar.the,nz,k0)

	for k in range(nz):
		globalVar.berhet['thet'][i][n][k] = globalVar.the[k]
	
	globalVar.blindl['tmitl'] = globalVar.blindl['brv'] * globalVar.berhet['thet'][i][n][k1]
	if globalVar.blindl['blv'] !=0:
		wqnin=0.0
		wqkin=0.0
	
	for k in range(nz):
		globalVar.the[k] = globalVar.berhet['thet'][i][n][k]

	CALTAH(i,n,ifk01,wqnin,wqkin,globalVar.the,nz,k0)
	
	for k in range(nz):
		globalVar.berhet['thet'][i][n][k] = globalVar.the[k]
		
	TMITL = TMITL + BLV * THETB(I,N,K1)
	globalVar.blindl['tmitl'] = globalVar.blindl['tmitl'] + globalVar.blindl['blv'] * globalVar.berhet['thet'][i][n][k1]
