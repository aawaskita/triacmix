import globalVar

"""
KONTROL PENGHAPUSAN KINERJA DI PERTUKARAN PANAS
"""

def WTSTEU(self,zeits,nulei1,iit,tk11,dtem1):
	globalVar.ui['nulein']=nulei1
	globalVar.ui['tk1']=tk11
	zeih=zeits/3600
	i=1
	while i<=globalVar.komvak['nqvar']:
		if globalVar.komvak['twuns']>zeih:
			globalVar.mputa['qwu']=globalVar.komvak['qwuns'][i-1] + (zeih-globalVar.komvak['twuns'][i-1]) * (globalVar.komvak['qwuns'][i] - globalVar.komvak['qwuns'][i-1])/(globalVar.komvak['twuns'][i]-globalVar.komvak['twuns'][i-1])	
		if i==globalVar.komvak['nqvar']:
			globalVar.mputa['qwu']=globalVar.komvak['qwuns'][globalVar.komvak['nqvar']]
		i=i+1
	
	if globalVar.komvak['komvar'] > 0:
		if iit<=1:
			globalVar.ui['t1']=1.0e-3 """Mengacu pada ui karena variabel ini diletakkan tepat di dalam subroutine wtsteu"""
			globalVar.ui['tmi']=70.0
			globalVar.ui['x1']=1.0
			globalVar.ui['xk0']=globalVar.komvak['xkstat']
			globalVar.ui['tk0']=globalVar.komvak['tstat']
			globalVar.ui['tk1']=globalVar.ui['tk0'] """ui digunakan karena dari kode sumber terletak di dalam subrutin wtsteu"""
			globalVar.komvak['xkstat']=globalVar.komvak['xksumk']
			globalVar.ui['z0']=zeih-(dtem1/3600)
			globalVar.ui['delth']=0.0
			globalVar.ui['dxl0']=0.0
			globalVar.ui['dtk0']=0.0
			globalVar.ui['tvh']=globalVar.komvak['tvsek']*3600
			
		zeitk=globalVar.zeug['delday'] * 24.0
		xk00=globalVar.ui['xk0']
		globalVar.ui['xk0']=globalVar.komvak['xksumk']
		dx0=globalVar.ui['xk0']-xk00
		z00 = globalVar.ui['z0']
		globalVar.ui['z0'] = zeih
		globalVar.ui['dz0'] = globalVar.ui['z0'] - z00

		if globalVar.ui['nulein'] == 2:
			globalVar.ui['dxk0']=dx0-globalVar.ui['dxl0']
			globalVar.ui['dxl0']=0.0
			globalVar.ui['delth']=0.0
		else:
			globalVar.ui['dxl0'] = globalVar.ui['dxl0'] + dx0
			globalVar.ui['delth'] = globalVar.ui['delth'] + globalVar.ui['dz0']
			if globalVar.ui['nulein'] == 1:
				tkmax = zeitk * globalVar.ui['tvh']
				globalVar.ui['dxl0'] = globalVar.ui['dxl0'] * globalVar.ui['dz0'] / globalVar.ui['delth']
				delqu = globalVar.mputa['qwu'] - globalVar.ui['xk0']
				dq1 = delqu - globalVar.ui['dxl0']
				if abs(globalVar.ui['dtk0']) >= globalVar.ui['t1']:
					if abs(globalVar.ui['dxk0']) >= globalVar.ui['x1']:
						globalVar.komvak['dtddx']=globalVar.ui['dtk0']/globalVar.ui['dxk0']		
				
				dtk1=dq1*globalVar.komvak['dtddx']
				dtk11=min(abs(dtk1),tkmax)
				"""
				DTK1=SIGN(DTK11,DTK1)
				"""
				if dtk1==0: dtk1=abs(dtk11)
				if dtk1<0: dtk11=-abs(dtk11)
				globalVar.ui['tk1']=globalVar.ui['tk0']+dtk1
				if globalVar.ui['tk1']<=globalVar.ui['tmi']:
					globalVar.ui['tk1']=globalVar.ui['tmi']
					dtk1=globalVar.ui['tmi']-globalVar.ui['tk0']
				globalVar.ui['tk0']=globalVar.ui['tk1']
				globalVar.ui['dtk0']=dtk1

