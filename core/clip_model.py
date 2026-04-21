import torch
from transformers import CLIPProcessor, CLIPModel
from sentence_transformers import SentenceTransformer

device = "cuda" if torch.cuda.is_available() else "cpu"

# Strong CLIP model
clip_model = CLIPModel.from_pretrained(
    "openai/clip-vit-large-patch14"
).to(device)

clip_processor = CLIPProcessor.from_pretrained(
    "openai/clip-vit-large-patch14"
)

# Strong text embedding model
text_model = SentenceTransformer(
    "all-mpnet-base-v2",
    device=device
)
