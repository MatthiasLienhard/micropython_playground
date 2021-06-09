# micropython_playground
Hallo Peter, mit dieser Anleitung lernst du MicroPython programmieren in einer halben Stunde. Klingt gut, oder? Los geht‘s. 

## REPL

Um Kommandos an den Microcontroller zu schicken und Ausgaben zu erhalten gibt es in Micropython die REPL (read eval print loop, also etwa Befehle annehmen, ausführen und Ergebnisse ausgeben Wiederholschleife). Diese ist entweder über USB oder WLAN (web-repl) erreichbar. Fürs erste ist WLAN einfacher und ausreichend. 
* Auf https://github.com/micropython/webrepl –> Code –> Download ZIP 
* In einen Ordner entpacken.
* Mit dem Access Point des Microcontrollers verbinden:
* SSID: esp32_micropython
* PW: HappyBirthday
* Mit dem Browser webrepl.html öffnen. 
* Die Adresse auf ws://192.168.4.1:8266/ lassen und auf Connect klicken. 
* Das Passwort ist „AllesGute“.
* Es sollte jetzt die folgende Zeile zu sehen sein: 
```
>>> 
```
Den folgenden Abschnitt kannst du erstmal überspringen. 

Um länger herumzuspielen ist es allerdings komfortabler, sich eine Entwicklunsumgebung (IDE) einzurichten. Ich empfehle VSCode mit dem pymakr plugin. Folgende Schritte sind dazu notwendig:
* Beides installieren:
    * https://code.visualstudio.com/download
    * https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr
* Den MicroController per USB verbinden.
* Den Com-port ermitteln: Unten auf „All commands“, dann „pymakr > Extra > List Serial ports“
* Das sollte einen Eintrag mit Silicon labs finden.
* Unter „All commands“, dann „global Settings“ klicken, eine Konfigurationsdatei.
* Unter "address" den comport (zB „COM1“) angeben, 
* Unter "autoconnect_comport_manufacturers" „Silicon labs“ angenen (, nicht vergessen)


### Grundbefehle:
Variablen
In der REPL können nun Variablen zugeordnet werden, das können Zahlen oder Text sein:
```
>>> x=1
>>> name=“Peter“ 
# ist das Kommentarzeichen, alles dannach wird nicht als Befehl interpretiert
>>> x+5 # wenn der Befehl ein Rückgabewert ergibt wird dieser in der nächsten Zeile ausgegeben
6
Ein = ist eine zuordnung von einem wert zu einer Variable, zwei == ein Vergleich:
>>> x==5 # das sollte doch 6 sein, oder?
False
```

### Container (fortgeschritten, kann auch erstmal übersprungen werden)
Mehrere Werte (egal ob Zahlen oder Text) können in Listen, Tupel, Sets oder Dicts zusammengefasst werden. Die Art der Klammer entscheidet:
```
>>> mylist=[1,2,10] # eine Liste namens mylist
>>> mytuple=(1,3,4) # die Namen können natürlich frei gewählt werden
>>> myset={1,42,5}
>>> mydict={10:20, 30:40}
```

Die Hauptunterschiede:
Listen können verändert und erweitert werden, Tuples nicht.
```
>>> mylist.append(20)
>>> mylist
[1, 2, 10, 20] 
```

Bei Listen und Tupeln kann man auf die Elemente mit der Nummer (startet bei 0) mit [] zugreifen, bei Sets geht das nicht:
```
>>> mytuple[0]
1
>>> mylist[1]=5
>>> mylist
[1, 5, 10, 20] 
```

Sets enthalten jedes Element nur einmal, und die Reihenfolge ist zufällig:
```
>>> myset.add(42) 
>>> myset
{42, 1, 5} 
```
Bei dicts greift man nicht mit der Nummer, sondern mit schlüsseln auf die Elemente zu:
```
>>> mydict[10]
20
>>> mydict[name]=66
>>> mydict
{'Peter': 66, 10: 20, 30: 40}
```

### Schleifen:
Sollen Befehle mehrfach ausgeführt werden so bieten sich Schleifen an. Bei einer While-Schleife wird der Befehl block solange ausgeführt, wie die Bedingung wahr ist.
```
>>>x=0
>>>while x < 5:
	x=x+1

>>>x
5

```
Bei for loops nimmt eine Variable (hier i) alle Werte aus einer Sequenz (zB Liste) an:
```
>>>for i in range(10):
	time.sleep(.5)
	led.on()
	time.sleep(.5)
	led.off()

```
Das Einrücken ist dabei wichtig. Es definiert, welche Befehle zu dem Block gehören, der wiederholt werden soll. 


### Funktionen
Komplexere Befehle können in Funktionen zusammengefasst werden. Dafür verwendet man def
```
>>>def blink(ontime=1, offtime=1):
	led.off()
	time.sleep(offtime)
	led.on()
	time.sleep(ontime)
	led.off()
```

Funktionen werden mit Parametern in runden Klammern aufgerufen. Es gibt viele bereits definierte Funktionen. Manche geben einen Wert zurück, andere (wie unsere Blink-Funktion) nicht.
```
>>>blink(1,2)
>>>print("Happy Birthday, Peter")# das ist eine eingebaute Funktion
```


### Klassen:
Komplexe Gruppen von Variablen und Funktionen Können in Klassen zusammengefasst werden, z.B. um Sensoren zu beschreiben, die eine Bestimmte Funktionalität bereitstellen, so wie die LED in dem Beispiel oben.

### Module:
Mehrere Klassen, Funktionen und Variablen können in Modulen zusammengefasst werden, damit diese bei Bedarf importiert werden können:
```
>>>import time # Das „time modul“ wird importiert
>>>time.sleep(5) # warte 5 sekunden
>>>import math # puh, Mathe
>>>math.sqrt(math.pi) # die Wurzel von pi
1.772454
```
Es gibt viele Mircopython spezifische Module, um die Hardware zu steuern. Die LED oben wurde Beispielsweise so definiert:
```
>>>import machine
>>>led=machine.Pin(5, machine.Pin.OUT)
```
Dabei ist Pin eine Klasse, und PIN.OUT eine Variable innerhalb der Klasse

### Programmablauf
Bei jedem Start führt der uC zunächst die Datei „boot.py“, dann die Datei „main.py“ aus. In der boot.py wird zB das wlan eingerichtet. Typischerweise, d.h. wenn der uC ohne Eingabe über die REPL eine Aufgabe erfüllen soll ist in der main.py eine Endlosschleife. Wenn nicht hört das Programm nach der main.py auf und wartet auf weitere Befehle über die REPL. Wärend einer 

### Beispiele:

Neopixel LEDs
Servo
Spannung messen

OLED display
Beschleunigugns und Lagesensor

