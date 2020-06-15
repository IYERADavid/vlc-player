from gtts import gTTS
import urllib3
import os
 
my_text="you get a virus from colege of science by a pro hacker zenil"

language="en" 


obj = gTTS(text=my_text, lang=language, slow=False)
obj.save('virus.mp4')

os.system('mpgvirus.mp4')


