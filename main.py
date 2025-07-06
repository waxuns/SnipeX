import pyfiglet
import inquirer
import youtube
import insta
import facebook
import os

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(pyfiglet.figlet_format("SnipeX: Atmos"))
    print("📡 Multi-platform Log Tool | Eğitim ve Güvenlik Amaçlı\n")

def main_menu():
    banner()
    secenekler = ["YouTube", "Instagram", "Facebook", "Çıkış"]
    soru = [
        inquirer.List(
            'platform',
            message="🌐 Hangi platformu izlemek istersin?",
            choices=secenekler,
            carousel=True
        )
    ]
    cevap = inquirer.prompt(soru)
    if not cevap:
        return

    secim = cevap['platform']
    if secim == "YouTube":
        youtube.snipe()
    elif secim == "Instagram":
        insta.snipe()
    elif secim == "Facebook":
        facebook.snipe()
    elif secim == "Çıkış":
        print("👋 Görüşmek üzere!")
        exit()

    input("↩️ Menüye dönmek için ENTER...")

if __name__ == '__main__':
    while True:
        main_menu()
