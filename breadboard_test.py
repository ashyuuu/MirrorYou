import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
button_pin_blue = 22
button_pin_yellow1 = 27
button_pin_red = 18
button_pin_green = 24
button_pin_yellow2 = 23

GPIO.setup(button_pin_blue, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_pin_yellow1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_pin_red, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_pin_green, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_pin_yellow2, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    print("ready for press")
    while True:
        if GPIO.input(button_pin_blue) == GPIO.LOW:
            print("blue")
        time.sleep(0.1)
        if GPIO.input(button_pin_yellow1) == GPIO.LOW:
            print("yellow1")
        time.sleep(0.1)
        if GPIO.input(button_pin_red) == GPIO.LOW:
            print("red")
        time.sleep(0.1)
        if GPIO.input(button_pin_green) == GPIO.LOW:
            print("green")
        time.sleep(0.1)
        if GPIO.input(button_pin_yellow2) == GPIO.LOW:
            print("yellow2")
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
                