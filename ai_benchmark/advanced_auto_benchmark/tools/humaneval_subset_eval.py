# File này sẽ:
# Đọc từng file .py do humaneval_run.py sinh ra trong thư mục results/humaneval_outputs
# Chạy từng file, kiểm tra kết quả với các test case đơn giản
import importlib.util
import sys
from pathlib import Path

OUT_DIR = Path(__file__).parent.parent / "results" / "humaneval_clean"
if not OUT_DIR.exists():
    print(f"Output directory {OUT_DIR} does not exist. Hãy chạy script clean_humaneval_outputs.py trước!")
    sys.exit(1)

TASKS = {
    "HumanEval/0": {
        "func": "has_close_elements",
        "tests": [
            ("has_close_elements([1.0, 2.0, 3.0], 0.5)", False),
            ("has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)", True),
            ("has_close_elements([1.0, 1.0, 1.0], 0.1)", True),
        ],
    },
    "HumanEval/5": {
        "func": "intersperse",
        "tests": [
            ("intersperse([], 4)", []),
            ("intersperse([1, 2, 3], 4)", [1, 4, 2, 4, 3]),
        ],
    },
    "HumanEval/10": {
        "func": "is_palindrome",
        "tests": [
            ("is_palindrome('racecar')", True),
            ("is_palindrome('hello')", False),
        ],
    },
    "HumanEval/20": {
        "func": "find_closest_elements",
        "tests": [
            ("find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])", (2.0, 2.2)),
            ("find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])", (2.0, 2.0)),
        ],
    },
    "HumanEval/30": {
        "func": "get_positive",
        "tests": [
            ("get_positive([-1, 2, -4, 5, 6])", [2, 5, 6]),
            ("get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])", [5, 3, 2, 3, 9, 123, 1]),
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
        return False, f"ImportError (có thể do syntax hoặc code không hợp lệ): {e}"

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
