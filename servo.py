from machine import Pin, PWM
import time
led = Pin(25, Pin.OUT)
servo = PWM(Pin(0))

servo.freq(50)
buttonu = Pin(14, Pin.IN, Pin.PULL_DOWN)
buttond = Pin(15, Pin.IN, Pin.PULL_DOWN)
sdc = 1350
servo.duty_u16(sdc)
def u():
    if buttonu.value():
        led.toggle()
        global sdc
        print ("Button pressed")
        sdc += 1000
        time.sleep(.2)
        print (sdc)
        time.sleep(.2)
        servo.duty_u16(sdc)
        time.sleep(.2)
        
def d():
    if buttond.value():
        led.toggle()
        global sdc
        print ("Button pressed")
        time.sleep(.2)
        sdc -= 1000
        time.sleep(.2)
        print (sdc)
        time.sleep(.2)
        servo.duty_u16(sdc)
        time.sleep
        
while True:
    if sdc <= 1350:
        sdc = 8350
    elif sdc >= 8350:
        sdc = 1350

    u()
    d()
