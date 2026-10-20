import discord
import subprocess

import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
VOICE_ID = os.getenv("VOICE_ID")
SOUNDLEVEL = os.getenv("SOUND_LEVEL")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'--- Ready to logged in ---')
    print(client.user.name)
    print(client.user.id)
    print(f'--------------------------')

@client.event
async def on_message(message):
    if not message.author.bot:
        # BOT以外の話者
        if message.channel.id == CHANNEL_ID:
            cmd = (f"./SeikaSay2/SeikaSay2.exe -cid {VOICE_ID} -volume {SOUNDLEVEL} -t {message.content}")
            returncode = subprocess.Popen(cmd)
            print(f"{message.author} Say: {message.content}")

def main():
    print("Hello from discord bot!")
    print(BOT_TOKEN)
    print(CHANNEL_ID)
    print(VOICE_ID)
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
