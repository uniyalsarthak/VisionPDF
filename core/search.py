import torch
from sklearn.metrics.pairwise import cosine_similarity
from core.embedding import encode_image, encode_text_clip

import numpy as np

def semantic_search(query, items, top_k=5, threshold=0.205):

    query_vec = encode_text_clip(query).cpu().numpy()

    results = []

    for item in items:

        image_vec = item["vector"]  

        score = cosine_similarity(query_vec, image_vec)[0][0]

        if score >= threshold:
            results.append({
                "path": item["path"],
                "caption": item["caption"],
                "pdf": item["pdf"],
                "score": float(score)
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:top_k]
