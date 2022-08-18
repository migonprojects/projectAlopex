import string
import random

ee=list(string.ascii_uppercase)
ee.append("/")
print("projectAlopex. Trifid Cipher Tool")
def key(x):
	i=[]
	for chr in x:
		if (chr not in i):
			i.append(chr)

	for items in ee:
		if (items not in i):
			i.append(items)
	listToStr = ''.join([str(elem) for elem in i])
	return(listToStr)

#***************************************************************
def onetime(x):
	print("Using one time key mode! Be careful to remember the key while decoding! ;-)")
	print()
	r=[]
	for i in range (1,x+1):
		r.append(i)
	u=[]
	for i in range (0,x):
		u.append(random.choice(r))
		r.pop(r.index(u[-1]))
	ii=[]
	for items in u:
		ii.append(ee[int(items)%27])
	listToStr = ''.join([str(elem) for elem in ii])
	return(listToStr)

def kanon2(x):
	u=x.upper()
	u=u.replace(" ","")
	return(u)

def kanon1(x):
	u=x.upper()
	u=u.replace(" ","/")
	u=u.replace(",","")
	u=u.replace("!","")
	u=u.replace("?","")
	u=u.replace(";","")
	u=u.replace("[","")
	u=u.replace("]","")
	u=u.replace(".","//")
	for i in range (0,10):
		u=u.replace(str(i),"")
	return(u)

def dict3():
	dd=[]
	for i1 in range (1,4):
		for i2 in range (1,4):
			for i3 in range (1,4):
				ooo=[]
				ooo.append(i1)
				ooo.append(i2)
				ooo.append(i3)
				listToStr = ''.join([str(elem) for elem in ooo])
				dd.append(listToStr)
	return(dd)

def dif(x,y):
	#TRIGRAPH GENERATION FUNCTION
	if ((len(x)%y)!=0):
		while ((len(x)%y)!=0):
			x=x+'/'
	u=int(len(x)//y)
	oi=[]
	for i in range (0,u):
		oi.append(x[y*i])
		if (i==u):
			oi.append("/")
		else:
			for m in range (1,y):
				oi.append(x[y*i+m])
		oi.append(" ")
	listToStr = ''.join([str(elem) for elem in oi])
	oo=listToStr.split()
	return(oo)

def table(x):
	#  Table 1  Table 2  Table 3
	#    1 2 3    1 2 3    1 2 3
	#  1 A B C  1 J K L  1 S T U | 1 2 3 10 11 12 19 20 21
	#  2 D E F  2 M N O  2 V W X | 4 5 6 13 14 15 22 23 24
	#  3 G H I  3 P Q R  3 Y Z / | 7 8 9 16 17 18 25 26 27
	print()
	print("Trifid cipher key:")
	print(" Table 1  Table 2  Table 3")
	print("   1 2 3    1 2 3    1 2 3")
	print(" 1 "+x[0]+" "+x[1]+" "+x[2]+"  1 "+x[9]+" "+x[10]+" "+x[11]+"  1 "+x[18]+" "+x[19]+" "+x[20])
	print(" 2 "+x[3]+" "+x[4]+" "+x[5]+"  2 "+x[12]+" "+x[13]+" "+x[14]+"  2 "+x[21]+" "+x[22]+" "+x[23])
	print(" 3 "+x[6]+" "+x[7]+" "+x[8]+"  3 "+x[15]+" "+x[16]+" "+x[17]+"  3 "+x[24]+" "+x[25]+" "+x[26])

def trifid_decr(p,y):
	xx=list(p)
	jj=list(str(y))
	mm=dict3()
	uu=[]
	for chr in p:
		uu.append(mm[jj.index(chr)])
	x=''.join([str(elem) for elem in uu])
	x=list(x)
#	u=x[0]+x[7]+x[14]+" "+x[1]+x[8]+x[15]+" "+x[2]+x[9]+x[16]+" "+x[3]+x[10]+x[17]+" "+x[4]+x[11]+x[18]+" "+x[5]+x[12]+x[19]++" "+x[6]+x[13]+x[20]
	ww=[]
	ww.append(x[0])
	ww.append(x[7])
	ww.append(x[14])
	ww.append(" ")
	ww.append(x[1])
	ww.append(x[8])
	ww.append(x[15])
	ww.append(" ")	
	ww.append(x[2])
	ww.append(x[9])
	ww.append(x[16])
	ww.append(" ")	
	ww.append(x[3])
	ww.append(x[10])
	ww.append(x[17])
	ww.append(" ")	
	ww.append(x[4])
	ww.append(x[11])
	ww.append(x[18])
	ww.append(" ")	
	ww.append(x[5])
	ww.append(x[12])
	ww.append(x[19])
	ww.append(" ")	
	ww.append(x[6])
	ww.append(x[13])
	ww.append(x[20])
	u=''.join([str(elem) for elem in ww])
	ww=u.split()
	oo=[]
	for items in ww:
		oo.append(jj[mm.index(str(items))])
	listToStr = ''.join([str(elem) for elem in oo])
	return(listToStr)

def trifid_encr(x,y):
	xx=list(x)
	jj=list(str(y))
	mm=dict3()
	w=[]
	x=[]
	k=[]
	count=0

	for items in xx:
		mko=''
		for chr in items:
			mnk=mm[jj.index(chr)]
			w.append(mnk[0])
			x.append(mnk[1])
			k.append(mnk[2])
		listToStr1 = ''.join([str(elem) for elem in w])
		listToStr2 = ''.join([str(elem) for elem in x])
		listToStr3 = ''.join([str(elem) for elem in k])
		listToStr=listToStr1+listToStr2+listToStr3
		hh=dif(listToStr,3)
		vv=[]
		for items in hh:
			for jit in mm:
				if (jit==items):
					vv.append(jj[mm.index(jit)])
			listToStr = ''.join([str(elem) for elem in vv])
	return(listToStr)

def trifid():
	print()
	u=kanon1(input("Key (AAA for Onetime Key)> "))
	if (u=="AAA"):
		u=onetime(27)
	else:
		u=key(u)
	print("Playfair-type key: "+u+" (27 bytes)")
	table(u)
	#print("*********************************************************")
	print()
	p=input("Plaintext> ")
	q=int(input("Mode: [1]Encrypt [2]Decrypt> "))
	if (q==1):
		p=kanon1(p)
		w=dif(p,7)
		mu=[]
		for it in w:
			mu.append(trifid_encr(it,u))
			mu.append("   ")
		listToStr = ''.join([str(elem) for elem in mu])
		print("")
		print("Encrypted message: ")
		print(listToStr)
		return(listToStr)

	elif (q==2):
		p=kanon2(p)
		oooo=dif(p,7)
		ii=[]
		for w in oooo:
			ii.append(trifid_decr(w,u))
		listToStr = ''.join([str(elem) for elem in ii])
		print("")
		print("Decrypted message: ")
		print(listToStr)
		return(listToStr)

trifid()
#
