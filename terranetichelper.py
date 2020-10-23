import discord


class TerraneticHelper(discord.Client):

    def __init__(self, **options):
        super().__init__(**options)
        self.prefix = "!"
        self.channel = "bot-commands"
        self.profiles = {
            "craftablescience#6001": {
                "portfolio": "git link",
                "timezone": "EST",
                "ticketcount": 1,
                "thumbnail": "https://avatars2.githubusercontent.com/u/26600014?s=460&u=7aae6b83e49784c397e038d8987ebd183f93c863&v=4"},
            "SebaSphere#0001": {
                "portfolio": "git link",
                "timezone": "EST",
                "ticketcount": 1,
                "thumbnail": "https://avatars0.githubusercontent.com/u/27737877?s=460&u=031ce51836265b5a24e446e7c4ff1aba9b68f36f&v=4"
            }
        }

    def get_response(self, message, author):
        cmd = message.strip().split(" ")
        embed: discord.Embed = discord.Embed()
        embed.colour = 0x0000FF

        if len(cmd) > 0:
            cmd = cmd[0]

            if cmd == "profile":
                if len(message.split(" ")) > 1:
                    if message.split(" ")[1] == "-m":
                        if author in self.profiles.keys():
                            embed.title = author
                            embed.description = "**Portfolio:** " + self.profiles[author]["portfolio"] + \
                                                "\n\n**Timezone:** " + self.profiles[author]["timezone"] + \
                                                "\n\n**Tickets Dealt With:** " + str(self.profiles[author]["ticketcount"])
                            embed.set_thumbnail(url=self.profiles[author]["thumbnail"])
                            return embed
                        else:
                            embed.title = "ERROR"
                            embed.description = "Must have a developer profile to use this command."
                            return embed
                    elif message.split(" ")[1] == "-e":
                        if not len(message.split(" ")) > 3:
                            embed.title = "ERROR"
                            embed.description = "Must provide an argument to this command. Check " + self.prefix + "help for options."
                            return embed
                        if message.split(" ")[2] == "-t":
                            self.profiles[author]["timezone"] = message.split(" ")[3]
                            embed.title = "PROFILE -> " + author + " -> TIMEZONE"
                            embed.description = "Updated to " + self.profiles[author]["timezone"] + " successfully."
                            return embed
                        elif message.split(" ")[2] == "-l":
                            self.profiles[author]["portfolio"] = message.split(" ")[3]
                            embed.title = "PROFILE -> " + author + " -> PORTFOLIO"
                            embed.description = "Updated to " + self.profiles[author]["portfolio"] + " successfully."
                            return embed
                else:
                    embed.title = "ERROR"
                    embed.description = "Must provide an argument to this command. Check " + self.prefix + "help for options."
                    return embed
            elif cmd == "help":
                if len(message.split(" ")) > 1:
                    if message.split(" ")[1] == "-c":
                        embed.title = "HELP -> COMMANDS"
                        embed.description = self.prefix + "help :: Get help with using the bot.\n" + \
                                            self.prefix + "help -c :: Prints a list of bot commands.\n" + \
                                            self.prefix + "profile -m :: Prints the message author's profile.\n" + \
                                            self.prefix + "profile -e -t TIME_ZONE_HERE :: Edit your profile's time zone.\n" + \
                                            self.prefix + "profile -e -l LINK_HERE :: Edit your profile's portfolio link."
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
