# Bạn Cóc: FAP Chatbot

Thành viên dự án: Hoàng Hồng Quân (HE195052)

## I. Giới thiệu

FPT Academic Portal đóng vai trò trung tâm trong đời sống học thuật của sinh viên, cung cấp các thông tin quan trọng như thời khóa biểu, lịch thi, điểm số và các thông báo từ nhà trường. Mặc dù là một công cụ mạnh mẽ, giao diện truyền thống của FAP đòi hỏi người dùng phải thực hiện nhiều bước để tìm kiếm thông tin cụ thể, dẫn đến tốn thời gian và đôi khi gây bất tiện. Sinh viên thường có những câu hỏi lặp đi lặp lại và mong muốn có một phương thức truy cập thông tin nhanh chóng, tự nhiên hơn.

Để giải quyết vấn đề này, dự án "Bạn Cóc" được đề xuất nhằm xây dựng một chatbot có khả năng hiểu ngôn ngữ tự nhiên với tiếng Việt và tự động phân loại yêu cầu của sinh viên thành các ý định tương ứng với các chức năng trên FAP.

## II. PHƯƠNG PHÁP LUẬN

Pipeline của dự án được xây dựng theo các bước chuẩn của một bài toán xử lý Ngôn ngữ Tự nhiên (NLP), từ thu thập dữ liệu, tiền xử lý, trích xuất đặc trưng đến huấn luyện và đánh giá mô hình.

**A. Dataset Curation**

Do không có sẵn bộ dữ liệu công khai cho tác vụ này, một bộ dữ liệu tiếng Việt đã được thu thập và xây dựng thủ công. Dữ liệu bao gồm các câu hỏi mà sinh viên có thể đặt cho chatbot, được gán nhãn với 11 loại ý định chính:

* `lich_hoc`: Các câu hỏi liên quan đến thời khóa biểu hàng tuần (thời gian, địa điểm, giảng viên).
* `lich_thi`: Các câu hỏi về lịch thi (ngày thi, phòng thi, hình thức thi).
* `diem_danh`: Các câu hỏi về tình trạng chuyên cần, số buổi vắng mặt.
* `diem_so`: Các câu hỏi về điểm thi, điểm thành phần, điểm tổng kết và GPA.
* `hoc_phi`: Các câu hỏi về học phí môn học.
* `chuong_trinh_hoc`: Các câu hỏi về khung chương trình, lộ trình học, môn tiên quyết.
* `xem_tin_tuc`: Các câu hỏi yêu cầu xem thông báo, tin tức mới nhất từ nhà trường.
* `chao_hoi`: Các câu chào hỏi để bắt đầu cuộc trò chuyện.
* `cam_on`: Các câu cảm ơn sau khi nhận được thông tin.
* `tam_biet`: Các câu tạm biệt để kết thúc cuộc trò chuyện.
* `chuc_nang`: Các câu hỏi về khả năng của chatbot.

**B. Pipeline Xử lý và Phân loại**

Pipeline được thiết kế để chuyển đổi câu hỏi đầu vào của người dùng thành một ý định có thể thực thi.

*1) Preprocessing:* Nhằm chuẩn hóa và làm sạch dữ liệu văn bản thô.

* **Chuẩn hóa:** Chuyển toàn bộ văn bản về dạng chữ thường (lowercase).
* **Loại bỏ Stopwords:** Các từ không mang nhiều ý nghĩa (như 'của', 'tôi', 'là'...) được loại bỏ để giảm nhiễu.
    > `['check', 'điểm_danh', 'môn', 'ail303m']`
* **Word Segmentation:** Câu được tách thành các từ có nghĩa.
    > `['check', 'điểm_danh', 'môn', 'ail303m', 'của', 'tôi']`
* **Named Entity Recognition:** Xác định các thực thể quan trọng như tên môn học.
    > `AIL303m` -> `COURSE`

*2) Feature Extraction:*

Các câu đã được tiền xử lý được chuyển đổi thành vector số học bằng phương pháp **TF-IDF (Term Frequency-Inverse Document Frequency)**. TF-IDF đánh giá tầm quan trọng của một từ trong một câu dựa trên tần suất xuất hiện của nó trong câu đó và tần suất nghịch đảo của nó trong toàn bộ tập dữ liệu. Phương pháp này hiệu quả trong việc làm nổi bật các từ khóa đặc trưng cho từng ý định.

*3) Target Variable Encoding:*

Biến mục tiêu `intent` sẽ được mã hoá bằng **LabelEncoder** để đảm bảo yêu cầu đầu ra của mô hình Machine Learning. 

*4) Training & Classification:*

Dữ liệu được chia thành tập huấn luyện (80%) và tập kiểm thử (20%). Các vector TF-IDF từ tập huấn luyện được sử dụng để đào tạo bốn mô hình Machine Learning:
* Random Forest
* Logistic Regression
* Support Vector Machine (SVM)
* Multinomial Naive Bayes

Sau khi huấn luyện, mô hình tốt nhất sẽ được sử dụng để dự đoán ý định cho các câu hỏi mới.

*5) Action:*

Dựa vào **Intent** dự đoán được và **Entity** trích xuất được, hệ thống sẽ gọi đến hàm xử lý tương ứng đến FAP để lấy dữ liệu và trả về cho người dùng.

## III. KẾT QUẢ VÀ PHÂN TÍCH

**A. Thiết lập thực nghiệm**

| Mô hình | Precision | Recall | F1-Score | Accuracy |
| :--- | :---: | :---: | :---: | :---: |
| Multinomial Naive Bayes |  |  |  |  |
| Logistic Regression |  |  |  |  |
| Support Vector Machine |  |  |  |  |
| Random Forest |  |  |  |  |

**B. Kết quả hiệu suất**

* **Hiệu suất mô hình:**
* **Error Analysis:**

## IV. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

**A. Kết luận**

Dự án đã thành công trong việc xây dựng một pipeline hoàn chỉnh để phân loại ý định người dùng cho chatbot FAP. Với việc sử dụng các kỹ thuật NLP cơ bản cho tiếng Việt và các mô hình Machine Learning, dự án đã đạt được độ chính xác tốt trong phân loại ý định.

**B. Hướng phát triển trong tương lai**

Để tiếp tục cải thiện và mở rộng hệ thống, các hướng phát triển sau đây được đề xuất:
* **Mở rộng và cân bằng Dataset:** Bổ sung thêm nhiều mẫu câu cho mỗi ý định, đặc biệt là các câu có cấu trúc phức tạp hoặc dễ gây nhầm lẫn. Sử dụng các kỹ thuật tăng cường dữ liệu (Data Augmentation) như thay thế từ đồng nghĩa hoặc back-translation.
* **Cải thiện biểu diễn văn bản:** Thử nghiệm với các kỹ thuật Word Embeddings (như Word2Vec, FastText) hay các mô hình Transformer như PhoBERT để cho ra embedding tốt hơn theo ngữ cảnh.
