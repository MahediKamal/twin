#source venv/bin/activate
# pip install virtualenv
# virtualenv env
# pip install keras
# pip install opencv-python
# pip install face-recognition


import time
import cv2
import get_image
import photo_matching
import notification
import mood_detection
import os.path
# import face
# import voice
class Main:
	def __init__(self):
		print("start main")

	def run(self):
		moodTimer = 0
		arreyOfMoods = []
		sendNotification = False

		while True:
			try:
				camera = get_image.getImageFromApp()
				image = camera.getImage()
				cv2.imshow('img', image)
				cv2.waitKey(10)

				# detect strenger
				matcher = photo_matching.Photo_Matching()
				owner = cv2.imread("images/prvStrenger2.png")

				isOwner = matcher.match(image, owner)
				print(isOwner)
				# # print(type(isOwner))
				if isOwner[0] == False: #is a strenger
					print("is stranger")
					file1 = open("text/moodFlg.txt", "w")
					file1.write("False")
					file1.close()

					writer = notification.Notification()
					writer.writeNofification()
					writer.saveStrengerPhoto(image)
			#
					#check if it is a new strenger
					curStrenger = cv2.imread("images/curStrenger.png")
					file1 = open("text/strengerCount.txt", "r")
					strengerNum = int(file1.read())
					file1.close()
					print(strengerNum)
					sameStrenger = False
					for i in range(strengerNum):
						name = "images/prvStrenger" + str(i+1) + ".png"
						filname = os.path.normpath(name)
						strng = cv2.imread(filname)
						cv2.imshow('img', strng)
						cv2.waitKey(10)
						dc = matcher.match(curStrenger, strng)
						if dc[0] == True:
							sameStrenger = True


					print(sameStrenger)

					file2 = open("text/notiFlg.txt", "w")
					if sameStrenger == False:
						matcher.replaceStrengerImage()
						sendNotification = True
						file2.write("True")
						strengerNum = strengerNum + 1
						file1 = open("text/strengerCount.txt", "w")
						file1.write(str(strengerNum))
						file1.close()
						name = "images/prvStrenger" + str(strengerNum) + ".png"
						cv2.imwrite(name, image)

					else:
						sendNotification = False
						file2.write("False")
					file2.close()
					break

				else:
					print("In owner")
					mood = mood_detection.Mood_Detection()
					curMood = mood.detect(image)
					print(curMood)
					writer = notification.Notification()
					writer.writeMood(curMood)

					break

			except:
				print("in except")
				file1 = open("text/moodFlg.txt", "w")
				file1.write("False")
				file1.close()

				file1 = open("text/notiFlg.txt", "w")
				file1.write("False")
				file1.close()
				break
			return None

# start.run()
# x = Main()
# x.run()