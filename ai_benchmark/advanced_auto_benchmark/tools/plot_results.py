import os
import csv
import matplotlib.pyplot as plt

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RESULTS_DIR = os.path.join(PROJECT_ROOT, 'results')
CSV_PATH = os.path.join(RESULTS_DIR, 'results_summary.csv')

if not os.path.exists(CSV_PATH):
    print('CSV summary not found at', CSV_PATH)
    raise SystemExit(1)

models = []
all_tasks = []
rows = []
with open(CSV_PATH, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    all_tasks = [c for c in reader.fieldnames if c.startswith('task')]
    for r in reader:
        models.append(r['model'])
        rows.append(r)

# Totals bar chart
totals = [int(r['total']) if r['total'] else 0 for r in rows]
plt.figure(figsize=(8,4))
plt.bar(models, totals, color='tab:blue')
plt.ylabel('Total score')
plt.title('Model total scores')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
out_total = os.path.join(RESULTS_DIR, 'results_total.png')
plt.savefig(out_total)
print('Saved', out_total)
plt.close()

# Stacked bar per-task
task_values = {t: [int(r[t]) if r[t] else 0 for r in rows] for t in all_tasks}
plt.figure(figsize=(10,5))
bottom = [0]*len(models)
colors = plt.cm.Set3.colors
for i, t in enumerate(all_tasks):
    vals = task_values[t]
    plt.bar(models, vals, bottom=bottom, label=t, color=colors[i % len(colors)])
    bottom = [bottom[j] + vals[j] for j in range(len(vals))]

plt.ylabel('Score')
plt.title('Per-task scores (stacked)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
out_stack = os.path.join(RESULTS_DIR, 'results_stacked.png')
plt.savefig(out_stack)
print('Saved', out_stack)
plt.close()
