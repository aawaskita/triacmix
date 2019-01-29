import globalVar

def STEUER(ifkon,itlam,tdiff,nloop,ifred,ifzw,itm3,cp0,iftest,nhet,zeith,xfr,iexpr,n200,ndr,nxs,pov,zf,nry,qnw,deldz,qthx,wtgint):
	nendk0=nendpt+1
	globalVar.ui['nulein']=-1
	tkel=273.0
	n55=55
	iti55=0

	if globalVar.specti['itik'][7]==1:
		iti55=1
	globalVar.specti['itik'][7]=0
	iri=0

	if globalVar.specti['itik'][1]>1 and globalVar.specti['itik'][10]==1:
		iri=1

	if globalVar.specti['itik'][9]<=0: """if else goto 12"""
		ifwarn=0
		ifppp=0
		ifkst=0
		globalVar.ui['ifkst']=0

	if globalVar.trans['ifinst'] ==0 and globalVar.ui['ifkon'] !=0:
		ifkst=1
		
	if iftest==1:
		intest(ifwarn,cp0)
		
	ifzent=1
	"""IF(INDGEO.EQ.2.AND.RAD0.EQ.0.) IFZENT=1 -> kenapa """
	
	if globalVar.feld2['imh']>=1 and globalVar.feld2['nmh']>=1:
		for i in range(1,feld2['imh']+1):
			for n in range(1,feld2['nmh']+1):
				ia=i+globalVar.feld2['idiff']
				na=n+globalVar.feld2['ndiff']
				"""K=KOM(IA,NA)"""
				k=globalVar.komp1['kom'][ia][na]
				if3=globalVar.berhet['ifbh'][i][n]
				globalVar.bheter['wqk'][i][n]=0
				globalVar.bheter['wqn'][i][n]=0
				tt=globalVar.calc['t'][ia][na]
				if if3==0 and globalVar.rstrt['ifrsta']<3:
					for IS in range(2,6):
						globalVar.berhet['thet'][i][n][IS]=0.0
						globalVar.blindl['thetb'][i][n][IS]=0.0
				globalVar.berhet['thet'][i][n][1]=tt
				globalVar.blindl['thetb'][i][n][1]=tt
				if if3!=0:
					globalVar.ui['kk1']=feld2['kkb'][i][n]
					nzz=globalVar.het1['nhzon'][globalVar.ui['kk1']]
					for NZ in range(2,nzz+1):
						globalVar.berhet['thet'][i][n][NZ]=tt
						globalVar.blindl['thetb'][i][n][NZ]=tt
						
		globalVar.ztpt['nzp']=0
		globalVar.ui['ifselb']=0
		globalVar.ui['ntape']=0
		zeith=0.0
		
		if globalVar.rstrt['ifrsta'] == 2 or globalVar.rstrt['ifrsta']>=4: zeith = globalVar.rstrt['zrst']
		
		globalVar.bilanz['izael']=0
		ovrm=globalVar.Iter1['ovrel']
		z1=globalVar.trans['zei'][1]
		z2=zeith+globalVar.trans['dzeit'][1]/3600.0
		
		if globalVar.trans['ifinst']==1 or z1 < z2:
			globalVar.trans['zei'][1]=zeith + 2.0*globalVar.trans['dzeit'][1]/3600.0
			
		for i in range(1,globalVar.komp1['kmax']+1):
			globalVar.jug[i]=0
			if globalVar.tvar['ntvar'][i]>0:
				globalVar.jug[i]=2
				
		globalVar.ui['ifneu']=0
		zeits=zeith * 3600
		globalVar.ui['delta']=0.1
		
		for k in range(globalVar.komp1['kmax']):
			qquel1[k]=0.0
			buins[k]=0.0
			qspei1[k]=0.0
			qkons1[k]=0.0
			qps1[k]=0.0
			"""initializing qspeiz, qkonvz and qnuklz are conducted in globalVar"""
			
		globalVar.ui['geofak']=1.0
		if globalVar.Print['indgeo']==2:
			globalVar.ui['geofak']=1000.0
			
		ifko1=1
		if globalVar.ui['ifkon']==-1:
			ifko1=-1
			
		globalVar.ui['fakz']=1.0
		globalVar.ui['xf']=xfr
		globalVar.ui['intv']=1
		globalVar.ui['nlp']=0
		globalVar.ui['ifstop']=0
		globalVar.ui['im']=globalVar.reg['imax']
		globalVar.ui['nm']=globalVar.reg['nmax']
		globalVar.ui['im1']=globalVar.ui['im']-1
		globalVar.ui['nm1']=globalVar.ui['nm']-1
		globalVar.ui['iflt1']=globalVar.lamt['iflamt']+1
		globalVar.ui['ifdt2']=0
		globalVar.ui['nko']=0
		dtem1=globalVar.trans['dzeit'][globalVar.ui['intv']]
		globalVar.ui['dtem4']=dtem1
		globalVar.ui['ifsfb']=0
		if globalVar.feld2['imh']>=1 or globalVar.feld2['nmh']>=1:
			for ii in range(globalVar.feld2['imh']):
				for nn in range(globalVar.feld2['nmh']):
					"""KK=KOM(IGG,NGG)"""
					igg=globalVar.feld2['idiff']+ii
					ngg=globalVar.feld2['ndiff']+nn
					kk=globalVar.komp1['kom'][igg][ngg]
					if1=globalVar.berhet['ifbh'][ii][nn]
					if if1 != 0:
						globalVar.het2['zkug'][ii][nn]=
