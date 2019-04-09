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
    await client.change_presence(game=discord.Game(name='Moderation Party 3!'))
    print(client.user.name)


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    print("running....")
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)


@client.event
async def on_message(message):
    """
    !getMembers command - List all members in the server
    """

    if message.content.startswith('!getMembers'):
        x = message.server.members
        for members in x:
            await client.send_message(message.channel, members)

    """ 
    Target Muting - !mute / !unmute (playernamehere) 
    """

    if message.content.startswith("!unmute"):
        contents = message.content.split(" ")
        try:
            targetList.remove(contents[1])
            print(contents[1], " has been unmuted")
        except ValueError:
            return

    if message.content.startswith("!mute"):
        contents = message.content.split(" ")
        targetList.append(contents[1])
        print(targetList)

    if message.author.name in targetList: # or message.author.id == '125774331837022208':
        try:
            print(message)
            await client.delete_message(message)
            await client.send_message(message.channel, message.author.name + " has been silenced. To unmute, a "
                                                                             "moderator should type"
                                                                            " !unmute (" + message.author.name + ")")

        except discord.errors.NotFound:
            return



client.run("API KEY HIDDEN") 
