from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = FastAPI()

# Load the trained model
model = load_model('path/to/your/model')

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the image
    return img_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Save the file
        file_path = 'uploads/' + file.filename
        with open(file_path, 'wb') as f:
            f.write(file.file.read())

        # Preprocess the image
        img_array = preprocess_image(file_path)

        # Make prediction
        prediction = model.predict(img_array)

        # Display the result
        result = "Endangered" if prediction > 0.5 else "Not Endangered"

        return {"result": result}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
