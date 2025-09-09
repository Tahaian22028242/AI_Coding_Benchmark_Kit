# File này sẽ:
# Đọc từng file .py do humaneval_run.py sinh ra trong thư mục results/humaneval_outputs
# Chạy từng file, kiểm tra kết quả với các test case đơn giản
import importlib.util
import sys
from pathlib import Path

# Thư mục chứa code mà humaneval_run.py đã sinh
OUT_DIR = Path(__file__).parent.parent / "results" / "humaneval_outputs"
if not OUT_DIR.exists():
    print(f"Output directory {OUT_DIR} does not exist.")
    sys.exit(1)

# Subset bài toán muốn test
TASKS = {
    "HumanEval/0": {  # Add two numbers
        "tests": [
            ("add(1, 2)", 3),
            ("add(-5, 7)", 2),
        ],
    },
    "HumanEval/5": {  # Is prime
        "tests": [
            ("is_prime(2)", True),
            ("is_prime(15)", False),
            ("is_prime(17)", True),
        ],
    },
    "HumanEval/10": {  # Fibonacci
        "tests": [
            ("fibonacci(0)", 0),
            ("fibonacci(5)", 5),
            ("fibonacci(10)", 55),
        ],
    },
    "HumanEval/20": {  # Reverse string
        "tests": [
            ("reverse_string('abc')", "cba"),
            ("reverse_string('racecar')", "racecar"),
        ],
    },
    "HumanEval/30": {  # Factorial
        "tests": [
            ("factorial(0)", 1),
            ("factorial(5)", 120),
        ],
    },
}

def run_tests(pyfile, task):
    """Load a .py file and run tests defined in TASKS"""
    spec = importlib.util.spec_from_file_location("candidate", pyfile)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:
        return False, f"ImportError: {e}"

    passed = 0
    total = len(TASKS[task]["tests"])
    for expr, expected in TASKS[task]["tests"]:
        try:
            result = eval(expr, mod.__dict__)
            if result == expected:
                passed += 1
        except Exception as e:
            return False, f"RuntimeError in {expr}: {e}"

    return passed == total, f"{passed}/{total} tests passed"

def main():
    results = []
    for task_id in TASKS:
        for pyfile in OUT_DIR.glob(f"{task_id.replace('/', '_')}_*.py"):
            model_name = pyfile.stem.split("_", 1)[1]
            ok, detail = run_tests(pyfile, task_id)
            results.append((task_id, model_name, ok, detail))

    # In bảng kết quả
    print("Task\tModel\tResult\tDetail")
    for task_id, model, ok, detail in results:
        print(f"{task_id}\t{model}\t{'PASS' if ok else 'FAIL'}\t{detail}")

if __name__ == "__main__":
    main()
