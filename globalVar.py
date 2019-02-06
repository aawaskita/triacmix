"""global common"""
basis={}
basis['tbase']=0

bez={}
bez['pkom']=[]
bez['uet']=[]

rstrt={}
rstrt['ifrst']=0
rstrt['ifrsta']=0
rstrt['zrst']=0
rstrt['ilogr']=5

Error={}
Error['abtext']=[]
Error['ierrm']=300
Error['ierrl']=0
Error['ierrf']=[1,2,5,25,10]
Error['nhin']=0
Error['nwarn']=0
Error['nfehl']=0

"""
maithx subroutine
"""
wkapt={}
wkapt['ifwkt']=[]
wkapt['ifwkpt']=0
"""and steuer subroutine"""

kopplg={}
kopplg['iftape']=0
kopplg['dtvor']=0
"""and steuer subroutine"""

trans={}
trans['ifinst']=0
trans['intval']=0
trans['dzeit']=[]
trans['zei']=[]
trans['nprint']=[]
trans['nkonv']=[]
trans['rho']=[]
trans['c']=[]
"""and steuer subroutine"""

lamt={}
lamt['iflt']=[]
lamt['iflamt']=0
"""and steuer subroutine"""

plot={}
plot['ifplot']=0
plot['ipun']=0

Print={}
Print['title']=[]
Print['au']=[]
Print['ar']=[]
Print['bu']=[]
Print['br']=[]
Print['phip']=[]
Print['radp']=[]
Print['indgeo']=0
"""add steuer subroutine"""

reg={}
reg['imax']=0
reg['nmax']=0
reg['dr']=[]
reg['dph']=[]
reg['rad']=[]
reg['phi']=[]
reg['ikom']=[]
reg['nkom']=[]
reg['rad0']=0
reg['phi0']=0
reg['ifrfi']=0
reg['ifrfa']=0
reg['ifrfl']=0
reg['ifrfr']=0
reg['ifref']=0
"""and steuer subroutine"""

komp1={}
komp1['kmax']=0
komp1['kom']=[]
komp1['lam']=[]
komp1['tvor']=[]
komp1['alp']=[]
komp1['ref']=[]
komp1['iftv']=[]
komp1['kart']=[]
komp1['bem']=0
"""and steuer subroutine"""

calc={}
calc['t']=[]
calc['wi']=[]
calc['wl']=[]
calc['wt']=[]
calc['tq']=[]
calc['ifwq']=[]
calc['tflu']=[]
calc['bu1']=[]
"""and steuer subroutine"""

zus={}
zus['ifber']=[]
"""and steuer subroutine"""

Iter1={}
Iter1['trmax']=0
Iter1['mit']=0
Iter1['tn']=0
Iter1['ovrel']=0
Iter1['itmax']=0
Iter1['t1']=0 """Ada juga di Ui"""
Iter1['t2']=0
Iter1['trela']=0
Iter1['ntmax']=0
Iter1['ifkor']=0
Iter1['etha']=0
Iter1['ormin']=0
Iter1['mitmax']=0
Iter1['ikorm']=0
Iter1['ifrel']=0
"""and steuer subroutine"""

ztpt={}
ztpt['nzp']=0
ztpt=['nzpm']=0
ztpt['ipt']=[]
ztpt['npt']=[]
ztpt['kpzl']=[]
ztpt['tptmx']=0
ztpt['tptmn']=0
ztpt['tzp']=[]
ztpt['zeipt']=[]
ztpt['ifpkt']=[]
"""and steuer subroutine"""

berhet={}
berhet['thet']=[]
berhet['wwk']=[]
berhet['ifbh']=[]
berhet['wkaph']=[]

feld2={}
feld2['idiff']=0
feld2['ndiff']=0
feld2['imh']=0
feld2['nmh']=0
feld2['kkb']=[]

het1={}
het1['nhzon']=[]
het1['xfwqz']=[]
het1['ifhet']=[]

