# 🎧 Auto-Playlist

**🏆 Award-Winning Project — Best Project @ UCSD CSES Tridev Hackathon 2022**

Auto-Playlist is an intelligent playlist generator that queues songs based on the currently playing track using a custom machine learning algorithm and the Spotify API.

---

## 🚀 Project Highlights

- 🎶 Automatically queues relevant songs based on your current Spotify track
- 📊 Uses a **modified K-Means clustering algorithm** to group and recommend songs
- 🔗 Integrates with the **Spotify Web API** to retrieve audio features and metadata

---

## 🔧 Spotify API Setup

### 1. Create a Developer Account

Go to [Spotify Developer Dashboard](https://developer.spotify.com/) and log in or sign up for an account.

### 2. Register an App

- Create a new app and give it any name.
- Under **Redirect URIs**, add: `https://google.com`
- Choose **Web API** under "APIs Used"

### 3. Get Your API Keys

- In the app dashboard, copy your **Client ID** and **Client Secret**
- Paste these keys into the appropriate fields in `app.py`

---

## 💻 How to Run the App

### 1. Initial Setup

```bash
cd Auto-Playlist
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Launch the App

Make sure you have a song currently playing on Spotify, then run:

```bash
python app.py
```

Follow the instructions provided in the terminal to generate your custom playlist.
