# Speech-Recognition

These are the training and recognition files for using the PiWho Library.

PiWho Library is located at:  https://github.com/Adirockzz95/Piwho

When using train_audio.py, you will need to edit the speaker name and sound file name and  location before running the program.
When using recog_audio.py, you will need to edit the sound file name and  location before running the location.
The default location is the working directory where the recog_audio.py and train_audio.py are located.

The record_audio.py program uses the record.sh file to record audio.  The record.sh files uses the arecord command from the ALSA tools.  
If you working on a non-linux system record.sh may not work.
