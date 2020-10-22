import discord

class TerraneticHelper(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = TerraneticHelper()
with open("token.txt", "r") as token:
    client.run(token.readline())
