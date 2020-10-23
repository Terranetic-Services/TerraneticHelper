import discord


class TerraneticHelper(discord.Client):

    def __init__(self, **options):
        super().__init__(**options)
        self.prefix = "!"
        self.channel = "bot-commands"
        self.profiles = {"craftablescience#6001": {"github": "git link", "timezone": "EST"},
                            "SebaSphere#0001": {"github": "git link", "timezone": "EST"}}

    def get_response(self, message, author):
        cmd = message.strip().split(" ")
        embed: discord.Embed = discord.Embed()
        embed.colour = 0x0000FF

        if len(cmd) > 0:
            cmd = cmd[0]

            if cmd == "seba":
                embed.title = "SEBA"
                embed.description = "Founder of Terranetic."
                embed.set_thumbnail(url="https://avatars0.githubusercontent.com/u/27737877?s=460&u=031ce51836265b5a24e446e7c4ff1aba9b68f36f&v=4")
                return embed
            elif cmd == "craft":
                embed.title = "CRAFTABLESCIENCE"
                embed.description = "Good at math, friend of SebaSphere."
                embed.set_thumbnail(url="https://avatars2.githubusercontent.com/u/26600014?s=460&u=7aae6b83e49784c397e038d8987ebd183f93c863&v=4")
                return embed
            elif cmd == "profile":
                if author in self.profiles.keys():
                    embed.title = author
                    embed.description = "botom text\n\n**Timezone:** " + self.profiles[author]["timezone"]
                    return embed
                else:
                    embed.title = "ERROR"
                    embed.description = "You must be a developer to use this command."
                    return embed
            elif cmd == "help":
                if len(message.split(" ")) > 1:
                    if message.split(" ")[1] == "-c":
                        embed.title = "HELP -> COMMANDS"
                        embed.description = self.prefix + "seba :: Prints a message about SebaSphere.\n" + \
                                            self.prefix + "craft :: Prints a message about craftablescience\n" + \
                                            self.prefix + "help :: Get help with using the bot.\n" + \
                                            self.prefix + "help -c :: Prints a list of bot commands." + \
                                            self.prefix + "profile :: Prints your developer profile."
                        return embed
                else:
                    embed.title = "HELP"
                    embed.description = "To see a list of commands, type \"" + \
                                        self.prefix + "help -c\" without quotes.\nMore to come soon!"
                    return embed

        embed.title = "ERROR"
        embed.description = "Not recognized! Type " + self.prefix + "help for help."
        return embed

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        if len(message.content) > 0 and message.content[0:1] == self.prefix and str(message.channel) == self.channel:
            await message.channel.send(embed=self.get_response(str(message.content[1:]), str(message.author)))

client = TerraneticHelper()
with open("token.txt", "r") as token:
    client.run(token.readline())
