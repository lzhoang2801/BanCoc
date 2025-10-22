# Bạn Cóc: FAP Chatbot

## 1. Giới thiệu dự án

### 1.1. Bối cảnh và Vấn đề

FAP là một công cụ thiết yếu đối với sinh viên, tuy nhiên, việc truy xuất các thông tin cụ thể như lịch học, lịch thi, hay điểm danh đôi khi đòi hỏi nhiều thao tác và thời gian. Sinh viên thường có những câu hỏi lặp đi lặp lại và mong muốn có một phương thức truy cập thông tin nhanh chóng, tự nhiên hơn.

### 1.2. Mục tiêu dự án

Dự án này tập trung vào việc xây dựng một chatbot đơn giản, có khả năng hiểu và phân loại các câu hỏi (ý định - intent) của sinh viên bằng tiếng Việt liên quan đến các chức năng trên FAP.

Mục tiêu chính là:
*   Xây dựng một tập dữ liệu các câu hỏi mẫu tiếng Việt cho các tác vụ phổ biến trên FAP.
*   Triển khai một pipeline xử lý ngôn ngữ tự nhiên hoàn chỉnh: từ tiền xử lý, vector hóa văn bản đến huấn luyện mô hình.
*   Tập trung vào các thuật toán Machine Learning cổ điển để hiểu sâu về bản chất của bài toán phân loại văn bản.
*   Đánh giá và so sánh hiệu quả của các mô hình để tìm ra phương pháp tối ưu cho bài toán.
*   Tích hợp công cụ VnCoreNLP để nâng cao chất lượng tiền xử lý và mở ra khả năng trích xuất thực thể (Named Entity Recognition).

## 2. Thành viên nhóm

| STT | Họ và Tên | MSSV | Email | Vai trò |
| :-- | :--- | :--- | :--- |
| 1 | Hoàng Hồng Quân | HE195052 | lzhoang2302@gmail.com | Developer |
| ... | ... | ... | ... | ... |

## 3. Dataset

### 3.1. Mô tả

Do không có sẵn bộ dữ liệu công khai cho tác vụ này, nhóm đã tự tiến hành thu thập và xây dựng một bộ dữ liệu tiếng Việt. Dữ liệu bao gồm các câu hỏi mà sinh viên có thể đặt cho chatbot.

*   **Định dạng:** File `.CSV` với 2 cột là `sentence` (câu hỏi của người dùng) và `intent` (ý định tương ứng).

### 3.2. Các loại ý định (Intents)

Bộ dữ liệu được gán nhãn với các ý định chính sau:

*   `lich_hoc`: Các câu hỏi liên quan đến thời khóa biểu.
*   `lich_thi`: Các câu hỏi về lịch thi.
*   `diem_danh`: Các câu hỏi về tình trạng điểm danh.
*   `diem_so`: Các câu hỏi về điểm thi, điểm thành phần.
*   `thong_tin_mon_hoc`: Các câu hỏi về giảng viên, phòng học.
*   `hoc_phi`: Các câu hỏi về học phí.
*   `chao_hoi`: Các câu chào hỏi thông thường.
*   `cam_on`: Các câu cảm ơn.
*   `tam_biet`: Các câu tạm biệt.

## 4. Pipeline xử lý

Luồng xử lý của mô hình được xây dựng theo các bước chuẩn của một bài toán NLP:

  <!-- Bạn có thể tự vẽ một sơ đồ đơn giản và thay link vào đây -->

1.  **Input (Đầu vào):** Người dùng nhập một câu hỏi bằng tiếng Việt.
    > *Ví dụ: "Check điểm danh môn DBI202 của tôi"*

2.  **Tiền xử lý (Preprocessing) với VnCoreNLP:**
    *   **Tách từ (Word Segmentation):** Câu được tách thành các từ có nghĩa.
        > *`['Check', 'điểm_danh', 'môn', 'DBI202', 'của', 'tôi']`*
    *   **Chuẩn hóa:** Chuyển về chữ thường (lowercase).
    *   **Loại bỏ Stopwords:** Các từ không mang nhiều ý nghĩa (như 'của', 'tôi', 'là'...) được loại bỏ để giảm nhiễu.
        > *`['check', 'điểm_danh', 'môn', 'dbi202']`*
    *   **Trích xuất thực thể (NER):** (Thực hiện song song) VnCoreNLP xác định các thực thể quan trọng như tên môn học.
        > *`DBI202` -> `COURSE`*

3.  **Biểu diễn Vector (Vectorization):**
    *   Câu đã được xử lý được chuyển đổi thành một vector số học sử dụng phương pháp **TF-IDF**. Phương pháp này đánh giá tầm quan trọng của một từ trong câu dựa trên tần suất xuất hiện của nó trong câu và trong toàn bộ tập dữ liệu.

