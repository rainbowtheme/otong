import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='!help'))
    await client.send_message(member, 'hi i am bot by @Blue Gaming#5147 ')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!buyMinecraft':
        await client.send_messagecmessage.channel,'https://minecraft.net/en-us/store/minecraft/?ref=h#register'
    if message.content == '!buyminecraft':
        await client.send_message(message.channel,'https://minecraft.net/en-us/store/minecraft/?ref=h#register')
    if message.content == '!laugh':
        em = discord.Embed(description='')
        em.set_image(url='https://media.giphy.com/media/YkkbVZma9gRKU/giphy.gif')
        await client.send_message(message.channel, embed=em)
    if message.content =='!botby':
        await client.send_message(message.channel,'@Blue Gaming#5147 ')
    if message.content == '!help':
        await client.send_message(message.channel,'bot by @Blue Gaming#5147  @everyone !buyminecraft,!laugh,!botby,!channel,!!help,!ping,!say,!test,!gen,!python3.6 @everyone Bot By @Blue Gaming#5147  ')
    if message.content =='!channel':
        await client.send_message(message.channel,'https://www.youtube.com/channel/UCmEbKBa9qC6C4cwzebG1i7w?view_as=subscriber')
    if message.content ==('!ping'):
         userID = message.author.id
         await client.send_message(message.channel,"pong")
    if message.content.upper() == '!SAY':
        args = message.content.split(" ")
        #args[0] = !SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (args[1:]))
    if message.content =='!test':
        await client.send_message(message.channel,'This a Test')
    if message.content.startswith('!gen'):
        randomlist = ['joni2509@hotmail.com:1,2,3,4,5,','jonathansayage@hotmail.com:waflly3601','sean@mpcstudios.com:clarke53','perezisaiah843@gmail.com:hectorxd27','draykor@hotmail.co.uk:goldstone32','g-kwacz@hotmail.com:Haslo987','shayshad@gmail.com:love5683','manuel_labor@comcast.net:bastardson1','aznkenshin@gmail.com:Kwee2702','ajdiaz90@msn.com:nov101990','alexkiechle@gmail.com:alexkiechle1']                                                                       
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!python3.6'):
        await client.send_message(message.channel,'https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe')
        
client.run('NDg4NTQwNDE0MDUyMTM5MDA5.Doh5dw.UWB_szdRlPAuU41QpvVu6jOa8yE')
