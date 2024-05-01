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
os.system("clear")
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
    os.system("clear")
    os.system("python Exxen_checker.py")
elif main == "2":
    os.system("clear")
    os.system("python ip_sorgu.py")
elif main == "3":
    os.system("clear")
    os.system("python bdfd_gen.py")
elif main == "4":
    os.system("clear")
    os.system("python tiktok.py")
elif main == "5":
    os.system("clear")
    os.system("python igtok.py")
else:
    print("Geçersiz seçenek")
