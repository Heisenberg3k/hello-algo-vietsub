---
comments: true
icon: material/rocket-launch-outline
---

# Lời nói đầu

Cách đây vài năm mình có chia sẻ cách giải bài toán “Sword for Offer” trên LeetCode và nhận được sự động viên, ủng hộ của rất nhiều độc giả. Trong quá trình tương tác với độc giả, câu hỏi tôi thường gặp nhất là "làm thế nào để bắt đầu với thuật toán". Dần dần, tôi bắt đầu quan tâm sâu sắc đến câu hỏi này.

Đi thẳng vào giải quyết vấn đề dường như là cách tiếp cận phổ biến nhất—nó đơn giản, trực tiếp và hiệu quả. Tuy nhiên, giải quyết vấn đề cũng giống như chơi Minesweeper: những người có khả năng tự học mạnh mẽ có thể tháo gỡ thành công từng quả mìn, trong khi những người không có nền tảng vững chắc có thể bị bầm dập, thất vọng rút lui từng bước. Đọc qua sách giáo khoa cũng là một thói quen phổ biến, nhưng đối với những người tìm việc, việc làm luận văn tốt nghiệp, nộp sơ yếu lý lịch và chuẩn bị cho các bài kiểm tra viết và phỏng vấn đã tiêu tốn phần lớn năng lượng của họ, khiến việc đọc những cuốn sách dày trở thành một thử thách khó khăn.

Nếu bạn đang phải đối mặt với những khó khăn tương tự thì thật may mắn khi cuốn sách này đã “tìm thấy” bạn. Cuốn sách này là câu trả lời của tôi cho câu hỏi này – ngay cả khi nó có thể không phải là giải pháp tối ưu thì ít nhất nó cũng là một nỗ lực tích cực. Mặc dù cuốn sách này không trực tiếp mang đến cho bạn lời mời làm việc nhưng nó sẽ hướng dẫn bạn về "tổng quan" về cấu trúc dữ liệu và thuật toán, giúp bạn hiểu về hình dạng, kích thước và sự phân bổ của các "mỏ" khác nhau và cho phép bạn thành thạo các "phương pháp rà phá bom mìn" khác nhau. Với những kỹ năng này, tôi tin bạn có thể giải quyết vấn đề và đọc tài liệu kỹ thuật một cách tự tin hơn, dần dần xây dựng được hệ thống kiến ​​thức hoàn chỉnh.

Tôi hoàn toàn đồng ý với câu nói của Giáo sư Feynman: "Kiến thức không miễn phí. Bạn phải chú ý." Theo nghĩa này, cuốn sách này không hoàn toàn "miễn phí". Để xứng đáng với sự “chú ý” quý ​​giá mà bạn dành cho cuốn sách này, tôi sẽ cố gắng hết sức và dành “sự chú ý” lớn nhất của mình để hoàn thành tác phẩm này.

Tôi nhận thức sâu sắc về giới hạn kiến ​​thức và kinh nghiệm của mình. Nội dung cuốn sách này tuy đã được chắt lọc qua thời gian nhưng chắc chắn vẫn còn nhiều sai sót, tôi chân thành hoan nghênh những phê bình, sửa chữa từ thầy cô và các bạn học sinh.

![Hello Algorithms](../assets/covers/chapter_hello_algo.jpg){ class="cover-image" }

<div style="text-align: center;">
    <h2 style="margin-top: 0.8em; margin-bottom: 0.8em;">Hello, Algorithms!</h2>
</div>

Sự ra đời của máy tính đã mang lại những thay đổi to lớn cho thế giới. Với khả năng tính toán tốc độ cao và khả năng lập trình tuyệt vời, chúng đã trở thành phương tiện lý tưởng để thực hiện các thuật toán và xử lý dữ liệu. Cho dù đó là đồ họa chân thực trong trò chơi điện tử, khả năng ra quyết định thông minh trong lái xe tự động, các trận đấu cờ vây xuất sắc của AlphaGo hay tương tác tự nhiên của ChatGPT, những ứng dụng này đều là những minh chứng nổi bật về thuật toán hoạt động trên máy tính.

Trên thực tế, trước khi máy tính ra đời, các thuật toán và cấu trúc dữ liệu đã tồn tại ở mọi nơi trên thế giới. Các thuật toán ban đầu tương đối đơn giản, chẳng hạn như các phương pháp đếm cổ xưa và quy trình chế tạo công cụ. Khi nền văn minh phát triển, các thuật toán dần dần trở nên tinh tế và phức tạp hơn. Từ sự khéo léo tài tình của những nghệ nhân bậc thầy, đến những sản phẩm công nghiệp giải phóng lực lượng sản xuất, đến những quy luật khoa học điều chỉnh sự vận hành của vũ trụ, đằng sau hầu hết mọi điều bình thường hay đáng kinh ngạc đều ẩn chứa tư duy thuật toán tài tình.

Tương tự, cấu trúc dữ liệu có ở khắp mọi nơi: từ mạng xã hội quy mô lớn đến hệ thống tàu điện ngầm nhỏ, nhiều hệ thống có thể được mô hình hóa dưới dạng “đồ thị”; từ quốc gia đến gia đình, các hình thức tổ chức cơ bản của xã hội đều mang đặc điểm “cây”; quần áo mùa đông giống như một “chồng”, trong đó món đồ mặc vào đầu tiên là món đồ cuối cùng được cởi ra; một ống cầu lông giống như một "hàng đợi", với các vật phẩm được đưa vào ở một đầu và lấy ra từ đầu kia; từ điển giống như một "bảng băm", cho phép tra cứu nhanh các mục đích.

Cuốn sách này nhằm mục đích giúp người đọc hiểu các khái niệm cốt lõi của thuật toán và cấu trúc dữ liệu thông qua các minh họa hoạt hình rõ ràng và dễ tiếp cận cũng như các ví dụ về mã có thể chạy được cũng như cách triển khai chúng trong mã. Dựa trên nền tảng đó, cuốn sách nỗ lực bộc lộ những biểu hiện sinh động của thuật toán trong thế giới phức tạp và giới thiệu vẻ đẹp của thuật toán. Tôi hy vọng cuốn sách này có thể giúp ích cho bạn!
