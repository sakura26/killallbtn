import RPi.GPIO as GPIO
import time
import os
import thread
# this version we turn off all kill script, just for DEMO with sound
# sound play with buzzer instand of speaker

# change pinout id here if you use diffrent pin
killbutton=15
alarmbutton=14
buzzer=2
# put our private keys here, those keys in this dir will be overwrited if you enabled "self-destory"
keyDir='keys'
ssh = "ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null "
# please add your server list and keys here
servers = [
  "-i keys/key1 root@192.168.0.170",
  "-i keys/key1 root@192.168.0.115"]

status_unlock=False
status_fire=False
status_alarmTone=False

GPIO.setmode(GPIO.BCM)
GPIO.setup(killbutton, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(alarmbutton, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(buzzer, GPIO.OUT)

def killall():
  print("kill all servers")
  # do evil codes here

def alarmKey(channel):
  global status_unlock,status_fire
  print("key unlocked")
  status_unlock = True
  while True:
    if(GPIO.input(alarmbutton) != 1):
      status_unlock=False
      print("disable alarm")
      return
    if GPIO.input(killbutton)==1:
      status_fire=True
      print("firing")
      killall()
      time.sleep(5)
      print("reset all")
      status_unlock=False
      status_fire=False
      return
    time.sleep(0.1)
GPIO.add_event_detect(alarmbutton, GPIO.RISING, callback=alarmKey, bouncetime=300)

p = GPIO.PWM(buzzer, 50)
while True:
  if(status_unlock and status_fire):
    p.start(50)
    p.ChangeFrequency(880)
    time.sleep(5)
    p.stop()
  elif(status_unlock):
    if status_alarmTone:
      p.start(50)
      p.ChangeFrequency(262)
      time.sleep(0.5)
      p.stop()
      status_alarmTone=False
    else:
      p.start(50)
      p.ChangeFrequency(659)
      time.sleep(0.5)
      p.stop()
      status_alarmTone=True
  else:
    time.sleep(0.1)
GPIO.cleanup()