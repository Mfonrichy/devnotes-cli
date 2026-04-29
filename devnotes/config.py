import os

APP_DIR = os.path.join(os.path.expanduser("~"), ".devnotes")
FILE_PATH = os.path.join(APP_DIR, "notes.json")

def ensure_storage():
    os.makedirs(APP_DIR, exist_ok=True)