from datetime import datetime
import cv2
class Notification:
    def __init__(self):
        print("notification object initialized")
    def moduledata(self):# this function contains information about this module
        print("Notification module info ***************")
        print("     Send notification")
        print("     Send video")
        print("end of info *****************")
    def writeNofification(self):
        file1 = open("text/notificationFile.txt","w")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        file1.write("Stranger detected at :" + current_time + "Avash,you must check it now.")
        file1.close()
    def writeMood(self, mood):
        file1 = open("text/moodFile.txt", "w")
        print("writing mood")
        file1.write(mood)
        file1.close()

        file1 = open("text/moodFlg.txt", "w")
        print("setting moodFlg True and NotificationFlg False")
        file1.write("True")
        file1.close()
        file1 = open("text/notiFlg.txt", "w")
        file1.write("False")
        file1.close()
    
    def saveStrengerPhoto(self, img):
        cv2.imwrite("images/curStrenger.png", img)