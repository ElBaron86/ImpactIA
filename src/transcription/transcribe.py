# ============================================================
# InspireAI - Transcription audio (via Whisper HF)
# ============================================================

from dotenv import load_dotenv
import os
import warnings
import pandas as pd
from tqdm import tqdm
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa
import numpy as np
import traceback
import math
import logging

# ============================================================
# Chargement de l'environnement
# ============================================================
load_dotenv()

# Variables d'environnement
TRANSCRIPTION_MODEL = os.getenv("TRANSCRIPTION_MODEL")
METADATA_PATH = os.getenv("METADATA_PATH")
DATA_DIR = os.getenv("DATA_DIR")
LOG_DIR = os.getenv("LOGS_DIR")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename=os.path.join(LOG_DIR, 'transcription.log'))

# Vérifications
assert TRANSCRIPTION_MODEL, "TRANSCRIPTION_MODEL manquant dans le fichier .env"
assert METADATA_PATH, "METADATA_PATH manquant dans le fichier .env"
assert DATA_DIR, "DATA_DIR manquant dans le fichier .env"

# ============================================================
# Configuration du modèle et du périphérique
# ============================================================
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
DTYPE = torch.float16 if torch.cuda.is_available() else torch.float32

logging.info(f"Chargement du modèle depuis {TRANSCRIPTION_MODEL}")
logging.info(f"Utilisation du device : {DEVICE}")

processor = WhisperProcessor.from_pretrained(TRANSCRIPTION_MODEL)
model = WhisperForConditionalGeneration.from_pretrained(TRANSCRIPTION_MODEL).to(DEVICE).to(DTYPE)
forced_decoder_ids = processor.get_decoder_prompt_ids(language="french", task="transcribe")

# ============================================================
# Fonction de transcription
# ============================================================
def transcribe_audio(file_path: str) -> str:
    """
    Transcrit un fichier audio (.mp3, .wav, etc.) en texte.
    Découpe automatiquement en segments de 30s si nécessaire.
    """
    try:
        audio, sr = librosa.load(file_path, sr=16000, mono=True)
    except Exception as e:
        raise RuntimeError(f"Erreur de lecture audio pour {file_path}: {e}")

    # Découpage automatique
    chunk_duration = 30  # secondes
    chunk_size = int(chunk_duration * sr)
    num_chunks = math.ceil(len(audio) / chunk_size)

    texts = []

    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, len(audio))
        chunk = audio[start:end]

        inputs = processor(chunk, sampling_rate=16000, return_tensors="pt")
        input_features = inputs.input_features.to(DEVICE).to(DTYPE)

        with torch.no_grad():
            predicted_ids = model.generate(
                input_features,
                max_new_tokens=128,
                language="french",
                task="transcribe"
            )
        text = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
        texts.append(text.strip())

    return " ".join(texts)


# ============================================================
# Boucle principale
# ============================================================
if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    logging.info(f"Lecture du fichier de métadonnées : {METADATA_PATH}")
    metadata = pd.read_csv(METADATA_PATH)

    # Dictionnaire pour regrouper les résultats par titre
    results_by_title = {}
    
    for idx, row in tqdm(metadata.iterrows(), total=len(metadata), desc="Transcription en cours"):
        title = row.get("title", "Unknown")
        author = row.get("author", "")
        chapter = row.get("chapter", "")
        keywords = row.get("keywords", "")
        audio_path = row.get("path", "")

        if not audio_path or not os.path.exists(audio_path):
            print(f"\nFichier manquant pour {title} ({chapter})")
            continue

        try:
            text = transcribe_audio(audio_path)
            
            # Initialiser la liste pour ce titre si elle n'existe pas
            if title not in results_by_title:
                results_by_title[title] = []
            
            results_by_title[title].append({
                "author": author,
                "title": title,
                "chapter": chapter,
                "keywords": keywords,
                "text": text
            })
            logging.info(f"Transcription réussie : {title} - {chapter}")
        except Exception as e:
            logging.error(f"Erreur pour {audio_path}:")
            logging.error(f"Type: {type(e).__name__}")
            logging.error(f"Message: {str(e)}")
            logging.error(f"Traceback:")
            traceback.print_exc()
            continue

    # Sauvegarde des résultats par titre
    if results_by_title:
        total_transcribed = 0
        for title, results in results_by_title.items():
            # Créer un dossier pour chaque titre
            output_dir = os.path.join(DATA_DIR, f"transcriptions/{title}")
            output_path = os.path.join(output_dir, "transcriptions.csv")
            os.makedirs(output_dir, exist_ok=True)
            
            # Sauvegarder le CSV pour ce titre
            pd.DataFrame(results).to_csv(output_path, index=False, encoding="utf-8")
            total_transcribed += len(results)
            logging.info(f"Enregistré : {output_path}")
            logging.info(f"Chapitres transcrits : {len(results)}")

        logging.info(f"Transcriptions terminées !")
        logging.info(f"Titres différents : {len(results_by_title)}")
        logging.info(f"Total de fichiers transcrits : {total_transcribed}/{len(metadata)}")
    else:
        logging.warning("Aucune transcription réussie. Aucun fichier créé.")