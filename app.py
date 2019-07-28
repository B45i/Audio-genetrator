import json
from gtts import gTTS

audio_count = 0

def generate_audio(text):
    global audio_count
    print 'Generating: {}'.format(text)
    tts = gTTS(text, lang='en')
    tts.save('{}.mp3'.format(audio_count))
    audio_count += 1

with open('audio_config.json') as audio_config:
    audio_data = json.load(audio_config)

    generate_audio(audio_data['welcomeMessage'])
    generate_audio(audio_data['notFound'])

    description = audio_data['description']

    for item in sorted(audio_data['items'], key=lambda k: k['audio_id']):
        generate_audio(description.format(
            name = item['name'],
            description = item['description'],
            expiry_date = item['expiryDate'],
            price = item['price']
        ))

print 'Done.'
