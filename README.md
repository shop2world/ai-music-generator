```markdown
# Générateur de Musique IA 🎶

**Générateur de Musique IA** est une application qui utilise les APIs d'OpenAI et de Suno AI pour générer de la musique à partir d'une invite fournie par l'utilisateur. Saisissez une invite, et l'application générera un titre, des tags de style, des paroles, et une piste musicale téléchargeable.

## Structure du Projet

```
├── main.py              # Interface frontend avec Streamlit pour l'interaction utilisateur
├── generate_music.py     # Logique de génération de musique via l'API de Suno AI
├── file_processing.py    # Génération d'invites musicales avec l'API d'OpenAI
├── requirements.txt      # Liste des packages nécessaires
└── README.md             # Documentation du projet
```

## Fonctionnalités Principales

- **Saisie d'Invites** - Les utilisateurs fournissent une invite pour générer de la musique.
- **Génération d'Invite Musicale** - Utilisation d'OpenAI pour générer un titre, des tags de style, et des paroles en fonction de l'invite fournie.
- **Génération de Musique** - L'API de Suno AI génère une piste musicale basée sur les résultats d'OpenAI et retourne un lien URL pour la musique générée.

## Installation

### 1. Cloner le Dépôt

```bash
git clone https://github.com/nomutilisateur/generateur-musique-ia.git
cd generateur-musique-ia
```

### 2. Installer les Dépendances

Installez les packages requis listés dans `requirements.txt` :

```bash
pip install -r requirements.txt
```

### 3. Configurer les Variables d'Environnement

Créez un fichier `.env` dans le répertoire racine du projet et ajoutez vos clés API pour OpenAI et Suno AI :

```plaintext
OPENAI_API_KEY=votre_cle_api_openai
SUNO_API_KEY=votre_cle_api_suno
```

### 4. Lancer l'Application

Démarrez l'application Streamlit avec la commande suivante :

```bash
streamlit run main.py
```

## Aperçu des Fichiers

### `main.py`

Le point d'entrée principal de l'application Streamlit, fournissant une interface utilisateur où les utilisateurs saisissent une invite pour générer de la musique. Lorsqu'une invite est saisie, l'application déclenche le processus de génération de musique et affiche les URLs de la musique générée.

### `generate_music.py`

Gère l'interaction avec l'API de Suno AI, en créant une tâche de génération musicale en fonction des informations fournies par l'invite et en récupérant les URLs de la musique générée.

### `file_processing.py`

Utilise l'API ChatCompletion d’OpenAI pour générer des invites musicales. Ce fichier comprend également `extract_json`, une fonction qui extrait de manière sécurisée les données JSON de la réponse d'OpenAI, ainsi que `MusicPrompt`, un modèle Pydantic pour la validation JSON.

## Exemple d'Utilisation

1. Lancez l'application Streamlit, puis entrez une invite décrivant la musique que vous souhaitez créer.
2. Cliquez sur le bouton **Générer la Musique** pour créer la musique.
3. Consultez et téléchargez la musique générée en utilisant les URLs fournies.

## Dépannage

- Assurez-vous que les deux clés API sont correctement configurées dans le fichier `.env`.
- Vérifiez que toutes les dépendances de `requirements.txt` sont installées.
- En cas d'erreurs de formatage JSON, vérifiez la logique d'extraction et de validation JSON dans `file_processing.py`.

## Licence

Ce projet est sous licence MIT. Vous êtes libre d'utiliser, de modifier et de distribuer ce projet, mais merci de créditer les auteurs originaux.
```

Vous pouvez adapter l'URL du dépôt et le nom d'utilisateur selon vos besoins.
