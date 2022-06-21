import tkinter as tk 
from tkinter import filedialog, Text 
import os

root = tk.Tk()

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempAps = f.read()
        tempAps = tempAps.split(',')
        apps = [x for x in tempAps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='pink')
        label.pack()

def runApp():
    for app in apps:
        # for mac use
        # couldnt find good documentation
        # for windows use
        os.startfile(app)

canvas = tk.Canvas(root, height=600, width=600, bg="#454B1B")
canvas.pack()

# add a frame inside
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# add btns
openFile = tk.Button(root, text="Open File", padx=10,
                      pady=5, fg="white", bg="#454B1B", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                      pady=5, fg="white", bg="#454B1B", command=runApp)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')