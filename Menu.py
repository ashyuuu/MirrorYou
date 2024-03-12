import tkinter as tk

class Menu:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("MirrorYou")

        # Set the size of the main window
        self.root.geometry("2000x2000")

        # Create the main menu
        self.create_main_menu()

        # Start the GUI
        self.root.mainloop()

    def show_weather(self):
        label.config(text="Weather option selected")
        self.show_submenu("Weather")

    def show_gallery(self):
        label.config(text="Gallery option selected")

    def perform_analysis(self):
        label.config(text="Analysis option selected")

    def do_nothing(self):
        label.config(text="Blank option selected")

    def show_submenu(self,option):
        # Clear the existing buttons
        self.clear_buttons()

        # Create a label for the submenu
        submenu_label = tk.Label(self.root, text=option, font=("Helvetica", 14))
        submenu_label.pack(pady=20)

        # Create a back button
        back_button = tk.Button(self.root, text="Back", command=self.show_main_menu)
        back_button.pack(pady=10)

    def show_main_menu(self):
        # Clear the existing labels and buttons
        self.clear_labels()
        self.clear_buttons()

        # Recreate the main menu
        self.create_main_menu()

    def clear_labels(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

    def clear_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

            buttons_frame.destroy()

    def create_main_menu(self):
        # Create a label in the middle
        global label
        label = tk.Label(self.root, text="How may I help you today?", font=("Helvetica", 20))
        label.pack(pady=20)

        # Create buttons with different functions and evenly spread them out
        global buttons_frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        weather_button = tk.Button(buttons_frame, text="Weather", command=self.show_weather)
        weather_button.pack(side="left", padx=10)

        gallery_button = tk.Button(buttons_frame, text="Photo Gallery & Analysis", command=self.show_gallery)
        gallery_button.pack(side="left", padx=10)

        analysis_button = tk.Button(buttons_frame, text="Take a picture", command=self.perform_analysis)
        analysis_button.pack(side="left", padx=10)

        blank_button = tk.Button(buttons_frame, text="Mirror", command=self.do_nothing)
        blank_button.pack(side="left", padx=10)
