from datetime import datetime

class Notification:
    def __init__(self):
        print("notification object initialized")
    def moduledata(self):# this function contains information about this module
        print("Notification module info ***************")
        print("     Send notification")
        print("     Send video")
        print("end of info *****************")
    def writeNofification():
        file1 = open("notificationFile.txt","w")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        file1.write("Strenger detected at :" + current_time)
        file1.close()
    
    def saveStrengerPhoto(img):
        curStrenger = cv2.imread("images/curStrenger.png")
        curStrenger = img
    

