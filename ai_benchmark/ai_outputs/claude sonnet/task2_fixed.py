# # Viết phiên bản đã sửa để sắp xếp tăng dần.
# def buggy_sort(arr):
#     # TODO: Thay bằng lời giải của AI
#     return list(arr)

def fixed_sort(arr):
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
