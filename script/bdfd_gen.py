import os
import colorama
import requests
import sys
import pyfiglet
import time

os.system("pkg install python")
os.system("pip install pyfiglet")
os.system("pip install colorama")
os.system("pip install sys")
os.system("pip install requests")
os.system("pip install time")
os.system("pip install os")

# Renkleri tanımla
colorama.init()
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[33;1m"
blue = "\033[34m"
cyan = "\033[36m"
reset = "\033[0m"

os.system("clear")

rez = requests.get("https://justpaste.it/djwcw").text
key = rez.split('<p>')[1]
key = key.split('</p>')[0]
gir = input("Key Giriniz: ")

if gir == key:
    print(green + "Key Doğru Tool Açılıyor" + reset)
    os.system("clear")
else:
    print(red + "Key Yanlış." + reset)
    sys.exit()

text = "Zindan Check"
figlet_text = pyfiglet.figlet_format(text)
print(figlet_text)

print(yellow + "Dev: " + red + "Vera" + reset + " & " + red + "Massive" + reset + green + "Discord: https://discord.com/invite/yFzkKsPh6Y")
print()
print(blue +"[1]Moderasyon Altyapı Kodlari")
print(cyan +"[2]Eğlence Altyapi Kodlari")
print(red +"[3]Patlatma Altyapı Kodlari")
print(yellow+"[4]Owo AltYapı kodu")
print(green+"[5]Public Server Altyapi kodu")
print()
secim = input("Seçmek İstediğiniz Seçenek: ")

if secim == "1":
    os.system("clear")
    os.system("figlet Zindan Check")
    print(blue +"[A]29 Komutlu Bot AltYapısı")
    print("[B]Gelişmiş Genel Bot Altyapısı")
    print("[C]Level Bot AltYapısı")
    print("[D]Resimli Rank AltYapısı")
    
    moderasyon = input("Hangi Seçenegi Seçiyorsunuz: ")
    if moderasyon == "A":
        print()
        time.sleep(2)
        print(blue + "Kod:" + cyan + " JbRcrwKrDX9WDP4yXIiVoxxCQ" + reset)
        
    elif moderasyon == "B":
        print()
        time.sleep(2)
        print(blue + "Kod:" + cyan + " mbf9PtrCKdZL5huRMSH0x1XOev" + reset)
        
    elif moderasyon == "C":
        print()
        time.sleep(2)
        print(blue + "Kod:" + cyan + " DAk2SQegQUJvWzw15u9LtH7Wu" + reset)
        
    elif moderasyon =="D":
        print()
        time.sleep(2)
        print(blue + "Kod:" + cyan + " 008zBzLqpg1Fi7m2ufEtMDkYs" + reset)
        
elif secim == "2":
    os.system("clear")
    os.system("figlet Zindan Check")
    print(cyan +"[Z]Adam Asmaca Altyapi kodu")
    
    eglence = input("Seçenek: ")
    
    if eglence == "Z":
        print()
        time.sleep(2)
        print(cyan + "Kod:" + yellow + " 4IrMKxQFKzsSoErQJTUajX29M" + reset)
 
elif secim == "3":
    os.system("clear")
    os.system("figlet Zindan Check")
    print(red + "[1]Patlatma Altyapı Kodları")
    
    patlat = input("Hangi Seçenegi Seçiyorsunuz: ")

    if patlat == "1":
        print()
        time.sleep(2)
        print(red + "Kod:" + yellow + " sdiYwunWZT2S11dQnJ4FeXaCF" + reset)

elif secim == "4":
    os.system("clear")
    os.system("figlet Zindan Check")
    print(yellow + "Owo AltYapı kodu")
    
    os.system("clear")
    os.system("figlet Zindan Check")
    print(yellow +"[A]Owo Bot AltYapısı")
   
    owo = input("Seçenek: ")

    if owo == "A":
        print()
        time.sleep(2)
        print(yellow + "Kod:" + green + " h4jkvhEpGMdcVYvEh9qXFa5UM" + reset)

elif secim == "5":
    os.system("clear")
    os.system("figlet Zindan Check")
    print(green + "Public Server Altyapi kodu")

    print(green + "[A]Kayıt Kodu")
    print("[B]Çekiliş AltYapisi")
    print("[C] Oy Ver altyapisi")
    print("[D]Premium altyapisi")
    print("[E]Loglu Warn AltYapisi")
    
    public = input("Seçenek: ")

    if public == "A":
        print()
        time.sleep(2)
        print(green + "Kod:" + yellow + " lyEyrgTNn3Rz5SSMDtk9tqDzq" + reset)
    elif public == "B":
        print()
        time.sleep(2)
        print(green + "Kod:" + yellow + " 53KlaXuApDm9wYBvW4HQzbr31" + reset)
    elif public == "C":
        print()
        time.sleep(2)
        print(green + "Kod:" + yellow + " nnVopo6roDLQQe5qH609JXQAX" + reset)
    elif public == "D":
        print()
        time.sleep(2)
        print(green + "Kod:" + yellow + " 4mFbQV616j1als8kgNoDZxuMf" + reset)
    elif public == "E":
        print()
        time.sleep(2)
        print(green + "Kod:" + yellow + " JDB71gcpEVQoy4T2Hv7rBEQg3" + reset)

else:
    print(red + "Geçersiz seçenek! Lütfen geçerli bir seçenek seçin." + reset)
  #EDİTLEYENLERİN ALLAHİNA ÇAKAYİM
