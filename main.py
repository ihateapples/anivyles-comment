import tkinter as ihateapples
from PIL import Image, ImageTk
import io
import requests

class GrenadeBeltGame:
    def __init__(self, root, image_url):
        self.root = root
        self.root.title("anivyle")

        self.ihateapples_count = 0

        image_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(image_data))
        self.photo = ImageTk.PhotoImage(image)

        # Increase the font size for the label
        label_font = ("Helvetica", 16)

        self.ihateapples_label = ihateapples.Label(root, text="click count: 0", font=label_font)
        self.ihateapples_label.pack(pady=10)

        self.grenadebelt_button = ihateapples.Button(root, image=self.photo, command=self.increment_ihateapples_count)
        self.grenadebelt_button.pack(pady=10)

    def increment_ihateapples_count(self):
        self.ihateapples_count += 1
        self.ihateapples_label.config(text=f"click count: {self.ihateapples_count}")

if __name__ == "__main__":
    image_url = "https://raw.githubusercontent.com/ihateapples/anivyles-comment/main/anivyle.png"

    root = ihateapples.Tk()
    game = GrenadeBeltGame(root, image_url)
    root.mainloop()
