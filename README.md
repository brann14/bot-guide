# Easy Bot Setup
> This guide explains how to set up, run, and host your Discord bot using the provided script.  
> The bot uses modern Python features, environment variables for security, structured logging, and a modular cog system.  

## Requirements  

Before you begin, make sure you have the following installed:  

### **1. Python 3.9 or higher**  
   Check your version:  
   ```bash
   python --version
   # or
   python3 --version
   ```
Download from [python.org](https://www.python.org/downloads/) if needed.

### **2. pip (python pack manager)**
Already included with Python, but confirm with:
```bash
pip --version
```

### **3. Discord Application & Bot Token**
Go to the [Discord Developer Portal](https://discord.com/developers/applications).
Create a new application.
Add a bot under the Bot tab.
Copy the bot token (keep it secret).

### **4. Visual Studio Code (recommended)**
Any text editor works, but VS Code is easier for Python development.

## Bot Structure
Make sure your bot structure looks like this with all the code posted on this repo.
```python
MyBot/
│── cogs/                  # Folder for your bot's modular extensions
│   ├── example.py
│   └── ...
│── main.py                 # The main bot script (provided)
│── requirements.txt        # Python dependencies
│── .env                    # Stores your bot token and additional keys
```

## Environment Variables
Your script uses .env to store secrets safely.
Inside your project folder, create a file named .env:
```.env
DISCORD_TOKEN=your_bot_token
```

## Installing Dependencies
Create a requirements.txt with the following (or just download it from the repo): 
```txt
discord.py==2.4.0
python-dotenv==1.0.1
aiohttp==3.9.5
loguru==0.7.2
jishaku==2.5.2
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

## Running the Bot
Run your bot locally with:
```bash
python main.py
# or
python3 main.py
```
If everything is set up correctly, you should see a log message:
```bash
[01-10-2025 15:20:35] (bot:on_ready) @ Connected to Discord as MyBot (123456789012345678)
```

## Adding Cogs
The bot is modular. To add commands, create new files in the cogs/ folder.
I left a basic cog structure in cogs/commands.py
When you restart the bot, it will auto-load the cogs, though they might get timed out, you can after how much time they get timed out in main.py.

There are a lot of tutorials on how you can make commands and functions that you want.

## Hosting with VPS
Once the bot works locally, you can host it on a VPS (Virtual Private Server) to run 24/7.

### Connecting to the VPS
Once the bot works locally, you can host it on a VPS (Virtual Private Server) to run 24/7.

### 1. Connect to the VPS
```bash
ssh root@YOUR_SERVER_IP
```
If successful, your prompt should look like:
```bash
[root@yourserver ~]#
```

### 2. Upload Files
On your local machine, upload your bot folder:
```pwsh
scp -r C:/Users/YourName/MyBot root@YOUR_SERVER_IP:/root/
```

Check if it uploaded:
```bash
ls
```

### 3. Install Dependencies
On the VPS, navigate to your bot’s folder:
```bash
cd MyBot
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Run in a Screen Session
Start a screen session (so your bot stays online after you log out):
```bash
screen -S DiscordBot
```

Run your bot:
```bash
python main.py
```

Detach from the session (bot keeps running):
CTRL + A, then press D

Check sessions later:
```bash
screen -ls
```

Reconnect:
```bash
screen -r DiscordBot
```

## Congratulations!
You’ve now:
- Set up your bot locally
- Secured your token with .env
- Installed dependencies with requirements.txt

-# © 2026 brann14
-# Licensed under CC-BY-NC 4.O.
- Learned how to add cogs (modular commands)
- Deployed your bot to a VPS for 24/7 hosting

From here, you can expand with new cogs, slash commands, APIs, and more, good luck in your futher development.
