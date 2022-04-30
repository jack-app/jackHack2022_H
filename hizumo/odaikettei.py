import tkinter as tk
import random

def dispLabel():
    odai=['レモン','みかん','りんご','ばなな','抹茶']
    lbl.configure(text=random.choice(odai))

root=tk.Tk()
root.geometry("200x100")

lbl=tk.Label(text="LABEL")
btn=tk.Button(text="PUSH",command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()