#-*-coding: utf-8-*-
import hashlib, random
from sys import argv
from os import system
from re import findall
from mechanize import Browser

#Renkler
bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

#Sabitler
passwords=[]

#Tarayıcı
browser = Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)')]

#Fonskyionlar
def logo():
	#system("clear")
	print bold+yellow+"\t\t\t     Akrep MD5Cracking"+endcolor
	print bold+"\t\t\t---------------------------"+endcolor
	print "\t\t\t--==[ Bug Researchers ]==--"
	print "\t\t\t--==[  {}Cyber-Warrior{}  ]==--".format(green, endcolor)
	print "\t\t\t--==[    {}ExitStars{}    ]==--".format(blue, endcolor)
	print bold+"\t\t\t---------------------------"+endcolor

def usage():
	print '{}Kullanım{}: ./md5cracker.py ["hash"] ["option"] ["auxiliary"]'.format(bold+green, endcolor)
	print "{}Örnek{}: ./md5cracker.py d8578edf8458ce06fbc5bb76a58c5ca4 -o -pass".format(bold+green, endcolor)
	print ""
	print bold+blue+"Options:"+endcolor
	print "-o | Online Tarama (MD5 Kırıcı Siteleri Tarar)"
	print "{}Örnek{}: ./md5cracker.py d8578edf8458ce06fbc5bb76a58c5ca4 -o -pass".format(bold+green, endcolor)
	print "-w | Wordlist Tarama (Wordlist Dosyasını Tarar)"
	print "{}Örnek{}: ./md5cracker.py d8578edf8458ce06fbc5bb76a58c5ca4 -w /root/wordlist.txt".format(bold+green, endcolor)
	print "-r | Random Tarama (Random Kelime Üretip Tarar)"
	print "{}Örnek{}: ./md5cracker.py d8578edf8458ce06fbc5bb76a58c5ca4 -r -2,8".format(bold+green, endcolor)
	print ""
	print bold+blue+"Auxiliary:"+endcolor
	print "-pass | Online Tarama (-o) İçin Girilecek Yardımcı Ayar"
	print "{}Örnek{}: ./md5cracker.py d8578edf8458ce06fbc5bb76a58c5ca4 -o -pass".format(bold+green, endcolor)
	print "/root/wordlist.txt | Wordlist Tarama (w) İçin WordList Yolu"
	print "{}Örnek{}: ./md5cracker.py d8578edf8458ce06fbc5bb76a58c5ca4 -w /root/wordlist.txt".format(bold+green, endcolor)
	print "-2,5 | Random Tarama (-r) İçin Üretilen Kelimenin Karakter Aralığı)"
	print "{}Örnek{}: ./md5cracker.py d8578edf8458ce06fbc5bb76a58c5ca4 -r -2,8".format(bold+green, endcolor)
	print ""
	print bold+blue+"Akrep MD5Cracking:"+endcolor
	print "Cyber-Warrior TIM | Bug Researachers Group"
	print "ExitStars | CoderLab"
	print "Sürüm V1 - Beta Sürüm"

def online_scan(hash):
	browser.open("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php")
	browser.select_form(nr=0)
	browser['md5'] = hash
	icerik = browser.submit().read()
	results = findall("Hashed string</span>: (.*?)</div>",icerik)
	if len(results) != 0:
		print bold+blue+"Hash Bulundu: "+endcolor+results[0]
	else:
		print "Hash Bulunamadı..."

def wordlist_scan(wordlistfiles, hash):
	wordfiles = open(wordlistfiles)
	words = wordfiles.readlines()
	found = 0
	for word in words:
		word = word.strip()
		md5word = hashlib.md5(word).hexdigest()
		if md5word == hash:
			print bold+blue+"Şifre Bulundu: "+endcolor+word
			found = 1
			break
		else:
			pass
	if found == 0:
		print bold+red+"Şifre Bulunamadı!"+endcolor
	else:
		pass

def random_scan(hash, minimum, maximum, password=""):
    while True:
        while 1:
            border = random.randint(minimum, maximum)
            for md in range(border):
                md5 = random.randint(97,122)
                password += chr(md5)
            break
        checking = password in passwords
        if checking == False:
            hashpass = hashlib.md5(password.encode())
            if hash == hashpass.hexdigest():
                print bold+blue+"Şifre Bulundu: "+endcolor+password
                break
            passwords.append(password)
            password = ""
    wordlist = open("es_wordlist.txt", "w")
    for passwd in passwords:
    	wordlist.write(passwd+"\n")
    wordlist.close()


logo()
if len(argv) == 4:
	if len(argv[1]) == 32:
		if argv[2] == "-o":
			print bold+blue+"Online Tarama Yapılıyor"+endcolor
			online_scan(argv[1])
		elif argv[2] == "-w":
			print bold+blue+"Wordlist Tarama Yapılıyor"+endcolor
			wordlistfiles = argv[3]
			wordlist_scan(wordlistfiles, argv[1])
		elif argv[2] == "-r":
			print bold+blue+"Random Tarama Yapılıyor"+endcolor
			aralik = argv[3].replace("-", "")
			minimum, dot, maximum = aralik.partition(",")
			random_scan(argv[1], int(minimum), int(maximum))
		else:
			print bold+red+"Böyle Bir Seçenek Bulunmamakta!"+endcolor
	else:
		print bold+red+"Hash 32 Karakter Olmalı!"+endcolor
else:
	usage()
