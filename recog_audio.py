import os
from operator import itemgetter
from subprocess import call

from piwho import recognition

recog = recognition.SpeakerRecognizer()

recog.set_feature_option('-lpc -cheb')

name = []
name = recog.identify_speaker('entry.wav')

dictn = recog.get_speaker_scores()
print dictn			#Lower the score, closer to the speaker
smallestKey, smallestNum = min(dictn.items(), key=itemgetter(1))

print smallestNum



if smallestNum < '1.0':
    print 'Hello ' + (name[0]) # Recognized speaker
else:
    print "Sorry, Do I know you?"
    DC = 0
