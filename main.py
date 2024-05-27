import keyboard as kb
from vidanova import vidanova
from dotenv import load_dotenv
import os

load_dotenv()

vidanova = vidanova(os.getenv("PATH_SAVE"))

print("Your files are located in: ", vidanova.getPath())

kb.hook(vidanova.obtenerData())

while(True):
    pass

