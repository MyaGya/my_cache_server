from pytube import YouTube


# YouTube('https://www.youtube.com/watch?v=riI4FGbKN9k').streams.first().download()
# print(YouTube('https://www.youtube.com/watch?v=riI4FGbKN9k').streams)
def download_youtube():
    data = YouTube('https://www.youtube.com/watch?v=riI4FGbKN9k').streams
    for s in data:
        if s.resolution == "1080p":
            s.download()
            return
    data[0].download()


#download_youtube()


