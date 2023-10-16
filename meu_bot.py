
import discord
import os 

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor sao:{os.linesep}1- Nao desrespeitar os membros{os.linesep}2- Nao Feedar e Tiltar{os.linesep}3- Se divertir')
        elif message.content == '?nivel':
            await message.author.send('Nivel 1')


async def on_member_join(self, member):
    guild = member.guild
    if guild.system_channel is not None:
        mensagem = f'{member.mention} Acabou de entrar no {guild.name}'
        await guild.system_channel.send(mensagem)

client = MyClient(intents=intents)
client.run('Seu Token Aqui !')