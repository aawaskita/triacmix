import globalVar
import math

def XIRE(re):
	if re > 3.0e4:
		re=3.0e4
	if re < 0.00001:
		re=0.00001
		
	return 65.0/re + 0.0235 * (1.0-math.exp(-4.0e-4 * re))

def XIRE1(re,xgeo,xqt,xlt):
	if re > 3.0e5:
		re=3.0e5
		
	if re < 0.00001:
		re=0.00001
		
	xiver=0.0
	if xgeo != 0:
		xiver=2.*(64./re+2./(re**.18))
		if xgeo >= 1:
			return xgeo*xiver/xlt
	
	xilam=100.0/re
	xiturb=5.0/(re**0.16)*(0.044+0.08*((xlt/1.2)**1.4)/( (xqt-1.)**(.43+1.13/xlt)) ) +0.25
	x=xilam/xiturb
	xiflu=0.0
	if x >= 1:
		xiflu=xilam
	else:
		a=x-0.15
		sgn=1.0
		if a < 0.0:
			sgn=-1
		g=0.6762988*( sgn*(abs(a)**0.3333) + 0.5313628 )
		xiflu=xiturb+g*(xilam-xiturb)
		
	return ((1.0-xgeo)*xiflu +xgeo*xiver)/xlt
