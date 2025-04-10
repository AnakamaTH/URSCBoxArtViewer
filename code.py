import sys
import os
import ctypes
from PIL import Image
from tkinter import Tk, Label
from PIL import ImageTk

def show_error(message):
    ctypes.windll.user32.MessageBoxW(0, message, "URSC Box Art Viewer", 0x10)

def show_image(image_path, auto_close=0):
    if not os.path.isfile(image_path):
        show_error(f"Image file not found:\n{image_path}")
        sys.exit(1)

    root = Tk()
    root.title("URSC Box Art Viewer")
    root.geometry("+100+100")
    root.configure(bg='black')
    root.overrideredirect(True)

    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    label = Label(root, image=photo, bg='black')
    label.pack()

    if auto_close > 0:
        root.after(auto_close * 1000, root.destroy)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_error("Usage (CMD):\nURSC_BoxViewer.exe <image_file> [autoclose_seconds]")
        sys.exit(1)

    image_file = sys.argv[1]
    auto_close = int(sys.argv[2]) if len(sys.argv) > 2 else 0

    show_image(image_file, auto_close)
