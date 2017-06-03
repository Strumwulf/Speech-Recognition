from piwho import recognition


recog = recognition.SpeakerRecognizer()

recog.set_feature_option('-lpc -cheb')
recog.speaker_name = 'David'
recog.debug = True

# train model with the newly recorded file
recog.train_new_data('/home/pi/Desktop/Omega2.0/training_audio/david5.wav')

print recog.get_speakers()
