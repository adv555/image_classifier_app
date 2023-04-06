
import numpy as np
from keras.models import load_model
import tensorflow as tf
from PIL import Image


def load_image(image_file):
    img = Image.open(image_file)
    img = img.resize((32, 32))
    img = np.array(img)
    return img


def image_classify(image_file, model_file):
    classes = ["Airplane", "Automobile", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck"]
    img = load_image(image_file)

    model = load_model(model_file, compile=False)
    print(model.summary())

    result = model.predict(np.expand_dims(img, axis=0))
    prediction = result[0]
    print('Prediction', prediction)

    result = np.argmax(prediction)

    if prediction[result] < 0.85:
        return ["Invalid photo"]
    else:
        return [classes[result], float(str(prediction[result])[:4])]


