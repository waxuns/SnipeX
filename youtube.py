import requests
import os
from datetime import datetime

def snipe():
    os.makedirs("logs", exist_ok=True)
    query = input("🔍 Aranacak kelime (örn: Rahmiye Sare Palalı): ")
    api_key = input("🔑 YouTube API Key: ")

    if not api_key:
        print("⛔ API Key boş bırakılamaz!")
        return

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 5,
        "key": api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        if "error" in data:
            print(f"❌ Hata: {data['error']['message']}")
            return

        log_file = "logs/youtube.txt"
        with open(log_file, "a", encoding="utf-8") as f:
            for item in data.get("items", []):
                title = item["snippet"]["title"]
                video_id = item["id"]["videoId"]
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log = f"[{timestamp}] {title} - {video_url}\n"
                print(log.strip())
                f.write(log)

        print(f"\n✅ Sonuçlar 'logs/youtube.txt' dosyasına kaydedildi.")

    except Exception as e:
        print(f"❌ API isteği başarısız: {e}")
