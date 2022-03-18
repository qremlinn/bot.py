import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import sqlite3


CONNECTION = sqlite3.connect("money.db")
cursor = CONNECTION.cursor()


class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    # СОЗДАНИЕ ТАБЛИЦ ПОЛЬЗОВАТЕЛЕЙ И МАГАЗИНА ======================================================

    @commands.Cog.listener()
    async def on_ready(self):
        client = self.client
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            id_member BIGINT,
            cash BIGINT,
            rep INT,
            lvl INT
        )""")

        cursor.execute('''CREATE TABLE IF NOT EXISTS shop(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_role INT,
            cost BIGINT
        )''')

        # ДОБАВЛЕНИЕ ПОЛЬЗОВАТЕЛЕЙ ======================================================
        for guild in client.guilds:  # проходимся по нашим серверам, где находится бот
            for member in guild.members:  # проходимся по пользователям каждого сервера
                # если такого пользователя нет, то добавляем
                if cursor.execute(f'''SELECT id_member FROM users WHERE id_member = {member.id}''').fetchone() is None:
                    cursor.execute(f'''INSERT INTO 
                    users(name, id_member, cash, rep, lvl) 
                    VALUES ('{member}', {member.id}, 0, 0, 1)''')
                else:
                    pass
        CONNECTION.commit()
        print("Gogs economy успешно запущен!")

    # СОБЫТИЕ ПРИСОЕДИНЕНИЕ ПОЛЬЗОВАТЕЛЯ ======================================================
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # проверяем если пользователь в таблице, если пользователя нет, то добавляем
        if cursor.execute(f"SELECT id_member FROM users WHERE id_member = {member.id}").fetchone() is None:
            cursor.execute(f"INSERT INTO "
                           f"users(name, id_member, cash, rep, lvl) "
                           f"VALUES ('{member}', {member.id}, 0, 0, 1)")
            CONNECTION.commit()
        else:
            pass

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<РЕДАКТИРОВАНИЕ БАЛАНСА ПОЛЬЗОВАТЕЛЕЙ>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # КОМАНДА БАЛАНСА ПОЛЬЗОВАТЕЛЯ ======================================================
    @commands.command(aliases=['balance', 'cash', 'деньги', 'баланс'])
    async def money(self, ctx, member: discord.Member = None):
        # если участник не указан, то показывает баланс автора сообщения
        if member is None:
            await ctx.send(f"""Баланс пользователя {ctx.author.mention} 
составляет {cursor.execute(f'SELECT cash FROM users WHERE id_member = {ctx.author.id}').fetchone()[0]}""")
        else:
            await ctx.send(f"""Баланс пользователя {member.mention} 
