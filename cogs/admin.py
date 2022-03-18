import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Gogs admin успешно запущен!")

    # КОМАНДА ЧИСТКА ===================================================
    @commands.command(aliases=["чистка"], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount + 1)
        # EMBED ==================
        emb = discord.Embed()
        emb.add_field(name="Чистка", value=f"Удалено {amount} сообщений", inline=False)
        await ctx.send(embed=emb)

    # КОМАНДА КИК ======================================================
    @commands.command(aliases=["кик"])
    @commands.has_any_role(906492061438599188)
    @commands.cooldown(rate=2, per=10000)
    async def kick(self, ctx, kick_member: discord.Member, *, reason):
        client = self.client
        # ПРОВЕРКИ =========================
        if ctx.author == kick_member:
            await ctx.send("мы против самоубийств")
            return

        # ПИШЕТ EMBED В ЛС ==================
        embed1 = discord.Embed(title="Kick",
                               description=f"Тебя на кикнул админ {ctx.author.mention} на \
                               сервере _{kick_member.guild}_ по причине `{reason}`",
                               color=0xe30d0d)
        embed1.set_footer(text="Чтобы обжаловать напиши ...")

        # САМ КИК ===========================
        await kick_member.send(embed=embed1)

        # КИКАЕТ И ПИШЕТ СООБЩЕНИЕ О КИКЕ ============
        await kick_member.kick(reason=reason)
        await client.get_channel(867014823433863169).send(f"{ctx.author.mention} кикнул {kick_member.mention} по"
                                                          f" причине `{reason}`")

    # КОМАНДА БАН ======================================================
    @commands.command(aliases=["бан"])
    @commands.has_any_role(906492061438599188)
    @commands.cooldown(rate=2, per=10000)
    async def ban(self, ctx, ban_member: discord.Member, *, reason):
        client = self.client
        # ПРОВЕРКИ =========================
        if ctx.author == ban_member:
            await ctx.send("мы против самоубийств")
            return

        # ПИШЕТ EMBED В ЛС ==================
        embed1 = discord.Embed(title="Kick",
                               description=f"Тебя на кикнул админ {ctx.author.mention} на \
                                           сервере _{ban_member.guild}_ по причине `{reason}`",
                               color=0xe30d0d)
        embed1.set_footer(text="Чтобы обжаловать напиши ...")

        # БАНИТ И ПИШЕТ СООБЩЕНИЕ О БАНЕ ============
        await ban_member.ban(reason=reason)
        await client.get_channel(867014823433863169).send(f"{ctx.author.mention} забанил {ban_member.mention} по"
                                                          f" причине `{reason}`")

    # ВЫВОД ОШИБОК =====================================================
    @clear.error
    async def clear_error(self, message, error):
        if isinstance(error, MissingPermissions):
            await message.send("Ты не обладаешь правами чистить!")
        if isinstance(error, commands.MissingRequiredArgument):
            await message.send("Ты не ввел все аргументы!")

    @kick.error
    async def kick_error(self, message, error):
        if isinstance(error, commands.MissingAnyRole):
            await message.send("Ты не обладаешь правами кикать!")
        if isinstance(error, commands.MissingRequiredArgument):
            await message.send("Ты не ввел все аргументы!")

    @ban.error
    async def ban_error(self, message, error):
        if isinstance(error, commands.MissingAnyRole):
            await message.send("Ты не обладаешь правами банить!")
        if isinstance(error, commands.MissingRequiredArgument):
            await message.send("Ты не ввел все аргументы!")


# ЗАПУСК КОГА ======================================================
def setup(client):
    client.add_cog(Admin(client))
