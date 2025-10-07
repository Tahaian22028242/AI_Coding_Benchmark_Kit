
# Baseline chậm: tính tổng bình phương 1..n bằng vòng lặp
def sum_of_squares_naive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    s = 0
    for i in range(1, n+1):
        s += i*i
    return s
