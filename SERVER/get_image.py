import cv2
# import AppImage
import SS
class getImageFromApp:
    def __init__(self):
        print("getImageFromApp object initialized")
    def moduledata(self):# this function contains information about this module
        print("getImageFromApp mo ***************")
        print("     get image from app")
        print("end of info *****************")
       
    def getImage(self):
    	#fetch image from app and return it
        ss = SS.SS()
        ss.takeSS()
        capturedImg = cv2.imread("monitor-1.png")
        # capturedImg = cv2.imread("images/capturedImg.png")
        cv2.imwrite("images/capturedImg.png", capturedImg)
        return capturedImg
