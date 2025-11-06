import discord
from discord import app_commands
from datetime import datetime, timedelta
import requests
import json
import asyncio

token = 'your token'

cooldowns = {}

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
        self.synced = False

    async def setup_hook(self):
        if not self.synced:
            await self.tree.sync()
            self.synced = True

client = MyClient()

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    
@client.tree.command(name="tfollow", description="[TWITCH] send twitch followers to anyone")
@app_commands.describe(username="The username to send followers to")
async def tfollow(interaction: discord.Interaction, username: str):
    user_id = interaction.user.id
    current_time = datetime.utcnow()
    
    if user_id in cooldowns:
        cooldown_time = cooldowns[user_id]
        if current_time < cooldown_time:
            remaining = cooldown_time - current_time
            await interaction.response.send_message(
                f"Please wait {remaining.seconds} seconds before using this command again.",
                ephemeral=True
            )
            return
    
    cooldowns[user_id] = current_time + timedelta(minutes=1)
    
    await interaction.response.send_message(
        f"Sending 100 followers to {username}",
        ephemeral=True
    )
    
    url = 'https://q9tx.com/send-followers'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://q9tx.com",
        "Referer": "https://q9tx.com/follow.html",
        "Sec-CH-UA": '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"
    }
    
    payload = {"username": username}
    
    try:
        response = requests.post(url, headers=headers, json=payload)
    except Exception as e:
        print(f"Error making request: {e}")

if __name__ == "__main__":
    client.run(token)