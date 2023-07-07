from transformers import AutoProcessor, AutoModelForZeroShotImageClassification
from typing import List
import numpy as np
import torch
import torch.nn as nn
from PIL import Image

processor = AutoProcessor.from_pretrained("geolocal/StreetCLIP")

model = AutoModelForZeroShotImageClassification.from_pretrained("geolocal/StreetCLIP",)


def predict(img: np.ndarray, labels: List[str]):
    inputs = processor(
        text=labels,
        images=img,
        return_tensors="pt",
        padding=True
    )
    outputs = model(**inputs)
    logits_per_image: torch.Tensor = outputs.logits_per_image # this is the image-text similarity score
    probs: torch.Tensor = logits_per_image.softmax(dim=1)
    index = torch.argmax(probs, dim=1).item()
    return labels[index]
