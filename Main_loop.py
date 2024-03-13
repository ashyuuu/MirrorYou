import RPi.GPIO as GPIO
import time
import mirrorYou

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

# 0: main menu, 1: photo gallery, 2: temperature, 3: photo, 4: mirror 5: popup
page = 0
mirror = mirrorYou.mirrorYou() 

try: 
    print("ready for press")
    while True:
        # Main Menu Mode
        if page == 0:
            mirror.backToMainMenu()
            # TODO: display weather forecast
            mirror.turnOnWeather()

            if GPIO.input(button_pin_blue) == GPIO.LOW:
                page = 1
                print("Photo gallery")
            time.sleep(0.1)
            if GPIO.input(button_pin_yellow1) == GPIO.LOW:
                page = 2
                print("Temperature")
            time.sleep(0.1)
            if GPIO.input(button_pin_red) == GPIO.LOW:
                page = 3
                print("Camera")
            time.sleep(0.1)
            if GPIO.input(button_pin_green) == GPIO.LOW:
                page = 4
                print("Mirror")
            time.sleep(0.1)

        # Photo Gallery Mode
        if page == 1:
            # TODO: Show photo gallery
            mirror.turnOnPhotoGallery()

            if GPIO.input(button_pin_blue) == GPIO.LOW:
                page = 0
                mirror.turnOffPhotoGallery()
                print("Back to Menu")
            time.sleep(0.1)
            if GPIO.input(button_pin_yellow1) == GPIO.LOW:
                #left
                mirror.nextPhoto()
                print("left")
            time.sleep(0.1)
            if GPIO.input(button_pin_red) == GPIO.LOW:
                #right
                mirror.prevPhoto()
                print("right")
            time.sleep(0.1)
            if GPIO.input(button_pin_green) == GPIO.LOW:
                #select
                page = 5
                print("select")
            time.sleep(0.1)  

        # Temperature Mode    
        if page == 2:
            # TODO: Show most recent temperature
            mirror.turnOnTemperature()

            if GPIO.input(button_pin_blue) == GPIO.LOW:
                page = 0
                print("Back to Menu")
            time.sleep(0.1)
            if GPIO.input(button_pin_yellow1) == GPIO.LOW:
                #record temperature
                print("temperature")
            time.sleep(0.1)

        # Camera Mode
        if page == 3:
            # TODO: Turn screen black
            mirror.turnOnMirrorMode()

            if GPIO.input(button_pin_blue) == GPIO.LOW:
                page = 0
                print("Back to Menu")
            time.sleep(0.1)
            if GPIO.input(button_pin_yellow1) == GPIO.LOW:
                #take picture
                print("take picture")
            time.sleep(0.1)

        # Mirror Mode
        if page == 4:
            # TODO: Turn screen black
            mirror.turnOnMirrorMode()

            if GPIO.input(button_pin_blue) == GPIO.LOW:
                page = 0
                print("Back to Menu")

        # Pop Up Window
        if page == 5:
            # TODO: Show photo
            if GPIO.input(button_pin_blue) == GPIO.LOW:
                page = 1
                print("Back to Gallery")
            time.sleep(0.1)
            if GPIO.input(button_pin_yellow1) == GPIO.LOW:
                # analyze and show most recent temperature
                print("analyze")
            

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
                