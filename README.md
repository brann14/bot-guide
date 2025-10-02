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

## Coding
To start off, you can download or just make your own files and copy my scripts that are posted on this repository.

After you've done that, install all the requirements with pip by running
```bash
pip install -r requirements.txt
```

Next step is to change all the ID's like guild ID, Application Id and bot token. Make sure to never share your bot token.

## Finishing

You can easily add new commands the same way I added those 2 in the commands.py. The `@commands.command` is a prefix command while `@app_commands.command` is a slash command.

And last step is to run the bot, you can do that buy running:
```bash
python main.py
```

If you're happy with your work, you can get yourself a nice VPS and SCP all the files to it. Below this part, there's a guide on how to connect to your VPS with SSH, SCP all the files and host it 24/7.

# Hosting with VPS
> If you've finished the previous part and you want to host your bot with a VPS (Visual Private Server) so it's running at all times, you can do so if you follow the next steps. Keep in mind this part requires you to have a VPS.
> Note that you will have to reinstall everything, like pip, python, and whatever your script is using.

## Connecting to the VPS

Below you can see the command to connect to the VPS, the name root is the automatic username though if you have a different one, change it. The second part is an IP, change it with your VPS's IP
```bash
ssh root@123.456.789
```
After you've ran that, it's going to ask you for your VPS's password, type it in and wait for you to connect to the VPS.

If you have connected to your VPS, it should look like `[root@Name ~]# `.

After you can successfully connect to your VPS, make a new terminal and run the following.
```bash
scp -r C:/Users/Name/Bot_Guide root@123.456.789:/root/
```
Change the path to your folder and where you want to SCP the file to your VPS. Also like before, make sure to change the username (root) and the IP.

After you've done that, switch back to that terminal and run
```bash
-ls
```
If you see your folder, you can move on the next step.

```bash
cd YOUR_FOLDER_NAME
```
Change the YOUR_FOLDER_NAME to your folder name. After you've done that, run the following to start a screen session.
```bash
screen -S DiscordAutomation
```
You can change the `DiscordAutomation` name to whatever you want, just so you can identify it easy.
Lastly, we have to run the script like we did before, to do that simply run
```bash
python main.py
```
After the bot goes online, you can leave the program you are using and it will stay online.

I know this is very simple but I did it fast as a lot of people are asking me. (Note that I do not use this main.py setup, I also use a few additonal scripts)

Congratulations on making your first discord bot, welcome to the discord development!
