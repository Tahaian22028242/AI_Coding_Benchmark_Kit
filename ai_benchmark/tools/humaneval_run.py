# File này sẽ:
# Đọc từng đề từ file HumanEval (jsonl)
# Gửi prompt tới các model AI
# Lưu kết quả code vào file hoặc biến để chấm điểm sau

import os
import json
import time
import sys
from pathlib import Path

# Optional: pip install openai anthropic google-generativeai
try:
    import openai
except ImportError:
    openai = None
try:
    import anthropic
except ImportError:
    anthropic = None
try:
    import google.generativeai as genai
except ImportError:
    genai = None

# CONFIG: Set your API keys here or use environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', 'YOUR_ANTHROPIC_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'YOUR_GOOGLE_API_KEY')

# Path to HumanEval dataset
DATA_PATH = Path(__file__).parent.parent / 'human-eval-master' / 'data' / 'HumanEval.jsonl.gz'
if not DATA_PATH.exists():
    DATA_PATH = Path(__file__).parent.parent / 'humaneval' / 'HumanEval.jsonl'

# Output folder
OUT_DIR = Path(__file__).parent.parent / 'results' / 'humaneval_outputs'
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Helper: Read HumanEval problems
def read_humaneval(path):
    problems = []
    if str(path).endswith('.gz'):
        import gzip
        with gzip.open(path, 'rt', encoding='utf-8') as f:
            for line in f:
                problems.append(json.loads(line))
    else:
        with open(path, encoding='utf-8') as f:
            for line in f:
                problems.append(json.loads(line))
    return problems

# Helper: Send prompt to OpenAI GPT
def call_openai(prompt, model='gpt-4o', max_tokens=512):
    if not openai:
        return 'openai library not installed'
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

# Helper: Send prompt to Anthropic Claude
def call_anthropic(prompt, model='claude-3-sonnet-20240229', max_tokens=512):
    if not anthropic:
        return 'anthropic library not installed'
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content

# Helper: Send prompt to Google Gemini
def call_gemini(prompt, model='gemini-pro', max_tokens=512):
    if not genai:
        return 'google-generativeai library not installed'
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text

# Main loop: For each problem, send to each model and save output
def main():
    problems = read_humaneval(DATA_PATH)
    models = {
        'openai_gpt4o': lambda prompt: call_openai(prompt, model='gpt-4o'),
        'anthropic_claude_sonnet': lambda prompt: call_anthropic(prompt, model='claude-3-sonnet-20240229'),
        'google_gemini': lambda prompt: call_gemini(prompt, model='gemini-pro'),
    }
    for i, prob in enumerate(problems):
        prompt = prob['prompt']
        task_id = prob.get('task_id', f'problem_{i}')
        for model_name, model_func in models.items():
            print(f"[HumanEval] {task_id} | {model_name}")
            try:
                code = model_func(prompt)
            except Exception as e:
                code = f'ERROR: {e}'
            out_path = OUT_DIR / f'{task_id}_{model_name}.py'
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(f'# Prompt:\n{prompt}\n\n# Model: {model_name}\n\n{code}\n')
            time.sleep(1)  # avoid rate limit

if __name__ == '__main__':
    main()
