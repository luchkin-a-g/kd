import discord
from discord.ext import commands

import random
import os

from settings import settings
from bot_logic import *

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix=settings["prefix"], intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def gen_pass(ctx, count_chars = 10):
    new_pass = gen_pass(count_chars)
    await ctx.send(new_pass)

@bot.command()
async def mem(ctx):
    new_mem = random.choice(os.listdir('images'))
    with open(f'images/{new_mem}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
    # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run(settings["TOKEN"])
