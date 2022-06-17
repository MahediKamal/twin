import cv2
import face_recognition

class Photo_Matching:
    def __init__(self):
        print("Photo_Matching object initialized")

    def moduledata(self):# this function contains information about this module
        print("photo matching module info ***************")
        print("     Stranger (match taken photo with the database)")
        print("     Owner (match taken photo with the database)")
        print("     Family member (match taken photo with the database)")
        print("end of info *****************")
    def match(self, img1, img2):
    	#return true/false after matching 2 image
        rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img_encoding1 = face_recognition.face_encodings(rgb_img1)[0]

        rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

        result = face_recognition.compare_faces([img_encoding1], img_encoding2)
        return result
    	
    def replaceStrengerImage(self):
    	#replace prev strenger with cur
        curStrenger = cv2.imread("images/curStrenger.png")
        cv2.imwrite("images/prvStrenger.png", curStrenger)
