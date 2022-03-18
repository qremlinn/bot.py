from discord.ext import commands


class User(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Gogs main успешно запущен!")

    # команды на инфо
    @commands.command(aliases=["инфо"])
    async def info(self, ctx, arg=None):

        if None == arg:
            await ctx.send("Введи команды:\n"
                           "!info gen   |   (общая информация о сервере)\n"
                           "!info admin |   (информация о администрации)\n"
                           "!info rules |   (информация о правилах)")

        elif arg == "gen":
            await ctx.send("тут будет инфа о сервере")

        elif arg == "rules":
            await ctx.send("тут будут правила")

        elif arg == "admin":
            await ctx.send("тут будет инфо о администрации")

        else:
            await ctx.send("такой команды нет")

    # реакция на подключения
    @commands.Cog.listener()
    async def on_member_join(self, member):

        guild = member.guild
        await member.send(f"Приветствую {member.mention}, на сервере {guild}.\n"
                          f"Чтобы узнать о нашем сервере пропиши команду `!info`")


def setup(client):
    client.add_cog(User(client))
