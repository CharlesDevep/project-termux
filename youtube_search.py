import os
from googleapiclient.discovery import build

def buscar_videos_youtube(api_key, query):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=11
    )
    response = request.execute()

    # Mostrar los resultados en la terminal
    videos = []
    print(f'Resultados de búsqueda para: {query}\n')
    
    for index, item in enumerate(response['items'], start=0):
        video_title = item['snippet']['title']
        video_id = item['id'].get('videoId')
        if video_id:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append((video_title, video_id))
            print(f"{index}. {video_title} - {video_url}")

    # Solicitar al usuario que elija un video
    seleccion = int(input("\nSelecciona el número del video que deseas ver: ")) - 1
    
    if 0 <= seleccion < len(videos):  # Cambié esta línea
        video_id = videos[seleccion][1]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"Reproduciendo video: {video_url}")
        
        # Crear un archivo HTML para reproducir el video en pantalla completa
        with open('video.html', 'w') as f:
            f.write(f'''
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Video de YouTube</title>
                <style>
                    body, html {{
                        margin: 0;
                        padding: 0;
                        height: 100%;
                        overflow: hidden;
                    }}
                    iframe {{
                        width: 100%;
                        height: 100%;
                        border: none;
                    }}
                </style>
            </head>
            <body>
                <iframe src="https://www.youtube.com/embed/{video_id}?autoplay=1&controls=0&fullscreen=1" allowfullscreen></iframe>
            </body>
            </html>
            ''')
        
        print("Se ha creado el archivo video.html. Ábrelo en tu navegador para ver el video.")
    else:
        print("Selección no válida.")

if __name__ == "__main__":
    API_KEY = 'AIzaSyDRTRZFoh846tB6eYY5Cn_07D2gQ0NGBwg'  # Reemplaza con tu API Key
    query = input("Introduce el término de búsqueda: ")
    buscar_videos_youtube(API_KEY, query)
