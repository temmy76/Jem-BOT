import re
import discord
from discord.ext import commands
import asyncio
import os
import typing
import random

from keep_alive import keep_alive
from math import ceil

token = os.environ["token"]

client = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)


def convert_to_int(target_honor: str):
    if "," in target_honor:
        target_honor = target_honor.replace(",", ".")
    if target_honor[-1] == "b" or target_honor[-1] == "B":
        target_honor = float(target_honor[:-1]) * 1000000000
    elif target_honor[-1] == "m" or target_honor[-1] == "M":
        target_honor = float(target_honor[:-1]) * 1000000
    elif target_honor[-1] == "k" or target_honor[-1] == "K":
        target_honor = float(target_honor[:-1]) * 1000
    else:
        target_honor = float(target_honor)
    return int(target_honor)


@client.event
async def on_ready():
    print("Success: Bot is Connected to Discord")


@client.command(name="sync", description="Syncing")
async def sync(ctx):
    if ctx.author.id != 370753654644277258:
        await ctx.send("You are not allowed to use this command")
        return
    await ctx.send("Syncing...")
    await client.tree.sync()
    await ctx.send("Synced!")


@client.hybrid_command(name="meathonor", description="ngitung meat")
async def meat_honor(ctx, honor: str):
    embed = discord.Embed(title="Jem-BOT")
    honor = convert_to_int(honor)

    HONOR_MEAT = 80000

    kill_mob = ceil(honor / HONOR_MEAT)

    meat = 0
    while kill_mob > 0:
        meat += random.randint(5, 10)
        kill_mob -= 1

    embed.add_field(
        name="Calculate meat from honor",
        value="{:,} honors approximately get {:,} meats".format(honor, meat),
        inline=True,
    )
    await ctx.reply(embed=embed, mention_author=False)


@client.command()
async def ping(ctx):
    await ctx.reply(f"Pong! {round(client.latency * 1000)} ms", mention_author=False)


@client.tree.command(name="hello", description="Say Hello")
async def introduce(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Hello <@{name}>".format(name=interaction.user.id)
    )


@client.hybrid_command(name="meat", description="ngitung meat")
async def meat(ctx, value: str):
    embed = discord.Embed(title="Jem-BOT")
    try:
        pattern = r"^\d+(?:[bmkBKM])?$"
        if not re.match(pattern, value):
            raise ValueError("True")
        meat = convert_to_int(value)
        if meat < 5:
            raise ValueError("False")
        nm90 = meat // 5
        nm95 = meat // 10
        nm100 = meat // 20
        nm150 = meat // 20
        nm200 = meat // 30
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/828790440240087052/1062699739147141160/image.png"
        )
        embed.add_field(
            name="Meat Calculator ▫️ {:,} meats".format(meat),
            value="**{:}** NM90 or **{:,}** honors\n**{:,}** NM95 or **{:,}** honors\n**{:,}** NM100 or **{:,}** honors\n**{:,}** NM150 or **{:,}** honors\n**{:,}** NM200 or **{:,}** honors\n".format(
                nm90,
                nm90 * 260000,
                nm95,
                nm95 * 910000,
                nm100,
                nm100 * 2650000,
                nm150,
                nm150 * 4100000,
                nm200,
                nm200 * 10200000,
            ),
            inline=False,
        )
        await ctx.reply(embed=embed, mention_author=False)
    except ValueError as ve:
        if str(ve) == "True":
            await ctx.reply(
                "https://media.discordapp.net/attachments/908974505773396021/1062868409936785509/FB_IMG_1673465472297.jpg?width=456&height=480",
                mention_author=False,
            )
        else:
            await ctx.reply(
                "minimal mikir kontol, minimal 5 meat", mention_author=False
            )


