# This code reads an srt file and converts it to a text file.

import pysrt
subs = pysrt.open("9.Text editing/captions.srt")

with open('9.Text editing/cap.txt', 'w') as file:
    for sub in subs:
        file.write(sub.text)
