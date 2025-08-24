
# AI Coding Benchmark Kit (UET-VNU)

Bộ benchmark thực hành để so sánh hiệu quả các **công cụ AI hỗ trợ lập trình** (ChatGPT, Cursor, Copilot, Codeium...).

## Cấu trúc
```
ai_benchmark/
  tasks/
    common.py
    task1_spec.md
    task2_bug.py
    task2_spec.md
    task3_spec.md
    task4_baseline.py
    task4_spec.md
  ai_outputs/
    task1.py          # điền hàm fibonacci của AI
    task2_fixed.py    # điền phiên bản đã sửa của buggy_sort
    test_task3.py     # viết pytest cho is_prime
    task4_refactor.py # điền hàm sum_of_squares_optimized
  run_benchmark.py
  requirements.txt
  README.md
```

## Cách dùng
1. Tải gói này về máy.
2. Mở `tasks/*_spec.md` để xem đề bài từng tác vụ.
3. Giao đề bài cho **mỗi công cụ AI** bạn muốn so sánh, sau đó **copy code AI trả về** vào các file tương ứng trong `ai_outputs/`.
4. (Lần đầu) Cài thư viện:
   ```bash
   pip install -r requirements.txt
   ```
5. Chạy chấm điểm:
   ```bash
   python run_benchmark.py
   ```
6. Xem điểm từng task và tổng điểm, file `results.json` sẽ lưu chi tiết.

## Mẹo benchmark nhiều công cụ
- Nhân bản thư mục `ai_outputs/` cho mỗi công cụ (vd: `ai_outputs_chatgpt`, `ai_outputs_copilot`), rồi lần lượt đổi tên thành `ai_outputs` trước khi chạy.
- Hoặc sửa nhẹ `run_benchmark.py` để nhận đường dẫn `--outputs-dir` (nâng cấp tuỳ chọn).

## Lưu ý
- Task 3 chấm điểm dựa trên pytest pass và số lượng test.
- Task 4 đánh giá cả **độ đúng** lẫn **hiệu năng** trên input lớn.
