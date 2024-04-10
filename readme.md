# Discord Chatbot using OpenAI's GPT-3.5 Model

This project is a Discord chatbot that utilizes OpenAI's GPT-3.5 model to generate responses to messages in Discord channels. The bot listens for mentions and responds with generated text based on the context of the conversation.

## Requirements

- Python 3.x
- discord.py
- openai

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain API keys:
   - [Discord Bot Token](https://discord.com/developers/applications)
   - [OpenAI API Key](https://platform.openai.com/signup)

4. Replace placeholders:
   - Replace `YOUR_DISCORD_TOKEN` in `keys.py` with your Discord bot token.
   - Replace `YOUR_OPENAI_API_KEY` in `keys.py` with your OpenAI API key.

## Usage

Run the bot using the following command:

```bash
python bot.py
