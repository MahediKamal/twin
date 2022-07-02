#pip install mss
from mss import mss
class SS:
    def __init__(self):
        print("SS object initialized")
    def moduledata(self):# this function contains information about this module
        print("Voice module info ***************")
        print("     Instruction ( get the instruction given by the user)")
        print("     Reminder ( will give the reminder)")
        print("     Text (convert voice to text)")
        print("end of info *****************")
    def takeSS(self):

        with mss() as sct:
            # sct.shot()
            filename = sct.shot()
            print(filename)
            print("image taken")