# ai_benchmark/tools/humaneval_run_subset.py
"""
Chạy subset HumanEval (5 bài) với các model AI
Sinh code và lưu vào results/humaneval_outputs/
"""

import os
import json
import time
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None
try:
    import anthropic
except ImportError:
    anthropic = None
try:
    import google.generativeai as genai
except ImportError:
    genai = None
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# CONFIG: Set API keys qua biến môi trường hoặc sửa trực tiếp
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Dataset HumanEval
DATA_PATH = Path(__file__).parent.parent / 'human-eval-master' / 'data' / 'human-eval-v2-20210705.jsonl'
OUT_DIR = Path(__file__).parent.parent / 'results' / 'humaneval_outputs'
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Subset task IDs muốn chạy
SUBSET_IDS = {"HumanEval/0", "HumanEval/5", "HumanEval/10", "HumanEval/20", "HumanEval/30"}

def read_humaneval(path):
    problems = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            problems.append(json.loads(line))
    return problems


def call_openai(prompt, model="gpt-4o-mini", max_tokens=512):
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

def call_anthropic(prompt, model='claude-3-sonnet-20240229', max_tokens=512):
    if not anthropic:
        return '# anthropic library not installed'
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def call_gemini(prompt, model='models/gemini-2.5-pro-preview-05-06'):
    if not genai:
        return '# google-generativeai library not installed'
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)
    return response.text

def main():
    problems = read_humaneval(DATA_PATH)
    models = {
        # 'openai_gpt4o': lambda prompt: call_openai(prompt, model='gpt-4o'),
        'google_gemini': lambda prompt: call_gemini(prompt, model='models/gemini-2.5-pro-preview-05-06'),
        # 'anthropic_claude': lambda prompt: call_anthropic(prompt),
    }
    for prob in problems:
        task_id = prob["task_id"]
        if task_id not in SUBSET_IDS:
            continue
        prompt = prob["prompt"]
        for model_name, model_func in models.items():
            print(f"[HumanEval] {task_id} | {model_name}")
            try:
                code = model_func(prompt)
            except Exception as e:
                code = f'# ERROR: {e}'
            out_path = OUT_DIR / f'{task_id.replace("/", "_")}_{model_name}.py'
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(f'# Prompt:\n{prompt}\n\n# Model: {model_name}\n\n{code}\n')
            time.sleep(1)

if __name__ == '__main__':
    main()
