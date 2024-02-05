import os
import random
import asyncio
from twitchio.ext import commands

# Definir as credenciais do bot
bot = commands.Bot(
    irc_token='your_oauth_token',  # Substitua 'your_oauth_token' pelo seu token
    client_id='your_client_id',          # Substitua 'your_client_id' pelo seu ID de cliente
    nick='your_bot_username',            # Substitua 'your_bot_username' pelo nome de usuário do seu bot
    prefix='!',
    initial_channels=['your_channel']    # Substitua 'your_channel' pelo canal que o bot deve se juntar
)

# Evento executado quando o bot se conecta ao canal
@bot.event
async def event_ready():
    print(f"{bot.nick} está online!")
    # Loop para manter o bot ativo com comportamento variável
    while True:
        await asyncio.sleep(random.randint(300, 600))  # Espera um tempo aleatório entre 5 e 10 minutos
        await bot.get_channel('your_channel').send(random.choice(['Salveeee', 'Como está o chat hoje?', 'koeeeee']))

# Comando de exemplo para responder no chat com variação
@bot.command(name='hello')
async def hello_command(ctx):
    await ctx.send(random.choice([f"Olá, {ctx.author.name}!", f"Oi, {ctx.author.name}, como vai?", f"Hey, {ctx.author.name}, tudo bem?"]))

# Iniciar o bot
bot.run()
