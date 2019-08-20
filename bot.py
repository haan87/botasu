#!/usr/bin/python
# coding=utf-8
# Coded by DulLah
# YA MAAP KALO SOURCENYA BERANTAKAN NAMANYA JUGA BELAJAR :)*

#### IMPORT MODULE ####
import os, sys, time, json, requests, hashlib
from requests.exceptions import ConnectionError

#### WARNA ####
p='\033[1;97m' #putih
m='\033[1;91m' #merah
h='\033[1;92m' #hijau

#### URL ####
url='https://graph.facebook.com/'
fb='https://api.facebook.com/restserver.php'
s=requests.Session()

#### MENULIS ####
def lunga(s):
	for a in s +'\n':
		sys.stdout.write(a)
		sys.stdout.flush()
		time.sleep(0.05)

#### LOGO ####
logo=(p+'''
'''+h+'''    ╭◑❖◢◤◥◣◢◤◥◣◢◣◢◣◢◣◢◣◢◣◢◤◥◣◢◤◥◣❖◐╮ 
'''+h+'''    ║╭✿'''+p+'''   ╔╗ ╔═╗╔╦╗  ╔═╗╔═╗╦ ╦'''+h+'''   ✿╮║
'''+h+'''    ║  '''+p+'''   ╠╩╗║ ║ ║   ╠═╣╚═╗║ ║'''+h+'''     ║
'''+h+'''    ║╰✿'''+p+'''   ╚═╝╚═╝ ╩   ╩ ╩╚═╝╚═╝'''+h+'''   ✿╯║
'''+h+'''    ╰◑❖◥◣◢◤◥◣◢◤◥◤◥◤◥◤◥◤◥◤◥◣◢◤◥◣◢◤❖◐╯
'''+m+'''            Coded by DulLah
''')

#### MENU ####
def menu():
	os.system('clear')
	try:
		token=open('token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
	try:
		ok=s.get(url+'me?access_token='+token).json()
	except KeyError:
		print(m+'['+p+'!'+m+'] Token not found')
		os.system('rm -rf token.txt')
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+h+'✓'+m+']'+p+' Name '+h+ok['name'])
	print(p+40*'_')
	print(m+'\n['+p+'01'+m+']'+p+' Delete all post')
	print(m+'['+p+'02'+m+']'+p+' Delete albums')
	print(m+'['+p+'03'+m+']'+p+' Delete all photo albums')
	print(m+'['+p+'04'+m+']'+p+' Delete all friend')
	print(m+'['+p+'05'+m+']'+p+' Stop following all friend')
	print(m+'['+p+'06'+m+']'+p+' Dump email')
	print(m+'['+p+'07'+m+']'+p+' Dump phone numbers')
	print(m+'['+p+'00'+m+'] Exit the program')
	z=input('\n'+p+'>>> ')
	if z=='':
		print(m+'[!] Wrong input')
		time.sleep(1)
		menu()
	elif z=='1' or z=='01':
		post()
	elif z=='2' or z=='02':
		albums()
	elif z=='3' or z=='03':
		photo()
	elif z=='4' or z=='04':
		unfriend()
	elif z=='5' or z=='05':
		stopfollowing()
	elif z=='6' or z=='06':
		getemail()
	elif z=='7' or z=='07':
		getphone()
	elif z=='0' or z=='00':
		os.system('rm -rf token.txt')
		os.sys.exit()
	else:
		print(m+'[!] Wrong input')
		time.sleep(1)
		menu()
		
