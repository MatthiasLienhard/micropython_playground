import network
import webrepl
import machine
import time

def set_wlan(ssid,pw):
    with open("credentials.txt", "a") as f:
        f.write('{} {}'.format(ssid,pw))

def remove_wlan(ssid):
    found=0
    wlan_pw=[]
    with open( 'credentials.txt','r') as f:
        # this file should contain ssid<space>pw, one per line
        line=f.readline().strip().split()
        while line:
            if line[0]!= ssid:
                wlan_pw.append(line)
            else:
                found+=1
            line=f.readline().strip().split()
    if found:
        with open("credentials.txt", "w") as f:
            for line in wlan_pw:
                f.write('{} {}'.format(*line))
    
def connect():
    led=machine.Pin(5, machine.Pin.OUT)
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    led.on()
    wifi=[con[0].decode('utf8') for con in sta.scan()]
    led.off()
    print('found {} wlans'.format(len(wifi)))
    for con in wifi:
        print(con)
    wlan_pw=list()
    try:
        with open( 'credentials.txt','r') as f:
            # this file should contain ssid<space>pw, one per line
            line=f.readline().strip().split()
            while line:
                wlan_pw.append(line)
                line=f.readline().strip().split()
    except OSError:
        pass

    for ssid,pw in wlan_pw:
        if ssid in wifi:
            sta.active(True)
            sta.connect(ssid, pw)
            for i in range(10):    
                time.sleep(.5)
                led.on()
                time.sleep(.5)
                led.off()
                if sta.isconnected():
                    print('connected to {}'.format(ssid))
                    break
            else:
                print('connection to {} failed'.format(ssid))
    
    if not sta.isconnected():
        print('make accesspoint')
        ap = network.WLAN(network.AP_IF)
        ap.active(True)
        ap.config(essid="esp32", authmode=network.AUTH_WPA_WPA2_PSK, password="HappyBirthday")
    led.on()
    webrepl.start()