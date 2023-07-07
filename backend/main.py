from typing import Union, List
import torch
from transformers import AutoProcessor, AutoModelForZeroShotImageClassification
from skimage import io
from fastapi import FastAPI
import torch.nn as nn
from PIL import Image
from street_clip import predict
from pydantic import BaseModel 

app = FastAPI()

processor = AutoProcessor.from_pretrained("geolocal/StreetCLIP")

model = AutoModelForZeroShotImageClassification.from_pretrained("geolocal/StreetCLIP")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/country-net/")
def country_net(countries: List[str] = ["Japan", "Chinese", "United States"], image_url: str = ""):
    img = io.imread(image_url)
    if img.shape[-1] == 4:
        img = img[:, :, :3]
    print("img", img.shape)
    label = predict(img=img, labels=countries)
    print("label", label)
    return label

@app.get('/hiyoshi-net/')
def hiyoshi_net(image_url: str):
    pass