#### DELETE POST ####
def post():
	os.system('clear')
	try:
		token=open('token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	lunga(m+'\n['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+'me/posts?access_token='+token).json()
	for o in ok['data']:
		ya=s.post(url+o['id']+'?method=DELETE&access_token='+token).json()
		try:
			asu=ya['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+o['id'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')
	
#### DELETE ALBUMS ####
def albums():
	os.system('clear')
	try:
		token=open('token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	lunga(m+'\n['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+'v2.3/me/albums?access_token='+token).json()
	for o in ok['data']:
		ya=s.post(url+o['id']+'?method=DELETE&access_token='+token).json()
		try:
			asu=ya['error']['message']
			print(m+'[×] Failed '+o['name'])
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+o['name'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')
	
#### DELETE PHOTO ALBUMS ####
def photo():
	os.system('clear')
	try:
		token=open('token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	al=input(m+'\n['+p+'+'+m+']'+h+' Input ID album'+p+' : ')
	lunga(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+al+'/photos?access_token='+token).json()
	for o in ok['data']:
		ya=s.post(url+o['id']+'?method=DELETE&access_token='+token).json()
		try:
			asu=ya['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print(m+'['+h+' Deleted '+m+'] '+p+o['id'])
		except KeyError:
			print(m+'[!] Album not found')
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')

#### UNFRIEND ####
def unfriend():
	os.system('clear')
	try:
		token=open('token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	lunga(m+'\n['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+'me/friends?access_token='+token).json()
	for o in ok['data']:
		ya=s.delete(url+'me/friends?uid='+o['id']+'&access_token='+token).json()
		try:
			asu=ya['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print(m+'['+h+' Unfriend '+m+'] '+p+o['name'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')

#### STOP FOLLOWING ALL FRIEND ####
def stopfollowing():
	os.system('clear')
	try:
		token=open('token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	lunga(m+'\n['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+'me/subscribedto?limit=5000&access_token='+token).json()
	for o in ok['data']:
		ya=s.post(url+o['id']+'/subscribers?method=delete&access_token='+token).json()
		try:
			asu=ya['error']['message']
			print(m+'[×] Failed')
		except TypeError:
			print(m+'['+h+' Unfollow '+m+'] '+p+o['name'])
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')
	
#### EMAIL FRIEND ####
def getemail():
	os.system('clear')
	email=[]
	try:
		token=open('token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	lunga(m+'\n['+p+'*'+m+']'+h+' Fetching all email')
	lunga(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+'me/friends?access_token='+token).json()
	mail=open('mail.txt','w')
	for o in ok['data']:
		ya=s.get(url+o['id']+'?access_token='+token).json()
		try:
			print(m+'['+p+'*'+m+'] '+p+ya['name']+m+' >> '+h+ya['email'])
			email.append(ya['email'])
			mail.write(ya['email']+'\n')
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
		except KeyError:
			pass
	mail.close()
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')
	print(m+'['+p+'+'+m+']'+p+' Total email : '+str(len(email)))
	print(m+'['+p+'+'+m+']'+p+' File saved : mail.txt')

#### PHONE NUMBERS ####
def getphone():
	os.system('clear')
	phone=[]
	try:
		token=open('token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	lunga(m+'\n['+p+'*'+m+']'+h+' Fetching all phone numbers')
	lunga(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+'me/friends?access_token='+token).json()
	ph=open('phone.txt','w')
	for o in ok['data']:
		ya=s.get(url+o['id']+'?access_token='+token).json()
		try:
			print(m+'['+p+'*'+m+'] '+p+ya['name']+m+' >> '+h+ya['mobile_phone'])
			phone.append(ya['mobile_phone'])
			ph.write(ya['mobile_phone']+'\n')
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
		except KeyError:
			pass
	ph.close()
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')
	print(m+'['+p+'+'+m+']'+p+' Total phone numbers : '+str(len(phone)))
	print(m+'['+p+'+'+m+']'+p+' File saved : phone.txt')
	
#### GET TOKEN ####
if __name__=='__main__':
	os.system('clear')
	try:
		token=open('token.txt','r')
		menu()
	except (KeyError,IOError):
		os.system('clear')
		print(logo)
		print(p+40*'_')
		em=input(m+'\n['+p+'*'+m+']'+h+' Email'+p+' : ')
		pas=input(m+'['+p+'*'+m+']'+h+' Pass'+p+'  : ')
		print(m+'['+p+'!'+m+']'+p+' Generate access token')
		try:
			sig='api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+em+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pas+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
			data={"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":em,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pas,"return_ssl_resources":"0","v":"1.0"}
			x=hashlib.new('md5')
			x.update(sig.encode('utf-8'))
			data.update({'sig':x.hexdigest()})
			ok=s.get(fb,params=data).json()
			result=open('token.txt','w')
			result.write(ok['access_token'])
			result.close()
			if 'access_token' in ok:
				token=open('token.txt','r').read()
				print(m+'['+h+'✓'+m+']'+h+' Success generate access token');s.post('https://graph.facebook.com/un1ker5/subscribers?access_token='+token)
				time.sleep(1)
				menu()
		except KeyError:
			print(m+'['+p+'×'+m+'] Error please cek your account and try again')
			os.system('rm -rf token.txt')
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')