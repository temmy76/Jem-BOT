import discord
from discord.ext import commands
import asyncio
import os
import typing
import random
from keep_alive import keep_alive
from math import ceil

token = os.environ['token']
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


def convert_to_int(target_honor: str):
  if "," in target_honor:
    target_honor = target_honor.replace(",", ".")
  if target_honor[-1] == "b":
    target_honor = float(target_honor[:-1]) * 1000000000
  elif target_honor[-1] == "m":
    target_honor = float(target_honor[:-1]) * 1000000
  elif target_honor[-1] == "k":
    target_honor = float(target_honor[:-1]) * 1000
  else:
    target_honor = float(target_honor)
  return int(target_honor)


@client.event
async def on_ready():
  print("Success: Bot is Connected to Discord")


@client.command()
async def sync(ctx):
  if ctx.author.id != 370753654644277258:
    await ctx.send("You are not allowed to use this command")
    return
  await client.tree.sync()
  await ctx.send("Synced!")


@client.hybrid_command(name="meathonor", description="ngitung meat")
async def meat_honor(ctx, honor: str):
  embed = discord.Embed(title="Jem-BOT", color=0x00FF00)
  honor = convert_to_int(honor)

  HONOR_MEAT = 80000

  kill_mob = ceil(honor / HONOR_MEAT)

  meat = 0
  while (kill_mob > 0):
    meat += random.randint(5, 10)
    kill_mob -= 1

  embed.add_field(name="Calculate meat from honor",
                  value="{:,} honors approximately get {:,} meats".format(
                    honor, meat),
                  inline=True)
  await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency * 1000)} ms")


@client.tree.command(name="hello", description="Say Hello")
async def introduce(interaction: discord.Interaction):
  await interaction.response.send_message(
    "Hello <@{name}> <:us:850985878461480980>".format(name=interaction.user.id)
  )


@client.tree.command(name="meat", description="ngitung meat")
async def meat(interaction: discord.Interaction, value: str):
  embed = discord.Embed(title="Meat bot")
  meat = value
  isStr = False
  try:
    if value.upper().isupper() == True:
      isStr = True
      print(isStr)
      raise Exception()
    meat = int(value)
    if meat < 5 or meat > 900000:
      raise Exception()
    nm90 = meat // 5
    nm95 = meat // 10
    nm100 = meat // 20
    nm150 = meat // 20
    nm200 = meat // 30
    embed.set_thumbnail(
      url=
      "https://cdn.discordapp.com/attachments/828790440240087052/1062699739147141160/image.png"
    )
    embed.add_field(
      name="Meat Calculator ▫️ {:,} meats".format(meat),
      value=
      "**{:}** NM90 or **{:,}** honors\n**{:,}** NM95 or **{:,}** honors\n**{:,}** NM100 or **{:,}** honors\n**{:,}** NM150 or **{:,}** honors\n**{:,}** NM200 or **{:,}** honors\n"
      .format(
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
    await interaction.response.send_message(embed=embed)
  except Exception:
    if isStr == False:
      await interaction.response.send_message(
        "minimal mikir kontol, minimal 5 meat")
    else:
      await interaction.response.send_message(
        "https://media.discordapp.net/attachments/908974505773396021/1062868409936785509/FB_IMG_1673465472297.jpg?width=456&height=480"
      )


# TODO
# 1. ppkm d1 d3 bisa di input user
# 2. d3 d4 bisa milih nm150 atau nm200
# 3. d2 bisa ngitung nm100 atau nm150
@client.tree.command(name="ppkm", description="ngitung honor berdasarkan ppkm")
async def ppkm(interaction: discord.Interaction,
               target_honor: str,
               day1: typing.Optional[str] = "50m",
               day2: typing.Optional[str] = "100m",
               day3: typing.Optional[str] = "150m",
               NM: typing.Optional[str] = "150"):
  temp_target_honor = convert_to_int(target_honor)
  target_honor = int(temp_target_honor) / 1000
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

  meat_track_init = (DAY1 + DAY2 + DAY3 + day4)

  meat_interlud_init = meat_track_init - 3000

  honor_interlud_init = meat_interlud_init * 10
  honor_total_init = (honor_interlud_init + HONOR_PRELIM + HONOR_D1 +
                      HONOR_D2 + HONOR_D3 + honor_d4)

  while honor_total_init < int(target_honor):
    honor_d4 += honor150
    meat_interlud_init += meat150
    honor_total_init -= honor_interlud_init
    honor_interlud_init += meat150 * 10
    honor_total_init = honor_total_init + honor_interlud_init + honor150

  day4 = ceil(honor_d4 / honor150) * meat150 if NM == "150" else ceil(
    honor_d4 / honor200) * meat200

  embed = discord.Embed(title="Jem-BOT")
  embed.add_field(
    name="Honor Calculator ▫️ {:,}".format(int(temp_target_honor)),
    value=
    "\n **Day 1** ▫ **{:,}** honors ▫ **{:,}** meats\n **Day 2** ▫ **{:,}** honors ▫ **{:,}** meats\n **Day 3** ▫ **{:,}** honors ▫ **{:,}** meats\n **Day 4** ▫ **{:,}** honors ▫ **{:,}** meats\n\n **Total** ▫ **{:,}** honors ▫ **{:,}** meats\n"
    .format(HONOR_D1 * 1000, DAY1, HONOR_D2 * 1000, DAY2, HONOR_D3 * 1000,
            DAY3, honor_d4 * 1000, day4, honor_total_init * 1000,
            meat_interlud_init + 3000),
    inline=False,
  )
  embed.set_footer(text="Assumption d2 - d4 using NM150")
  await interaction.response.send_message(embed=embed)


async def main():
  async with client:
    await client.start(token)


keep_alive()

try:
  asyncio.run(main())
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system('kill 1')
  os.system("python restarter.py")
