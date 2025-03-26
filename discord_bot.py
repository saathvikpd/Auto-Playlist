import os
import importlib
from discord.ext import commands
from dotenv import load_dotenv
import subprocess

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='queue')
async def queue(ctx, arg):
    subprocess.run(["python3", "app.py", arg])
    await ctx.send("{} songs added to your queue.".format(arg))
bot.run(TOKEN)
