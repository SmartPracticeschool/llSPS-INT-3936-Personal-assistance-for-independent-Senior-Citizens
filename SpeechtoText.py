import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('4qiTUyt_9JtAUQ-9td87CcliqXjd1eFqR8ZT6hndzcPJ')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/bab69765-c8fb-4722-8d28-a749e0e8cf85')

with open(join(dirname(__file__), './.', 'medicine1.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',    
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))

with open(join(dirname(__file__), './.', 'medicine2.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',    
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))

with open(join(dirname(__file__), './.', 'medicine3.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',    
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))


with open(join(dirname(__file__), './.', 'medicine4.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',    
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))
