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

hiyoshi_maps = {
    "1-chome": "〒223-0061 神奈川県横浜市港北区日吉1丁目",
    "2-chome": "〒223-0061 神奈川県横浜市港北区日吉2丁目",
    "3-chome": "〒223-0061 神奈川県横浜市港北区日吉3丁目",
    "4-chome": "〒223-0061 神奈川県横浜市港北区日吉4丁目",
    "5-chome": "〒223-0061 神奈川県横浜市港北区日吉5丁目",
    "6-chome": "〒223-0061 神奈川県横浜市港北区日吉6丁目",
    "7-chome": "〒223-0061 神奈川県横浜市港北区日吉7丁目",
}