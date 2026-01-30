import discord
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# --- Small test deck ---
from src.data.deck import draw_card


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def deck(ctx):
    card = draw_card()

    embed = discord.Embed(
        title="🃏 You drew a card!",
        description=f"**{card[0]}**\n\n{card[1]}",
        color=discord.Color.gold()
    )

    await ctx.send(embed=embed)


bot.run(TOKEN)
