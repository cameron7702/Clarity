import io
import os
from PIL import Image, ImageDraw, ImageFont, ImageGrab
from google.cloud import vision
from picamera import PiCamera
import time

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/pi/Desktop/smartglasses/emotion-glasses-fecb95fef2fe.json'

emotion_dict = {'UNKNOWN': 0, 'VERY_UNLIKELY': 1, 'UNLIKELY': 2, 'POSSIBLE': 3,
                       'LIKELY': 4, 'VERY_LIKELY': 5}
emotions = ['ANGER', 'JOY', 'SURPRISE', 'SORROW']
cam = PiCamera()

def detect_faces(path):
    face_list = []
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.face_detection(image=image)
    faces = response.face_annotations

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    for face in faces:
        emotion_rank = []
        emotion_rank.append(emotion_dict[likelihood_name[face.anger_likelihood]])
        emotion_rank.append(emotion_dict[likelihood_name[face.joy_likelihood]])
        emotion_rank.append(emotion_dict[likelihood_name[face.surprise_likelihood]])
        emotion_rank.append(emotion_dict[likelihood_name[face.sorrow_likelihood]])

        if max(emotion_rank) > 3:
            face_list.append(emotions[emotion_rank.index(max(emotion_rank))])
        else:
            face_list.append('NEUTRAL')

    try:
        emotion = face_list[0]
    except:
        emotion = 'No face detected'

    if response.error.message:
        raise Exception(response.error.message)

    return emotion

def get_emotions():
    cam.start_preview()
    time.sleep(1)
    cam.capture('/home/pi/Desktop/smartglasses/input.png')
    cam.stop_preview()

    emotion = detect_faces('/home/pi/Desktop/smartglasses/input.png')
    return emotion