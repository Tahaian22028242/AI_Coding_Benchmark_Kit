import pytest

# ---- Hàm mẫu đúng để so sánh ----
def correct_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# ---- Đây là nơi bạn sẽ import hàm từ AI output ----
# Ví dụ AI sinh ra file ai_outputs/chatgpt/task2_sort.py
# thì bạn chỉ việc sửa lại import dưới đây.
from ai_benchmark.ai_outputs.gpt_4o.task2_fixed import buggy_sort as ai_sort


@pytest.mark.parametrize("arr", [
    [],
    [1],
    [5, 3, 1, 4, 2],
    [10, -1, 3, 7, 0],
    [1, 2, 3, 4, 5],
    [5, 5, 5, 5],
    list(range(100, 0, -1)),  # dãy dài giảm dần
])
def test_sort(arr):
    assert ai_sort(arr) == correct_sort(arr)
