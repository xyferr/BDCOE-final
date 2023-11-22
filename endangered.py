from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.applications.resnet50 import preprocess_input as resnet_preprocess_input
from tensorflow.keras.applications.vgg16 import preprocess_input as vgg16_preprocess_input
import numpy as np


mobilenet_model = load_model(r'model\mobilenet_checkpoint_accuracy.h5') # Loading MobileNet model


resnet50_model = load_model(r'model\resnet50_checkpoint_accuracy.h5') # Loading ResNet50 model


vgg16_model = load_model(r'model\vgg16_checkpoint_accuracy.h5') # Loading VGG16 model


def preprocess_image(model_name, img_path):
    target_size = (224, 224)  

    if model_name == 'mobilenet':
        preprocess_func = preprocess_input
    elif model_name == 'resnet50':
        preprocess_func = resnet_preprocess_input
    elif model_name == 'vgg16':
        preprocess_func = vgg16_preprocess_input
    else:
        raise ValueError(f"Unsupported model: {model_name}")

    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = preprocess_func(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


#test_img_path = r'C:\Users\XYFER\Pictures\tiger.webp' # Testing image ka path

# results ko hardcode karne wala function
def interpret_results(predictions):
    if predictions[0][0] >= 0.5:
        return "Class 1 (Not Endangered)"
    else:
        return "Class 0 (Endagered)"

# frontend is function ko call karega
def get_predictions(img_path):
    mobilenet_predictions = mobilenet_model.predict(preprocess_image('mobilenet', img_path))
    resnet50_predictions = resnet50_model.predict(preprocess_image('resnet50', img_path))
    vgg16_predictions = vgg16_model.predict(preprocess_image('vgg16', img_path))

    return {
        "MobileNet": interpret_results(mobilenet_predictions),
        "ResNet50": interpret_results(resnet50_predictions),
        "VGG16": interpret_results(vgg16_predictions)
    }