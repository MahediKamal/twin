#pip install mss
from mss import mss
import cv2
import ssl
import certifi
import urllib
import urllib.request
import numpy as np
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

        # with mss() as sct:
        #     # sct.shot()
        #     filename = sct.shot()
        #     print(filename)
        #     print("image taken")

        print("image taken using opencv")
        url = 'https://192.168.43.85:8080/shot.jpg'

        # while True:
        ssl._create_default_https_context = ssl._create_unverified_context
        imgResp = urllib.request.urlopen(url)
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)

        cv2.imwrite("monitor-1.png", img)
        cv2.imshow('test', img)
        cv2.waitKey(100)

# x = SS()
# x.takeSS()