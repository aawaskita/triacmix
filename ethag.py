import globalVar

def ETHAG(t):
	t0 = -272.0
	t=max(t,t0)
	return 3.674E-07 * (t+273.)**0.7
