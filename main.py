from xml.dom.minidom import Element
import eel
import  pyperclip
import pandas as pd 
import numpy as np
def copy_element():
    element = get_element()
    pyperclip.copy(element)

def get_element (name):
    df = pd.read_csv("base.csv")
    return df.loc[df["name"] == name]["key"]

def save_element(name, key):
    d_frame = pd.read_csv('base.csv')
    print(d_frame)
    d_frame.loc[len(d_frame.index)] = [name, key]
    d_frame.to_csv("base.csv")
    

# eel.init("web")
# eel.start("index.html", size = (700, 700))