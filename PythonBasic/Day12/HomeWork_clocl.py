import datetime
import time
import sys

while True:

    sys.stdout.write(datetime.datetime.now().strftime("%H:%M:%S"))
    sys.stdout.write('\r')
    sys.stdout.write(datetime.datetime.now().strftime("%H:%M:%S"))

    time.sleep(1)