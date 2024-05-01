import requests

def query_ip():
    ip = input("\033[93mIP adresini girin: ")
    if not ip:
        print("\033[91mGeçersiz IP adresi!")
        return

    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        if data["status"] == "fail":
            print("\033[91mIP sorgusu başarısız oldu.")
        else:
            print(f"""
                IP Adresi: {data["query"]}
                Ülke: {data["country"]}
                Şehir: {data["city"]}
                Konum: {data["lat"]}, {data["lon"]}
                ISP: {data["isp"]}
            """)
    except Exception as e:
        print("\033[91mBir hata oluştu:", e)

def main_menu():
    print("\033[1m  ______           _                ____ _               _               ")
    print(" |__  (_)__ _ __  | |__ _ _ __    / ___| |__   ___  ___| | __           ")
    print("    / / / _` '_ \ | '_ \ '_ \  | |   | '_ \ / _ \/ __| |/ /          ")
    print("   / /_| (_| | | || | | | | | | |___| | | |  __/ (__|   <           ")
    print("  /____|\__,_|_| ||_| |_| |_|  \____|_| |_|\___|\___|_|\_\  ")

    print("\033[1mİP CHECK")

    print("1- İp Sorgu")

    choice = input("\033[93mHangi aracı kullanmak istersiniz (1): ")
    if choice == "1":
        query_ip()
    else:
        print("\033[91mGeçersiz seçenek!")
        main_menu()

main_menu()

print("\nMade By Veraildez")
print("Instagram: veraildez_v33")
print("Github: github.com/VeraMarka")
