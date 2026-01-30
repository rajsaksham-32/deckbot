![Deck of Many Things Banner](images/DOMT.webp)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue" />
  <img src="https://img.shields.io/badge/discord.py-2.x-green" />
  <img src="https://img.shields.io/badge/Discord-Slash%20Commands-purple" />
  <img src="https://img.shields.io/badge/Project-Type%3A%20Hobby%20%26%20Learning-orange" />
</p>

# Deck of Many Things Discord Bot

A fully interactive Discord bot implementation of the legendary **Deck of Many Things**, built as a hobby project to explore Discord bot development, UI interactions, and structured game logic.

This bot allows users to draw cards from the deck inside Discord through a clean and immersive experience using buttons, embeds, and modern slash commands.

---

## What is the Deck of Many Things?

The **Deck of Many Things** is one of the most iconic magical artifacts in *Dungeons & Dragons (D&D)*.

It is a mysterious deck of enchanted cards where each draw can bring:

- Great fortune  
- Powerful rewards  
- Dangerous curses  
- Sudden chaos  
- Unexpected twists in a campaign  

Every card has a unique magical effect, making it a famous storytelling and gameplay tool for Dungeon Masters and players alike.

---

## Purpose of This Project

This project was created to bring the Deck of Many Things into Discord as an interactive experience.

With this bot, users can:

- Start a deck session using `/deck`
- Declare how many cards they wish to draw through a popup prompt
- Draw cards one-by-one using interactive buttons
- View card results through rich Discord embeds
- End the session early, triggering remaining cards automatically

This makes it perfect for:

- Online D&D campaigns  
- Roleplay servers  
- Fun community interactions  
- Learning Discord bot development  

---

## Features

-  Modern **Slash Command Support** (`/deck`)
-  Modal-based input (Discord popup prompt)
-  Interactive UI buttons:
  - Draw Next Card  
  - Stop Drawing  
-  Rich embedded card display with descriptions
-  Image support through hosted URLs or local assets
-  Session-based drawing with proper state tracking
-  Final summary embed of all drawn cards

---
## Demo

![DeckBot Demo](images/sample.gif)

---

## Impact 

This project demonstrates practical software engineering skills through an engaging real-world application.

Key highlights include:

- Built an **interactive Discord application** used for game-based community engagement  
- Implemented modern **UI-driven command flows** using modals and button interactions  
- Strengthened knowledge of **asynchronous programming** in Python  
- Designed clean modular architecture separating game logic and bot interaction  
- Improved ability to develop user-focused systems with real-time event handling  

This project reflects strong foundations in:

- Backend development  
- API integration  
- Interactive system design  
- Clean code organization  

---

## Tech Stack Used

This project was built using:

- **Python 3**
- **discord.py (2.x)**  
  - Slash commands (`app_commands`)
  - UI Views & Buttons
  - Modals for user input
- **Discord API**
- **dotenv** for secure token handling
- Modular project structure (`src/data/deck.py`) for card logic and data handling

---

## What I Learned

Building and deploying this project helped me gain hands-on experience in:

- Discord bot architecture and event-driven programming  
- Slash commands and modern Discord interactions  
- UI-based user flows with buttons and modals  
- Maintaining session state across asynchronous interactions  
- Clean embed formatting and user experience design  
- Structuring a Python project professionally  
- Using external assets (image hosting + URLs)

Additionally, I learned how to deploy and host a real Discord bot for public use, including:

- Configuring cloud deployment platforms (Railway/Render)  
- Managing environment variables securely (bot tokens, `.env`)  
- Writing deployment startup files such as `Procfile` and `requirements.txt`  
- Debugging deployment issues through build logs and runtime monitoring  

This project strengthened my understanding of real-world asynchronous programming, deployment workflows, and interactive application development.


---

## How to Run Locally (Personal Use)

Follow these steps to use the bot on your own machine:

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/deck-bot.git
cd deck-bot

# Install Dependencies

pip install -r requirements.txt

# Create a .env File
# Inside the project folder, create a file named .env:

DISCORD_TOKEN=your_bot_token_here

# Run the Bot

python main.py

# Use in Discord
# Once the bot is online, type:

/deck
```

# Future Improvements

- Planned enhancements for this project include:
- Card effect automation (instead of only descriptions)
- Multi-user session support
- Deck reshuffling + draw history tracking
- Campaign logging features
- Configurable house rules for custom decks


# Disclaimer

This project is a fan-made hobby implementation created for learning and entertainment purposes.
All rights, names, and concepts related to the Deck of Many Things belong to:
Wizards of the Coast (WotC)
(Dungeons & Dragons intellectual property)
I do not claim ownership of any official D&D content.
This project is purely non-commercial and intended as a personal development project.


# Author

Developed by Saksham Raj
A hobby project combining software engineering, game design inspiration, and Discord interaction development.