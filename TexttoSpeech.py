from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from playsound import playsound
import time

authenticator = IAMAuthenticator('A-byYc7kDPoZfScLm1O5OKLU3NLNwC9UoOEoYWPVkPq2')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/e31acf7f-081c-4e28-93d8-7c422e71c988')


while True:
    localtime=time.localtime()
    result=time.strftime("%I:%M:%S %p",localtime)
    print(result)
    if(result=="08:00:00 AM"):
        with open('medicine1.mp3', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    'Time to take medicine Omeprazole', 
                    voice='en-US_AllisonV3Voice',
                    accept='audio/mp3'
                ).get_result().content)
        playsound('medicine1.mp3')
    
    
    if(result=="12:00:00 PM"):
        with open('medicine2.mp3', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    'Time to take medicine Atenolol',
                    voice='en-US_AllisonV3Voice',
                    accept='audio/mp3'
                ).get_result().content)
        playsound('medicine2.mp3')
        
    
    if(result=="05:00:00 PM"):
        with open('medicine3.mp3', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    'Time to take medicine Istamet',
                    voice='en-US_AllisonV3Voice',
                    accept='audio/mp3'
                ).get_result().content)
        playsound('medicine3.mp3')
        
    
    if(result=="07:30:00 PM"):
        with open('medicine4.mp3', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    'Time to take medicine Metformin',
                    voice='en-US_AllisonV3Voice',
                    accept='audio/mp3'
                ).get_result().content)
        playsound('medicine4.mp3')
    time.sleep(1)
