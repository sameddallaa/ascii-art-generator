import tkinter as tk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)


ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ascii_chars = [char for char in ascii_chars]

def resize_image(image, new_height=100):
    width, height = image.size
    ratio = new_height / height
    new_width= int(width * ratio)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def grayscale_to_ascii(image):
    pixels = image.getdata()
    chars = "".join([ascii_chars[int(pixel // 145)] for pixel in pixels])
    return chars

def display_ascii_art(ascii_art, font_name, font_size):
    root = tk.Tk()
    root.title("ASCII Art Viewer")

    text_widget = tk.Text(root, font=(font_name, font_size), wrap=tk.NONE)
    text_widget.insert(tk.END, ascii_art)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill=tk.BOTH)

    root.mainloop()