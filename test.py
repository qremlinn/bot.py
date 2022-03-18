import discord
from discord.ext import commands

from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Gogs admin успешно запущен!")

# КОМАНДА ЧИСТКА ===================================================
@client.command(aliases=["чистка"], pass_context=True)
@has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount + 1)

# КОМАНДА КИК ======================================================
@client.command(aliases=["кик"])
@commands.has_any_role(906492061438599188)
@commands.cooldown(rate=2, per=10000)
async def kick(ctx, kick_member: discord.Member, *, reason=None):
    await kick_member.send(f"Тебя кикнул {ctx.author} по причине {reason}.\n"
                           f"Чтобы это обжаловать напиши ")
    await kick_member.kick(reason=reason)
    await ctx.send(f"{ctx.author.mention} кикнул {kick_member.mention} по причине `{reason}`")

# КОМАНДА БАН ======================================================
@client.command(aliases=["бан"])
@commands.has_any_role(906492061438599188)
@commands.cooldown(rate=2, per=10000)
async def ban(ctx, ban_member: discord.Member, *, reason=None):
    await ban_member.send(f"Тебя забанил {ctx.author} по причине {reason}.\n"
                          f"Чтобы это обжаловать напиши ")
    await ban_member.ban(reason=reason)
    await ctx.send(f"{ctx.author.mention} кикнул {ban_member.mention} по причине `{reason}`")

# ВЫВОД ОШИБОК =====================================================
@ban.error
async def ban_error(message, error):
    if isinstance(error, MissingPermissions):
        await message.send("Ты не обладаешь правами банить!")

@kick.error
async def ban_error(message, error):
    if isinstance(error, MissingPermissions):
        await message.send("Ты не обладаешь правами банить!")


token = open("E:\\Project\\bot_discord\\server\\token.txt", "r").readline()
client.run(token)