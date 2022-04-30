#import tkinter as tk
import random

def dispLabel():
    odai=['レモン','みかん','りんご','ばなな','抹茶']
    text=random.choice(odai)
    print(text)
    return text