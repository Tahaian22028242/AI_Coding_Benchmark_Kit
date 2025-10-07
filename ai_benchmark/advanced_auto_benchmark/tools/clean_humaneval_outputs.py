import os
from pathlib import Path
import re




IN_DIR = Path(__file__).parent.parent / 'results' / 'humaneval_outputs'
OUT_DIR = Path(__file__).parent.parent / 'results' / 'humaneval_clean'
OUT_DIR.mkdir(exist_ok=True)

def extract_python_code(text):
    # Tự động xóa toàn bộ phần đề, chỉ giữ lại phần code sau '# Model:' hoặc sau markdown block cuối cùng
    lines = text.splitlines()
    code_lines = []
    start = False
    for line in lines:
        if not start:
            if line.strip().startswith('# Model'):
                start = True
                continue
            if line.strip().startswith('```python') or line.strip().startswith('```'):
                start = True
                continue
        if start:
            # Bỏ mọi dòng bắt đầu bằng ``` hoặc chỉ chứa ```
            if line.strip().startswith('```') or line.strip() == '```':
                continue
            code_lines.append(line)
    # Loại bỏ các dòng ```python và ``` ở đầu/cuối code
    while code_lines and code_lines[0].strip().startswith('```'):
        code_lines.pop(0)
    while code_lines and code_lines[-1].strip().startswith('```'):
        code_lines.pop()
    code = '\n'.join(code_lines)
    return code

for f in IN_DIR.glob('*.py'):
    with open(f, encoding='utf-8') as file:
        raw = file.read()
    code = extract_python_code(raw)
    out_path = OUT_DIR / f.name
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(code)
    print(f"Wrote: {out_path}")

print(f"Done. Cleaned files in {OUT_DIR}")
