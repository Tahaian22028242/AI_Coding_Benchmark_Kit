import os
import sys
import subprocess
import json
import csv
import re
from ast import literal_eval

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
AI_OUTPUTS = os.path.join(PROJECT_ROOT, 'ai_outputs')
RESULTS_DIR = os.path.join(PROJECT_ROOT, 'results')

os.makedirs(RESULTS_DIR, exist_ok=True)

models = [d for d in sorted(os.listdir(AI_OUTPUTS)) if os.path.isdir(os.path.join(AI_OUTPUTS, d))]
if not models:
    print('No models found in', AI_OUTPUTS)
    sys.exit(1)

summary = {}
for model in models:
    print(f"Running benchmark for model: {model}")
    cmd = [sys.executable, os.path.join(PROJECT_ROOT, 'run_benchmark.py'), '--model', model]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    out = (proc.stdout or '') + '\n' + (proc.stderr or '')

    # Save raw output
    raw_path = os.path.join(RESULTS_DIR, f"{model}.txt")
    with open(raw_path, 'w', encoding='utf-8') as f:
        f.write(out)

    # Try to parse scores
    scores = None
    total = None
    m = re.search(r"Scores:\s*(\{.*?\})\s*Total:\s*(\d+)", out, re.S)
    if m:
        try:
            scores = literal_eval(m.group(1))
            total = int(m.group(2))
        except Exception:
            scores = None

    summary[model] = {
        'returncode': proc.returncode,
        'scores': scores,
        'total': total,
        'raw_output': raw_path
    }

# Write JSON summary
json_path = os.path.join(RESULTS_DIR, 'results_summary.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

# Write CSV summary (flat)
csv_path = os.path.join(RESULTS_DIR, 'results_summary.csv')
all_tasks = ['task1', 'task2', 'task3', 'task4']
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    header = ['model'] + all_tasks + ['total', 'returncode']
    writer.writerow(header)
    for model in models:
        row = [model]
        scores = summary[model]['scores'] or {}
        for t in all_tasks:
            row.append(scores.get(t, ''))
        row.append(summary[model]['total'] if summary[model]['total'] is not None else '')
        row.append(summary[model]['returncode'])
        writer.writerow(row)

print('\nFinished. Summary written to:')
print(' -', json_path)
print(' -', csv_path)
print('Raw outputs are in', RESULTS_DIR)
