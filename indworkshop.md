IND Workshop
=====

## 講義

[講義](README.md)

[投影片](https://slides.com/sakura26/self-terminator)

## 材料套組

基本款：提供麵包板與基本套件，以後可以自行更換零件 1300$

* Raspberry pi zero WH
* 創建16G SD Card 
* USB 5v變壓器
* 1k電阻 x3 
* 紅色LED x1
* 小顆按鈕 x2
* 單心線 數根
* 蜂鳴器 x1
* 麵包板 x1

中二款：真實可用的鑰匙與可大力拍打的大紅按鈕，拍下去很爽，但請確保你的資料都已經備份了 1700$

* Raspberry pi zero WH
* 創建16G SD Card 
* USB 5v變壓器
* 1k電阻 x3 
* 紅色LED x1
* 小顆按鈕 x2
* 單心線 數根
* 蜂鳴器 x1
* 麵包板 x1
* 鑰匙開關 x1
* 緊急停止按鈕 x1
* 塑膠外殼 x1


## 其他工具

* 尖嘴鉗 數隻
* 延長線排插 
* 焊接工具組
* WIFI AP

## 參考

[準備好你的SD卡](https://www.raspberrypi.org/documentation/installation/installing-images/)

[入門教學](https://elementztechblog.wordpress.com/2016/05/03/controlling-gpio-pins-of-raspberry-pi-zero/)

[接腳參考](https://pinout.xyz/pinout/servo_pwm_pi_zero)

[點亮一盞燈](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)

[驅動蜂鳴器](https://sites.google.com/site/zsgititit/home/raspberry-shu-mei-pai/raspberry-shi-yong-fengbuzzier
)

[聲音頻率參考](https://zh.wikipedia.org/wiki/%E9%9F%B3%E7%AC%A6)

## 自爆裝置使用流程

* 轉開鑰匙，聽見警報聲
* 按下按鈕，聽見長達五秒的尖銳音，此時kill程式碼已啟動，資料一去不復返

## DIY

* 準備好材料
* 把SD卡寫入Rasbian OS（這一步可能會花上你15-60min）(IO操作有風險，請謹慎小心別把自己的硬碟洗了)
* 插入SD卡、HDMI螢幕、USB鍵鼠、電源，看見開機畫面
* 設定鍵盤locale與WIFI連線
* 下載 範例程式碼
  * http://www.ccsakura-net.com/up/indemo.py
* 將程式碼設定為開機即啟動(optional) 
  * ```vi /etc/rc.local```
  * ```python /home/pi/indemo.py &```
  * 放在```exit 0```之前
* 插麵包板
* 接上RPi
* 執行程式碼
  * ```python /home/pi/indemo.py &```
* 觀察輸出的LED與音效
* 如果都沒有問題，嘗試焊接到電路板，並組合至箱子中

## Raspberry pi的更多應用

* [用RPi裝XBMC做多媒體中心](https://www.youtube.com/watch?v=1L5GCmXgHK8)（影片播放啥的，電視盒能做的他都能做）
* [RetroPie遊戲模擬器](https://www.youtube.com/watch?v=Qpqjy87g0Y8)
  * <https://dotblogs.com.tw/bowwowxx/2015/06/03/151483>
* [如何把RPi zero改造成gameboy](https://www.youtube.com/watch?v=dV-W23lONI4)
* [另一個](https://www.youtube.com/watch?v=ux9lXBexw0o)