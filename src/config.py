# Configuration globale du projet
import os
from pathlib import Path
import sys
import torch
import os
from dotenv import load_dotenv

# Charge les variables du .env
load_dotenv()

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"



# Chemins des fichiers et répertoires
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
AUDIO_DIR = DATA_DIR / "raw/audio"
VIDEO_DIR = DATA_DIR / "raw/video"
BOOKS_DIR = DATA_DIR / "raw/book"
MODEL_DIR = ROOT_DIR / "models"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
METADATA_PATH = DATA_DIR / "metadata/repertory.csv"

# sentence-transformer model path
SENTENCE_TRANSFORMER_MODEL = os.getenv("SENTENCE_TRANSFORMER_MODEL")

# transcription model path
TRANSCRIPTION_MODEL = os.getenv("TRANSCRIPTION_MODEL")

