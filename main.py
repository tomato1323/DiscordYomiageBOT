import discord
import subprocess

import re

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

def sanitize_text(text):
    text = re.sub(r'https?://\S+', 'URL省略', text)
    text = re.sub(r'[&|<>\^"%]', '', text)
    return text

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
            msg = sanitize_text(message.content)
            cmd = (f"./SeikaSay2/SeikaSay2.exe -cid {VOICE_ID} -volume {SOUNDLEVEL} -t {msg}")
            returncode = subprocess.Popen(cmd)
            print(f"{message.author} Say: {msg}")

def main():
    print("読み上げBOT起動します")
    # print(BOT_TOKEN)
    # print(CHANNEL_ID)
    print(f"話者ID: {VOICE_ID}")
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
