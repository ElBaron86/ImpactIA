import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

load_dotenv()

SENTENCE_TRANSFORMER_MODEL = os.getenv("SENTENCE_TRANSFORMER_MODEL")
EMBEDDINGS_DIR = os.getenv("EMBEDDINGS_DIR")
METADATA_PATH = os.getenv("METADATA_PATH")


sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer(SENTENCE_TRANSFORMER_MODEL)

def vectorize_text(text: str):
    """
    Convertit un texte en vecteur numérique à l'aide d'un modèle de sentence transformer.

    Args:
        text (str): Le texte à vectoriser.

    Returns:
        np.ndarray: Vecteur numérique représentant le texte.
    """
    embedding = model.encode(text)
    return embedding

