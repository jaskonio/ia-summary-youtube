import os
import requests

class TranscriptionSummarizer:
    def __init__(self):
        pass

    def summarize(self, transcription, model="gemma:2b", max_tokens=150):
        try:
            OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

            OLLAMA_PROMPT = self.create_prompt(transcription)
        
            OLLAMA_DATA = {
            "model": "gemma:2b",
            "prompt": OLLAMA_PROMPT,
            "stream": False,
            "keep_alive": "1m",
            }

            response = requests.post(OLLAMA_ENDPOINT, json=OLLAMA_DATA)

            return response.json()["response"]
        except Exception as e:
            print(f"Error al generar el resumen: {e}")
            return None

    def create_prompt(self, transcription):
        prompt = (
            "A continuación se muestra una transcripción de un directo que ha hecho un creador de contenido en youtube sobre temas de AWS."
            "Por favor, haz un resumen compliendo los siguiente requerimientos:"
            "Resalta los temas más importantes discutidos durante el directo"
            "Enumera todas los servicios de interes que se mencionan en el directo"
            "Destaca los ejemplos y actividades para el futuro cercan"
            "El resumen debe ser entendido para aquellas personas que estan empezando en aws."
            "transcripción:\n\n"
            f"{transcription}\n"
        )

        return prompt

    def save_summary(self, summary, output_path, file_name):
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        output_file_path = output_path + "\\" + file_name

        try:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(summary)
            print(f"Resumen guardado en: {output_file_path}")
        except Exception as e:
            print(f"Error al guardar el resumen: {e}")
