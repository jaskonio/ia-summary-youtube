from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

class YouTubeToMP3:
    def __init__(self, url):
        self.url = url
        self.video = None

    def download_video(self, output_path, file_name):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        try:
            yt = YouTube(self.url)
            self.video = yt.streams.filter(only_audio=True).first()

            video_file_path = self.video.download(output_path=output_path, filename=file_name)
            print(f"Video descargado en: {video_file_path}")
        except Exception as e:
            print(f"Error al descargar el video: {e}")
