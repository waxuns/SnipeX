from datetime import datetime
import os

def snipe():
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/facebook.txt"
    page = input("📘 Facebook sayfa adı: ")

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    content = f"[{timestamp}] 📰 {page} sayfası simülasyon olarak izlendi.\n"

    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(content)

    print(f"📁 Log yazıldı: {log_file}")
