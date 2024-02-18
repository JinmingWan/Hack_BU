# Import the required module for text
# to speech conversion

from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
from io import BytesIO
import playsound


mp3_fp = BytesIO()

text=input("please input your text: \n")
# The text that you want to convert to audio


# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
tts = gTTS(text=text, lang=language, slow=False)
tts.save("welcome.mp3")
playsound.playsound("welcome.mp3")



