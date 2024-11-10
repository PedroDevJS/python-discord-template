import discord
from discord.ext import commands
import os
from discord import app_commands
import dotenv

dotenv.load_dotenv()

guild_id = 1303751446130462740

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

# for synchronizing slash commands
synced = False

# function to load cogs
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Cog {filename} read!')
            except Exception as e:
                print(f'error to load cog {filename}: {e}')

@bot.event
async def on_ready():
    global synced
    print(f'Logged in as {bot.user}')

    await load_cogs()

    if not synced:
        await bot.tree.sync(guild=discord.Object(id=guild_id))
        synced = True
        print("Comandos sincronizados com sucesso para a guilda específica.")
    
    for command in bot.tree.get_commands():
        print(f'Comando registrado: {command.name}')

bot.run(TOKEN)
