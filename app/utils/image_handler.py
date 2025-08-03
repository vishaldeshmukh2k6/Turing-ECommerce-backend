import os
from werkzeug.utils import secure_filename
from uuid import uuid4

UPLOAD_FOLDER = "static/uploads"

def save_image(file):
    filename = secure_filename(file.filename)
    unique_name = f"{uuid4().hex}_{filename}"
    filepath = os.path.join(UPLOAD_FOLDER, unique_name)
    file.save(filepath)
    return unique_name

def delete_image(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
