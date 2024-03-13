# photo gallery in python
import os
import tkinter as tk
from PIL import Image, ImageTk

class PhotoGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Gallery")
        self.photoArray = []
        self.currentPhoto = 0
        self.image_folder = "photos/train/red"  # Path to your image folder
        self.loadImage()

        self.canvas = tk.Canvas(self.root, width = 620, height = 700)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.gallery_frame = tk.Frame(self.canvas)
        self.displayImages()

        self.canvas.create_window((0, 0), window=self.gallery_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.gallery_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def resize_and_crop(self, image, size):
        img_width, img_height = image.size
        aspect_ratio = img_width / img_height
        target_width, target_height = size

        if aspect_ratio > 1:
            # Landscape orientation
            new_width = int(target_width * aspect_ratio)
            new_height = target_height
        else:
            # Portrait orientation
            new_width = target_width
            new_height = int(target_height / aspect_ratio)

        resized_img = image.resize((new_width, new_height), Image.LANCZOS)

        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2

        return resized_img.crop((left, top, right, bottom))
    
    def displayImages(self):
        num_columns = 3  # Number of columns in the grid
        target_size = (200, 200)  # Target size for cropped images

        for index, image in enumerate(self.photoArray):
            image = self.resize_and_crop(image, target_size)
            photo = ImageTk.PhotoImage(image)

            row = index // num_columns
            col = index % num_columns

            label = tk.Label(self.gallery_frame, image=photo)
            label.image = photo
            label.grid(row=row, column=col, padx=5, pady=5)
            # Bind click event to each image
            label.bind("<Button-1>", lambda event, img=image: self.show_image_in_new_window(img))

            # print(f"Photo Name: {photo['name']}, Photo Path: {photo['path']}")
            # try:
            #     image = Image.open(photo['path'])
            #     image.show()
            # except:
            #     print("Unable to open image")
    
    def loadImage(self):
        image_files = []
        for f in os.listdir(self.image_folder):
            if os.path.isfile(os.path.join(self.image_folder, f)):
                image_files.append(f)
        for f in image_files:
            self.photoArray.append(Image.open(os.path.join(self.image_folder, f)))
        # photo = {"name": name, "path": path, "date": date, "tags": tags}
        # self.photoArray.append(photo)
            
    def remove_highlight(self, event):
        label = event.widget
        label.config(highlightthickness=0)

    def hover(self, index):
        # Remove highlight from previous photo
        self.remove_highlight(None)

        # Highlight the hovered photo
        label = self.gallery_frame.grid_slaves()[index]
        label.config(highlightbackground="red", highlightcolor="red", highlightthickness=3)


    def nextPhoto(self):
        self.currentPhoto += 1
    
    def prevPhoto(self):
        self.currentPhoto -= 1

    #helper functions below

    def show_image_in_new_window(self, image):
        top = tk.Toplevel()
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(top, image=photo)
        label.image = photo
        label.pack()
        delete_button = tk.Button(top, text="Delete", command=lambda: self.delete_image(image, top))
        delete_button.pack()
        top.mainloop()
    
    def delete_image(self, image, top):
        self.photoArray.remove(image)
        top.destroy()
        self.refresh_gallery()

    def refresh_gallery(self):
        for widget in self.gallery_frame.winfo_children():
            widget.destroy()

        self.displayImages()

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

