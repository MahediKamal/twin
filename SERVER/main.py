#source venv/bin/activate
import time

import cv2
import get_image
import photo_matching
import notification
import mood_detection
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
				owner = cv2.imread("images/owner.png")
				isOwner = matcher.match(image, owner)
				print(isOwner)
				# # print(type(isOwner))
				if isOwner[0] == False: #is a strenger
					print("is strenger")
					writer = notification.Notification()
					writer.writeNofification()
					writer.saveStrengerPhoto(image)
			#
					#check if it is a new strenger
					curStrenger = cv2.imread("images/curStrenger.png")
					prvStrenger = cv2.imread("images/prvStrenger.png")
					sameStrenger = matcher.match(curStrenger, prvStrenger)

					print(sameStrenger)

					file2 = open("text/notiFlg.txt", "w")
					if sameStrenger[0] == False:
						matcher.replaceStrengerImage()
						sendNotification = True
						file2.write("True")
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
					arreyOfMoods.append(curMood)
					# moodTimer = moodTimer + 1
					# if moodTimer == 60:
			# 			# find average mood
			# 			Angry = 0
			# 			Disgust = 0
			# 			Fear = 0
			# 			Happy = 0
			# 			Neutral = 0
			# 			Sad = 0
			# 			Surprise = 0
			# 			for m in arreyOfMoods:
			# 				if(m == "Angry"):
			# 					Angry = Angry + 1
			# 				if(m == "Disgust"):
			# 					Disgust = Disgust + 1
			# 				if(m == "Fear"):
			# 					Fear = Fear + 1
			# 				if(m == "Happy"):
			# 					Happy = Happy + 1
			# 				if(m == "Neutral"):
			# 					Neutral = Neutral + 1
			# 				if(m == "Sad"):
			# 					Sad = Sad + 1
			# 				if(m == "Surprise"):
			# 					Surprise = Surprise + 1
			# 			moodTimer = 0
			# 			arreyOfMoods.clear()
			# 		# write mood in txt
			# 		# set flg = true
			except:
				print("in except")
				file1 = open("text/moodFlg.txt", "w")
				file1.write("Flase")
				file1.close()

				file1 = open("text/notiFlg.txt", "w")
				file1.write("Flase")
				file1.close()
				break
			return None

# start.run()
