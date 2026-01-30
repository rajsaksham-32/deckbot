import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

from src.data.deck import draw_card

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands.")
    except Exception as e:
        print("❌ Slash sync failed:", e)


# ----------------------------
# Deck Buttons View
# ----------------------------
class DeckView(discord.ui.View):
    def __init__(self, interaction, total_draws):
        super().__init__(timeout=3600)

        self.interaction = interaction
        self.total_draws = total_draws

        self.current = 0
        self.drawn = []
        self.discarded = set()
        self.finished = False

    async def draw_one(self):
        card = draw_card(self.discarded)

        self.drawn.append(card)
        self.current += 1

        embed = discord.Embed(
            title=f"🎴 Draw {self.current}/{self.total_draws}: {card['num']}. {card['name']}",
            description=card["desc"],
            color=discord.Color.gold()
        )

        embed.set_image(url=card["img"])

        await self.interaction.channel.send(embed=embed)

    async def finish_deck(self, forced=False):
        if self.finished:
            return
        self.finished = True

        if forced and self.current < self.total_draws:
            remaining = self.total_draws - self.current

            await self.interaction.channel.send(
                f"⚠ You stopped early!\n"
                f"The remaining **{remaining}** cards fly out at once!"
            )

            for _ in range(remaining):
                await self.draw_one()

        summary = "\n".join(
            [f"{i+1}. {c['num']}. {c['name']}" for i, c in enumerate(self.drawn)]
        )

        final_embed = discord.Embed(
            title="✅ Deck Complete!",
            description="Cards drawn:\n\n" + summary,
            color=discord.Color.green()
        )

        await self.interaction.channel.send(embed=final_embed)
        self.stop()

    @discord.ui.button(label="Draw Next Card", style=discord.ButtonStyle.green)
    async def next_card(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user != self.interaction.user:
            return await interaction.response.send_message(
                "❌ Only the drawer can press this button.",
                ephemeral=True
            )

        await interaction.response.defer()

        if self.current >= self.total_draws:
            return await self.finish_deck()

        await self.draw_one()

        if self.current >= self.total_draws:
            await self.finish_deck()

    @discord.ui.button(label="Stop Drawing", style=discord.ButtonStyle.red)
    async def stop_draw(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user != self.interaction.user:
            return await interaction.response.send_message(
                "❌ Only the drawer can stop.",
                ephemeral=True
            )

        await interaction.response.defer()
        await self.finish_deck(forced=True)


# ----------------------------
# Modal Popup for Card Count
# ----------------------------
class DeckModal(discord.ui.Modal, title="🎴 Deck of Many Things"):

    cards = discord.ui.TextInput(
        label="How many cards will you draw?",
        placeholder="Enter a number (example: 3)",
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):

        try:
            total = int(self.cards.value)

            if total < 1:
                return await interaction.response.send_message(
                    "❌ Must draw at least 1 card.",
                    ephemeral=True
                )

        except:
            return await interaction.response.send_message(
                "❌ Please enter a valid number.",
                ephemeral=True
            )

        await interaction.response.send_message(
            f"✅ You declared **{total}** card(s).\n"
            "Press **Draw Next Card** to begin."
        )

        view = DeckView(interaction, total)
        await interaction.channel.send("🎴 Deck Ready:", view=view)


# ----------------------------
# Slash Command: /deck
# ----------------------------
@bot.tree.command(name="deck", description="Draw from the Deck of Many Things")
async def deck(interaction: discord.Interaction):

    await interaction.response.send_modal(DeckModal())


bot.run(TOKEN)
