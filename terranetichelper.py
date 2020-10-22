import discord


class TerraneticHelper(discord.Client):

    def __init__(self, **options):
        super().__init__(**options)
        self.prefix = "!"
        self.channel = "bot-commands"

    def get_response(self, message, author):
        cmd = message.split(" ")
        if len(cmd) > 0:
            cmd = cmd[0]

            if cmd == "seba":
                return "mines dimens"
            elif cmd == "craft":
                return "cool guy"
            elif cmd == "help":
                return "no. youre on your own"
            elif cmd == "laugh":
                return "haha"
        return "Not recognized! Type " + self.prefix + "help for help."

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        if len(message.content) > 0 and message.content[0:1] == self.prefix and str(message.channel) == self.channel:
            await message.channel.send(self.get_response(str(message.content[1:]), str(message.author)))

client = TerraneticHelper()
with open("token.txt", "r") as token:
    client.run(token.readline())
