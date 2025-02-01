from pytube import YouTube, Playlist
import os

def download_video(url, output_folder="downloads", format="mp4"):
    try:
        yt = YouTube(url)
        title = yt.title.replace(" ", "_").replace("/", "_")  # Уникнення проблем із назвами файлів
        
        if format == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            filename = f"{title}.mp3"
        else:
            stream = yt.streams.get_highest_resolution()
            filename = f"{title}.mp4"
        
        os.makedirs(output_folder, exist_ok=True)
        filepath = os.path.join(output_folder, filename)
        stream.download(output_folder, filename)
        
        print(f"✅ Завантажено: {filename}")
    except Exception as e:
        print(f"❌ Помилка: {e}")

def download_playlist(playlist_url, output_folder="downloads", format="mp4"):
    try:
        pl = Playlist(playlist_url)
        print(f"📥 Завантаження плейлиста: {pl.title}")
        for video in pl.video_urls:
            download_video(video, output_folder, format)
        print("✅ Плейлист завантажено!")
    except Exception as e:
        print(f"❌ Помилка: {e}")

if __name__ == "__main__":
    url = input("🔗 Введіть посилання на відео або плейлист: ").strip()
    format_choice = input("🎵 Введіть формат (mp4/mp3): ").strip().lower()
    
    if "playlist" in url:
        download_playlist(url, format=format_choice)
    else:
        download_video(url, format=format_choice)
