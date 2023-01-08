import discord
import requests
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']
# client = discord.Client()
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.content.startswith('!uptime'):
        # Get the URL from the message
        url = message.content[7:]
        try:
            # Send a request to the URL
            response = requests.get(url)
            # Check the status code of the response
            if response.status_code == 200:
                await message.channel.send('The URL is up and running!')
            else:
                await message.channel.send('The URL is not responding.')
        except:
            await message.channel.send('There was an error checking the uptime of the URL.')

client.run(TOKEN)
