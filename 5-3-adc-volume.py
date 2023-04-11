import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
maxVoltage = 3.3
levels = 2**(len(dac))
leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

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
        leds_out = [0]*8
        value = adc()
        print(value, '{:.2f}'.format((value/levels) * maxVoltage))
        leds_value = round((value/255)*8)
        for i in range(leds_value):
            leds_out[i] = 1
        leds_out.reverse()
        GPIO.output(leds, leds_out)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()