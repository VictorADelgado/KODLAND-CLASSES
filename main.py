import discord
from discord.ext import commands
import os,random,requests,io
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "$",intents=intents)
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f"images/{img_name}","rb") as archivo:#read binary
        picture = discord.File(archivo)
        await ctx.send(file=picture)
def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url).json()
    image_url = res["url"]
    image_data = requests.get(image_url).content
    file = discord.File(io.BytesIO(image_data),filename="duck.jpg")
    return file
@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(file=image_url)
@bot.command()
async def help(ctx):
    help_text = """
    Comandos disponibles:
    $meme - Envía un meme aleatorio.
    $duck - Envía una imagen aleatoria de un pato.
    $help - Muestra este mensaje de ayuda.
    """
    await ctx.send(help_text)
@bot.command()
async def keyword(ctx,keyword:str):
    words_list = {
        "economy":"stonks",
        "peep-peep":"my honest reaction: ._.",
        "why":"what can i say except you're welcome",
    }
    
bot.run(TOKEN)