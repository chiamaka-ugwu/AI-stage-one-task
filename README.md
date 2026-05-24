# AI Text Generation CLI

A simple command-line tool that sends a prompt to an AI model via OpenRouter and prints the response.

## Setup

1. Clone the repo and navigate into it:

```bash
   git clone <your-repo-url>
   cd <repo-folder>
```

2. Install dependencies:

```bash
   pip install -r requirements.txt
```

3. Create a `.env` file in the same folder by copying the example:

```bash
   cp .env.example .env
```

4. Open `.env` and fill in your values:

```bash
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   MODEL_NAME=openai/gpt-4o-mini
```

N.B. Get your API key from [openrouter.ai](https://openrouter.ai).

## Usage

```bash
python main.py "Your prompt here"
```

**Example:**

```bash
python main.py "How many states are there in Nigeria?"
```

**Output:**
Nigeria has 36 states plus the Federal Capital Territory (FCT).

## Environment Variables

| Variable             | Description                                  |
| -------------------- | -------------------------------------------- |
| `OPENROUTER_API_KEY` | Your OpenRouter API key                      |
| `MODEL_NAME`         | The model to use (e.g. `openai/gpt-4o-mini`) |
