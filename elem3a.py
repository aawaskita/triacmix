import globalVar

def ELEM3A(j,ppn,ifmk,ovrel,ifmxy):
	kp=globalVar.hohlr['kpar'][j]
	globalVar.Print1['xz']=0.0
	xn=0.0
	for ip in range(kp):
		i=globalVar.hohlr['ipar'][ip][j]
		n=globalVar.hohlr['npar'][ip][j]
		l=globalVar.hohlr['jpar'][ip][j]
		if l==1:
			xk=globalVar.drukk['xkr'][i][n]
			globalVar.ui8['pb']=globalVar.drukk['p'][i][n]
			globalVar.ui8['rog']=0.0
		if l==2:
			if globalVar.TEMP['ifb'][i][n] != 2:
				xk=globalVar.drukk['xkz'][i][n]
				globalVar.ui8['rog']=float(globalVar.prandl['rogg'][i][n])
				globalVar.ui8['pb']=globalVar.drukk['p'][i][n]
			else:
				l=3
				break """from KONVEK1, it should leave this if l==2 section immediately when ifb == 2"""
				
			k0=globalVar.komptx['kom'][i][n]
			for nv in range(globalVar.verti['nverti']):
				k01=globalVar.verti['kkomv'][nv]
				if k0 == k01:
					io=globalVar.verti['iover'][n][nv]-1
					xk=globalVar.verti['sumxk'][n][nv]+globalVar.drukk['xkz'][io][n]
					globalVar.ui8['rog']=float(globalVar.verti['sumrg'][n][nv]+globalVar.prandl['rogg'][io][n])
					globalVar.ui8['pb']=globalVar.drukk['p'][io][n]
				else:
					l=3
					break """from KONVEK1, it should leave this if l==2 section immediately when k0!=k01"""
		if l==3:
			xk=globalVar.drukk['xkr'][i][n-1]
			globalVar.ui8['pb']=globalVar.drukk['p'][i][n]
			globalVar.ui8['rog']=0.0
		if l=4:
			if globalVar.TEMP['ifb'][i][n] != 2:
				xk=globalVar.drukk['xkz'][i-1][n]
				globalVar.ui8['pb']=globalVar.drukk['p'][i][n]
				globalVar.ui8['rog']=float(globalVar.prandl['rogg'][i-1][n])
				globalVar.ui8['rog']=globalVar.ui8['rog']*(-1)
				break
			else:
				k0=globalVar.komptx['kom'][i][n]
				for nv in range(globalVar.verti['nverti']):
					k01=globalVar.verti['kkomv'][nv]
					if k0 == k01:
						io=globalVar.verti['iuver'][n][nv]+1
						xk=globalVar.verti['sumxk'][n][nv]+globalVar.drukk['xkz'][i-1][n]
						globalVar.ui8['rog']=-float(globalVar.verti['sumrg'][n][nv]+globalVar.prandl['rogg'][i-1][n])
						globalVar.ui8['pb']=globalVar.drukk['p'][io][n]
					else:
						break """from KONVEK1, it should leave this if l==2 section immediately when k0!=k01"""
		globalVar.xkp[ip]=xk
		if xk != 1.0e30:
			globalVar.rogp[i]=globalVar.ui8['rog']+globalVar.ui8['pb']
			globalVar.Print1['xz']=globalVar.Print1['xz']+(globalVar.ui8['pb']+globalVar.ui8['rog'])/xk
			xn=xn+1.0/xk
	
	kk=globalVar.hohlr['kkom'][j]
	if globalVar.boc21b['ikon'] < 0:
		globalVar.Print1['xz']=globalVar.Print1['xz']+globalVar.boc21b['xzsum'][kk]
		xn=xn+globalVar.boc21b['xnsum1'][kk]
	if globalVar.boc21b['ikon'] >= 0:
		globalVar.Print1['xz']=globalVar.Print1['xz']+globalVar.zwang['stzuk'][kk]*globalVar.hohlr['vol'][j]
		
	pp=globalVar.Print1['xz']/xn
	nl=globalVar.hohlr['nml'][j]
	nr=globalVar.hohlr['nmr'][j]
	ppn=globalVar.drukk['p'][i][nl]+(pp-globalVar.drukk['p'][i][nl])*ovrel """in this sub routine, ovrel was sent as a value not as a pointer like globalVar.Iter1['ovrel']"""
	i=globalVar.hohlr['il'][j]
	for n in range(nl, nr):
		globalVar.drukk['p'][i][n]=ppn
	globalVar.hohlr['phohl'][j]=ppn/1.0E5
	
	if ifmxy == 1:
		nl=globalVar.hohlr['nml'][j]
		nr=globalVar.hohlr['nmr'][j]
		mrl=0.0
		if globalVar.xkp[0] != 1.0e30:
			mrl=(globalVar.rogp[0]-pp)/globalVar.xkp[0]
			
		nn=0
		for n in range(nl,nr):
			for i1 in range(4):
				globalVar.m[i1]=0.0
			nn=nn+1
			npo=nn*2
			npu=npo+1
			globalVar.m[0]=mrl
			if globalVar.xkp[npo] != 1.0e30:
				globalVar.m[1]=(globalVar.rogp[npo]-pp)/globalVar.xkp[npo]
			if globalVar.xkp[npu] != 1.0e30:
				globalVar.m[3]=(globalVar.rogp[npu]-pp)/globalVar.xkp[npu]
			globalVar.m[2]=-globalVar.m[0]-globalVar.m[1]-globalVar.m[3]-globalVar.zwang['stzuk'][kk]*globalVar.geo['fzq'][n]*globalVar.geo['dz'][i]
			if ifmk != 1:
				globalVar.drukk['mr'][i][n]=(globalVar.m[0]-globalVar.m[2])/2.0
				globalVar.drukk['mz'][i][n]=(globalVar.m[1]-globalVar.m[3])/2.0
			else:
				globalVar.drukk['mr'][i][n]=-globalVar.m[2]/2.0
				globalVar.drukk['mz'][i][n]=-globalVar.m[3]/2.0
			globalVar.drukk['p'][i][n]=ppn
			mrl=-globalVar.m[2]
