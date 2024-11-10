# Discord Bot in Python with SlashCommand

This is a simple Discord bot written in Python that utilizes the `discord.py` library to handle slash commands. It includes the pre-defined `/ping` command which responds with "Pong!" when called.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Code Structure](#code-structure)
5. [License](#license)

## Requirements

To run this bot, you'll need:

- Python 3.8 or higher
- `discord.py` library
- A `.env` file with your bot token

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/PedroDevJS/python-discord-template.git
cd python-discord-template
```

### 2. Create a virtual environment

If you don't have `virtualenv` installed, install it first:

```bash
pip install virtualenv
```

Then, create and activate a virtual environment:

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For MacOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Once your virtual environment is activated, install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory of the project and add the following:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

Replace `your_discord_bot_token_here` with your actual Discord bot token.

### 5. Run the bot

To run the bot, execute the following command:

```bash
python main.py
```

Your bot should now be online and connected to your Discord server.

## Usage

Once the bot is running, it will respond to the following slash command:

### `/ping`

This simple command responds with "Pong!" when invoked.

#### Example:

- `/ping` → Bot responds with "Pong!"

## Bot Commands

### `/ping`
- **Description**: This command returns a simple "Pong!" response.
- **Usage**: `/ping`
    - The bot replies with `Pong!`

## Code Structure

### main.py

This file is the entry point of the bot. It loads and runs the bot, syncing the commands for the specified guild.

### cogs/ping.py

This file contains the `PingCommand` class, which defines the `/ping` command. It registers the command to respond with "Pong!" when invoked.

### .env

This file holds your environment variables, including your Discord bot token (`DISCORD_TOKEN`).

### requirements.txt

This file contains the necessary Python libraries that your project depends on. It should contain at least:

```txt
discord.py
python-dotenv
```

You can install these dependencies with `pip` by running the command mentioned in the Installation section.

## License

This project is licensed under the **GNU General Public License v3.0**. You can freely use, modify, and distribute this code, but please ensure that any modifications or redistributions are done under the same license.

For more information about this license, please refer to the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

---

### Notes:

1. Replace `your_discord_bot_token_here` with your actual bot token in the `.env` file.
2. Ensure that your bot is added to a server and has permissions to send messages.