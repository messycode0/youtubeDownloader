from pytube import YouTube as yt

url = "https://www.youtube.com/watch?v=7BXJIjfJCsA"
videoObj = yt(url)

print(videoObj.title)

videoObj = videoObj.streams.get_highest_resolution().download(filename="Output.mp4")
