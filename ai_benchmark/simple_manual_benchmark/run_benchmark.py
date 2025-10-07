import argparse
import importlib.util
import os
import sys
import time
import traceback
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # dòng này được thêm vào để xác định thư mục hiện tại của script
TASKS_DIR = os.path.join(SCRIPT_DIR, "tasks")
OUTPUTS_DIR = os.path.join(SCRIPT_DIR, "ai_outputs")

def load_module(path, module_name):
    """Dynamically load module from file path."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError(f"Cannot import {module_name} from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def score_task1(model_dir):
    """Check fibonacci correctness."""
    try:
        mod = load_module(os.path.join(model_dir, "task1.py"), "task1")
        fib = mod.fibonacci
        tests = [(0,0),(1,1),(5,5),(10,55)]
        for n, expected in tests:
            if fib(n) != expected:
                return 0
        return 10
    except Exception as e:
        print("Task1 error:", e)
        return 0

def score_task2(model_dir):
    """Check if buggy_sort was fixed correctly."""
    try:
        mod = load_module(os.path.join(model_dir, "task2_fixed.py"), "task2_fixed")
        srt = mod.fixed_sort
        tests = [
            [3,1,2],
            [5,4,3,2,1],
            [],
            [7]
        ]
        for arr in tests:
            if srt(arr) != sorted(arr):
                return 0
        return 10
    except Exception as e:
        print("Task2 error:", e)
        return 0

def score_task3(model_dir):
    """Run pytest on the generated test file."""
    try:
        test_file = os.path.join(model_dir, "test_task3.py")
        # run pytest with a timeout to avoid hangs
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", test_file],
            capture_output=True, text=True,
            timeout=20
        )
        if result.returncode == 0:
            return 10
        else:
            print(result.stdout)
            return 0
    except Exception as e:
        # Distinguish timeout from other errors
        if isinstance(e, subprocess.TimeoutExpired):
            print("Task3 error: pytest timed out")
        else:
            print("Task3 error:", e)
        return 0

def score_task4(model_dir):
    """Compare baseline vs refactored performance."""
    try:
        baseline_mod = load_module(os.path.join(TASKS_DIR, "task4_baseline.py"), "task4_baseline")
        refactor_mod = load_module(os.path.join(model_dir, "task4_refactor.py"), "task4_refactor")

        # Ensure required functions exist
        if not hasattr(baseline_mod, 'sum_of_squares_naive'):
            print("Task4 error: baseline missing 'sum_of_squares_naive'")
            return 0
        if not hasattr(refactor_mod, 'sum_of_squares_optimized'):
            print("Task4 error: refactor missing 'sum_of_squares_optimized'")
            return 0

        baseline = baseline_mod.sum_of_squares_naive
        refactor = refactor_mod.sum_of_squares_optimized

        # Use an integer workload and validate inputs
        workload = 2000
        if not isinstance(workload, int) or workload < 0:
            print("Task4 error: invalid workload")
            return 0

        # Measure execution times with simple try/except; keep it local to avoid cross-process overhead
        try:
            t0 = time.time()
            baseline(workload)
            t1 = time.time()
        except Exception as e:
            print("Task4 error while executing baseline:", e)
            return 0

        try:
            t_start = time.time()
            refactor(workload)
            t_end = time.time()
        except Exception as e:
            print("Task4 error while executing refactor:", e)
            return 0

        baseline_time = t1 - t0
        refactor_time = t_end - t_start

        if refactor_time < baseline_time:
            return 10
        else:
            return 5  # at least runs
    except Exception as e:
        print("Task4 error:", e)
        return 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Name of the model (subdir in ai_outputs/)")
    args = parser.parse_args()

    model_dir = os.path.join(OUTPUTS_DIR, args.model)
    if not os.path.isdir(model_dir):
        print(f"Model directory {model_dir} not found!")
        sys.exit(1)

    print(f"=== Running benchmark for model: {args.model} ===")
    scores = {}
    scores["task1"] = score_task1(model_dir)
    scores["task2"] = score_task2(model_dir)
    scores["task3"] = score_task3(model_dir)
    scores["task4"] = score_task4(model_dir)

    total = sum(scores.values())
    print("Scores:", scores, "Total:", total)

if __name__ == "__main__":
    main()
