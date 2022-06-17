import cv2
import AppImage
class getImageFromApp:
    def __init__(self):
        print("getImageFromApp object initialized")
    def moduledata(self):# this function contains information about this module
        print("getImageFromApp mo ***************")
        print("     get image from app")
        print("end of info *****************")
       
    def getImage(self):
    	#fetch image from app and return it

        d = AppImage.Dummy()
        capturedImg = d.get_image()
        # capturedImg = cv2.imread("images/owner.png")
        cv2.imwrite("images/capturedImg.png", capturedImg)
        return capturedImg
