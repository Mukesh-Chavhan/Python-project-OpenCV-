import cv2
import os
import time
import random
import pygame
pygame.init()
# import matplotlib.pyplot as plt
from deepface import DeepFace


def most_common_string(array_string):
    string_count = {}
    for i in array_string:
        if i in string_count:
            string_count[i] += 1
        else:
            string_count[i] = 1

    max_count = 0
    dominant_emotion = ""
    for i, count in string_count.items():
        if count > max_count:
            max_count = count
            dominant_emotion = i

    print("Most commonly repeated string: ", dominant_emotion)
    print("Count: ", max_count)
    if dominant_emotion=="happy":

            happy_songs=['D:\demo_Opencv\happy_songs\Aye_Khuda_[Full_Song]_Paathshaala(256k).mp3']
            Happy_songs=random.choice(happy_songs)

  # songs="D:\demo_Opencv\songs\Alan_Walker_-_The_Drum_(Official_Music_Video)(128k).mp3"
            pygame.mixer.music.load(Happy_songs)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                    continue
            pygame.quit()
    elif dominant_emotion=="sad":
      
            sad_songs=['D:\demo_Opencv\sad_songs\Ava_Max_-_Into_Your_Arms__NO_RAP__%5BLyrics_Vietsub%5D_%7E_TikTok_Hits_%7E(256k).mp3']
            Sad_songs=random.choice(sad_songs)


#    songs="D:\openCV\Alec_Benjamin_-_Let_Me_Down_Slowly_(Lyrics)(128k).mp3"
            pygame.mixer.music.load(Sad_songs)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                 continue
            pygame.quit()

    elif dominant_emotion=="neutral":

            NEUTRAL_songs=['D:\demo_Opencv\sadharan_songs\A.R._Rahman_-_Tere_Bina_Best_Video__Guru_Aishwarya_Rai_Abhishek_Bachchan_Chinmayi(256k).mp3']


            Neutrals_songs=random.choice(NEUTRAL_songs)
            pygame.mixer.music.load(Neutrals_songs)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                   continue
            pygame.quite()

    elif dominant_emotion=="angry":

              angry_songs=['D:\demo_Opencv\Angry_songs\Apna_Time_Aayega___Gully_Boy___Ranveer_Singh___Alia_Bhatt___DIVINE___Dub_Sharma___Zoya_Akhtar(256k).mp3']
              Angry_songs=random.choice(angry_songs) 
              pygame.mixer.music.load(Angry_songs)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                    continue
              pygame.quite()
    elif dominant_emotion=="disgust":
   
              disgust_song=['D:\demo_Opencv\disgust_songs\BHAAG_DK_BOSE_I_DELHI_BELLY_I_RAM_SAMPATH(256k).mp3']
              Disgust_songs=random.choice(disgust_song)
     
    #  Angry_songs=random.choice(Disgust_songs) 
              pygame.mixer.music.load(Disgust_songs)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                    continue
              pygame.quite()

    elif dominant_emotion=="fear":
   
              fear_songs=['D:\demo_Opencv\Fear_songs\Ajnabi_Hawaayein_[Full_Song]_Shaapit_By_Shreya_Ghoshal(256k).mp3']
              Fear_songs=random.choice(fear_songs)
              pygame.mixer.music.load(Fear_songs)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                    continue
              pygame.quite()

    else:
    
              surprise_songs=['D:\demo_Opencv\surprise_songs\_Lungi_Dance_Chennai_Express__New_Video_Feat._Honey_Singh%2C_Shahrukh_Khan%2C_Deepika(256k).mp3' ] 
              Surprise_songs=random.choice(surprise_songs)

              pygame.mixer.music.load(Surprise_songs)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                    continue
              pygame.quite()

    # plt.waitforbuttonpress()
    # plt.close('all')


# no. of photos to be clicked
NUM_PHOTOS = 5
# array of string to store the location of images
photos = []

cap = cv2.VideoCapture(0)
# loop for capturing multiple photo
for i in range(NUM_PHOTOS):

    # cv2.waitKey()

#    capture photo
    ret, frame = cap.read()
# store file name according to real time stam 
    filename = f"photo_{time.time()}.jpg"
    # creating file path to images
    filepath = os.path.join("images", filename)

    cv2.imwrite(filepath, frame)
#    storing file path in array of string i.e photos
    photos.append(filepath)

cap.release()
#  creating another array of string to store the every photo emotion
string_array=[]

size=len(photos)
for i in range(0,size):
    
    img = cv2.imread(photos[i])
    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    pred = DeepFace.analyze(img)
    emotions_dict = pred[0]['emotion']

    emotion = max(emotions_dict, key=emotions_dict.get)
    string_array.append(emotion)

most_common_string(string_array) 
cv2.destroyAllWindows()



