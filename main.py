#source venv/bin/activate
import cv2
import get_image
import photo_matching
import notification
import mood_detect
# import face
# import voice

moodTimer = 0
arreyOfMoods = []
sendNotification = False
while True:
	try:
		camera = get_image.getImageFromApp()
		image = camera.getImage()
		break
		# detect strenger
		matcher = photo_matching.Photo_Matching()
		owner = cv2.imread("images/owner.png")
		bool isOwner = matcher.match(image, owner)
		if isOwner == False: #is a strenger
			writer = notification.Notification()
			writer.writeNofification()
			writer.saveStrengerPhoto(image)
			
			#check if it is a new strenger
			curStrenger = cv2.imread("images/curStrenger.png")
			prvStrenger = cv2.imread("images/prvStrenger.png")
			bool sameStrenger = matcher.match(curStrenger, prvStrenger)
			if sameStrenger == False:
				matcher.replaceStrengerImage() 
				sendNotification = True 
			else: 
				sendNotification = False
		else:
			mood = mood_detection.Mood_Detection()
			curMood = mood.detect()
			arreyOfMoods.append(curMood)
			moodTimer = moodTimer + 1
			if moodTimer == 60:
				# find average mood
				Angry = 0 
				Disgust = 0 
				Fear = 0
				Happy = 0
				Neutral = 0
				Sad = 0
				Surprise = 0
				for m in arreyOfMoods:
					if(m == "Angry"):
						Angry = Angry + 1
					if(m == "Disgust"):
						Disgust = Disgust + 1
					if(m == "Fear"):
						Fear = Fear + 1
					if(m == "Happy"):
						Happy = Happy + 1
					if(m == "Neutral"):
						Neutral = Neutral + 1
					if(m == "Sad"):
						Sad = Sad + 1
					if(m == "Surprise"):
						Surprise = Surprise + 1
				moodTimer = 0
				arreyOfMoods.clear()
			# write mood in txt
			# set flg = true
	except:
		print("camera.getImage() not working")
		break

