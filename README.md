# 🎧 Auto-Playlist Discord Bot

**🏆 Best Project — UCSD CSES Tridev Hackathon 2022**

Auto-Playlist is an intelligent **Discord bot** that automatically queues songs based on the currently playing Spotify track. It uses a modified K-Means clustering algorithm and the Spotify API to generate smart playlists on the fly.

---

## 🚀 Features

- 🔁 Queue songs similar to the one currently playing on your Spotify
- 🤖 Easily controlled through a `!queue [num_songs]` command on Discord
- 🧠 Uses a custom K-Means-based clustering algorithm for intelligent song recommendations
- 🎵 Integrates with the Spotify API to fetch song data and features

---

## 🔧 Setup Instructions

### 1. Clone the Repository & Set Up Environment

```bash
git clone https://github.com/your-username/Auto-Playlist.git
cd Auto-Playlist
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 💬 Discord Bot Setup

### 1. Create a Discord Application
- Go to the [Discord Developer Portal](https://discord.com/developers/applications)
- Click **"New Application"**, and give it a name

### 2. Add a Bot to Your App
- Navigate to the **Bot** tab on the left sidebar
- Click **"Add Bot"**
- Reveal and **copy your Bot Token**
- Paste this token into your `discord.py` file in the appropriate location

### 3. Set OAuth2 & Bot Permissions
- Go to **OAuth2 → URL Generator**
- Under **Scopes**, check: `bot`
- Under **Bot Permissions**, select:
  - `View Channels`
  - `Send Messages`
  - `Read Message History`
  - `Connect`
  - `Speak`
- Copy the generated URL, paste it into your browser, and invite the bot to your Discord server

---

## 🎵 Spotify API Setup

### 1. Create a Spotify Developer Account
- Visit the [Spotify Developer Dashboard](https://developer.spotify.com/)
- Log in or sign up for an account

### 2. Register a New App
- Go to **Dashboard → Create an App**
- Give it a name (anything works)
- Under **Redirect URIs**, add: `https://google.com`
- Note your **Client ID** and **Client Secret**
- Paste these credentials into `app.py` where required

---

## ▶️ Running the Bot

Make sure:
- ✅ A song is currently playing on your Spotify
- ✅ The bot has been added to your Discord server

Then run:

```bash
python discord.py
```

## ▶️ Running the Bot Command in Discord

In your Discord server, type:

```discord
!queue [number_of_songs]
```

The bot will respond with a Spotify authorization URL.

### Complete the following steps:

1. Click the link and log in to Spotify  
2. After authorization, you will be redirected to a URI (likely starting with `https://google.com`)  
3. Copy the **entire redirected URL**  
4. Paste it into your terminal when prompted

🎉 Your playlist will now be intelligently queued with similar songs!

---

## 🧪 Technologies Used

- Python
- Discord.py (Bot) 
- Spotify Web API  
- K-Means Clustering (custom implementation)

