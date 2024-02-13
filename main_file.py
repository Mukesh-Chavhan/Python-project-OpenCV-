import cv2
import os
import time
import random
import pygame
pygame.init()
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

            happy_songs=['D:\demo_Opencv\happy_songs\Aye_Khuda_[Full_Song]_Paathshaala(256k).mp3',
              
                      'D:\demo_Opencv\happy_songs\Clean_Bandit_-_Rockabye_(Lyrics)_feat._Sean_Paul_&_Anne-Marie(256k).mp3',

                      'D:\demo_Opencv\happy_songs\I_Hate_Luv_Storys_Title_Track_Full_Video_-_Sonam_Kapoor_Imran_Khan_Vishal_Dadlani_Kumaar(256k).mp3',

                      'D:\demo_Opencv\happy_songs\Kabhi_Kabhi_Aditi_Zindagi___Bollywood_Lo-fi__Slowed___Reverbed_(256k).mp3',

                      'D:\demo_Opencv\happy_songs\Lyrical__Ik_Junoon__Paint_It_Red____Zindagi_Na_Milegi_Dobara___Hrithik%2C_Katrina%2C_Farhan_Akhtar(256k).mp3',

                      'D:\demo_Opencv\happy_songs\MITRAZ_-_Mashup_2(256k).mp3',

                ' D:\demo_Opencv\surprise_songs\Chal_Chaiya_Chaiya___4K_Video_Song___Dil_Se_1998___Sukhwinder_Singh___Sapna_Awasthi___Shahrukh_Khan(256k).mp3',

                      'D:\demo_Opencv\happy_songs\OneRepublic_-_Counting_Stars_(Lyrics)(48k).mp3',

                      'D:\demo_Opencv\happy_songs\RRR__Naatu_Naatu_Song__TELUGU__NTR%2C_Ram_Charan___M_M_Keeravaani___SS_Rajamouli___Telugu_Songs_2021(256k).mp3',

                      'D:\demo_Opencv\happy_songs\Sadi_Gali_Full_Song_Tanu_Weds_Manu___Ft._Kangna_Ranaut%2C_R_Madhavan(256k).mp3',

                      'D:\demo_Opencv\happy_songs\Tum_Hi_Ho_Bandhu-_Cocktail_HQ_(Audio)(256k).mp3',

                      'D:\demo_Opencv\happy_songs\Zoobi_Doobi_-_3_Idiots___Aamir_Khan___Kareena_Kapoor__Sonu_Nigam%2CShreya_Ghoshal_Shantanu_M%2CSwanand_K(256k).mp3']
            Happy_songs=random.choice(happy_songs)

            pygame.mixer.music.load(Happy_songs)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                    continue
            pygame.quit()
    elif dominant_emotion=="sad":
      
            sad_songs=['D:\demo_Opencv\sad_songs\Ava_Max_-_Into_Your_Arms__NO_RAP__%5BLyrics_Vietsub%5D_%7E_TikTok_Hits_%7E(256k).mp3',


                    'D:\demo_Opencv\sad_songs\Glass_Animals_-_Heat_Waves_(Official_Video)(256k).mp3',

                    'D:\demo_Opencv\sad_songs\LO_MAAN_LIYA_Full_Video_Song___Raaz_Reboot___Arijit_Singh_Emraan_Hashmi%2CKriti_Kharbanda%2CGaurav_Arora(256k).mp3',

                    'D:\demo_Opencv\sad_songs\Main_Dhoondne_Ko_Zamaane_Mein_Lyrics___Heartless___Arijit_Singh___Arafat%2C_Gaurav___Adhyayan%2C_Ariana_(256k).mp3',

                    'D:\demo_Opencv\sad_songs\Main_Rahoon_Ya_Na_Rahoon_Full_Video___Emraan_Hashmi%2C_Esha_Gupta___Amaal_Mallik%2C_Armaan_Malik(256k).mp3',

                    'D:\demo_Opencv\sad_songs\O_Khuda_Full_Song_with_LYRICS___Hero___Sooraj_Pancholi%2C_Athiya_Shetty___Amaal_Mallik___T-Series(256k).mp3',

                   'D:\demo_Opencv\sad_songs\ZAYN_-_Dusk_Till_Dawn_(Official_Video)_ft._Sia(256k).mp3']
            Sad_songs=random.choice(sad_songs)


            pygame.mixer.music.load(Sad_songs)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                 continue
            pygame.quit()

    elif dominant_emotion=="neutral":

            NEUTRAL_songs=['D:\demo_Opencv\sadharan_songs\A.R._Rahman_-_Tere_Bina_Best_Video__Guru_Aishwarya_Rai_Abhishek_Bachchan_Chinmayi(256k).mp3',
                           
                        'D:\demo_Opencv\sadharan_songs\Full_Song_Tera_Ban_Jaunga___Kabir_Singh___Shahid_K%2C_Kiara_A%2C_Sandeep_V___Tulsi_Kumar%2C_Akhil_Sachdeva(256k).mp3',

                        'D:\demo_Opencv\sadharan_songs\Full_Video__Tum_Se_Hi___Jab_We_Met___Kareena_Kapoor%2C_Shahid_Kapoor___Mohit_Chauhan___Pritam(256k).mp3',

                        'D:\demo_Opencv\sadharan_songs\Kabira_Encore_-_Yeh_Jawaani_Hai_Deewani___Ranbir_Kapoor%2C_Deepika_Padukone(256k).mp3',

                        'D:\demo_Opencv\sadharan_songs\Malang__Chal_Ghar_Chalen___Aditya_Roy_Kapur%2C_Disha_Patani___Mithoon_ft._Arijit_Singh%2C_Sayeed_Quadri(256k).mp3',

                        'D:\demo_Opencv\sadharan_songs\Muskurane_ki_Wajah_tum_ho_song__lyrics___Arijit_Singh___Movie-_Citylight(256k).mp3',

                        'D:\demo_Opencv\sadharan_songs\Tujh_Mein_Rab_Dikhta_Hai___Female_Version___Rab_Ne_Bana_Di_Jodi%2C_SRK%2C_Anushka_Sharma%2C_Shreya_Ghoshal(256k).mp3',

                        'D:\demo_Opencv\sadharan_songs\Yeh_Dooriyan_-_Official_Music_Video___Love_Aaj_Kal___Sara___Kartik___Pritam___Mohit_Chouhan(256k).mp3']


            Neutrals_songs=random.choice(NEUTRAL_songs)
            pygame.mixer.music.load(Neutrals_songs)
            pygame.mixer.music.play()
            # print("playing: Illahi_-_Yeh_Jawaani_Hai_Deewani___Ranbir_Kapoor")

            while pygame.mixer.music.get_busy():
                   continue
            pygame.quite()

    elif dominant_emotion=="angry":

              angry_songs=['D:\demo_Opencv\Angry_songs\Apna_Time_Aayega___Gully_Boy___Ranveer_Singh___Alia_Bhatt___DIVINE___Dub_Sharma___Zoya_Akhtar(256k).mp3',

                        'D:\demo_Opencv\Angry_songs\Brothers_Anthem_Lyric_Video_-_Brothers___Akshay_Kumar___Sidharth_Malhotra(256k).mp3',

                        'D:\demo_Opencv\Angry_songs\DIVINE_-_3_59_AM___Prod._by_Stunnah_Beatz___Official_Music_Video(256k).mp3',

                        'D:\demo_Opencv\Angry_songs\EMIWAY_BANTAI-KHATAM_(OFFICIAL_MUSIC_VIDEO)(256k).mp3',

                        'D:\demo_Opencv\Angry_songs\Get_Ready_To_Fight_Full_Video_Song___BAAGHI___Tiger_Shroff%2C_Grandmaster_Shifuji___Benny_Dayal(256k).mp3',

                        'D:\demo_Opencv\Angry_songs\Jee_Karda__Official_Full_Song____Badlapur___Varun_Dhawan___Yami_Gautam(256k).mp3',

                        'D:\demo_Opencv\Angry_songs\Mera_Intkam_Dekhegi___Shaadi_Mein_Zaroor_Aana___Rajkummar_R%2C_Kriti_K___Krishna_Beuraa__Anand_R_Anand(256k).mp3',

                        'D:\demo_Opencv\Angry_songs\Sulthan_Lyrical__Hindi____KGF_Chapter_2___Rocking_Star_Yash___Prashanth_Neel___Ravi_Basrur__Hombale(256k).mp3',

                        'D:\demo_Opencv\Angry_songs\YALGAAR_-_CARRYMINATI_X_Wily_Frenzy(256k).mp3']
              Angry_songs=random.choice(angry_songs) 
              pygame.mixer.music.load(Angry_songs)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                    continue
              pygame.quite()
    elif dominant_emotion=="disgust":
   
              disgust_song=['D:\demo_Opencv\disgust_songs\BHAAG_DK_BOSE_I_DELHI_BELLY_I_RAM_SAMPATH(256k).mp3',

                         'D:\demo_Opencv\disgust_songs\Chaar_Botal_Vodka_Full_Song_Feat._Yo_Yo_Honey_Singh%2C_Sunny_Leone___Ragini_MMS_2(256k).mp3',

                         'D:\demo_Opencv\disgust_songs\Dhinchak_Pooja_-_Dilon_Ka_Shooter_(On_public_demand_)(256k).mp3',

                         'D:\demo_Opencv\disgust_songs\Dhinchak_Pooja_-_Gaadi_Meri_2_Seater(256k).mp3',

                         'D:\demo_Opencv\disgust_songs\EMIWAY_BANTAI-GIRAFTAAR_(OFFICIAL_MUSIC_VIDEO)(256k).mp3']
              Disgust_songs=random.choice(disgust_song)
      
              pygame.mixer.music.load(Disgust_songs)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                    continue
              pygame.quite()

    elif dominant_emotion=="fear":
   
              fear_songs=['D:\demo_Opencv\Fear_songs\Ajnabi_Hawaayein_[Full_Song]_Shaapit_By_Shreya_Ghoshal(256k).mp3',

                       'D:\demo_Opencv\Fear_songs\Ami_Je_Tomar__Video__Bhool_Bhulaiyaa_2___Kartik_Kiara_Tabu___Pritam_Arijit_Singh_Sameer___Bhushan_K(256k).mp3',

                       'D:\demo_Opencv\Fear_songs\Goody_Addams_Sings_A_Song_(Wednesday_2022_Tim_Burton_Horror_Parody)(256k).mp3',

                       'D:\demo_Opencv\Fear_songs\Lady_Gaga_-_Bloody_Mary__TikTok_Remix___Speed_Up____Wednesday_Dance_Scene(256k).mp3',

                       'D:\demo_Opencv\Fear_songs\Sathi_Mere_Sathi__I____Kavita_Krishnamurthy___Veerana_1988_Songs___Jasmin(256k).mp3',

                       'D:\demo_Opencv\Fear_songs\Wednesday_Sings_A_Song_(Wednesday_2022_Tim_Burton_Horror_Parody)(NEW_SONG_EVERYDAY!)(256k).mp3']
              Fear_songs=random.choice(fear_songs)
              pygame.mixer.music.load(Fear_songs)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                    continue
              pygame.quite()

    else:
    
              surprise_songs=['D:\demo_Opencv\surprise_songs\_Lungi_Dance_Chennai_Express__New_Video_Feat._Honey_Singh%2C_Shahrukh_Khan%2C_Deepika(256k).mp3',

                           'D:\demo_Opencv\surprise_songs\Aankhon_Mein_Teri_Ajab_Si___Om_Shanti_Om___Shahrukh_Khan___Deepika_Padukone(256k).mp3',

                           'D:\demo_Opencv\surprise_songs\Afghan_Jalebi__Ya_Baba__FULL_VIDEO_Song___Phantom___Saif_Ali_Khan%2C_Katrina_Kaif___T-Series(256k).mp3',

                           'D:\demo_Opencv\surprise_songs\Illahi_-_Yeh_Jawaani_Hai_Deewani___Ranbir_Kapoor%2C_Deepika_Padukone(256k).mp3',

                           'D:\demo_Opencv\surprise_songs\Chal_Chaiya_Chaiya___4K_Video_Song___Dil_Se_1998___Sukhwinder_Singh___Sapna_Awasthi___Shahrukh_Khan(256k).mp3',

                           'D:\demo_Opencv\surprise_songs\Radha_-_SOTY_Alia_Bhatt_Sidharth_Malhotra_Varun_Dhawan_Udit_Narayan_Shreya_Ghoshal(256k).mp3',

                          'D:\demo_Opencv\surprise_songs\Sooraj_Ki_Bahoon_Mein___Zindagi_Na_Milegi_Dobara___Hrithik_Roshan%2C_Katrina_Kaif%2C_Farhan_Akhtar(256k).mp3' ] 
              Surprise_songs=random.choice(surprise_songs)

              pygame.mixer.music.load(Surprise_songs)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                    continue
              pygame.quite()


# no. of photos to be clicked
NUM_PHOTOS = 5
# array of string to store the location of images
photos = []

cap = cv2.VideoCapture(0)
# loop for capturing multiple photo
for i in range(NUM_PHOTOS):


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

    pred = DeepFace.analyze(img)
    emotions_dict = pred[0]['emotion']

    emotion = max(emotions_dict, key=emotions_dict.get)
    string_array.append(emotion)

most_common_string(string_array) 
# cv2.destroyAllWindows()



