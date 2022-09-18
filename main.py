from webbrowser import get
from xml.dom.minidom import Element
import eel
from back.back import *

eel.init("web")
eel.start("index.html", size=(700, 700))