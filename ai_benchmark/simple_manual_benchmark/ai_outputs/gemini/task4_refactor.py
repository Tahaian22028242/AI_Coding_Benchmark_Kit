def sum_of_squares_optimized(n: int) -> int:
    """
    Tính tổng bình phương từ 1 đến n bằng công thức đóng (O(1)).

    Công thức: S_n = n * (n + 1) * (2n + 1) / 6

    Args:
        n (int): Số nguyên dương.

    Returns:
        int: Tổng bình phương từ 1 đến n.

    Raises:
        ValueError: Nếu n là số âm.
    """
    if n < 0:
        raise ValueError("n phải là số nguyên không âm.")
    if n == 0:
        return 0
    # Sử dụng công thức đóng để tính tổng bình phương
    # Chia cho 6 cuối cùng để đảm bảo kết quả là số nguyên
    return n * (n + 1) * (2 * n + 1) // 6