rzcomp={}
rzcomp['irearz']=0
rzcomp['mcr']=0
rzcomp['mcz']=0
rzcomp['mfr']=[]
rzcomp['mfz']=[]
rzcomp['iconvc']=0

specti={}
specti['itik']=[]
"""and steuer subroutine"""

opt={}
opt['kenn']=0
opt['iopt']=0
opt['nifko']=0
"""3 fungsi pertama ada juga di steuer subroutine"""
opt['dzt']=0
opt['konin']=0

qvar={}
qvar['dum']=[]
qvar['jrestw']=0
qvar['jrestr']=0
qvar['jrest']=0
qvar['tau']=0

blindl={}
blindl['thetb']=[]
blindl['thaltb']=[]
blindl['tmitl']=0.0
blindl['m24']=0
blindl['ngeom']=0
blindl['cizet0']=0
blindl['dosi']=[]
blindl['brv']=0
blindl['blv']=0

ksum={}
ksum['iti']=0
ksum['du']=0
ksum['sig']=0
ksum['vorz']=0
ksum['bkv']=0
ksum['rhoks']=0
ksum['rl']=0
ksum['sm']=0
ksum['burn']=0

speiko={}
speiko['f']=[]
speiko['iko']=[]
speiko['mx']=0
speiko['mm']=0
speiko['tmadbh']=[]
speiko['tmidbh']=[]
"""dan steuer subroutine"""

vardit={}
vardit['b']=[]
"""dan steuer subroutine"""

addrt={} 
addrt['kx']=[]
addrt['ky']=[]
addrt['lz']=[]
addrt['nendpt']=0
"""dan steuer subroutine"""

ui2={}
ui2['ifdf']=0

"""
wtsteu subroutine
"""
komvak={}
komvak['komvar']=0
komvak['konvar']=0
komvak['xksumk']=0
komvak['nqvar']=0
komvak['tstat']=0
komvak['xkstat']=0
komvak['dtddx']=0
komvak['twuns']=[]
komvak['qwuns']=[]
komvak['tvsek']=0
"""dan steuer subroutine"""

zeug={}
zeug['du']=[]
zeug['delday']=0

qvar={}
qvar['dum']=[]
qvar['qav']=0
qvar['tk']=0

mputa={}
mputa['teimin']=0
mputa['teimax']=0
mputa['emp0']=0
mputa['tau0']=0
mputa['mputau']=0
mputa['qwu']=0

ui={}
ui['dumm']=[]
ui['nm1']=0
ui['im1']=0
ui['dm']=[]
ui['intv']=0
ui['dtm1']=0
ui['ntape']=0
ui['geofak']=0.0
ui['ifstop']=0
ui['kk1']=0
ui['nko']=0
ui['qrat']=0
ui['dtem4']=0
ui['fak1']=0
ui['ifu']=0
ui['xf']=0
ui['dtem3']=0
ui['fakz']=0
ui['ifdt2']=0
ui['ifsfb']=0
ui['nlp']=0
ui['ifkst']=0
ui['ifneu']=0
ui['ifselb']=0
ui['iit']=0
ui['im']=0
ui['nm']=0
ui['vkug']=0
ui['vmat']=0
ui['fak2']=0
ui['delta']=0
ui['iflt1']=0
ui['iima']=0
ui['nnma']=0
ui['dxl0']=0.0
ui['tk1']=0
ui['xk0']=0
ui['delth']=0.0
ui['dtk0']=0.0
ui['dzav']=0
ui['dz0']=0
ui['nulein']=0
ui['tk0']=0
ui['dxk0']=0
ui['tmi']=0.0
ui['z0']=0
ui['tvh']=0
ui['t1']=0 """Ada juga di Iter1"""
ui['x1']=0.0
ui['cp']=0
ui['xla']=0
ui['ifred']=0
ui['tz']=0
ui['dpp']=0
ui['ifkon']=0
"""dan steuer subroutine"""

