import globalVar
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
