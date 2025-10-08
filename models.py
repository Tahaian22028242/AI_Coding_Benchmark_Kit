import sys
import os

script = os.path.join(os.path.dirname(__file__), "ai_benchmark", "advanced_auto_benchmark", "tools", "models.py")
with open(script, encoding="utf-8") as f:
    code = compile(f.read(), script, 'exec')
    exec(code, {"__name__": "__main__"})
