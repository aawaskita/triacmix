"""
HITUNG JUMLAH BE DI MESIN HET DAN MESIN CAMPURAN
"""
import globalVar

def ZKUGL(ii,nn,kk):
	iff=globalVar.berhet['ifbh'][ii][nn]
	globalVar.ui['kk1']=globalVar.feld2['kkb'][ii][nn]
	i=ii+globalVar.feld2['idiff']
	n=nn+globalVar.feld2['ndiff']
	if iff == 0: 
		return 0.0
	
	if iff ==1:
		volm1=globalVar.Print['au'][i-1][n-1]
		volm2=globalVar.Print['au'][i][n-1]
		volm3=globalVar.Print['au'][i-1][n]
		volm4=globalVar.Print['au'][i][n]
	else:
		if iff == 2 or iff==5 or iff==6 or iff==9 or iff==10 or iff==13 of iff==14:
			volm1=0.0
		else:
			volm1=globalVar.Print['au'][i-1][n-1]
			
		if iff == 3 or iff == 5 or iff == 7 or iff == 9  or iff == 11 or iff == 13 or iff == 15:
			volm2=0.0
		else:
			volm2=globalVar.Print['au'][i][n-1]
			
		if iff == 4 or iff == 6 or iff == 7 or iff == 9 or iff == 12 or iff == 14 or iff == 15:
			volm3=0.0
		else:
			volm3=globalVar.Print['au'][i-1][n]
			
		if iff == 8 or iff == 10 or iff == 11 or iff == 12 or iff == 13 or iff == 14 or iff == 15:
			volm4=0.0
		else:
			volm4=globalVar.Print['au'][i][n]
			
	volm=volm1+volm2+volm3+volm4
	return volm*(1-globalVar.het['heps'][globalVar.ui['kk1']])/(0.52*globalVar.het['hkug'][globalVar.ui['kk1']]**3)
