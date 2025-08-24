# --- Hàm sắp xếp tăng dần đã sửa (Selection Sort) ---

def fixed_sort(arr):
    """
    Sửa lỗi hàm sắp xếp tăng dần bằng thuật toán Sắp xếp chọn (Selection Sort).
    Độ phức tạp thời gian: O(n^2).

    Args:
        arr (list): Danh sách các phần tử cần sắp xếp.

    Returns:
        list: Danh sách đã được sắp xếp tăng dần.
    """
    a = list(arr)  # Tạo một bản sao để không làm thay đổi mảng gốc
    n = len(a)

    # Lặp qua từng phần tử của mảng
    for i in range(n):
        # Giả sử phần tử hiện tại là nhỏ nhất
        min_idx = i
        # Tìm phần tử nhỏ nhất trong phần còn lại của mảng
        for j in range(i + 1, n):
            # Sửa lỗi: dùng dấu < để tìm phần tử nhỏ nhất
            if a[j] < a[min_idx]:
                min_idx = j

        # Sửa lỗi: Hoán vị phần tử nhỏ nhất tìm được với phần tử tại vị trí hiện tại
        # Chỉ hoán vị nếu phần tử nhỏ nhất không phải là phần tử hiện tại
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            
    return a