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
    task_id, model_name = name.split('_', 1)

    with open(f, encoding='utf-8') as file:
        code = file.read()

    items.append({
        "task_id": task_id,
        "model": model_name,
        "completion": code
    })

with open(OUT_FILE, 'w', encoding='utf-8') as out:
    for item in items:
        out.write(json.dumps(item) + '\n')

print(f"Done: {OUT_FILE}")
