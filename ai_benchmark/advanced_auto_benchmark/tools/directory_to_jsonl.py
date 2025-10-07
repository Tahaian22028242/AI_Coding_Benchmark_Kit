# ai_benchmark/tools/directory_to_jsonl.py
import os
import json
from pathlib import Path

# Đầu vào: folder chứa .py do humaneval_run.py sinh ra
IN_DIR = Path(__file__).parent.parent / 'results' / 'humaneval_outputs'
OUT_FILE = Path(__file__).parent.parent / 'results' / 'samples.jsonl'

items = []
for f in IN_DIR.glob('*.py'):
    # Tên file dạng: <task_id>_<model_name>.py
    name = f.stem
    if '_' not in name:
        continue
    parts = name.split('_')
    if len(parts) < 3:
        continue
    task_id = f"{parts[0]}/{parts[1]}"
    model_name = '_'.join(parts[2:])

    with open(f, encoding='utf-8') as file:
        code = file.read()
    # Extract only code block starting from first 'def ' or 'class '
    lines = code.splitlines()
    code_lines = []
    start = False
    for line in lines:
        if not start and (line.strip().startswith('def ') or line.strip().startswith('class ')):
            start = True
        if start:
            # Skip markdown block lines
            if line.strip().startswith('```'):
                continue
            code_lines.append(line)
    code_clean = '\n'.join(code_lines).strip()
    items.append({
        "task_id": task_id,
        "model": model_name,
        "completion": code_clean
    })

with open(OUT_FILE, 'w', encoding='utf-8') as out:
    for item in items:
        out.write(json.dumps(item) + '\n')

print(f"Done: {OUT_FILE}")
