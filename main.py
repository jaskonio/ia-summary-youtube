
import os
from src.mp3_transcriber import MP3Transcriber
from src.youtube_to_mp3 import YouTubeToMP3
from src.transcription_summarizer import TranscriptionSummarizer


if __name__ == "__main__":
    url = "xxx"
    parent_path = os.getcwd()

    downloads_mp3 = f'{parent_path}\\downloads'
    mp3_file_name = f'audiofile.mp3'


    transcription_path = f'{parent_path}\\transcription'
    transcription_file_name = 'transcription.txt'

    summary_path = f'{parent_path}\\summary'
    summary_file_name = 'summary.txt'

    yt_to_mp3 = YouTubeToMP3(url)
    yt_to_mp3.download_video(downloads_mp3, mp3_file_name)

    transcriber = MP3Transcriber(model_size="base")
    transcription = transcriber.transcribe(downloads_mp3 + "\\" + mp3_file_name)

    transcriber.save_transcription(transcription, transcription_path, transcription_file_name)

    transcription_file = ''
    with open(transcription_path + '\\' + transcription_file_name, 'r', encoding='utf-8') as file:
        transcription_file = file.read()

    summarizer = TranscriptionSummarizer()
    summary = summarizer.summarize(transcription_file)
    summarizer.save_summary(summary, summary_path, summary_file_name)
