from gtts import gTTS
import os

fh= open("text.txt","r")
textToRead = fh.read().replace("\n", " ")
 
language = 'en'

output = gTTS(text=textToRead,lang=language,slow=False)

output.save("output.mp3")

fh.close()

os.system("start output.mp3")