import youtube_dl
urls = []
while True:
    url = input('Url:')
    if url == '':
        break
    else:
        urls.append(url)
print(urls)
ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': 'true',
    'outtmpl': 'G:/My Drive/320kbps_songs' + '/%(title)s.%(ext)s',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'flac',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)