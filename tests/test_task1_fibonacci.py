import importlib.util
import sys
import os
import pytest

# === Cấu hình ===
# Đường dẫn tới file AI output (ví dụ: ai_outputs/chatgpt/task1_fibonacci.py)
AI_OUTPUT_PATH = os.environ.get("AI_OUTPUT_PATH", "ai_outputs/gpt-4o/task1_fibonacci.py")


def load_ai_module(path):
    """Load file Python AI sinh ra như 1 module."""
    spec = importlib.util.spec_from_file_location("ai_solution", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["ai_solution"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="session")
def ai_solution():
    """Fixture load code AI một lần duy nhất."""
    if not os.path.exists(AI_OUTPUT_PATH):
        pytest.skip(f"❌ Không tìm thấy file: {AI_OUTPUT_PATH}")
    return load_ai_module(AI_OUTPUT_PATH)


# === Test Cases ===
def test_small_numbers(ai_solution):
    assert ai_solution.fibonacci(0) == 0
    assert ai_solution.fibonacci(1) == 1
    assert ai_solution.fibonacci(2) == 1
    assert ai_solution.fibonacci(3) == 2
    assert ai_solution.fibonacci(4) == 3
    assert ai_solution.fibonacci(5) == 5


def test_larger_numbers(ai_solution):
    assert ai_solution.fibonacci(10) == 55
    assert ai_solution.fibonacci(15) == 610
    assert ai_solution.fibonacci(20) == 6765


def test_invalid_inputs(ai_solution):
    with pytest.raises((ValueError, TypeError)):
        ai_solution.fibonacci(-1)
    with pytest.raises((ValueError, TypeError)):
        ai_solution.fibonacci("abc")
