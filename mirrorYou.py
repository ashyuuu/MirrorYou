from PhotoGallery import PhotoGallery
from Temperature import Temperature
from redness import redness
from weather import Weather
from MirrorMode import MirrorMode
from Menu import Menu
import os
import tkinter as tk
from PIL import Image


class mirrorYou:
    def __init__(self):
        self.root = tk.Tk()

        # image = tk.Image()
        # self.redness = redness(image)
        # self.root.mainloop()

    def turnOnPhotoGallery(self):
        # activate photo gallery
        self.gallery = PhotoGallery(self.root)
        self.root.mainloop()

    def turnOnMirrorMode(self):
        # activate mirror mode
        self.mirrorMode = MirrorMode()
        self.mirrorMode.turnMirrorOn()

    def turnOnTemperature(self):
        # activate temperature
        self.temp = Temperature()
        self.temp.getTemperature()
    
    def turnOnWeather(self):
        # activate weather
        self.weather = Weather()
        # self.root.mainloop()

    def backToMainMenu(self):
        # back to main menu
        self.menu = Menu()

    def turnOffPhotoGallery(self):
        # deactivate photo gallery
        self.gallery.root.destroy()

    def nextPhoto(self):
        # go to next photo
        self.gallery.nextPhoto()
    
    def prevPhoto(self):
        # go to previous photo
        self.gallery.prevPhoto()

    def goBack(self):  
        # go back to where it was
        self.root.destroy()
        
if __name__ == "__main__":
    mirror = mirrorYou()
    # mirror.turnOnPhotoGallery()
    # mirror.turnOnGallery()
    # mirror.turnOnMirrorMode()
    # mirror.turnOnTemperature()
    # mirror.turnOnWeather()
    # image = Image.open("Redness_Photo_1.png")
    # mirror.redness(image)

    # mirror.temp.getTemperature()
    # mirror.temp.setTemperature()
    # mirror.temp.getTemperature()
    
   