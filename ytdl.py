import pafy

url = "https://www.youtube.com/watch?v=9fw3rCU_5jI"
video = pafy.new(url)

bestaudio = video.getbestaudio()
bestaudio.download()


