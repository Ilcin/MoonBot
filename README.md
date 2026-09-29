# MoonBot

A Discord bot with AI integration that can think and respond intelligently.

## Features

- **Discord Integration**: Full Discord bot capabilities
- **AI Thinking**: When someone writes "think" in a message, MoonBot calls an external AI API to generate a response
- **OpenAI-compatible**: Works with any OpenAI-compatible API endpoint
- **Model Selection**: Supports multiple AI models (GPT-4, GPT-3.5-Turbo, Claude, Llama, etc.)

## Configuration

Create a `moonbot_config.py` file with the following variables:

```python
# MoonBot Character/Personality
MOONBOT_CHARACTER = """You are MoonBot, a sarcastic, witty, and slightly rude Discord bot..."""

# Discord Configuration
moontoken = "your-discord-bot-token-here"  # Get from Discord Developer Portal

# AI API Configuration
ai_api_url = "https://api.openai.com/v1/chat/completions"  # Your AI provider URL
ai_api_key = "your-ai-api-key-here"  # Your AI provider API key (e.g., OpenAI API key)
valid_models = ["gpt-4", "gpt-3.5-turbo", "claude-3", "llama-3", "nemo-3-omni"]
default_model = "nemo-3-omni"
```

## Environment Variables

Set these environment variables when running the bot:

- `MOONTOKEN`: Your Discord bot token (required)
- `AI_API_URL`: Your AI provider URL (default: OpenAI)
- `AI_API_KEY`: Your AI provider API key (default: empty)

## Running with Docker

Build the Docker image:
```bash
docker build -t grossbaa/moonbot:latest .
```

Run the container:
```bash
docker run -e MOONTOKEN=your-token -e AI_API_URL=https://api.openai.com/v1/chat/completions -e AI_API_KEY=your-key grossbaa/moonbot:latest
```

## How It Works

1. When someone writes "think" in a Discord message, MoonBot detects it
2. MoonBot sends the message to your configured AI API
3. The AI generates a response based on the MOONBOT_CHARACTER prompt
4. MoonBot sends the response back to Discord

## Requirements

- Python 3.8+
- discord.py
- aiohttp

## License

MIT