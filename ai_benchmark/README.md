# AI Coding Benchmark Kit

Framework đánh giá và benchmark các mô hình AI sinh mã nguồn trên tập bài toán lập trình chuẩn (HumanEval, MBPP, ...), hỗ trợ tự động chấm điểm, tổng hợp kết quả, và so sánh nhiều mô hình khác nhau.



## Luồng đánh giá mô hình AI

1. **Chạy subset và gọi API sinh code:**
  - Sử dụng script như `humaneval_run_subset.py` để chọn tập con các bài HumanEval, tự động gửi prompt cho AI (ví dụ Gemini, GPT-4o, Claude, ...), nhận về code output cho từng bài.
  - Output AI sẽ được lưu lại trong thư mục `results/humaneval_outputs/` (mỗi file tương ứng một bài).

2. **Làm sạch output:**
  - Dùng script `clean_humaneval_outputs.py` để loại bỏ phần thừa (markdown, chú thích, định dạng sai) và chuẩn hóa code về đúng format Python, lưu vào `results/humaneval_clean/`.

3. **Chấm điểm output:**
  - Chạy script chấm điểm `humaneval_subset_eval.py` để import từng file code đã clean, chạy test case chuẩn, thống kê pass/fail, phát hiện lỗi trình bày code, lỗi logic, ...
  - Kết quả chi tiết từng bài, từng model sẽ được tổng hợp và lưu lại.

4. **Tổng hợp, trực quan hóa kết quả:**
  - Dùng các script như `plot_results.py` để tổng hợp, vẽ biểu đồ so sánh hiệu năng các model AI trên tập bài test.



- **simple_manual_benchmark/**: Benchmark thủ công, dễ mở rộng, phù hợp cho các bài test nhỏ hoặc kiểm thử nhanh.
- **advanced_auto_benchmark/**: Benchmark tự động, hỗ trợ nhiều bộ dữ liệu và công cụ đánh giá chuyên sâu.
   - **evalplus-0.3.1/**: Bộ công cụ đánh giá chương trình sinh mã tự động.
   - **human-eval-master/**: Bộ dữ liệu HumanEval và script chấm điểm gốc.
   - **results/**: Kết quả benchmark, output AI, file tổng hợp, và output đã được làm sạch.
   - **tools/**: Script tiện ích (chạy chấm điểm, clean output, vẽ biểu đồ, ...).
- **ai_outputs/**: Output code sinh ra từ các mô hình AI, tổ chức theo từng model.
- **tasks/**: Đề bài, baseline, và các file mô tả task lập trình.
- **tests/**: Unit test cho các task.

## Hướng dẫn sử dụng nhanh

1. **Cài đặt phụ thuộc**
  ```bash
  pip install -r requirements.txt
  ```
  (Có thể cần cài thêm requirements trong các thư mục con nếu dùng advanced benchmark)

2. **Chạy benchmark thủ công**
  ```bash
  python simple_manual_benchmark/run_benchmark.py --model <tên_model>
  ```
  Output sẽ lưu trong `simple_manual_benchmark/results.json`.

3. **Chạy benchmark tự động với HumanEval**
  ```bash
  python advanced_auto_benchmark/tools/humaneval_run_subset.py
  ```
  Kết quả lưu trong `advanced_auto_benchmark/results/`.

4. **Làm sạch output AI**
  ```bash
  python advanced_auto_benchmark/tools/clean_humaneval_outputs.py
  ```
  Output sạch sẽ lưu trong `advanced_auto_benchmark/results/humaneval_clean/`.

5. **Chấm điểm output AI**
  ```bash
  python advanced_auto_benchmark/tools/humaneval_subset_eval.py
  ```
  Script này sẽ đọc output đã clean, chạy test case, xuất báo cáo pass/fail, thống kê chi tiết từng bài/testcase.

6. **Tổng hợp, vẽ biểu đồ kết quả**
  ```bash
  python advanced_auto_benchmark/tools/plot_results.py
  ```

## Một số script tiện ích

- `clean_humaneval_outputs.py`: Làm sạch output AI về đúng format Python để chấm điểm.
- `list_all_models.py`: Liệt kê các model AI có thể sử dụng.
- `run_all_models.py`: Chạy benchmark cho toàn bộ model trong output.

## Đóng góp

Mọi đóng góp về task mới, script tiện ích, hoặc cải tiến framework đều được hoan nghênh!


