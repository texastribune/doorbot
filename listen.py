import RPi.GPIO as GPIO
import time
import subprocess
import knockknock

if __name__ == '__main__':
    while True:
        time.sleep(20)
        knockknock.post_to_slack()