
# # Cung cấp hàm sum_of_squares_optimized(n: int) nhanh và đúng.
# def sum_of_squares_optimized(n: int) -> int:
#     # TODO: Điền lời giải AI
#     raise NotImplementedError

def sum_of_squares_optimized(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    return n * (n + 1) * (2 * n + 1) // 6
