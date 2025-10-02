# This is just a simple template cog.
# You can keep it, change it, delete it or whatever you want to do with it.
# The commands I made are meant to show you how to make a slash and a prefix command.
import discord
from discord.ext import commands
from discord import app_commands

GUILD_ID = 000000000000000000 # Replace with your server ID.

class CommandsCog(commands.Cog):
    def __init__(self, commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="hello", description="Greet the bot.") # You can change the command to whatever you want.
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Greetings, {interaction.user.mention}!")

    @commands.command(name="hello") # You can change the command to whatever you want.
    async def hello_prefix(self, ctx):
        await ctx.send(f"Greetings, {ctx.author.mention}!")

async def setup(bot: commands.Bot):
    cog = CommandsCog(bot)
    await bot.add_cog(cog)
    await bot.tree.sync(guild=discord.Object(id=GUILD_ID))

