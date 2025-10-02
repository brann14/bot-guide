# This script is required to power your bot.
# .env is being used for security reasons and so you don't accidently leak your token.
# Make sure you install all the requirements before running the bot.
from __future__ import annotations
import asyncio
import os
import discord
import aiohttp
import jishaku
from asyncio import CancelledError, sleep, TimeoutError, wait_for
from pathlib import Path
from sys import stdout
from typing import List, Optional
from jishaku import Flags
from loguru import logger
from discord import AllowedMentions
from discord.ext.commands import Bot, Bot as NonShardedBot
from aiohttp import ClientSession
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

logger.remove()
logger.add(
    stdout,
    colorize=True,
    level="INFO",
    format="<fg #34D19D>[</fg #34D19D><fg #34D19D>{time:DD-MM-YYYY HH:MM:SS}</fg #34D19D><fg #34D19D>]</fg #34D19D> (<fg #34D19D>bot:{function}</fg #34D19D>) <fg #34D19D>@</fg #34D19D> <fg #34D19D>{message}</fg #34D19D>",
)

class App(NonShardedBot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="-",
            case_intensitive=True,
            intents=discord.Intents.all(),
            owner_ids=[1],
            help_command=None,
            activity=discord.CustomActivity(name="watching over the server", emoji=None), # You can change the status to whatever you want.
            allowed_mentions=AllowedMentions(
                everyone=True,
                users=True,
                roles=True,
                replied_user=True
            ),
            max_messages=500,
        )

        self.token = os.getenv("DISCORD_TOKEN")
        if not self.token:
            raise ValueError("No DISCORD_TOKEN found in environment or .env file")

        self.session: Optional[ClientSession] = None
        self.tasks: List[asyncio.Task] = []
        self.start_time = datetime.now()

    async def ensure_session(self):
        if self.session is None or self.session.closed:
            self.session = ClientSession()

    async def setup_hook(self) -> None:
        await self.ensure_session()
        await self.load_extensions()

    async def load_extensions(self):
        Flags.RETAIN = True
        Flags.NO_DM_TRACEBACK = True
        Flags.FORCE_PAGINATOR = True
        Flags.NO_UNDERSCORE = True
        Flags.HIDE = True

        await self.load_extension("jishaku")

        cogs_path = Path("cogs")
        if cogs_path.exists() and cogs_path.is_dir():
            for module in cogs_path.iterdir():
                if module.is_file() and module.suffix == '.py':
                    await asyncio.sleep(0.001)
                    try:
                        await wait_for(self.load_extension(f"cogs.{module.stem}"), timeout=65)
                        logger.success(f"Loaded cog: {module.stem}")
                    except TimeoutError:
                        logger.warning(f"Timed out whilst loading cog: {module.stem}")
                    except CancelledError:
                        logger.warning(f"Cancelled whilst loading cog: {module.stem}")
                    except Exception as e:
                        logger.error(f"Failed to load cog: {module.stem} // {str(e)}")
                        raise

    async def on_ready(self) -> None:
        logger.success(f"Connected to Discord as {self.user.name} ({self.user.id})")

    def run(self: App) -> None:
        try:
            super().run(self.token, reconnect=True)
        except KeyboardInterrupt:
            logger.info("Received exit signal, shutting down gracefully.")
        finally:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.graceful_shutdown())

    async def graceful_shutdown(self):
        logger.info("Understood, closing aiohttp session.")
        if self.session and not self.session.closed:
            await self.session.close()


if __name__ == "__main__": # This is the main part that actually powers your bot.
    app = App()
    app.run()
