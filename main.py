import discord
from discord import app_commands
import os
from dotenv import load_dotenv
import aiohttp
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

@tree.command(
    name="copy",
    description="Copies all messages in a channel",
)
async def copy(interaction, channel1:str, channel2:str):
    channel1 = client.get_channel(int(channel1))
    channel2 = client.get_channel(int(channel2))
    await interaction.response.send_message("Copying images..")
    async for msg in channel1.history(limit=None):
        if msg.author == interaction.user:
            if msg.attachments:
                for atch in msg.attachments:
                    url = atch.url
                    print(url)
                    if url[0:26] == 'https://cdn.discordapp.com':
                        await channel2.send(url)
            if msg.content[0:26] == 'https://cdn.discordapp.com':
                print(msg.content + "2")
                await channel2.send(msg.content)

client.run(os.getenv('TOKEN'))