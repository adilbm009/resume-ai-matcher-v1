from pathlib import Path

def get_file_extension(uploaded_file):
    return Path(uploaded_file.name).suffix.lower()