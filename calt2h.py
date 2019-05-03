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
	for j in range(4):
		arand=arand+globalVar.wc[j]*globalVar.tm[j]/globalVar.het2['zkug'][i][n]
		
	wq1=wqkin/globalVar.het2['zkug'][i][n] * brkon
	if ifk01 == -1:
		wtt=wtt+wq1
		
	if ifk01 ==-1:
		wq1=wq1-tf

	wq2=wqnin/globalVar.het2['zkug'][i][n]
	nzm=nz-1
	for k in range(nzm):
		tt=(globalVar.the[k] + globalVar.the[k+1])/2.
		d0=dos[k0]
		if d0 < 0:
			d0=globalVar.setwd['dos'][na]
		mat=globalVar.het['nhmat1'][k0][k]
		alam0=globalVar.komp1['lam'][k0]
		globalVar.ui['xla'] = XLAMT(tt,dO,mat,alam0,ifprnt)
		globalVar.wc[k]=globalVar.berhet['wwk'][k0][k] * globalVar.ui['xla']
		
	for j in range(nz):
		for k in range(nz):
			globalVar.xkoeff[j][k]=0.0
			
	wka1 = globalVar.berhet['wkaph'][i][n][1][ibl]
	"""index starts with 0"""
	globalVar.xkoeff[0][0]=-wtt-globalVar.wc[0]-2.0 * wka1
	globalVar.xkoeff[0][1]=globalVar.wc[0]
	globalVar.xkoeff[nz][nz-1]=globalVar.wc[nz-1]
	wka = globalVar.berhet['wkaph'][i][n][nz][ibl]
	globalVar.xkoeff[nz][nz] = -globalVar.wc[nz-1]-2.0 * wka
	globalVar.xinh[0] = -arand-wq1-wq2 * globalVar.het1['xfwqz'][k0][0]-2.0 * wka1 * globalVar.tha[0]
	globalVar.xinh[nz]=-wq2*globalVar.het1['xfwqz'][k0][nz]-2.0 * wka * globalVar.tha[nz]
	
	if nz >= 2:
		"""index starts with 0"""
		for nk in range(1,nzm):
			wka = globalVar.berhet['wkaph'][i][n][nk][ibl]
			globalVar.xinh[nk]=-wq2*globalVar.het1['xfwqz'][k0][nk]-2.0 * wka * globalVar.tha[nk]
			globalVar.xkoeff[nk][nk-1] = globalVar.wc[nk-1]
			globalVar.xkoeff[nk][nk] = -globalVar.wc[nk] - globalVar.wc[nk-1]-2.0 * wka
			globalVar.xkoeff[nk][nk+1] = globalVar.wc[nk]
			
	for k in range(nzm):
		k1=k+1
		xmult=globalVar.xkoeff[k1][k]/globalVar.xkoeff[k][k]
		for kk in range(nz):
			globalVar.xkoeff[k1][kk]=globalVar.xkoeff[k1][kk]-xmult * globa.xkoeff[k][kk]
		globalVar.xinh[k1]=globalVar.xinh[k1]-xmult*globalVar.xinh[k]

	for j in range(nz):
		if globalVarxkoeff[j][j] == 0:
			globalVar.xkoeff[j][j] = globalVar.xinh[j] / globalVar.tha[j]
			
	for k in range(nz):
		kk=nz+1-k
		globalVar.x[kk]=globalVar.xinh[kk]/globalVar.xkoeff[kk][kk]
		globalVar.the[kk]=2.0*globalVar.x[kk]-globalVar.tha[kk]
		if kk!=0:
			globalVar.xinh[kk-1]=globalVar.xinh[kk-1]-globalVar.x[kk]*globalVar.xkoeff[kk-1][kk]
