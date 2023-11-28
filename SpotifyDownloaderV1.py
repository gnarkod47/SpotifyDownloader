import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch
import yt_dlp

def download_playlist(playlist_id, output_dir, client_id, client_secret):

    # Connect to Spotify
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Get playlist tracks
    playlist = sp.playlist(playlist_id)
    tracks = playlist['tracks']['items']

    # Download songs
    for track in tracks:
        song_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']

        # Search for song on YouTube
        search_query = f'{song_name} by {artist_name}'
        video_search = VideosSearch(search_query, limit=1)

        results = video_search.result()

        if results and 'link' in results['result'][0]:
            video_url = results['result'][0]['link']
            print(f'Downloading: {song_name} by {artist_name}')

            # Download video using yt-dlp
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': f'{output_dir}/{playlist["name"]}/%(title)s.%(ext)s',
                'default_search': 'ytsearch',
            }
            ydl = yt_dlp.YoutubeDL(ydl_opts)
            ydl.download([video_url])

        else:
            print(f'No search results for: {song_name} by {artist_name}')

if __name__ == '__main__':
    client_id = '2c00c05a2ba9483ba0a4df441d26c090'
    client_secret = '6680c05d9c3c47a4a35d17434a244427'
    playlist_id = '7xmpNYZ15D6b43BHzYQCLt'
    output_directory = r"C:\Users\gnark\Downloads\Spotify playlist"
    download_playlist(playlist_id, output_directory, client_id, client_secret)




