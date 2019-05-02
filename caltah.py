import globalVar

def CALTAH(i,n,ifk01,wqnin,wqkin,nz,k0):
	ifprnt=0
	ia=i+globalVar.feld2['idiff']
	na=n+globalVar.feld2['ndiff']
	tf=globalVar.calc['tflu'][ia][na]
	brkon=1.0
	
	if ifk01!=-1:
		x1=1.0
		tt=tf-globalVar.calc['t'][ia][na]
		if abs(tt < x1):
			if tt>=0:
				tt=abs(tt)
			if tt<0:
				tt=-abs(tt)
		brkon = (tf - globalVar.the[1) / tt
	wtt=globalVar.calc['wt'][ia][na]/globalVar.het2['zkug'][i][n]
	"""indeks wc dan tm mengikuti python, dimulai dari 0"""
	globalVar.wc[0]=globalVar.calc['wl'][ia,na-1]
	globalVar.wc[2]=globalVar.calc['wl'][ia,na]
	globalVar.wc[3]=globalVar.calc['wi'][ia,na]
	globalVar.tm[0]=globalVar.calc['t'][ia,na-1]+globalVar.basis['tbase']
	globalVar.tm[2]=globalVar.calc['t'][ia,na+1]+globalVar.basis['tbase']
	globalVar.tm[3]=globalVar.calc['t'][ia+1,na]+globalVar.basis['tbase']
	
	if ia==1:
		globalVar.wc[1]=0
		globalVar.tm[1]=0
	else:
		globalVar.wc[1]=globalVar.calc['wi'][ia-1,na]
		globalVar.tm[1]=globalVar.calc['t'][ia-1,na]+globalVar.basis['tbase']
	
	arand=0
	for j in range(4):
		arand=arand+globalVar.wc[j]*globalVar.tm[j]/globalVar.het2['zkug'][i][n]
		
	wq1=wqkin/globalVar.het2['zkug'][i][n]*brkon
	if ifk01==-1:
		wtt=wtt+wq1

	if ifk01 ==-1:
		wq1=wq1*tf

	wq2=wqnin/globalVar.het2['zkug'][i][n]
	nzm=nz-1
	for k in range(nzm):
		tt=(globalVar.the[k]+globalVar.the[k+1])/2.
		d0=globalVar.setwd['dos'][k0]
		if d0 < 0:
			d0=globalVar.setwd['zdos'][na]
			
		mat=globalVar.het['nhmat1'][kO][k]
		alam0=globalVar.komp1['lam'][kO]
		
		if wq2>0 or k==1:
			globalVar.ui['xla']=XLAMT(tt,d0,mat,alam0,ifprnt)
			
		globalVar.wc[k]=globalVar.berhet['wwk'][k0,k]*globalVar.ui['xla']
	
	for j in range(nz):
		for k in range(nz):
			globalVar.xkoeff[j][k]=0.0
			
	globalVar.xkoeff[1][1]=-wtt-globalVar.wc[1]
	globalVar.xkoeff[1][2]=globalVar.wc[1]
	globalVar.xkoeff[nz,nz-1]=globalVar.wc[nz-1]
	globalVar.xkoeff[nz][nz]=-globalVar.wc[NZ-1]
	globalVar.xinh[1]=-arand-wq1-wq2*globalVar.het1['xfwqz'][kO][1]
	globalVar.xinh[nz]=-wq2*globalVar.het1['xfwqz'][kO][nz]
	
	if nz > 2:
		for nk in range(1,nzm):
			globalVar.xinh[nk]=-wq2*globalVar.het1['xfwqz'][k0][nk]
			globalVar.xkoeff[nk][nk-1]=globalVar.wc[nk-1]
			globalVar.xkoeff[nk][nk]=-globalVar.wc[nk]-globalVar.wc[nk-1]
			globalVar.xkoeff[nk][nk+1]=globalVar.wc[nk]
			
	for k in range(nzm):
		k1=k+1
		xmult=globalVar.xkoeff[k1][k]/globalVar.xkoeff[k][k]
		for kk in range(nz):
			globalVar.xkoeff[k1][kk]=globalVar.xkoeff[k1][kk]-xmult*globalVar.xkoeff[k][kk]
		globalVar.xinh[k1]=globalVar.xinh[k1]-xmult*globalVar.xinh[k]
		
	for k in range(nz):
		"""line 2181-2187"""
		
	for k in range(nz):
		kk=nz+1-k
		globalVar.x[kk]=globalVar.xinh[kk]/globalVar.xkoeff[kk][kk]
		globalVar.the[kk]=globalVar.x[kk]
		if kk!=0:
			"""asumsi indeks dimulai dari 0"""
			globalVar.xinh[kk-1]=globalVar.xinh[kk-1]-globalVar.x[kk]*globalVar.xkoeff[kk-1][kk]