составляет {cursor.execute(f'SELECT cash FROM users WHERE id_member = {member.id}').fetchone()[0]}""")

    # КОМАНДА ДОБАВЛЕНИЯ ПОЛЬЗОВАТЕЛЮ ДЕНЕГ======================================================
    @commands.command(aliases=['addmoney'])
    @commands.has_permissions(administrator=True)  # если нет прав админа, то команда не сработает
    async def add_money(self, ctx, member: discord.Member = None, amount: int = 100):
        if member == None:
            await ctx.send(f"{ctx.author}, тэгни пользователя!")
        else:
            if amount < 0:
                await ctx.send(f"Без отрицательных чисел")
            else:
                cursor.execute(f'''UPDATE users SET cash=cash + {amount} WHERE id_member={member.id}''')
                CONNECTION.commit()
                await self.client.get_channel(867014823433863169).send(f'Админ {ctx.author.mention}, добавил '
                                                                       f'пользователю {member.mention} {amount} валюты')

    # КОМАНДА ОТНЯТЬ ПОЛЬЗОВАТЕЛЮ ДЕНЬГИ ======================================================
    @commands.command(aliases=['takemoney'])
    @commands.has_permissions(administrator=True)
    async def take_money(self, ctx, member: discord.Member = None, amount=None):
        if member is None:
            await ctx.send(f"{ctx.author}, тэгни пользователя!")
        elif amount == "all":
            cursor.execute(f'''UPDATE users SET cash={0} WHERE id_member={member.id}''')
            CONNECTION.commit()
            await self.client.get_channel(867014823433863169).send(f'Админ {ctx.author.mention}, обнулил баланс '
                                                                   f'пользователю {member.mention}')
        else:
            if int(amount) < 0:
                await ctx.send(f"Без отрицательных чисел")
            else:
                if cursor.execute(f'SELECT cash FROM users WHERE id_member={member.id} AND cash-{amount} > 0') is True:
                    cursor.execute(f'''UPDATE users SET cash=cash - {amount} WHERE id_member={member.id}''')
                    CONNECTION.commit()
                    await self.client.get_channel(867014823433863169).send(f'Админ {ctx.author.mention}, отнял '
                                                                           f'пользователю {member.mention} '
                                                                           f'{amount} валюты')
                else:
                    await ctx.send("У него столько нету")

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< МАГАЗИН >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    @commands.command(aliases=['addrole'])
    @commands.has_permissions(administrator=True)
    async def add_role(self, ctx, role: discord.Role = None, cost: int = None):
        if role is None:  # применяю is потому что cost уже равно None и pep8 ругается
            await ctx.send(f'{ctx.author.mention}, укажите сначала айди роли!')
        else:
            if cost is None:
                await ctx.send(f'{ctx.author.mention}, укажите стоймость!')
            elif cost < 0:
                await ctx.send(f'{ctx.author.mention}, стоймость роли не может быть отрицательной!')
            else:
                cursor.execute(f'''INSERT INTO shop(id_role, cost) VALUES ({role.id}, {cost})''')
                CONNECTION.commit()
                await ctx.send(f'Роль добавлена!')

    @commands.command(aliases=['removerole'])
    @commands.has_permissions(administrator=True)
    async def remove_role(self, ctx, role: discord.Role = None, amount=None):
        if role is None:
            await ctx.send(f"{ctx.author.mention}, ты не ввел роль!")
        elif cursor.execute(f"SELECT id_role FROM shop WHERE id_role = {role.id}").fetchone() is None:
            await ctx.send(f"{ctx.author.mention}, такой роли нету в магазине!")
        else:
            if amount == "all":
                cursor.execute('''DELETE FROM shop''')
                CONNECTION.commit()
                await ctx.send(f'{ctx.author.mention}, вы удалили все роли из магазина!')
            else:
                cursor.execute(f'''DELETE FROM shop WHERE id_role = {role.id}''')
                CONNECTION.commit()
                await ctx.send(f'{ctx.author.mention}, вы удалили роль <@{role.id}>')

    @commands.command(aliases=['магазин'])
    async def shop(self, ctx):
        embed = discord.Embed(title="Магазин ролей")
        for row in cursor.execute('''SELECT id_role, cost FROM shop'''):
            if ctx.guild.get_role(row[0]) != None:
                embed.add_field(
                    name=f'Стоймость {row[1]}',
                    value=f'{ctx.guild.get_role(row[0]).mention}',
                    inline=False
                )
        await ctx.send(embed=embed)

    @commands.command(aliases=['купить'])
    async def buy(self, ctx, role: discord.Role = None):
        if role is None:
            await ctx.send(f'{ctx.author.mention}, укажите роль!')
        else:
            if role in ctx.author.roles:
                await ctx.send(f'{ctx.author.mention},у вас уже есть такая роль!')
            elif cursor.execute(f'''SELECT cost FROM shop WHERE id_role = {role.id}''').fetchone()[0] > cursor.execute(f'''SELECT cash FROM users WHERE id_member = {ctx.author.id}''').fetchone()[0]:
                await ctx.send(f'У вас недостаточно средств!')
            else:
                cursor.execute(f'''UPDATE users SET cash = cash - 
{cursor.execute(f'SELECT cost FROM shop WHERE id_role = {role.id}').fetchone()[0]} WHERE id_member={ctx.author.id}''')
                await ctx.author.add_roles(role)
                await ctx.send(f"{ctx.author.mention}, вы успешно купили роль {ctx.guild.get_role(role).mention}")

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ОБРАБОТКИ ОШИБОК >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # ОБРАБОТКА ОШИБКИ ДОБАВЛЕНИЕ ДЕНЕГ======================================================
    @add_money.error
    async def add_money_error(self, message, error):
        if isinstance(error, MissingPermissions):
            await message.send("Ты не обладаешь правами добавлять деньги!")

    # ОБРАБОТКА ОШИБКИ ДОБАВЛЕНИЕ РОЛИ=================================
    @add_role.error
    async def add_role_error(self, message, error):
        if isinstance(error, MissingPermissions):
            await message.send("Ты не обладаешь правами добавлять роли!")

    # ОБРАБОТКА ОШИБКИ ОТНЯТЬ ДЕНЬГИ======================================================
    @take_money.error
    async def take_money_error(self, message, error):
        if isinstance(error, MissingPermissions):
            await message.send("Ты не обладаешь правами отнимать деньги!")


# ЗАПУС КОГА ===========================
def setup(client):
    client.add_cog(Economy(client))
