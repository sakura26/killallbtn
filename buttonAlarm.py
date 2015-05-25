import RPi.GPIO as GPIO
import time
import os
import thread
from pygame import mixer

# change pinout id here if you use diffrent pin
killbutton=26
alarmbutton=24
# put our private keys here, those keys in this dir will be overwrited if you enabled "self-destory"
keyDir='keys'
ssh = "ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null "
# please add your server list and keys here
servers = [
  "-i keys/key1 root@192.168.0.170",
  "-i keys/key1 root@192.168.0.115"]
# alarm file here
musicPath='alarm.wav'

lockon=True
fired=False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(killbutton, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(alarmbutton, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#enable sound to headphone
os.system('sudo amixer cset numid=3 1')

def killFunction(channel):
  global lockon,fired
  if lockon == False:
    if fired == True:
      return
    print("Firing...")
    for index in range(len(servers)):
      print("kill "+servers[index])
      os.system(ssh+servers[index]+" bash -s < kill.sh &")
    # lock the system to avoid fire multiple times
    fired = True
    # stop alarm
    print("abort alarm")
    mixer.music.stop()
    # === finally, destroy RPi itself. remove marks here ===
    #print("Self-destroy in progress...")
    # erase all keys...
    #from os import listdir
    #from os.path import isfile, join
    #onlyfiles = [ f for f in listdir(keyDir) if isfile(join(keyDir,f)) ]
    #for f in onlyfiles:
    #  os.system("dd count=10 if=/dev/urandom of="+f)
    # kill scripts
    #onlyfiles = [ f for f in listdir('.') if isfile(f) ]
    #for f in onlyfiles:
    #  os.system("dd count=10 if=/dev/urandom of="+f)
    # full disk erase..
    #os.system("dd if=/dev/urandom of=/dev/mmcblk0p2")
GPIO.add_event_detect(killbutton, GPIO.RISING, callback=killFunction, bouncetime=300)

while True:
  if(GPIO.input(alarmbutton) == 1):
    if lockon == True:
      lockon = False
      #playing alarm
      print("playing alarm")
      mixer.init()
      mixer.music.load(musicPath)
      mixer.music.play(-1)
  else:
    if lockon == False:
      lockon = True
      #stop alarm
      print("abort alarm")
      mixer.music.stop()
      fired=False
  time.sleep(0.1)
GPIO.cleanup()