# /usr/lib/python
# Kirnath Morscheck
# ZeroByte.ID

import sys
import requests
import urllib3
import time
from termcolor import colored

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

class warna:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
merah = "\033[01;31m{0}\033[00m"
hijau = "\033[01;35m{0}\033[00m"

w 		= merah.format(" _   ___                  _   _     \n")
gans 	= merah.format("| | / (_)                | | | |    \n")
sangat 	= merah.format("| |/ / _ _ __ _ __   __ _| |_| |__  \n")
kirnath = merah.format("|    \| | '__| '_ \ / _` | __| '_ \ \n")
coded 	= merah.format("| |\  \ | |  | | | | (_| | |_| | | |\n")
me 		= merah.format("\_| \_/_|_|  |_| |_|\__,_|\__|_| |_|\n")
exit = "[========]"
for l in w:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in gans:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in sangat:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in coded:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
for l in me:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.005)
print hijau.format("                       ZeroByte.ID\n")

def main():
	print warna.WARNING + "[!] Enter site without http:// or https:// (e.g google.com)" + warna.ENDC
	site = str(raw_input("[+] Enter Site: "))
	time.sleep(2)
	print warna.GREEN + "[+] Processing ",site + warna.ENDC
	listed = open('data.txt', 'r')
	head   = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
	baca   = listed.read().split('\n')
	for i in baca:
		process = requests.get('http://{}{}'.format(site,i), headers=head, verify=False)
		status = str(process.status_code)
		if "200" in status:
			print warna.GREEN + "[+] Yeay! I've Found it!\n[+] ",process.url + warna.ENDC
			keluar = str(raw_input("[+] Do you want to exit?(y/n): "))
			if keluar =="y":
				print warna.GREEN + "[+] Job Done! Bye honeey <3 :) ...." + warna.ENDC
				sys.exit()
			else:
				print warna.FAIL + "[+] FUUCCKKK YOU -_- i'm tired -_-"
				continue
		else:
			print warna.FAIL + "[!] ",process.url + " Not Found !" + warna.ENDC
	print "[+] Job Done, and i'm tired :( let me sleep Okay."
main()
