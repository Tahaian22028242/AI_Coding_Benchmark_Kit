
# # Điền lời giải của AI tại đây.
# # Phải cung cấp hàm: fibonacci(n: int) -> int

# def fibonacci(n: int) -> int:
#     raise NotImplementedError("Điền lời giải AI vào đây")

def fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
