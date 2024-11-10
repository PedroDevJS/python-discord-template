import discord
from discord.ext import commands
from discord import app_commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="A simple command that returns Pong!")
    @app_commands.guilds(discord.Object(id="1303751446130462740"))
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message('Pong!')
0
async def setup(bot):
    await bot.add_cog(PingCommand(bot))
