import whisper
import os

class MP3Transcriber:
    def __init__(self, model_size="small"):
        self.model = whisper.load_model(model_size)

    def transcribe(self, mp3_file_path):
        if not os.path.exists(mp3_file_path):
            print(f"El archivo {mp3_file_path} no existe.")
            return None

        try:
            result = self.model.transcribe(mp3_file_path, language='spanish')
            transcription = result["text"]

            return transcription
        except Exception as e:
            print(f"Error al transcribir el archivo .mp3: {e}")
            return None

    def save_transcription(self, transcription, output_path, file_name):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        output_file_path = output_path + "\\" + file_name
        try:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(transcription)
            print(f"Transcripción guardada en: {output_file_path}")
        except Exception as e:
            print(f"Error al guardar la transcripción: {e}")
