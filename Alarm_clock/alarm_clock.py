
import time
import sys
import winsound

alarm = str(input('Alarm Time: '))

while True:
    time_now = time.strftime("%H:%M:%S")
    sys.stdout.write('\r' + time_now)
    time.sleep(1)
    if alarm == time_now:
        winsound.PlaySound('music.wav', winsound.SND_FILENAME)
