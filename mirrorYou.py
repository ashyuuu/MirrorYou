from PhotoGallery import PhotoGallery
from Temperature import Temperature
from redness import redness
from MirrorMode import MirrorMode
import os
import tkinter as tk
from PIL import Image


class mirrorYou:
    def __init__(self):
        root = tk.Tk()
        # image = tk.Image()
        # self.temp = Temperature()
        # self.gallery = PhotoGallery(root)
        # self.redness = redness(image)
        self.mirrorMode = MirrorMode()
        root.mainloop()
        
if __name__ == "__main__":
    mirror = mirrorYou()
    mirror.mirrorMode.turnMirrorOn()
    # image = Image.open("Redness_Photo_1.png")
    # mirror.redness(image)

    # mirror.temp.getTemperature()
    # mirror.temp.setTemperature()
    # mirror.temp.getTemperature()
    
    # mirror.gallery.addPhoto("chaesoo", os.path.join(os.getcwd(), "photos/chaesoo.jpg"))
    # mirror.gallery.addPhoto("concert1", os.path.join(os.getcwd(), "photos/concert1.jpg"))
    # mirror.gallery.addPhoto("fireworks", os.path.join(os.getcwd(), "photos/fireworks.jpg"))
    # mirror.gallery.addPhoto("group", os.path.join(os.getcwd(), "photos/group.jpg"))
    # mirror.gallery.addPhoto("itzysigned", os.path.join(os.getcwd(), "photos/itzysigned.jpg"))
    # mirror.gallery.addPhoto("jennieheart", os.path.join(os.getcwd(), "photos/jennieheart.jpg"))
    # mirror.gallery.addPhoto("jennielook", os.path.join(os.getcwd(), "photos/jennielook.jpg"))
    # mirror.gallery.addPhoto("loca", os.path.join(os.getcwd(), "photos/loca.jpg"))
    # mirror.gallery.addPhoto("loco", os.path.join(os.getcwd(), "photos/loco.jpg"))
    # mirror.gallery.addPhoto("meg", os.path.join(os.getcwd(), "photos/meg.jpg"))
    # mirror.gallery.addPhoto("peach", os.path.join(os.getcwd(), "photos/peach.jpg"))
    # mirror.gallery.addPhoto("screenshot", os.path.join(os.getcwd(), "photos/screenshot.jpg"))
    # mirror.gallery.addPhoto("sign", os.path.join(os.getcwd(), "photos/sign.jpg"))
    # mirror.gallery.addPhoto("ting", os.path.join(os.getcwd(), "photos/ting.jpg"))
    # mirror.gallery.addPhoto("verdy", os.path.join(os.getcwd(), "photos/verdy.jpg"))
    # mirror.gallery.addPhoto("yuqi", os.path.join(os.getcwd(), "photos/yuqi.jpg"))

