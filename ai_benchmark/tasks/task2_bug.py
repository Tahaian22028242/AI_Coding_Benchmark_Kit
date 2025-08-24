
# Mã lỗi cần sửa — hàm sắp xếp tăng dần

def buggy_sort(arr):
    # BUGS: dùng thuật toán chọn nhưng nhầm dấu so sánh và quên hoán vị đúng cách
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] > a[min_idx]:  # lẽ ra là < để tìm phần tử nhỏ nhất
                min_idx = j
        # Hoán vị bị lỗi (không hoán vị khi min_idx == i sẽ không sao, nhưng dưới đây lại gán sai)
        a[i] = a[min_idx]
    return a
