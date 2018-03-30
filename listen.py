import RPi.GPIO as GPIO
import time
import subprocess

while True:
    time.sleep(20)
    subprocess.call([['python knockknock.py']])