# @client.tree.command(name="ppkm", description="ngitung honor berdasarkan ppkm")
@client.hybrid_command(name="ppkm", description="ngitung honor berdasarkan ppkm")
async def ppkm(
    ctx,
    target_honor: str,
    NM: typing.Optional[str] = "150",
    day1: typing.Optional[str] = "50m",
    day2: typing.Optional[str] = "100m",
    day3: typing.Optional[str] = "150m",
):
    temp_target_honor = convert_to_int(target_honor)
    target_honor = int(temp_target_honor) / 1000
    if target_honor * 1000 < convert_to_int("1b"):
        await ctx.reply(
            "Target honor minimal 1B", mention_author=False,
        )
        await ctx.send("https://media.discordapp.net/attachments/627855503921512487/927122622746087434/unknown.png")
        return
    HONOR_PRELIM = 30000
    HONOR_D1 = int(convert_to_int(day1) / 1000)
    HONOR_D2 = int(convert_to_int(day2) / 1000)
    HONOR_D3 = int(convert_to_int(day3) / 1000)
    honor_d4 = 150000

    meat95 = 10
    meat150 = 20
    meat200 = 30

    honor95 = 910
    honor150 = 4100
    honor200 = 10200

    if NM == "150":
        DAY1 = ceil(HONOR_D1 / honor95) * meat95
        DAY2 = ceil(HONOR_D2 / honor150) * meat150
        DAY3 = ceil(HONOR_D3 / honor150) * meat150
        day4 = ceil(honor_d4 / honor150) * meat150
    elif NM == "200":
        DAY1 = ceil(HONOR_D1 / honor95) * meat95
        DAY2 = ceil(HONOR_D2 / honor150) * meat150
        DAY3 = ceil(HONOR_D3 / honor200) * meat200
        day4 = ceil(honor_d4 / honor200) * meat200

    meat_track_init = DAY1 + DAY2 + DAY3 + day4

    meat_interlud_init = meat_track_init - 3000

    honor_interlud_init = meat_interlud_init * 10
    honor_total_init = (
        honor_interlud_init + HONOR_PRELIM + HONOR_D1 + HONOR_D2 + HONOR_D3 + honor_d4
    )

    honorgain = honor150 if NM == "150" else honor200
    meatgain = meat150 if NM == "150" else meat200
    while honor_total_init < int(target_honor):
        honor_d4 += honorgain
        meat_interlud_init += meatgain
        honor_total_init -= honor_interlud_init
        honor_interlud_init += meatgain * 10
        honor_total_init = honor_total_init + honor_interlud_init + honorgain

    day4 = (
        ceil(honor_d4 / honor150) * meat150
        if NM == "150"
        else ceil(honor_d4 / honor200) * meat200
    )

    # TODO
    # send the honor and meat for interlude
    embed = discord.Embed(title="Jem-BOT")
    embed.add_field(
        name="**Honor Calculator ▫️ {:,}**".format(int(temp_target_honor)),
        value="\n``` Interlude ▫ {:,} honors, get {:,} meats\n Day 1 \t▫ {:,} honors ▫ {:,} meats\n Day 2 \t▫ {:,} honors ▫ {:,} meats\n Day 3 \t▫ {:,} honors ▫ {:,} meats\n Day 4 \t▫ {:,} honors ▫ {:,} meats``` **Total** ▫ **{:,}** honors ▫ **{:,}** meats\n".format(
            honor_interlud_init * 1000,
            meat_interlud_init,
            HONOR_D1 * 1000,
            DAY1,
            HONOR_D2 * 1000,
            DAY2,
            HONOR_D3 * 1000,
            DAY3,
            honor_d4 * 1000,
            day4,
            honor_total_init * 1000,
            meat_interlud_init + 3000,
        ),
        inline=False,
    )
    embed.set_footer(text="Assumption get 30m honor and 3k meats in prelim")
    await ctx.send(embed=embed)

@client.hybrid_command(name="help", description="Displays a list of available commands.")
async def help(ctx, command: typing.Optional[str] = None):
    command = command.lower() if command is not None else None
    commands = {
        "meat": "Menghitung jumlah honor NM90, NM95, NM100, NM150 dan NM200 dari jumlah meat yang diinputkan.",
        "meathonor": "Menghitung jumlah meat yang didapat dari jumlah honor yang diinputkan",
        "ppkm": "Menghitung jumlah meat yang digunakan setiap hari untuk mencapai honor yang diinginkan",
    }
    usage = {
        "meat": "`!meat *<meat>`",
        "meathonor": "`!meathonor *<honor>`",
        "ppkm": "`!ppkm *<honor> -<NM> -<day1> -<day2> -<day3>`",
    }
    command_key = list(commands.keys())
    if command is None:
        help_embed = discord.Embed(title="Jem-BOT Commands", description = "Gunakan`!help <command>` untuk mendapatkan info lebih lanjut dari daftar command dibawah.")
        for commandItem in commands:
            help_embed.add_field(name=commandItem, value=commands[commandItem], inline=False)
    elif command in command_key:
        help_embed = discord.Embed(title="Jem-BOT Commands")
        help_embed.add_field(name="Description", value=commands[command], inline=False)
        help_embed.add_field(name="Usage", value=usage[command], inline=False)
        help_embed.set_footer(text="* = required, - = optional")
    else:
        help_embed = discord.Embed(title="Jem-BOT Commands")
        help_embed.add_field(name="Error", value="Command not found.", inline=False)
    
    await ctx.send(embed=help_embed)



async def main():
    async with client:
        await client.start(token)


keep_alive()

try:
    asyncio.run(main())
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("kill 1")
    os.system("python restarter.py")
