import discord
from discord.ext import commands
import valorantstats
import secretvars

ss = secretvars.secretvars()
TOKEN = OTA4NjIyNTAxNTk1MjAxNTc2.YY4apQ.9rjPG1KUbJ4bxtTw9-jQwBUT49s
GUILD = 765932359236452382
client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    game = discord.Game("!stats {username#tag}")
    await bot.change_presence(activity=game)
    for guild in bot.guilds:
        print(f'{client.user} is connected to the following guild:\n{guild.name}(id: {guild.id})\n')
        if guild.name == GUILD:
            break

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.command(name='stats')
async def stat(ctx):
    await ctx.send(embed=valorantstats.valstats(ctx))

bot.run(TOKEN)
