from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import os
from endangered import get_predictions

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Save the file
        file_path = 'uploads/' + file.filename
        with open(file_path, 'wb') as f:
            f.write(file.file.read())

        # Get predictions using the logic from endangered.py
        predictions = get_predictions(file_path)

        return {"result": predictions}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
