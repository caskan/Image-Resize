import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def resize_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        quality = int(quality_entry.get())
        resized_image = image.resize((new_width, new_height))
        output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if output_path:
            resized_image.save(output_path, format="JPEG", quality=quality)

app = tk.Tk()
app.title("Image Resizer (Made specially for Burcu Yolasigmaz by Can Mavi)")
import os

script_path = os.path.abspath(__file__)
print("Script path:", script_path)

# Set the width and height of the app window
app.geometry("500x200")  # Adjust the width and height as needed

width_label = tk.Label(app, text="Width:")
width_label.pack()
width_entry = tk.Entry(app)
width_entry.pack()

height_label = tk.Label(app, text="Height:")
height_label.pack()
height_entry = tk.Entry(app)
height_entry.pack()

quality_label = tk.Label(app, text="Quality (between 0-100):")
quality_label.pack()
quality_entry = tk.Entry(app)
quality_entry.pack()

resize_button = tk.Button(app, text="Resize Image", command=resize_image)
resize_button.pack()

app.mainloop()

script_path = os.path.abspath(__file__)
print("Script path:", script_path)
pillow_path = os.path.dirname(Image.__file__)
print("Pillow (PIL) module path:", pillow_path)