# AI Text Generation CLI

A simple command-line application that sends a prompt to an AI model via OpenRouter and prints the generated response.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/chiamaka-ugwu/AI-stage-one-task.git
cd AI-stage-one-task
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Copy the example environment file:

```bash
cp .env.example .env
```

### 4. Configure environment variables

Open the `.env` file and add your values:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
MODEL_NAME=your_model_name_here
```

Get your API key from [OpenRouter](https://openrouter.ai).

---

## Usage

Run the application from the terminal:

```bash
python main.py "Your prompt here"
```

### Example

```bash
python main.py "How many states are there in Nigeria?"
```

### Example Output

```text
Nigeria has 36 states plus the Federal Capital Territory (FCT).
```

---

## Environment Variables

| Variable             | Description                                     |
| -------------------- | ----------------------------------------------- |
| `OPENROUTER_API_KEY` | Your OpenRouter API key                         |
| `MODEL_NAME`         | The AI model to use (e.g. `openai/gpt-4o-mini`) |

---

## Notes

- Ensure Python and pip are installed on your system before running the project.
- Make sure your OpenRouter account has access to the selected model.
- Never share your `.env` file or API key publicly.
