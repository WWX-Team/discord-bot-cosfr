import discord, os
from discord.ext import commands


token = os.getenv("1240754119669579797")
bot_name = "scratch portal"
cmd_prefix = "/"

client = commands.Bot(command_prefix = cmd_prefix, intents = discord.Intents.all())


"""

Fonctions et classes rimitives pouvant être utilisées par le bot.

"""

class user:

  def __init__(id : int):
    self.id = id
    # https://discord.com/api/v9/users/
    # https://stackoverflow.com/questions/64933979/discord-get-user-by-id

def cmd_vérifier(utilisateur)
