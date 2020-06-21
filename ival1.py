import os
import cc2
import qst 
from mshfi import *
from wpos import *

dir_path = os.path.dirname(os.path.realpath(__file__))
rs = open(dir_path+'\out4.txt', 'w', encoding="utf-8")

hwstr= qst.qst
qrstr= "إن الله لا يخفى عليه شيء في الأرض ولا في السماء هو الذي يصوركم في الأرحام كيف يشاء لا إله إلا هو العزيز الحكيم هو الذي أنزل عليك الكتاب منه آيات محكمات هن أم الكتاب وأخر متشابهات"
#qrstr= "الحمد للًه ربٍ العـــالمين"
# qrstr= "     من     الجنة       والناس    "
#qrstr= "وقيل الحمد لله"


def deNoise(text):
# Tashdid, Fatha, Tanwin Fath, Damma, Tanwin Damm, Kasra, Tanwin Kasr, Sukun, Tatwil/Kashida.
    # noise = re.compile(" ّ | َ | ً | ُ | ٌ | ِ | ٍ | ْ | ـ ", re.VERBOSE)
    # text = re.sub(noise, '', text)
	tlist= ["ّ","َ","ً","ُ","ٌ","ِ","ْ","ـ","ٍ"]
	for tc in tlist: 
		text=text.replace(tc, "")		
	return text
#'\n', '\t' to ' '

def normalizeAlif(text):
	tlist= ['إ','أ','ٱ','آ','ا']
	for tc in tlist: 
		text=text.replace(tc, "ا")		
	return text
	
def processQry(txt):
	#txt=txt.replace('  ', " ");
	txt=' '.join(txt.split())
	txt=txt.replace('\n', " ")
	txt=txt.replace('\t', " ")
	txt=deNoise(txt)
	txt=normalizeAlif(txt)
	return txt

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        ret= a_str[:start].count(' ')
        yield ret
        start += len(sub) # use start += 1 to find overlapping matches
		
def aysr(ff , ll ):
	for ss in wpos:
		for aa in ss:
			if aa<=ff: reta=ss.index(aa); rets= wpos.index(ss)
			if aa>=ll: return(reta+1 , rets , ss.index(aa) , wpos.index(ss))

def fromSrAy(sr,ay):
	return slice(wpos[sr-1][ay-1] , wpos[sr-1][ay])

	
	
qrstr= processQry(qrstr)
lenqrstr= qrstr.count(' ')+1
slc= fromSrAy(1,1)
rs.write(' '.join(mshf[slc])+"\n")
for el in find_all(hwstr, qrstr): 
	print(el)
	print(aysr(el , el+lenqrstr))
	(ay1,sr,ay2,sr) = aysr(el , el+lenqrstr)
	if (ay1==ay2): info= "\n[%s:%d]"%(srname[sr] , ay1)
	else: info= "\n[%s:%d-%d]"%(srname[sr] , ay1 , ay2)
	rs.write(' '.join(mshf[el:el+lenqrstr])+ info +"\n")


def fc0():
	for el in find_all(hwstr, qrstr): 
		print(el)
		print(aysr(el , el+lenqrstr))
	(ay1,sr,ay2,sr) = aysr(el , el+lenqrstr)
	if (ay1==ay2): info= "\n[%s:%d]"%(srname[sr] , ay1)
	else: info= "\n[%s:%d-%d]"%(srname[sr] , ay1 , ay2)
	rs.write(' '.join(mshf[el:el+lenqrstr])+ info +"\n")
	

