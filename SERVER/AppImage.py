import cv2

class Dummy:
    def __init__(self):
        print("app image send object initialized")
    def moduledata(self):# this function contains information about this module
        print("Voice module info ***************")
        print("     Instruction ( get the instruction given by the user)")
        print("     Reminder ( will give the reminder)")
        print("     Text (convert voice to text)")
        print("end of info *****************")
    def get_image(self):
        cap = cv2.VideoCapture(0)
        _, frame = cap.read()
        return frame
