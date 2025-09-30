import discord
import os
import asyncio
import jishaku
from discord.ext import commands
from datetime import datetime

TOKEN = "" # Put your bot token in the quotes.

GUILD_ID = 000000000000000000 # Replace with your server ID.
APPLICATION_ID = 000000000000000000 # Replace with your bot's application ID.

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

client = commands.Bot(
    command_prefix="-", # You can change this to the prefix you want.
    intents=intents,
    application_id=APPLICATION_ID
)
client.start_time = datetime.now()

@client.event
async def on_ready():
    print(f"Bot is ready as {client.user} ({client.user.id})")

    try:
        synced = await client.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Synced {len(synced)} commands to guild {GUILD_ID}")
    except Exception as e:
        print(f"Command sync failed: {e}")

async def main():
    print("Loading extensions...")

    await client.load_extension("jishaku")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            ext = f"cogs.{filename[:-3]}"
            try:
                await client.load_extension(ext)
                print(f"Loaded: {ext}")
            except Exception as e:
                print(f"Failed to load {ext}: {e}")

    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
