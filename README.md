killallbtn - A Self-destruct button for Killing all your server and data!!
=============

![Self-destruct button](https://c1.staticflickr.com/9/8385/8602816297_af960b44e9_k.jpg)

## what is killallbtn ##

[中文投影片請往此](http://slides.com/sakura26/self-terminator)

Sometimes, you may need a method to quickly erase all your data, especially when you have lots sensitive data.
You can login to all the server to delete files and wait, setup TNT in your datacenter,
or just try this cool things..

"Self-destruct button" !!

This project conbines with Raspberry Pi and some scripts, to provide rapid-start and hardly-recover way to prevent your data from leaking. the project provides:

- Rapid and easy to use - just hit the button!
- A lock and warning sound to avoid unexcepted start
- Support remote systems over network (NAS, VPS, oversea datacenter...with SSH)
- Support linux (BSD & other platform can br done in future)
- Fast erase (take less then secodes)
- Full erase (take long times but hard to recover)
- Store all private key in secure area(RPi), and destroy when used.
- Can add 3G/4G connection and Batteries, in case of "power cut" or "net cut"

身為一個憂國憂民正直有為的年輕人，偶而遇到有人來查水錶也是很正常低（？）
為了保護~~糟糕物~~機密資料不要外流，一個酷炫的自爆按鈕是一個科技宅該有的基本行頭！

這裏我們示範如何用簡短的程式碼，與Raspberry pi快速的完成一個酷炫而且真的會爆的自爆按鈕，支援以下幾大功能：

- 快速有效：敲下這個按鈕的瞬間，所有機敏資料直接GG
- 鑰匙解鎖：除了避免被你家的貓踩到，看起來更炫，還有自爆前的警報聲
- 支援遠端系統：只要是能SSH到的設備，就算在地球另一端，一樣給他爆～
- 支援Linux：其他系統的支援還在開發中～
- 高速銷毀：敲下去的瞬間完成隨即摧毀檔案系統與磁碟表頭，大幅提高恢復難度
- 完整銷毀：只要有足夠的時間，資料將會被摧毀到無法恢復的程度
- 安全性：所有私鑰儲存於獨立的RPi中，外界難以入侵，且可設定在自爆後一併摧毀。
- 強固性：可以另加3G/4G or 電池，斷電斷網路都不怕！

## sample button ##

![sample button](https://raw.githubusercontent.com/sakura26/killallbtn/master/pics/button_sample.JPG)

## how it works ##

1. Unlock the key, the alarm sounds
2. Hit the button
3. RPi deamon triggers kill procedure, connecting to servers in list, send kill.sh script
4. Server runs the kill script, disk wipes and os hangs

## To be done ##

- Rewrite kill script to support "initrd kill on boot"
- more secure erase method for RAID or [SSD](https://www.thomas-krenn.com/en/wiki/SSD_Secure_Erase)
- more effective way for "anti-recover"
- Support encrypt filesystem
- A fancy box blueprint for 3D printing
- watchdog to make sure the box is still alive

## install instruction ##

### Prepare hardware: ###

you will need a Rasperberry Pi, you can get one [here](https://www.raspberrypi.org) (you may want to take SD card too)
ofcourse, you will need to setup the OS too, you can [Download RASPBIAN](https://www.raspberrypi.org/downloads/), and [install instruction here](https://www.raspberrypi.org/documentation/installation/installing-images/)

Also, if you want to have a real button, you will need some electronic circuit skill.
here is the ingredients:
- 1x breadboard
- 1x box
- 3x 1k resister
- 1x LED
- 1x Key button
- 1x "Big Red" button
- some single-core wires or Dupont wires

You can follow the circuit.png to connect the ingredients together.
![circuit.png](https://raw.githubusercontent.com/sakura26/killallbtn/master/circuit.png)
![circuit_sample.png](https://raw.githubusercontent.com/sakura26/killallbtn/master/pics/circuit_sample.jpg)

If you don't know where the GND\5V+\Pin24\Pin26 should connect, google [raspberry pi pinout](https://www.google.com.tw/search?q=raspberry+pi+pinout&es_sm=91&tbm=isch&tbo=u&source=univ&sa=X&ei=ZR5hVc-KC4Xg8gXgwYGICQ&ved=0CB0QsAQ#imgrc=1TnjLqridDLpxM%253A%3Bpto2jAOMLfe_LM%3Bhttp%253A%252F%252Fwww.megaleecher.net%252Fsites%252Fdefault%252Ffiles%252Fimages%252Fraspberry-pi-rev2-gpio-pinout.jpg%3Bhttp%253A%252F%252Fwww.megaleecher.net%252FRaspberry_Pi_GPIO_Pinout_Helper%3B1050%3B733) may helps you.

### Prepare software: ###

First, the killer used ssh private key to do his job, 
you will need to setup your private keys and hosts ssh.
you can follow this [guide](http://www.ece.uci.edu/~chou/ssh-key.html) to do so.

Change settings in buttonAlarm.py
you MUST modify the server list to yours
!!! KEYS IN THE SOURCE ONLY FOR TEST PURPOSE, FOR SECURITY REASON YOU MUST GENERATE YOUR OWN KEYS!!!
```
# please add your server list and keys here
servers = [
  "-i keys/key1 root@192.168.0.170",
  "-i keys/key1 root@192.168.0.115"]
```

Put scripts to your RPi ( Ex. /home/pi/killallbtn )
Then, put your private key to "keys" directory
make sure the permission of all keys is root:root and 600 for security reason.

add startup script in /etc/rc.local ( before the exit statment! )
```
cd /home/pi/killallbtn 
python buttonAlarm.py &
```

thats all! power up your RPi, hit the button and enjoy 
![troll face](http://cdn.alltheragefaces.com/img/faces/svg/troll-troll-face.svg)

### hardening your button ###

If you don't want hackers steal your private key, this step is STRONGLY RECOMMAND.
To build a standalone system, its good to disable sshd, and make sure there is no service open on network.
Or, you can config firewall(iptables) to deny all incoming traffic.
and don't forget to change password

and.. prevent someone get your privte keys after you hit the button, you can enable this codes to destruct the RPi itself:
```
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
```

## Notice ##

DONT DO ANY ILLEGAL THINGS WITH THIS PROJECT!

### License ###

This content is released under the BSD & CC License.

The sound effect comes from [Google Audio Library](https://www.youtube.com/audiolibrary/music) "Spaceship Alarm".