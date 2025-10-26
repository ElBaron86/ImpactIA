<!-- Lien retour en haut -->
<a id="readme-top"></a>

<!-- BADGES DU PROJET -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- LOGO DU PROJET -->
<br />
<div align="center">
  <a href="https://github.com/votre-username/inspireAI">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">InspireAI</h3>

  <p align="center">
    Moteur de Recommandation Intelligent pour Contenus de Développement Personnel
    <br />
    <a href="https://github.com/votre-username/inspireAI"><strong>Explorer la documentation »</strong></a>
    <br />
    <br />
    <a href="https://github.com/votre-username/inspireAI">Voir la démo</a>
    ·
    <a href="https://github.com/votre-username/inspireAI/issues/new?labels=bug&template=bug-report.md">Signaler un bug</a>
    ·
    <a href="https://github.com/votre-username/inspireAI/issues/new?labels=enhancement&template=feature-request.md">Demander une fonctionnalité</a>
  </p>
</div>



<!-- TABLE DES MATIÈRES -->
<details>
  <summary>Table des matières</summary>
  <ol>
    <li>
      <a href="#à-propos-du-projet">À propos du projet</a>
      <ul>
        <li><a href="#construit-avec">Construit avec</a></li>
      </ul>
    </li>
    <li>
      <a href="#démarrage">Démarrage</a>
      <ul>
        <li><a href="#prérequis">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#utilisation">Utilisation</a></li>
    <li><a href="#architecture">Architecture</a></li>
    <li><a href="#feuille-de-route">Feuille de route</a></li>
    <li><a href="#contribuer">Contribuer</a></li>
    <li><a href="#licence">Licence</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#remerciements">Remerciements</a></li>
  </ol>
</details>



<!-- À PROPOS DU PROJET -->
## À propos du projet

