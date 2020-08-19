
from gtts import gTTS
import os
import time
import subprocess



def say(inputString):
    #inputString = "hello world"
    
    num_of_words = inputString.split(' ')
    
    tts = gTTS(inputString, lang = 'en')
    
    buffer_name = "string_speak_buff.mp3"

    tts.save(buffer_name)
    
    os.system("open {}".format(buffer_name))
    
    time.sleep(1*0.6*len(num_of_words))
    
    dir_path_mp3 = "/Users/joentze/Documents/python_test/{}".format(buffer_name)
    dir_path_musicplayer = "/Users/joentze/Music/Music/Media.localized/Unknown\ Artist/Unknown\ Album/{}".format(buffer_name)

    string_to_rm = "rm "+ dir_path_mp3
    recent_rm = "rm" + dir_path_musicplayer

    subprocess.call([string_to_rm, recent_rm],shell = True)
    #os.remove("buffer.mp3")
    print("deleted")


