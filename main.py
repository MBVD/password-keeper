from webbrowser import get
from xml.dom.minidom import Element
import eel
import  pyperclip
import pandas as pd 
import numpy as np
def copy_element():
    element = get_element()
    pyperclip.copy(element)

def get_element (name):
    try:
        df = pd.read_csv("base.csv")
        return df.loc[df["name"] == name]["key"].to_dict()[0]
    except Exception as e:
        return None

def save_element(name, key):
    d_frame = pd.read_csv('base.csv')
    if get_element(name):
        return False
    d_frame.loc[len(d_frame), d_frame.columns] = name, key
    d_frame.to_csv("base.csv",index=False)
    return True
    

# eel.init("web")
# eel.start("index.html", size = (700, 700))