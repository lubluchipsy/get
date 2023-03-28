import RPi.GPIO as gpio
import sys
dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
def translate(a, n):
    return [int(element) for element in bin(a)[2:].zfill(n)]
try:
    while True:
        a = input('input 0-255 ')
        if a == 'q':
            sys.exit()
        elif a.isdigit() and 0 <= int(a) <= 255:
            gpio.output(dac, translate(int(a), 8))
            print("{:.4f}".format(int(a)/256*3.3))
        elif int(a) < 0:
            print("Negative number. Input 0-255")
        elif int(a) > 255:
            print("Number greater than 255. Input 0-255")
        elif not a.isdigit():
            print('input number 0-255')
except ValueError:
        print('input number 0-255')
except KeyboardInterrupt:
        print('done')
finally:
        gpio.output(dac, 0)
        gpio.cleanup()

