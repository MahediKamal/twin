#source venv/bin/activate
import get_image
import photo_matching
import notification
import mood_detect
# import face
# import voice

moodTimer = 0
arreyOfMoods[]
while True:
	try:
		camera = get_image.getImageFromApp()
		image = camera.getImage()
		
		#detect strenger
		matcher = photo_matching.Photo_Matching();
		bool isOwner = matcher.match(image, 'images/owner.png')
		if isOwner == False: #is a strenger
			writer = notification.Notification()
			writer.writeNofification()
			writer.saveStrengerPhoto()
			
			#check if it is a new strenger
			bool sameStrenger = matcher.match('images/curStrenger.png', 'images/prvStrenger.png')
			if sameStrenger == False:
				matcher.replaceStrengerImage()
				sendNotification = True 
			else: 
				sendNotification = False
		else:
			mood = mood_detection.Mood_Detection()
			curMood = mood.detect()
			arreyOfMoods.append()
			moodTimer = moodTimer + 1
			if moodTimer == 60:
				#find average mood
				
				moodTimer = 0
				arreyOfMoods.clear()
	except:
		print("camera.getImage() not working")