"""
steuer subroutine
"""
bock21={}
bock21['pkpop']=[]
bock21['tfkop']=[]
bock21['qkop']=[]
bock21['ifkost']=0
bock21['dszeit']=0

het={}
het['heps']=[]
het['hkug']=[]
het['di']=[]
het['nhmat1']=[]
het['nhmat2']=[]

het2={}
het2['volk']=[]
het2['obrk']=[]
het2['dvmk']=[]
het2['zkug']=[]
het2['volz']=[]
het2['vk']=[]

berhet={}
berhet['thet']=[]
berhet['wwk']=[]
berhet['wkaph']=[]

bheter={}
bheter['thalt']=[]
bheter['wqn']=[]
bheter['wqk']=[]

bilanz={}
bilanz['tgasm']=0
bilanz['izael']=0

coupl={}
coupl['iprint']=0
coupl['zquell']=[]
coupl['rquell']=[]

tvar={}
tvar['iftkv']=0
tvar['zeiv']=[]
tvar['tkv']=[]
tvar['ntvar']=[]

konthx={}
konthx['du']=[] """ada juga di ksum"""
konthx['falast']=0

"""tambahan qvar yang ada di global common pada steuer subroutine"""
qvar['ivar']=0
qvar['endkef']=0
qvar['qvolll']=0
qvar['qreduz']=0
qvar['qremax']=0
qvar['epq']=0
qvar['epc']=0
qvar['dqddc']=0
qvar['delc']=0
qvar['dcn']=0
qvar['sbu']=0
qvar['te']=[]
qvar['ta']=[]
qvar['n61']=0
qvar['urz']=0
qvar['zleka']=0
qvar['abxen']=0
qvar['ti']=0

fugra={}
fugra['ifugra']=0
fugra['tgra']=[]
fugra['tful']=[]

mpunkt={}
mpunkt['impu']=0
mpunkt['kmpu']=0
mpunkt['empu']=0
mpunkt['tttein']=0
mpunkt['tttaus']=0

zwang={}
zwang['stzuk']=[]
zwang['tflvor']=[]
zwang['ifnetz']=0

"""tambahan utk variabel mputa yang ada di wsteu subroutine"""
mputa['dtau']=0
mputa['tei0']=0
mputa['nvr']=0

"""tambahan utk variabel ksum yang ada di maithx subroutine"""
ksum['d']=[]
ksum['da']=[]
ksum['zeitmi']=0

"""tambahan untuk variabel array di subroutine steuer"""
jug=[]
for i in range(31):
	jug.append(0)

qquel1=[]
for i in range(31):
	qquel1.append(0.0)

buins=[]
for i in range(31):
	buins.append(0.0)
	
qspei1=[]
for i in range(31):
	qspei1.append(0.0)
	
qkons1=[]
for i in range(31):
	qkons1.append(0.0)
	
qps1=[]
for i in range(31):
	qps1.append(0.0)

temp=[0.0, 0.0, 0.0, 0.0, 0.0]
qspeiz=[]
for i in range(31):
	qspeiz.append(temp)
	
qkonvz=[]
for i in range(31):
	qkonvz.append(temp)
	
qnuklz=[]
for i in range(31):
	qnuklz.append(temp)

"""
printt subroutine
"""
bezei={}
bezei['bi']=0
bezei['bn']=0

"""
Dimensions
"""
tpun=[] """13 elements"""
npun=[] """4 elements"""
ipun1=[] """4 elements"""
plam=[] """5 elements"""
tpl=[] """100 elements"""
qx=[] """31 elements"""
zeipkt=[] """31 elements"""
tppkt=[] """31 elements"""
zeipk1=[] """10x31 elements"""
tppk1=[] """10x31 elements"""
iftv=[] """31 elements"""
fakz1=[] """80 elements"""
fakz2=[] """80 elements"""
fakz1a=[] """80 elements"""
feld=[] """50x80 elements"""
wkph=[] """5 elements"""

"""
Temporary file, intended to anticipate N61 writing process.
"""
n61file=open('N61','w')
