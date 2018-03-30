import RPi.GPIO as GPIO
import time
import subprocess

if __name__ == '__main__':
    while True:
        time.sleep(20)
        subprocess.call(['python knockknock.py'])