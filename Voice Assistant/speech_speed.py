from pygame import mixer as m

m.init(25500)
print('laying')
m.music.load('intro.mp3')
m.music.play()
