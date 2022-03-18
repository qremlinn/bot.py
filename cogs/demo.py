import json
import requests
import discord
from discord.ext import commands


class Demo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Gogs demo успешно запущен!")

    @commands.command(aliases=["демо"])
    async def demo(self, ctx, arg=None):

        # Проверка на все аргументы <=============================
        if arg is None:
            await ctx.send("Что вы хотите запустить?")

        # Подключение ютуба <=====================================
        elif arg == "you" or arg == "ютуб":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 755600276941176913,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение покера <====================================
        elif arg == "pocker" or arg == "покер":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 755827207812677713,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение Betrayal.io <=====================================
        elif arg == "betra" or arg == "бетра":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 773336526917861400,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение Fishington <=====================================
        elif arg == "fishing" or arg == "рыбалка":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 814288819477020702,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение Chess in the Park <=====================================
        elif arg == "chess" or arg == "шахматы":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 832012774040141894,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение Checkers in the Park <=====================================
        elif arg == "check":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 832013003968348200,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение Doodle Crew <=====================================
        elif arg == "doodle":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 878067389634314250,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение Letter Tile <=====================================
        elif arg == "letter":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 879863686565621790,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение Word Snacks <=====================================
        elif arg == "word" or arg == "слово":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 879863976006127627,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            await ctx.send(f"https://discord.com/invite/{link['code']}")

        # Подключение SpellCast <=====================================
        elif arg == "spell":
            data = {
                "max_age": 86400,
                "max_uses": 0,
                "target_application_id": 852509694341283871,
                "target_type": 2,
                "temporary": False,
                "validate": None
            }
            headers = {
                "Authorization": "Bot OTA1NTA5OTg0MTQ0NTkyOTU3.YYLH4w.ADNDh1j8PGPUynu27eY8bM03PwE",
                "Content-Type": "application/json"
            }
            if ctx.author.voice is not None:
                if ctx.author.voice.channel is not None:
                    channel = ctx.author.voice.channel.id
                else:
                    await ctx.send("Зайди в канал")
            else:
                await ctx.send("Зайди в канал")
            channel = ctx.author.voice.channel.id
            response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites",
                                     data=json.dumps(data), headers=headers)
            link = json.loads(response.content)

            embed = discord.Embed(title="Развлечения",
                                  description=f"Эй, {ctx.author}, тебе надо нажать на ссылку "
                                              f"[<https://discord.com/invite/{link['code']}>]",
                                  color=0x9e4af2)
            embed.set_footer(text="Будет круто!")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Demo(client))
