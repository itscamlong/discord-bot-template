from dotenv import load_dotenv
import discord
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    # Various connection info for console.
    print(f'{client.user.name} has connected to Discord!')
    print(f'{client.user.name} is connected to the following guild(s): \n')

    for guild in client.guilds:
        print(f'{guild.name} (id: {guild.id})')

client.run(token)