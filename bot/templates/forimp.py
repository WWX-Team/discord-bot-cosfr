import discord, os
from discord.ext import commands



my_secret = os.environ['bot_token']

token = os.getenv("bot_token")
bot_name = "My First Bot"
cmd_prefix = "/"
mod_role = "Mod Role Name"

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
