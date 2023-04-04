import cloudinary
from cloudinary.uploader import upload
from .keras_model import image_classify


def classify_image(image_path, model_path):
    result = image_classify(image_path, model_path)
    if result != ["Invalid photo"]:
        return {'prediction': result[0], 'accuracy': result[1]}
    return None


def upload_image(image_file):
    upload_result = upload(image_file)
    return upload_result.get('url')
