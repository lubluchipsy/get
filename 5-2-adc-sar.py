import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
maxVoltage = 3.3
levels = 2**(len(dac))

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        out = decimal2binary((value))
        GPIO.output(dac, out)
        time.sleep(0.01)
        inp = GPIO.input(comp)
        if inp == 0:
            value -= 2**i
    return value
            
try:
    while True:
        value = adc()
        print(value, '{:.2f}'.format((value/levels) * maxVoltage))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()