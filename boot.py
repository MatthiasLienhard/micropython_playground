import network
import webrepl
import time
import machine

led=machine.Pin(5, machine.Pin.OUT)
ssid=b'ssid'
pw=b'PW'
sta = network.WLAN(network.STA_IF)
sta.active(True)
led.on()
wifi=sta.scan()
led.off()
print('found {} wlans'.format(len(wifi)))
for con in wifi:
    print(con[0])

if ssid in [con[0] for con in wifi]:
    sta.active(True)
    sta.connect(ssid, pw)
    for i in range(10):    
        time.sleep(.5)
        led.on()
        time.sleep(.5)
        led.off()
        if sta.isconnected():
            break
if not sta.isconnected():
    print('make accesspoint')
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid="esp32", authmode=network.AUTH_WPA_WPA2_PSK, password="HappyBirthday")
led.on()
webrepl.start()