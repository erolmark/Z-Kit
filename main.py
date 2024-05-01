import os
import colorama
from pyfiglet import Figlet
import requests

class Renkler:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'

colorama.init()

figlet = Figlet(font='slant')
text = figlet.renderText("Zindan Web")
formatted_text = f"{Renkler.RED}{text}{Renkler.RESET}"

print(formatted_text)
print("\033[33mDev: Erol Ve Batu\033[1m")
print()
print()
print(Renkler.YELLOW + "[1]Exxen Checker")
print(Renkler.MAGENTA + "[2]İp Sorgu")
print(Renkler.CYAN + "[3]Bdfd Altyapı Gen")
print(Renkler.BLUE + "[4]Tiktok İzlenme Tool")
print(Renkler.RED + "[5]İnsta & Tiktok Hile")
print()
print()
main = input("Hangi Seçeneği Seçiyorsunuz: ")

if main == "1":
os.system("ls")
os.system("clear")
os.system("Exxen.checker.py")
else:
    print("geçersiz Seçenek")
elif main == "2":
os.system("ls")
os.system("clear")
os.system("ip_sorgu.py")
else:
    print("geçersiz seçenek")
elif main == "3":
os.system("ls")
os.system("clear")
os.system("bdfd_gen.py")
else:
    print("geçersiz seçenek")
elif main == "4":
os.system("ls")
os.system("clear")
os.system("tiktok.py")
else:
    print("geçersiz seçenek")
elif main == "5":
os.system("ls")
os.system("clear")
os.system("igtok.py")
else:
print("geçersiz seçenek")
