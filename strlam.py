import globalVar
from vau import VAU
from reyn import REYN
from xire import XIRE, XIRE1
from ethag import ETHAG

"""
BERECHNET DIE KONSTANTEN FUER DIE STROEMUNGSBERECHNUNG
Perhitungan konstan untuk aliran
"""
def STRLAM(ifxkk):
	for nv in range(globalVar.verti['nverti']):
		for n in range(1,globalVar.ui['nm1']):
			globalVar.verti['sumxk'][n][nv]=0.0
			
	if ifxkk !=0:
		for i in range(1,globalVar.ui['im1']):
			for n in range(1, globalVar.ui['nm1']):
				globalVar.TEMP['xkk'][i][n]=0.0
				kk=globalVar.komptx['kom'][i][n]
				globalVar.konst['epsi']=globalVar.spezi['epsil'][kk] """how can we assure that the value of kk is never exceed the element of the array"""
				ifb1=globalVar.TEMP['ifb'][i][n]+1
				
				if ifb1==3 or ifb1==4 or ifb1==5:
					V=VAU(i,n)
					if V == 0.0:
						V=0.0002
					re=REYN(i,n)
					if ifb1==3:
						psi=1.0-0.7854/globalVar.kuel2['qtv'][kk]
						re=re * globalVar.konst['epsi']/psi
						xg=globalVar.kuel2['xgeo'][k]
						xq=globalVar.kuel2['qtv'][kk]
						xl=globalVar.kuel2['ltv'][k]
						globalVar.TEMP['xkk'][i][n]=v*globalVar.TEMP['rho'][i][n]/2./psi**2*(XIRE1(re,xg,xq,xl)/globalVar.spezi['dhyd'][kk]*100. +globalVar.spezi['xkon'][kk]*100.)
					else:
						globalVar.TEMP['xkk'][i][n]=v*globalVar.TEMP['rho'][i][n]/2./globalVar.konst['epsi']**2*(XIRE(re)/globalVar.spezi['dhyd'][kk]*100. +globalVar.spezi['xkon'][kk]*100.)
				
				elif ifb1==2:
					tem=(globalVar.TEMP['tfl'][i][n]+globalVar.TEMP['tfl'][i-1][n]+globalVar.TEMP['tfl'][i][n-1]+globalVar.TEMP['tfl'][i-1][n-1])/4.
					et=ETHAG(tem)
					re=REYN(i,n)
					xklam=142.22 + 3.663*re**.9
					globalVar.TEMP['xkk'][i][n]=globalVar.konst['pk']*xklam*et/globalVar.konst['rek']*(1.0-globalVar.konst['epsi'])**2/globalVar.konst['epsi']**3
	
	for i in range(1,globalVar.ui['im1']):
		for n in range(1,globalVar.ui['nm1']):
			ifb1=globalVar.TEMP['ifb'][i][n]+1
			if ifb1 !=1:
				kk=globalVar.komptx['kom'][i][n]
				if globalVar.drukk['xkr'][i][n] != 1.0e30:
					globalVar.drukk['xkr'][i][n]=globalVar.TEMP['xkk'][i][n]/globalVar.TEMP['rho'][i][n]/globalVar.geo['frq'][i][n]*globalVar.geo['dr'][n]/2.
					globalVar.drukk['xkr'][i][n]=globalVar.drukk['xkr'][i][n]+globalVar.TEMP['xkk'][i][n+1]/globalVar.TEMP['rho'][i][n+1]/globalVar.geo['frq'][i][n+1]*globalVar.geo['dr'][n+1]/2.
					if ifb1 == 5:
						globalVar.drukk['xkr'][i][n]=globalVar.drukk['xkr'][i][n]/globalVar.kuel2['qtv'][kk]
						
				if globalVar.drukk['xkz'][i][n] != 1.0e30:
					globalVar.drukk['xkz'][i][n]=globalVar.TEMP['xkk'][i][n]/globalVar.TEMP['rho'][i][n]/globalVar.geo['fzq'][n]*globalVar.geo['dz'][i]/2.
					globalVar.drukk['xkz'][i][n]=globalVar.drukk['xkz'][i][n]+globalVar.drukk['xkz'][i+1][n]/globalVar.TEMP['rho'][i+1][n]/globalVar.geo['fzq'][n]*globalVar.geo['dz'][i+1]/2.
					if ifb1 == 3:
						kO=globalVar.komptx['kom'][i][n]
						k01=k0
						nv=0
						while nv < globalVar.verti['nverti'] and k0==k01:
							kO1=globalVar.verti['kkomv'][nv]
							globalVar.verti['sumxk'][n][nv]=globalVar.verti['sumxk'][n][nv]+globalVar.drukk['xkz'][i][n]
							nv=nv+1
							
	
