import tkinter
from tkinter.ttk import *
from PIL import ImageTk, Image
import time
import math
from os import listdir
from os.path import isfile, join
import random

# Frequency in flicker cycles per second
freq = 2

# Cycles per stimulus
reps = 1

# Time between frames
animation_refresh = 0.02

image_paths = [f for f in listdir("Controls") if isfile(join("Controls", f))][1:]
random.shuffle(image_paths)

image_array = []

for image in image_paths:
  image_array.append(Image.open("Controls/" + image).resize((500,500)))

print(image_paths)
def create_animation_window():
    window = tkinter.Tk()
    window.title("Poirot")
    window.geometry("700x700")
    return window

def create_animation_canvas(window):
    canvas = tkinter.Canvas(window, width = 500, height = 500)
    canvas.configure(bg="black")
    canvas.pack(fill="both", expand=True)
    return canvas

def animate_image(window, canvas):
    initial_time = time.perf_counter()
    while True:
      current_time = time.perf_counter()
      relative_time = current_time - initial_time
      index = round((relative_time - initial_time)//freq//reps)
      img = image_array[index]
      transparency = round((math.sin(current_time*2*math.pi*freq)+1)*127)
      img.putalpha(transparency)
      new_img = ImageTk.PhotoImage(img)
      canvas.create_image(325, 325, image = new_img)
      window.update()
      time.sleep(animation_refresh)
    

animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
animate_image(animation_window, animation_canvas)