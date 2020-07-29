import os

import discord
import datetime
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'I am not your friend, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content == 'coinflip':
            response = 'heads' if random.randint(0, 1) == 1 else 'tails'
            await message.channel.send(response)

        if message.content == 'date':
            await message.channel.send(datetime.date.today())

        if message.content == 'time':
            await message.channel.send(datetime.datetime.now().strftime("%I:%M%p"))


client = CustomClient()
client.run(TOKEN)