[![InspireAI Screen Shot][product-screenshot]](https://example.com)

**InspireAI** est un projet d'intelligence artificielle qui révolutionne l'expérience de développement personnel et spirituel en personnalisant les recommandations de contenus pour chaque utilisateur.

Voici pourquoi InspireAI est unique :
* **Transcription automatique** : Convertit automatiquement vos contenus audio et vidéo en texte grâce à Whisper
* **Compréhension sémantique** : Analyse en profondeur le sens des contenus via des embeddings NLP avancés
* **Recommandations quotidiennes** : Propose chaque jour des contenus adaptés à votre profil et à votre évolution personnelle
* **Apprentissage continu** : S'améliore en fonction de vos interactions et préférences

L'objectif est de rendre le développement personnel accessible et personnalisé pour chacun, en utilisant les dernières avancées en IA.

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



### Construit avec

Ce projet utilise les technologies les plus avancées en IA et développement web :

* [![Python][Python.org]][Python-url]
* [![FastAPI][FastAPI.com]][FastAPI-url]
* [![PyTorch][PyTorch.org]][PyTorch-url]
* [![Hugging Face][HuggingFace.co]][HuggingFace-url]
* [![SQLAlchemy][SQLAlchemy.org]][SQLAlchemy-url]

**Technologies clés :**
- **Transcription** : [Whisper](https://github.com/openai/whisper) (optimisé pour le français)
- **Embeddings** : [Sentence Transformers](https://www.sbert.net/)
- **Résumés** : [Transformers Hugging Face](https://huggingface.co/docs/transformers)
- **API** : [FastAPI](https://fastapi.tiangolo.com/)
- **Base de données** : SQLite / PostgreSQL avec SQLAlchemy

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- DÉMARRAGE -->
## Démarrage

Pour obtenir une copie locale fonctionnelle, suivez ces étapes simples.

### Prérequis

* Python 3.10 ou supérieur
  ```sh
  python --version
  ```

* pip (gestionnaire de paquets Python)
  ```sh
  pip --version
  ```

* ffmpeg (pour l'extraction audio des vidéos)
  ```sh
  # Ubuntu/Debian
  sudo apt-get install ffmpeg
  
  # macOS
  brew install ffmpeg
  
  # Windows
  # Télécharger depuis https://ffmpeg.org/download.html
  ```

### Installation

1. Clonez le dépôt
   ```sh
   git clone https://github.com/votre-username/inspireAI.git
   cd inspireAI
   ```

2. Créez un environnement virtuel
   ```sh
   python -m venv icc_env
   source icc_env/bin/activate  # Sur Windows: icc_env\Scripts\activate
   ```

3. Installez les dépendances
   ```sh
   pip install -r requirements.txt
   ```

4. Configurez les variables d'environnement
   ```sh
   cp .env.example .env
   ```
   Puis éditez `.env` avec vos paramètres :
   ```env
   TRANSCRIPTION_MODEL=./models/whisper-small
   METADATA_PATH=./data/metadata/repertory.csv
   DATA_DIR=./data
   ```

5. Téléchargez le modèle Whisper (première utilisation)
   ```sh
   python -c "from transformers import WhisperProcessor; WhisperProcessor.from_pretrained('openai/whisper-small')"
   ```

6. Lancez le projet
   ```sh
   ./run_local.sh
   ```

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- UTILISATION -->
## Utilisation

### 1. Transcription audio

Pour transcrire des fichiers audio en texte :

```sh
python ./src/transcription/transcribe.py
```

Les transcriptions seront sauvegardées dans `./data/transcriptions/[TITRE]/transcriptions.csv`

### 2. Génération d'embeddings

```sh
python ./src/text_processing/embeddings.py
```

### 3. Obtenir des recommandations

```python
from src.recommendation.recommend import get_recommendations

user_profile = {
    "interests": ["développement personnel", "spiritualité"],
    "preferences": ["court", "pratique"]
}

recommendations = get_recommendations(user_profile)
print(recommendations)
```

### 4. API FastAPI

Lancez l'API :

```sh
uvicorn src.api.main:app --reload
```

Accédez à la documentation interactive : `http://localhost:8000/docs`

_Pour plus d'exemples, consultez la [Documentation](https://github.com/votre-username/inspireAI/wiki)_

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- ARCHITECTURE -->
## Architecture

```
ImpactAI/
│
├── data/
│   ├── raw/                 # Contenus bruts : audios, vidéos
│   ├── processed/           # Transcriptions, résumés, embeddings
│   ├── transcriptions/      # Transcriptions organisées par titre
│   └── metadata/            # Métadonnées (CSV, JSON)
│
├── notebooks/               # Notebooks Jupyter pour l'exploration
│   ├── 01_transcription_tests.ipynb
│   ├── 02_embeddings_exploration.ipynb
│   └── 03_recommendation_prototype.ipynb
│
├── src/
│   ├── transcription/       # Traitement audio/vidéo
│   ├── text_processing/     # NLP et embeddings
│   ├── recommendation/      # Système de recommandation
│   ├── database/            # Gestion base de données
│   ├── api/                 # API FastAPI
│   └── utils/               # Utilitaires
│
├── tests/                   # Tests unitaires
├── requirements.txt
├── .env
└── README.md
```

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- FEUILLE DE ROUTE -->
## Feuille de route

- [x] Transcription automatique avec Whisper
- [x] Organisation des transcriptions par titre
- [ ] Génération de résumés automatiques
- [ ] Création d'embeddings sémantiques
- [ ] Système de recommandation basé sur la similarité
- [ ] API REST complète
- [ ] Interface utilisateur web
- [ ] Apprentissage des préférences utilisateur
- [ ] Support multilingue
    - [x] Français
    - [ ] Anglais
    - [ ] Espagnol

Consultez les [issues ouvertes](https://github.com/votre-username/inspireAI/issues) pour voir la liste complète des fonctionnalités proposées (et des problèmes connus).

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- CONTRIBUER -->
## Contribuer

Les contributions sont ce qui fait de la communauté open source un endroit incroyable pour apprendre, inspirer et créer. Toutes vos contributions sont **grandement appréciées**.

Si vous avez une suggestion pour améliorer ce projet, forkez le dépôt et créez une pull request. Vous pouvez aussi simplement ouvrir une issue avec le tag "enhancement".
N'oubliez pas de donner une étoile au projet ! Merci encore !

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Principaux contributeurs :

<a href="https://github.com/votre-username/inspireAI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=votre-username/inspireAI" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- LICENCE -->
## Licence

Distribué sous la licence MIT. Voir `LICENSE.txt` pour plus d'informations.

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- CONTACT -->
## Contact

Votre Nom - [@votre_twitter](https://twitter.com/votre_username) - email@example.com

Lien du projet : [https://github.com/votre-username/inspireAI](https://github.com/votre-username/inspireAI)

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- REMERCIEMENTS -->
## Remerciements

Ressources et outils qui ont rendu ce projet possible :

* [Whisper by OpenAI](https://github.com/openai/whisper)
* [Hugging Face Transformers](https://huggingface.co/docs/transformers)
* [Sentence Transformers](https://www.sbert.net/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>



<!-- LIENS ET IMAGES MARKDOWN -->
[contributors-shield]: https://img.shields.io/github/contributors/votre-username/inspireAI.svg?style=for-the-badge
[contributors-url]: https://github.com/votre-username/inspireAI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/votre-username/inspireAI.svg?style=for-the-badge
[forks-url]: https://github.com/votre-username/inspireAI/network/members
[stars-shield]: https://img.shields.io/github/stars/votre-username/inspireAI.svg?style=for-the-badge
[stars-url]: https://github.com/votre-username/inspireAI/stargazers
[issues-shield]: https://img.shields.io/github/issues/votre-username/inspireAI.svg?style=for-the-badge
[issues-url]: https://github.com/votre-username/inspireAI/issues
[license-shield]: https://img.shields.io/github/license/votre-username/inspireAI.svg?style=for-the-badge
[license-url]: https://github.com/votre-username/inspireAI/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/votre-profile
[product-screenshot]: images/screenshot.png

[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[FastAPI.com]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/
[PyTorch.org]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[PyTorch-url]: https://pytorch.org/
[HuggingFace.co]: https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black
[HuggingFace-url]: https://huggingface.co/
[SQLAlchemy.org]: https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlite&logoColor=white
[SQLAlchemy-url]: https://www.sqlalchemy.org/