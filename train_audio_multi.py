from piwho import recognition

recog = recognition.SpeakerRecognizer()
recog.set_feature_option('-low -lpc -cheb')

recog.speaker_name = 'David'
recog.debug = True

# train model with the recorded file
recog.train_new_data('/home/pi/Speaker_Recognition/training_audio/David01.wav')
recog.train_new_data('/home/pi/Speaker_Recognition/training_audio/david2.wav')
recog.train_new_data('/home/pi/Speaker_Recognition/training_audio/David02.wav')
recog.train_new_data('/home/pi/Speaker_Recognition/training_audio/david3.wav')

recog.speaker_name = 'Maria'
recog.debug = True

# train model with the recorded file
recog.train_new_data('/home/pi/Speaker_Recognition/training_audio/Maria1.wav')
recog.train_new_data('/home/pi/Speaker_Recognition/training_audio/Maria2.wav')
recog.train_new_data('/home/pi/Speaker_Recognition/training_audio/Maria03.wav')
recog.train_new_data('/home/pi/Speaker_Recognition/training_audio/Maria04.wav')

print recog.get_speakers()
