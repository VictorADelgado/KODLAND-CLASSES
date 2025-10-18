import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot=commands.Bot(command_prefix="!",intents=intents)
@bot.event
async def onready():
    print(f"Connected as {bot.user}")
@bot.command()
async def hello(ctx):
    await ctx.send("Hi! I'm your ecollogic bot :seedling:")
@bot.command()
async def recycle(ctx,objeto:str):
    clasificacion = {
        "botella": "♻️ Va al contenedor de PLÁSTICO.",
        "papel": "📄 Va al contenedor de PAPEL.",
        "cáscara": "🍌 Va al contenedor ORGÁNICO.",
        "pilas": "⚠️ Las PILAS deben ir a un punto especial de reciclaje."
    }
    respuesta = clasificacion.get(objeto.lower(),"No se donde va ese objeto")
    await ctx.send(respuesta)
@bot.command()
async def time(ctx, objeto:str):
    degradacion = {
        "botella": "🍼 Una botella de plástico tarda ¡450 años! en degradarse 😱",
        "papel": "📄 El papel tarda unos 2 a 6 meses.",
        "cáscara": "🍌 Una cáscara tarda solo unas semanas.",
        "pilas": "⚠️ Las pilas pueden tardar ¡1000 años! y además contaminan el suelo."
    }
    respuesta = degradacion.get(objeto.lower(), "No sé cuanto puede durar en el ambiente")
    await ctx.send(respuesta)

bot.run(TOKEN)