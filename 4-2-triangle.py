import RPi.GPIO as gpio

from time import sleep
dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def translate(a, n):
    return [int(element) for element in bin(a)[2:].zfill(n)]

try:
    T = input('Input time ')
    if not T.isdigit():
        print('Enter the number')
    t = int(T)/512
    print(t)
    while True:
        
        for i in range(256):
            gpio.output(dac, translate(i, 8))
            sleep(t)
        for i in range(255, 0, -1):
            gpio.output(dac, translate(i, 8))
            sleep(t)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()