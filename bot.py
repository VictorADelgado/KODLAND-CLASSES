import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
def gen_pass(length):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789_$#&@*+-¿¡?!"
    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password
bot = commands.Bot(command_prefix="!",intents=intents)
@bot.event
async def on_ready():
    print(f"hemos iniciado sesión como {bot.user}")
@bot.command()
async def hello(ctx):
    await ctx.send("Hola")
@bot.command()
async def password(ctx,lenght:int):
    await ctx.send(gen_pass(lenght))
bot.run("MTQxNjI0NDExMDkwNTU3MzQ2OA.GWTIbs.DeDqiBrRVQFn6QsOQjPwhQQPBCiaBT7TtSSL-M")
