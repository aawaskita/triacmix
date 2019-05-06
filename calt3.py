import globalVar

def CALT3(i,n,ifk01):
	ifprnt=0
	ITER=0 """This is the first and probably the only one variable with all capital letters due to its corresponding lowercase was already used by python"""
	iterm=.iterh['ihmax']
	ovrelh=1.0
	dttt=1.0e-10
	while ITER <= iterm  and dttt > 0.01:
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
		nzm=nz-1
		for k in range(nzm):
			tt=(globalVar.berhet['thet'][i][n][k]+globalVar.berhet['thet'][i][n][k+1])/2.
			dO=globalVar.setwd['dos'][k0] """is it true? d0 will only depends on k0"""
			if d0 < 0:
				dO=globalVar.setwd['zdos'][na] """d0 will only depends on na?"""
			mat=globalVar.het['nhmat1'][k0][k]
			alam0=globalVar.komp1['lam'][k0]
			globalVar.wc[k]=globalVar.berhet['wwk'][k0][k]*XLAMT(tt,dO,mat,alam0,ifprnt)
		
		for k in range(nz):
			globalVar.tm[k]=(globalVar.berhet['thet'][i][n][k]+globalVar.bheter['thalt'][i][n][k])/2.0
		
		dt=globalVar.berhet['thet'][i][n][1]
		globalVar.berhet['thet'][i][n][1]=(globalVar.bheter['thalt'][i][n][1]*(globalVar.berhet['wkaph'][i][n][0][0]-globalVar.wc[0]/2.0-wtt/2.0)+globalVar.wc[0]*globalVar.tm[1]+wq2*globalVar.het1['xfwqz'][k0][0]+arand+wq1)/(globalVar.berhet['wkaph'][i][n][0][0]+globalVar.wc[0]/2.+wtt/2.)
		dtt=dt-globalVar.berhet['thet'][i][n][0]
		if dtt < 0:
			dtt=dtt/dt
		
		if dtt > 0:
			dtt=dtt/globalVar.berhet['thet'][i][n][0]
	
		dtt=abs(dtt)
		if dtt > globalVar.iterh['dttt']:
			globalVar.iterh['dttt']=dtt
		
		globalVar.berhet['thet'][i][n][0]=dt-(dt-globalVar.berhet['thet'][i][n][0])*ovrelh
		globalVar.tm[0]=(globalVar.berhet['thet'][i][n][0]+globalVar.bheter['thalt'][i][n][0])/2.0
	
		if nz>2:
			for k in range(1,nzm):
				dt=globalVar.berhet['thet'][i][n][k]
				globalVar.berhet['thet'][i][n][k]=(globalVar.bheter['thalt'][i][n][k]*(globalVar.berhet['wkaph'][i][n][k][0]-globalVar.wc[k]/2.0-globalVar.wc[k-1]/2.0)+globalVar.wc[k]*globalVar.tm[k+1]+globalVar.wc[k-1]*globalVar.tm[k-1]+wq2*globalVar.het1['xfwqz'][k0][k])/(globalVar.berhet['wkaph'][i][n][k][0]+globalVar.wc[k]/2.+globalVar.wc[k-1]/2.0)
				dtt=dt-globalVar.berhet['thet'][i][n][k]
				if dtt < 0:
					dtt=dtt/dt
				if dtt > 0:
					dtt=dtt/globalVar.berhet['thet'][i][n][k]
				dtt=abs(dtt)
				if dtt > dttt:
					dttt=dtt
				globalVar.berhet['thet'][i][n][k]=dt-(dt-globalVar.berhet['thet'][i][n][k])*ovrelh
				globalVar.tm[k]=(globalVar.berhet['thet'][i][n][k]+globalVar.bheter['thalt'][i][n][k])/2.0
			
		dt=globalVar.berhet['thet'][i][n][nz]
		globalVar.berhet['thet'][i][n][nz]=(globalVar.bheter['thalt'][i][n][nz]*(globalVar.berhet['wkaph'][i][n][nz][0]-globalVar.wc[nz-1]/2.)+globalVar.wc[nz-1]*globalVar.tm[nz-1]+wq2*globalVar.het1['xfwqz'][k0][nz])/(globalVar.berhet['wkaph'][i][n][nz][0]+globalVar.wc[nz-1]/2.0)
		dtt=dt-globalVar.berhet['thet'][i][n][nz]
	
		if dtt < dt:
			dtt=dtt/dt
		
		if dtt > 0:
			dtt=dtt/globalVar.berhet['thet'][i][n][nz]
		
		dtt=abs(dtt)
		if dtt > globalVar.iterh['dttt']:
			globalVar.iterh['dttt']=dtt
	
		globalVar.berhet['thet'][i][n][nz]=dt-(dt-globalVar.berhet['thet'][i][n][nz])*ovrelh
		ITER=ITER+1
	
	if ITER > iterm:
		print(i,n,ITER,dttt)
