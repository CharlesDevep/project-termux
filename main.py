import os
from googleapiclient.discovery import build

def buscar_videos_youtube(api_key, query):
    # Crear un objeto de servicio
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Hacer una solicitud para buscar videos
    request = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=10
    )
    response = request.execute()

    # Mostrar los resultados
    for item in response['items']:
        video_title = item['snippet']['title']
        video_id = item['id'].get('videoId')
        if video_id:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            print(f'Título: {video_title}\nURL: {video_url}\n')

if __name__ == "__main__":
    API_KEY = 'AIzaSyDRTRZFoh846tB6eYY5Cn_07D2gQ0NGBwg'  # Reemplaza con tu API Key
    query = input("Introduce el término de búsqueda: ")
    buscar_videos_youtube(API_KEY, query)