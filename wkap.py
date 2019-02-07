import globalVar

def WKAP(dtem1):
	ifprnt=0
	im1=globalVar.reg['imax']-1
	nm1=globalVar.reg['nmax']-1
	for i in range(im1):
		for n in range(nm1):
			if3=16
			k=globalVar.komp1['kom'][i][n]
			ifz=0
			ii=i-globalVar.feld2['idiff']
			nn=n-globalVar.feld2['ndiff']
			if ii>0 and nn>0 and ii<=globalVar.feld2['imh'] and nn<=globalVar.feld2['nmh']:
				if3=globalVar.berhet['ifbh'][ii][nn]
			ifkt=globalVar.wkapt['ifwkt'][k]
			if ifkt==30:
				globalVar.ui['wkapzt']=globalVar.trans['c'][k]

			else:
				ifkt=ifkt-1
				if globalVar.zus['ifber'][i][n]
