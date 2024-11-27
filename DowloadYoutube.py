import os
from yt_dlp import YoutubeDL

def download_youtube_with_yt_dlp(url, choice, output_folder):
    """Descargar videos o audios de YouTube usando yt-dlp"""
    try:
        # Convertir ruta de salida a absoluta
        output_folder = os.path.abspath(output_folder)
        
        # Configuración según la elección del usuario
        if choice == '1':  # Descargar video
            options = {
                'format': 'bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',  # Asegurar salida en MP4
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',  # Asegurar formato MP4 compatible
                }],
                'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Ruta de salida
            }
        elif choice == '2':  # Descargar solo audio
            options = {
                'format': 'bestaudio/best',  # Mejor calidad de audio
                'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Ruta de salida
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',  # Convertir a MP3
                    'preferredquality': '192',  # Calidad de audio
                }],
            }
        else:
            print("Opción no válida.")
            return
        
        # Crear carpeta de destino si no existe
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Descargar el contenido
        with YoutubeDL(options) as ydl:
            print(f"Descargando desde: {url}")
            ydl.download([url])
            print(f"Descarga completada. Archivo guardado en: {output_folder}")
    except Exception as e:
        print("Error al descargar:", e)

if __name__ == "__main__":
    # Solicitar datos al usuario
    url = input("Ingresa el enlace del video de YouTube: ")
    print("¿Qué deseas descargar?")
    print("1. Video")
    print("2. Solo audio (MP3)")
    choice = input("Elige una opción (1 o 2): ")
    output_folder = input("Ingresa la carpeta donde guardar los archivos (ruta completa o nombre): ")
    
    # Llamar a la función
    download_youtube_with_yt_dlp(url, choice, output_folder)