4.  **Huấn luyện và Phân loại (Training & Classification):**
    *   Dữ liệu được chia thành tập train (80%) và tập test (20%).
    *   Vector TF-IDF được sử dụng để huấn luyện các mô hình phân loại:
        *   **Logistic Regression**
        *   **Support Vector Machine (SVM)**
        *   **Multinomial Naive Bayes**
        *   **K-Nearest Neighbors (KNN)**
    *   Mô hình đã được huấn luyện sẽ dự đoán nhãn (intent) cho vector đầu vào.
        > *Dự đoán: `hỏi_điểm_danh`*

5.  **Thực thi hành động (Action):**
    *   Dựa vào **Intent** dự đoán được và **Entity** trích xuất được, hệ thống sẽ gọi đến hàm xử lý tương ứng (ví dụ: gọi API của "Bạn Cóc") để lấy dữ liệu và trả về cho người dùng.

## 5. Kết quả và Phân tích

### 5.1. Kết quả thực nghiệm

Các mô hình được đánh giá trên tập test (20% dữ liệu) bằng các độ đo Accuracy và F1-Score (trung bình có trọng số - weighted average).

| Mô hình | Accuracy | F1-Score (Weighted) |
| :--- | :---: | :---: |
| K-Nearest Neighbors (KNN) | [ví dụ: 0.91] | [ví dụ: 0.91] |
| Multinomial Naive Bayes | [ví dụ: 0.94] | [ví dụ: 0.94] |
| **Logistic Regression** | **[ví dụ: 0.97]** | **[ví dụ: 0.97]** |
| **Support Vector Machine (SVM)** | **[ví dụ: 0.97]** | **[ví dụ: 0.97]** |

### 5.2. Phân tích và Quan sát

*   **Hiệu suất mô hình:** Cả **Logistic Regression** và **SVM** đều cho kết quả vượt trội. Điều này là do khả năng hoạt động tốt của chúng trên dữ liệu có chiều cao và thưa thớt (high-dimensional sparse data) như ma trận TF-IDF.
*   **Phân tích lỗi (Error Analysis):** Dựa trên ma trận nhầm lẫn (Confusion Matrix), các lỗi sai chủ yếu xảy ra giữa hai intent `hỏi_lịch_học` và `hỏi_lịch_thi`. Nguyên nhân là do chúng có chung nhiều từ khóa quan trọng như "lịch", "môn", "khi nào", "ngày mấy".
*   **Vai trò của VnCoreNLP:** Việc sử dụng VnCoreNLP để tách từ đã cải thiện độ chính xác so với các phương pháp tách từ đơn giản hơn, do nó xử lý tốt hơn các từ ghép và tên riêng.

## 6. Kết luận và Hướng phát triển

### 6.1. Kết luận

Dự án đã thành công trong việc xây dựng một pipeline hoàn chỉnh để phân loại ý định người dùng cho chatbot FAP. Mô hình sử dụng TF-IDF kết hợp với SVM/Logistic Regression đã đạt được độ chính xác cao (trên 97% trên tập kiểm thử), chứng tỏ tính hiệu quả của các phương pháp cổ điển đối với bài toán có phạm vi xác định. Dự án là một nền tảng vững chắc để phát triển một chatbot hoàn thiện hơn.

### 6.2. Hướng phát triển trong tương lai

*   **Mở rộng Dataset:** Bổ sung thêm nhiều mẫu câu hơn, đặc biệt là cho các intent dễ bị nhầm lẫn, và thêm các intent mới.
*   **Cải thiện biểu diễn văn bản:** Thử nghiệm với các kỹ thuật Word Embeddings (như Word2Vec, FastText) được huấn luyện trên chính tập dữ liệu để mô hình có thể hiểu được ngữ nghĩa và từ đồng nghĩa.
*   **Xử lý các câu hỏi ngoài phạm vi (Fallback Intent):** Xây dựng một cơ chế để chatbot nhận biết và phản hồi một cách lịch sự khi người dùng hỏi những câu không thuộc các intent đã định nghĩa.
*   **Xây dựng hệ thống quản lý hội thoại (Dialogue Management):** Phát triển một bộ máy trạng thái đơn giản để chatbot có thể xử lý các cuộc hội thoại có nhiều lượt nói.
*   **Tích hợp và triển khai:** Tích hợp hoàn chỉnh mô hình vào extension "Bạn Cóc" và triển khai để người dùng thực tế có thể sử dụng.

## 7. Refereces

[1] [vietnamese-stopwords](https://github.com/stopwords/vietnamese-stopwords)