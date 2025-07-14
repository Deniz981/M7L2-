import discord
from discord.ext import commands
from bot_token import TOKEN
from logic import detect_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def detect(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            filepath = f'images/{filename}'
            await attachment.save(filepath)
            await ctx.send(f"Görsel başarıyla kaydedildi.")

            name, score = detect_class("converted_keras (1)/keras_model.h5","converted_keras (1)/labels", filepath)
            await ctx.send(f"{name} {score}")
    else: 
        await ctx.send(f"Lütfen bir görsel ekleyiniz.")

@bot.command()
async def taze(ctx):
    await ctx.send("Bu meyve/sebze tazedir. Güvenle tüketebilirsiniz.")   

@bot.command()
async def curuk(ctx):
    await ctx.send ("Bu meyve/sebze çürümüştür. Sağlığınız için tüketmemeniz ve çöpe atmanız gerekmektedir.")       
    

bot.run(TOKEN)