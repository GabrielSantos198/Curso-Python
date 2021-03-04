from pygame import mixer

mixer.init()
mixer.music.load('som.mp3')
mixer.music.play()
while True:
	print("")