import json
from devnotes.config import FILE_PATH, ensure_storage
from devnotes.models import Note

def load_notes():
    ensure_storage()
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(FILE_PATH, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(text, tags):
    notes = load_notes()
    note = Note.create(text, tags)
    notes.append(note.to_dict())
    save_notes(notes)

def list_notes():
    return load_notes()

def search_notes(keyword):
    return [
        n for n in load_notes()
        if keyword.lower() in n["text"].lower()
    ]

def delete_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        removed = notes.pop(index)
        save_notes(notes)
        return removed
    return None