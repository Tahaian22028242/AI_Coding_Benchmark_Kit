def fibonacci(n: int) -> int:
    """
    Tính và trả về số Fibonacci thứ n.
    Phương pháp lặp này hiệu quả hơn đệ quy,
    đặc biệt với các giá trị n lớn (ví dụ: n=10.000).

    Args:
        n (int): Chỉ số của số Fibonacci cần tính (n >= 0).

    Returns:
        int: Số Fibonacci thứ n.

    Raises:
        ValueError: Nếu n là số âm.
    """
    if n < 0:
        # Số Fibonacci chỉ được định nghĩa cho các số nguyên không âm.
        raise ValueError("n phải là số nguyên không âm.")
    elif n == 0:
        # F0 = 0
        return 0
    elif n == 1:
        # F1 = 1
        return 1
    else:
        # Khởi tạo hai số Fibonacci đầu tiên
        a, b = 0, 1
        # Vòng lặp để tính các số Fibonacci tiếp theo
        # Bắt đầu từ F2 cho đến Fn
        for _ in range(2, n + 1):
            # Tính số Fibonacci tiếp theo bằng cách cộng hai số trước đó
            # Sau đó, cập nhật a thành giá trị cũ của b và b thành giá trị mới tính được
            a, b = b, a + b
        return b
