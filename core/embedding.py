import torch
from PIL import Image
from core.clip_model import clip_model, clip_processor, text_model, device


def encode_image(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = clip_processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        features = clip_model.get_image_features(**inputs)

    return features / features.norm(dim=-1, keepdim=True)


def encode_text_clip(text):
    inputs = clip_processor(text=[text], return_tensors="pt", padding=True).to(device)

    with torch.no_grad():
        features = clip_model.get_text_features(**inputs)

    return features / features.norm(dim=-1, keepdim=True)


def encode_text_semantic(text):
    return text_model.encode(text, normalize_embeddings=True)
