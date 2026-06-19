# ⌨️ QWERTY Master - 50 Bài Tập Luyện Gõ Bàn Phím

Một ứng dụng web tĩnh trực quan, gọn nhẹ giúp người dùng rèn luyện kỹ năng gõ bàn phím 10 ngón theo chuẩn bố cục QWERTY. Hệ thống lộ trình gồm 50 bài học được thiết kế khoa học bằng **Google AI Studio (Gemini 1.5)** đi từ các phím cơ sở (Home Row) cho đến các đoạn văn bản phức tạp và ký tự lập trình đặc biệt.

🚀 **[Trải nghiệm ứng dụng trực tuyến tại đây](https://nhatdh85.github.io/qwerty-master/dist/index.html)** 

---

## ✨ Tính năng nổi bật

*   **Lộ trình 50 bài học toàn diện:** Chia làm 3 cấp độ rõ rệt (Cơ bản, Trung cấp, Nâng cao).
*   **Giao diện Grid sinh động:** Danh sách bài tập hiển thị dạng lưới bắt mắt với các biểu tượng (icon) trực quan, hiển thị rõ ràng nội dung trọng tâm của từng bài.
*   **Phản hồi thời gian thực (Real-time Typing):** Hệ thống phân tích từng phím bấm, đổi màu chữ ngay khi gõ (Xanh: Đúng, Đỏ: Sai) kèm hiệu ứng rung cảnh báo lỗi.
*   **Bảng thống kê tức thời:** Theo dõi tiến độ kết thúc bài học (%) và bộ đếm số lỗi sai để người dùng tự đánh giá.
*   **Tối ưu hiệu năng:** Thiết kế dưới dạng Single Page Application (SPA), không load lại trang, tương thích tốt trên cả máy tính lẫn thiết bị di động có bàn phím rời.

---

## 🛠️ Công nghệ sử dụng

Ứng dụng được xây dựng dựa trên sự kết hợp giữa tư duy lập trình cấu trúc của Python và tính linh hoạt của Web tĩnh:

*   **Dữ liệu (AI Generated):** `Google AI Studio (Gemini 1.5)` cấu trúc danh mục bài tập sang định dạng JSON chuẩn.
*   **Backend Compiler:** `Python 3.x` đóng vai trò đọc file cấu trúc và biên dịch tự động ra mã nguồn giao diện web tĩnh.
*   **Frontend:** HTML5, JavaScript (ES6) thuần xử lý logic nhận diện ký tự sự kiện bàn phím.
*   **Styling:** `Tailwind CSS (v4)` mang lại giao diện UI/UX phẳng, hiện đại và thư viện `FontAwesome 6` cho hệ thống Icon.
*   **Deployment:** `GitHub Pages` phục vụ lưu trữ trang web tĩnh miễn phí, tốc độ cao.

---

## 📁 Cấu trúc thư mục dự án

```text
qwerty-master/
├── exercises.json       # Chứa dữ liệu chi tiết của 50 bài tập (Sinh bởi Gemini)
├── build_site.py        # Python script để biên dịch dữ liệu thành file HTML
└── dist/                # Thư mục chứa sản phẩm sau khi build (Deploy lên GitHub Pages)
    └── index.html       # File ứng dụng web duy nhất chứa toàn bộ Logic & UI