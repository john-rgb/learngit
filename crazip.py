#-*- coding:utf-8 -*-
import zipfile
import threading

def crack(zfile,password):	
	try:
		zfile.extractall(pwd=password)
		print 'password is'+password
		return password
	except:
		pass

z=zipfile.ZipFile('a.zip')
f=open('dictionary.txt')
for pwd in f.readlines():
	pawd=pwd.strip('\n')
	thd=threading.Thread(target=crack, args=(z, pawd))
	thd.start()	
#print crack(z,'123456')
