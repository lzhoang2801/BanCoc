# Bạn Cóc: FAP Chatbot

## I. Giới thiệu

FPT Academic Portal đóng vai trò trung tâm trong đời sống học thuật của sinh viên, cung cấp quyền truy cập vào các thông tin quan trọng như thời khóa biểu, lịch thi, điểm số và các thông báo từ nhà trường. Mặc dù là một công cụ mạnh mẽ, giao diện truyền thống của FAP đòi hỏi người dùng phải thực hiện nhiều bước để tìm kiếm thông tin cụ thể, dẫn đến tốn thời gian và đôi khi gây bất tiện. Sinh viên thường có những câu hỏi lặp đi lặp lại và mong muốn có một phương thức truy cập thông tin nhanh chóng, tự nhiên hơn.

Để giải quyết vấn đề này, dự án "Bạn Cóc" được đề xuất nhằm xây dựng một chatbot có khả năng hiểu ngôn ngữ tự nhiên với tiếng Việt và tự động phân loại yêu cầu của sinh viên thành các ý định tương ứng với các chức năng trên FAP.

Mục tiêu chính của dự án bao gồm:
* Xây dựng một tập dữ liệu các câu hỏi mẫu tiếng Việt cho các tác vụ phổ biến trên FAP.
* Triển khai một pipeline xử lý ngôn ngữ tự nhiên hoàn chỉnh: từ tiền xử lý, vector hóa văn bản đến huấn luyện mô hình.
* Đánh giá và so sánh hiệu quả của các mô hình để tìm ra phương pháp tối ưu cho bài toán.

Thành viên nhóm thực hiện dự án:

| STT | Họ và Tên | MSSV | Email | Vai trò |
| :-- | :--- | :--- | :--- | :--- |
| 1 | Hoàng Hồng Quân | HE195052 | lzhoang2302@gmail.com | Developer |

## II. PHƯƠNG PHÁP LUẬN

Luồng xử lý của hệ thống được xây dựng theo các bước chuẩn của một bài toán NLP, từ việc thu thập dữ liệu đến việc triển khai mô hình.

**A. Dataset Curation**

Do không có sẵn bộ dữ liệu công khai cho tác vụ này, một bộ dữ liệu tiếng Việt đã được thu thập và xây dựng thủ công. Dữ liệu bao gồm các câu hỏi mà sinh viên có thể đặt cho chatbot, được gán nhãn với 11 loại ý định chính, ánh xạ trực tiếp tới các chức năng của FAP:

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

* **Chuẩn hóa:** Chuyển về chữ thường.
* **Loại bỏ Stopwords:** Các từ không mang nhiều ý nghĩa (như 'của', 'tôi', 'là'...) được loại bỏ để giảm nhiễu.
    > `['check', 'điểm_danh', 'môn', 'ail303m']`
* **Word Segmentation:** Câu được tách thành các từ có nghĩa.
    > `['check', 'điểm_danh', 'môn', 'ail303m', 'của', 'tôi']`
* **Named Entity Recognition:** Xác định các thực thể quan trọng như tên môn học.
    > `AIL303m` -> `COURSE`

*2) Feature Extraction:*

Câu đã được tiền xử lý được chuyển đổi thành một vector số học sử dụng phương pháp **TF-IDF (Term Frequency-Inverse Document Frequency)**. TF-IDF đánh giá tầm quan trọng của một từ trong một văn bản bằng cách xem xét tần suất xuất hiện của nó trong văn bản đó và tần suất nghịch đảo của nó trong toàn bộ kho văn bản (corpus). Phương pháp này rất hiệu quả đối với các bài toán phân loại văn bản, đặc biệt khi làm việc với dữ liệu thưa thớt.

*3) Training & Classification:*

Dữ liệu được chia thành tập huấn luyện (80%) và tập kiểm thử (20%). Các vector TF-IDF từ tập huấn luyện được sử dụng để đào tạo bốn mô hình Machine Learning cổ điển:
*   Logistic Regression
*   Support Vector Machine (SVM)
*   Multinomial Naive Bayes
*   K-Nearest Neighbors (KNN)

Sau khi huấn luyện, mô hình tốt nhất sẽ được sử dụng để dự đoán ý định cho các câu hỏi mới.

*4) Action:*

Dựa vào **Intent** dự đoán được và **Entity** trích xuất được, hệ thống sẽ gọi đến hàm xử lý tương ứng đến FAP để lấy dữ liệu và trả về cho người dùng.

## III. KẾT QUẢ VÀ PHÂN TÍCH

**A. Thiết lập thực nghiệm**

Các mô hình được đánh giá trên tập test (20% dữ liệu) bằng các độ đo Accuracy và F1-Score (trung bình có trọng số - weighted average).

| Mô hình | Accuracy | F1-Score (Weighted) |
| :--- | :---: | :---: |
| K-Nearest Neighbors |  |  |
| Multinomial Naive Bayes |  |  |
| Logistic Regression |  |  |
| Support Vector Machine |  |  |

**B. Kết quả hiệu suất**

* **Hiệu suất mô hình:**
* **Error Analysis:**

## IV. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

**A. Kết luận**

Dự án đã thành công trong việc xây dựng một pipeline hoàn chỉnh để phân loại ý định người dùng cho chatbot FAP.

**B. Hướng phát triển trong tương lai**

Để tiếp tục cải thiện và mở rộng hệ thống, các hướng phát triển sau đây được đề xuất:
*   **Mở rộng và Cân bằng Dataset:** Bổ sung thêm nhiều mẫu câu hơn, đặc biệt là cho các ý định dễ bị nhầm lẫn. Đồng thời, xem xét việc thêm các ý định mới để bao phủ nhiều chức năng hơn của FAP.
*   **Cải thiện Biểu diễn Văn bản:** Thử nghiệm với các kỹ thuật Word Embeddings (như Word2Vec, FastText) được huấn luyện trên kho văn bản tiếng Việt hoặc trên chính tập dữ liệu của dự án. Các kỹ thuật này có khả năng nắm bắt ngữ nghĩa và mối quan hệ giữa các từ, có thể giúp giải quyết vấn đề nhầm lẫn giữa các ý định tương tự.
*   **Xử lý các câu hỏi ngoài phạm vi (Fallback Intent):** Xây dựng một cơ chế phân loại để chatbot có thể nhận biết khi người dùng đặt câu hỏi không thuộc các ý định đã được định nghĩa, và đưa ra phản hồi phù hợp thay vì cố gắng phân loại sai.