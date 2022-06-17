from gtts import gTTS
import webbrowser

class Voice:
    def __init__(self):
        print("voice object initialized")
    def moduledata(self):# this function contains information about this module
        print("Voice module info ***************")
        print("     Instruction ( get the instruction given by the user)")
        print("     Reminder ( will give the reminder)")
        print("     Text (convert voice to text)")
        print("end of info *****************")
    def speak(self, strr):# this function contains information about this module
        language = 'en'
        myobj = gTTS(text=strr, lang=language, slow=False)
        myobj.save("voice.mp3")
        webbrowser.open("voice.mp3")

		
