import discord
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix="!")

targetList = []  # Muted List
userList = []
bypassList = ['141735448052498433', '562838169452544014']  # Owner ID, Bot ID, testing purposes


@client.event
async def on_ready():
    print('Bot is connected to the client and is ready to run!')
    print(client.user.name) 


@client.event
async def on_message(message):

    """
    Get all server members / Initial setup stuff
    """
    contents = message.content.split(" ")
    print(contents, " --- ", message.author.name)

    """
    !members command - List all members in the server 
    """

    if message.content.startswith('!getMembers'):
        x = message.server.members
        for members in x:
            await client.send_message(message.channel, members)

    """ 
    Target Muting - !Tmute / !unmute (playernamehere) 
    """

    if message.author.name in targetList:  # or message.author.id == '125774331837022208':
        try:
            print(message)
            await client.delete_message(message)
            await client.send_message(message.channel, message.author.name + " has been silenced. To unmute, a "
                                                                             "moderator should type"
                                                                            " !unmute (" + message.author.name + ")")

        except discord.errors.NotFound:
            return

    if message.content.startswith("!Tmute"):
        targetList.append(contents[1])
        print(targetList)

    if message.content.startswith("!unmute"):
        try:
            targetList.remove(contents[1])
            print(contents[1], " has been unmuted")
        except ValueError:
            return

client.run("API KEY HIDDEN")
