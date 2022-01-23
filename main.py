import face
import voice
import notification
import mood_detection
import photo_matching

f = face.Face()
f.moduledata()

v = voice.Voice()
v.moduledata()

n = notification.Notification()
n.moduledata()

p = photo_matching.Photo_Matching();
p.moduledata()

m = mood_detection.Mood_Detection()
m.moduledata()
