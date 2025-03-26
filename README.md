## Hackathon: UCSD Computer Science & Engineering Society Tridev Hackathon 2022

### Award: Best Project

## Project Description:
- Queues songs based on current song
- Employs a modified K-Means Clustering algorithm to find relevant songs
- Leverages Spotify API to retrieve song data

## Spotify API Setup

### 1. Create Developer Account

Got to 'https://developer.spotify.com/', and create an account.

### 2. Create Sample App

Name the app whatever you want to call it. Add 'https://google.com' under 'Redirect URIs'. Select 'Web API' under 'APIs Used'.

### 3. Take Note Of Access Keys

Find the Client ID and Client Secret keys in App Settings. Input them in the respective fields inside the app.py file.

## Run Code

Initial set up
```bash
cd Auto-Playlist
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Run app and follow instructions in terminal (ensure you have a song playing on Spotify)
```bash
python app.py
```

