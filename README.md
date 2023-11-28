# SpotifyDownloader
Python programme to search and download Spotify playlist from youtube.
pre-installs
pip install spotipy --upgrade
pip install youtube-search-python
pip install -U yt-dlp

ffmpeg is needed for post processing after download
Here are the steps to install ffprobe and ffmpeg:
Download FFmpeg:
Visit the official FFmpeg website: https://ffmpeg.org/download.html
Download the appropriate version for your operating system (Windows, in this case).
Extract the downloaded archive to a folder of your choice.

Add FFmpeg to the System Path:
Add the path to the bin folder inside the extracted FFmpeg folder to your system's PATH environment variable.
On Windows, you can do this by adding the following to your system or user environment variables:
Variable Name: PATH
Variable Value: Path to the bin folder inside the extracted FFmpeg folder.

Run the Script:
After installing FFmpeg and updating the PATH, try running your script again.
By adding FFmpeg to the PATH, the script will be able to find and use these tools for post-processing during the download. If the issue persists, please double-check the PATH variable and ensure    that it includes the correct path to the FFmpeg bin folder.

Get your spotify client id and secret key by apllying for spotify developer in this link https://developer.spotify.com/

The playlist id is the id present in the URL of the spotify playlist 
for example take this URL https://open.spotify.com/playlist/7xmpNYZ15D6b43BHzYQCLt?si=fb02f907c40a49dd
                                                            7xmpNYZ15D6b43BHzYQCLt   this is the ID  
