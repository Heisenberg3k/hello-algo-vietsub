# Độ phức tạp về thời gian

Thời gian chạy có thể phản ánh trực quan và chính xác hiệu quả của thuật toán. Nếu muốn ước tính chính xác thời gian chạy của một đoạn mã, chúng ta nên tiến hành như thế nào?

1. **Xác định nền tảng đang chạy**, bao gồm cấu hình phần cứng, ngôn ngữ lập trình, môi trường hệ thống, v.v. vì những yếu tố này đều ảnh hưởng đến hiệu quả thực thi mã.
2. **Đánh giá thời gian chạy cần thiết cho các hoạt động tính toán khác nhau**, ví dụ: thao tác cộng `+` yêu cầu 1 ns, thao tác nhân `*` yêu cầu 10 ns, thao tác in `print()` yêu cầu 5 ns, v.v.
3. **Đếm tất cả các thao tác tính toán trong mã** và tính tổng thời gian thực hiện của tất cả các thao tác để có được thời gian chạy.

Ví dụ: trong đoạn mã sau, kích thước dữ liệu đầu vào là $n$:

=== "Trăn"

    ```python title=""
    # On a certain running platform
    def algorithm(n: int):
        a = 2      # 1 ns
        a = a + 1  # 1 ns
        a = a * 2  # 10 ns
        # Loop n times
        for _ in range(n):  # 1 ns
            print(0)        # 5 ns
    ```

=== "C++"

    ```cpp title=""
    // On a certain running platform
    void algorithm(int n) {
        int a = 2;  // 1 ns
        a = a + 1;  // 1 ns
        a = a * 2;  // 10 ns
        // Loop n times
        for (int i = 0; i < n; i++) {  // 1 ns
            cout << 0 << endl;         // 5 ns
        }
    }
    ```

=== "Java"

    ```java title=""
    // On a certain running platform
    void algorithm(int n) {
        int a = 2;  // 1 ns
        a = a + 1;  // 1 ns
        a = a * 2;  // 10 ns
        // Loop n times
        for (int i = 0; i < n; i++) {  // 1 ns
            System.out.println(0);     // 5 ns
        }
    }
    ```

=== "C#"

    ```csharp title=""
    // On a certain running platform
    void Algorithm(int n) {
        int a = 2;  // 1 ns
        a = a + 1;  // 1 ns
        a = a * 2;  // 10 ns
        // Loop n times
        for (int i = 0; i < n; i++) {  // 1 ns
            Console.WriteLine(0);      // 5 ns
        }
    }
    ```

=== "Đi"

    ```go title=""
    // On a certain running platform
    func algorithm(n int) {
        a := 2     // 1 ns
        a = a + 1  // 1 ns
        a = a * 2  // 10 ns
        // Loop n times
        for i := 0; i < n; i++ {  // 1 ns
            fmt.Println(a)        // 5 ns
        }
    }
    ```

=== "Nhanh chóng"

    ```swift title=""
    // On a certain running platform
    func algorithm(n: Int) {
        var a = 2 // 1 ns
        a = a + 1 // 1 ns
        a = a * 2 // 10 ns
        // Loop n times
        for _ in 0 ..< n { // 1 ns
            print(0) // 5 ns
        }
    }
    ```

=== "JS"

    ```javascript title=""
    // On a certain running platform
    function algorithm(n) {
        var a = 2; // 1 ns
        a = a + 1; // 1 ns
        a = a * 2; // 10 ns
        // Loop n times
        for(let i = 0; i < n; i++) { // 1 ns
            console.log(0); // 5 ns
        }
    }
    ```

=== "TS"

    ```typescript title=""
    // On a certain running platform
    function algorithm(n: number): void {
        var a: number = 2; // 1 ns
        a = a + 1; // 1 ns
        a = a * 2; // 10 ns
        // Loop n times
        for(let i = 0; i < n; i++) { // 1 ns
            console.log(0); // 5 ns
        }
    }
    ```

=== "Phi tiêu"

    ```dart title=""
    // On a certain running platform
    void algorithm(int n) {
      int a = 2; // 1 ns
      a = a + 1; // 1 ns
      a = a * 2; // 10 ns
      // Loop n times
      for (int i = 0; i < n; i++) { // 1 ns
        print(0); // 5 ns
      }
    }
    ```

=== "Rỉ sét"

    ```rust title=""
    // On a certain running platform
    fn algorithm(n: i32) {
        let mut a = 2;      // 1 ns
        a = a + 1;          // 1 ns
        a = a * 2;          // 10 ns
        // Loop n times
        for _ in 0..n {     // 1 ns
            println!("{}", 0);  // 5 ns
        }
    }
    ```

=== "C"

    ```c title=""
    // On a certain running platform
    void algorithm(int n) {
        int a = 2;  // 1 ns
        a = a + 1;  // 1 ns
        a = a * 2;  // 10 ns
        // Loop n times
        for (int i = 0; i < n; i++) {   // 1 ns
            printf("%d", 0);            // 5 ns
        }
    }
    ```

=== "Kotlin"

    ```kotlin title=""
    // On a certain running platform
    fun algorithm(n: Int) {
        var a = 2 // 1 ns
        a = a + 1 // 1 ns
        a = a * 2 // 10 ns
        // Loop n times
        for (i in 0..<n) {  // 1 ns
            println(0)      // 5 ns
        }
    }
    ```

=== "Ruby"

    ```ruby title=""
    # On a certain running platform
    def algorithm(n)
        a = 2       # 1 ns
        a = a + 1   # 1 ns
        a = a * 2   # 10 ns
        # Loop n times
        (0...n).each do # 1 ns
            puts 0      # 5 ns
        end
    end
    ```

Theo phương pháp trên, thời gian chạy của thuật toán có thể được lấy là $(6n + 12)$ ns:

$$
1 + 1 + 10 + (1 + 5) \times n = 6n + 12
$$

Tuy nhiên, trên thực tế, **việc cố gắng tính thời gian chạy chính xác của một thuật toán là không thực tế cũng như không thực tế**. Đầu tiên, chúng tôi không muốn ràng buộc thời gian ước tính với nền tảng đang chạy, vì thuật toán cần chạy trên nhiều nền tảng khác nhau. Thứ hai, rất khó để biết thời gian chạy của từng loại hoạt động, điều này khiến quá trình ước tính trở nên vô cùng khó khăn.

## Đếm thời gian Xu hướng tăng trưởng

Phân tích độ phức tạp về thời gian không tính thời gian chạy của thuật toán, **mà tính xu hướng tăng trưởng của thời gian chạy thuật toán khi khối lượng dữ liệu tăng**.

Khái niệm “xu hướng tăng trưởng theo thời gian” khá trừu tượng; hãy để chúng tôi hiểu nó thông qua một ví dụ. Giả sử kích thước dữ liệu đầu vào là $n$ và cho ba thuật toán `A`, `B` và `C`:

=== "Trăn"

    ```python title=""
    # Time complexity of algorithm A: constant order
    def algorithm_A(n: int):
        print(0)
    # Time complexity of algorithm B: linear order
    def algorithm_B(n: int):
        for _ in range(n):
            print(0)
    # Time complexity of algorithm C: constant order
    def algorithm_C(n: int):
        for _ in range(1000000):
            print(0)
    ```

=== "C++"

    ```cpp title=""
    // Time complexity of algorithm A: constant order
    void algorithm_A(int n) {
        cout << 0 << endl;
    }
    // Time complexity of algorithm B: linear order
    void algorithm_B(int n) {
        for (int i = 0; i < n; i++) {
            cout << 0 << endl;
        }
    }
    // Time complexity of algorithm C: constant order
    void algorithm_C(int n) {
        for (int i = 0; i < 1000000; i++) {
            cout << 0 << endl;
        }
    }
    ```

=== "Java"

    ```java title=""
    // Time complexity of algorithm A: constant order
    void algorithm_A(int n) {
        System.out.println(0);
    }
    // Time complexity of algorithm B: linear order
    void algorithm_B(int n) {
        for (int i = 0; i < n; i++) {
            System.out.println(0);
        }
    }
    // Time complexity of algorithm C: constant order
    void algorithm_C(int n) {
        for (int i = 0; i < 1000000; i++) {
            System.out.println(0);
        }
    }
    ```

=== "C#"

    ```csharp title=""
    // Time complexity of algorithm A: constant order
    void AlgorithmA(int n) {
        Console.WriteLine(0);
    }
    // Time complexity of algorithm B: linear order
    void AlgorithmB(int n) {
        for (int i = 0; i < n; i++) {
            Console.WriteLine(0);
        }
    }
    // Time complexity of algorithm C: constant order
    void AlgorithmC(int n) {
        for (int i = 0; i < 1000000; i++) {
            Console.WriteLine(0);
        }
    }
    ```

=== "Đi"

    ```go title=""
    // Time complexity of algorithm A: constant order
    func algorithm_A(n int) {
        fmt.Println(0)
    }
    // Time complexity of algorithm B: linear order
    func algorithm_B(n int) {
        for i := 0; i < n; i++ {
            fmt.Println(0)
        }
    }
    // Time complexity of algorithm C: constant order
    func algorithm_C(n int) {
        for i := 0; i < 1000000; i++ {
            fmt.Println(0)
        }
    }
    ```

=== "Nhanh chóng"

    ```swift title=""
    // Time complexity of algorithm A: constant order
    func algorithmA(n: Int) {
        print(0)
    }

    // Time complexity of algorithm B: linear order
    func algorithmB(n: Int) {
        for _ in 0 ..< n {
            print(0)
        }
    }

    // Time complexity of algorithm C: constant order
    func algorithmC(n: Int) {
        for _ in 0 ..< 1_000_000 {
            print(0)
        }
    }
    ```

=== "JS"

    ```javascript title=""
    // Time complexity of algorithm A: constant order
    function algorithm_A(n) {
        console.log(0);
    }
    // Time complexity of algorithm B: linear order
    function algorithm_B(n) {
        for (let i = 0; i < n; i++) {
            console.log(0);
        }
    }
    // Time complexity of algorithm C: constant order
    function algorithm_C(n) {
        for (let i = 0; i < 1000000; i++) {
            console.log(0);
        }
    }

    ```

=== "TS"

    ```typescript title=""
    // Time complexity of algorithm A: constant order
    function algorithm_A(n: number): void {
        console.log(0);
    }
    // Time complexity of algorithm B: linear order
    function algorithm_B(n: number): void {
        for (let i = 0; i < n; i++) {
            console.log(0);
        }
    }
    // Time complexity of algorithm C: constant order
    function algorithm_C(n: number): void {
        for (let i = 0; i < 1000000; i++) {
            console.log(0);
        }
    }
    ```

=== "Phi tiêu"

    ```dart title=""
    // Time complexity of algorithm A: constant order
    void algorithmA(int n) {
      print(0);
    }
    // Time complexity of algorithm B: linear order
    void algorithmB(int n) {
      for (int i = 0; i < n; i++) {
        print(0);
      }
    }
    // Time complexity of algorithm C: constant order
    void algorithmC(int n) {
      for (int i = 0; i < 1000000; i++) {
        print(0);
      }
    }
    ```

=== "Rỉ sét"

    ```rust title=""
    // Time complexity of algorithm A: constant order
    fn algorithm_A(n: i32) {
        println!("{}", 0);
    }
    // Time complexity of algorithm B: linear order
    fn algorithm_B(n: i32) {
        for _ in 0..n {
            println!("{}", 0);
        }
    }
    // Time complexity of algorithm C: constant order
    fn algorithm_C(n: i32) {
        for _ in 0..1000000 {
            println!("{}", 0);
        }
    }
    ```

=== "C"

    ```c title=""
    // Time complexity of algorithm A: constant order
    void algorithm_A(int n) {
        printf("%d", 0);
    }
    // Time complexity of algorithm B: linear order
    void algorithm_B(int n) {
        for (int i = 0; i < n; i++) {
            printf("%d", 0);
        }
    }
    // Time complexity of algorithm C: constant order
    void algorithm_C(int n) {
        for (int i = 0; i < 1000000; i++) {
            printf("%d", 0);
        }
    }
    ```

=== "Kotlin"

    ```kotlin title=""
    // Time complexity of algorithm A: constant order
    fun algoritm_A(n: Int) {
        println(0)
    }
    // Time complexity of algorithm B: linear order
    fun algorithm_B(n: Int) {
        for (i in 0..<n){
            println(0)
        }
    }
    // Time complexity of algorithm C: constant order
    fun algorithm_C(n: Int) {
        for (i in 0..<1000000) {
            println(0)
        }
    }
    ```

=== "Ruby"

    ```ruby title=""
    # Time complexity of algorithm A: constant order
    def algorithm_A(n)
        puts 0
    end

    # Time complexity of algorithm B: linear order
    def algorithm_B(n)
        (0...n).each { puts 0 }
    end

    # Time complexity of algorithm C: constant order
    def algorithm_C(n)
        (0...1_000_000).each { puts 0 }
    end
    ```

Hình dưới đây cho thấy độ phức tạp về thời gian của ba hàm thuật toán trên.

- Thuật toán `A` chỉ có thao tác in $1$ và thời gian chạy của thuật toán không tăng khi $n$ tăng. Chúng tôi gọi độ phức tạp về thời gian của thuật toán này là "thứ tự không đổi".
- Trong thuật toán `B`, thao tác in cần lặp $n$ lần và thời gian chạy của thuật toán tăng tuyến tính khi $n$ tăng. Độ phức tạp về thời gian của thuật toán này được gọi là "thứ tự tuyến tính".
- Trong thuật toán `C`, thao tác in cần lặp $1000000$ lần. Mặc dù thời gian chạy rất dài nhưng nó độc lập với kích thước dữ liệu đầu vào $n$. Do đó, độ phức tạp về thời gian của `C` giống như `A`, vẫn là "thứ tự không đổi".

![Time growth trends of algorithms A, B, and C](time_complexity.assets/time_complexity_simple_example.png)

So với việc đếm trực tiếp thời gian chạy của thuật toán, đặc điểm của phân tích độ phức tạp thời gian là gì?

- **Độ phức tạp về thời gian có thể đánh giá hiệu quả của thuật toán một cách hiệu quả**. Ví dụ: thời gian chạy của thuật toán `B` tăng tuyến tính; khi $n > 1$ thì nó chậm hơn thuật toán `A` và khi $n > 1000000$ thì nó chậm hơn thuật toán `C`. Trên thực tế, miễn là kích thước dữ liệu đầu vào $n$ đủ lớn, thuật toán có độ phức tạp "bậc không đổi" sẽ luôn vượt trội so với thuật toán có độ phức tạp "bậc tuyến tính", đây chính xác là ý nghĩa của xu hướng tăng trưởng theo thời gian.
- **Phương pháp suy diễn độ phức tạp thời gian đơn giản hơn**. Rõ ràng, nền tảng đang chạy và các loại hoạt động tính toán đều không liên quan đến xu hướng tăng trưởng thời gian chạy của thuật toán. Do đó, trong phân tích độ phức tạp về thời gian, chúng ta có thể đơn giản coi thời gian thực hiện của tất cả các thao tác tính toán là cùng một "đơn vị thời gian", giảm việc "theo dõi thời gian chạy của từng thao tác" thành "đếm số lượng thao tác", điều này giúp giảm đáng kể độ khó của việc ước tính.
- **Độ phức tạp về thời gian cũng có những hạn chế nhất định**. Ví dụ: mặc dù các thuật toán `A` và `C` có cùng độ phức tạp về thời gian nhưng thời gian chạy thực tế của chúng khác nhau đáng kể. Tương tự, mặc dù thuật toán `B` có độ phức tạp về thời gian cao hơn `C`, nhưng khi kích thước dữ liệu đầu vào $n$ nhỏ, thuật toán `B` rõ ràng vượt trội hơn thuật toán `C`. Trong những trường hợp như vậy, thường rất khó để đánh giá hiệu quả của thuật toán chỉ dựa trên độ phức tạp về thời gian. Tất nhiên, bất chấp những vấn đề trên, phân tích độ phức tạp vẫn là phương pháp hiệu quả nhất và được sử dụng phổ biến nhất để đánh giá hiệu quả của thuật toán.

## Giới hạn trên tiệm cận của hàm

Cho một hàm có kích thước đầu vào $n$:

=== "Trăn"

    ```python title=""
    def algorithm(n: int):
        a = 1      # +1
        a = a + 1  # +1
        a = a * 2  # +1
        # Loop n times
        for i in range(n):  # +1
            print(0)        # +1
    ```

=== "C++"

    ```cpp title=""
    void algorithm(int n) {
        int a = 1;  // +1
        a = a + 1;  // +1
        a = a * 2;  // +1
        // Loop n times
        for (int i = 0; i < n; i++) { // +1 (i++ is executed each round)
            cout << 0 << endl;    // +1
        }
    }
    ```

=== "Java"

    ```java title=""
    void algorithm(int n) {
        int a = 1;  // +1
        a = a + 1;  // +1
        a = a * 2;  // +1
        // Loop n times
        for (int i = 0; i < n; i++) { // +1 (i++ is executed each round)
            System.out.println(0);    // +1
        }
    }
    ```

=== "C#"

    ```csharp title=""
    void Algorithm(int n) {
        int a = 1;  // +1
        a = a + 1;  // +1
        a = a * 2;  // +1
        // Loop n times
        for (int i = 0; i < n; i++) {   // +1 (i++ is executed each round)
            Console.WriteLine(0);   // +1
        }
    }
    ```

=== "Đi"

    ```go title=""
    func algorithm(n int) {
        a := 1      // +1
        a = a + 1   // +1
        a = a * 2   // +1
        // Loop n times
        for i := 0; i < n; i++ {   // +1
            fmt.Println(a)         // +1
        }
    }
    ```

=== "Nhanh chóng"

    ```swift title=""
    func algorithm(n: Int) {
        var a = 1 // +1
        a = a + 1 // +1
        a = a * 2 // +1
        // Loop n times
        for _ in 0 ..< n { // +1
            print(0) // +1
        }
    }
    ```

=== "JS"

    ```javascript title=""
    function algorithm(n) {
        var a = 1; // +1
        a += 1; // +1
        a *= 2; // +1
        // Loop n times
        for(let i = 0; i < n; i++){ // +1 (i++ is executed each round)
            console.log(0); // +1
        }
    }
    ```

=== "TS"

    ```typescript title=""
    function algorithm(n: number): void{
        var a: number = 1; // +1
        a += 1; // +1
        a *= 2; // +1
        // Loop n times
        for(let i = 0; i < n; i++){ // +1 (i++ is executed each round)
            console.log(0); // +1
        }
    }
    ```

=== "Phi tiêu"

    ```dart title=""
    void algorithm(int n) {
      int a = 1; // +1
      a = a + 1; // +1
      a = a * 2; // +1
      // Loop n times
      for (int i = 0; i < n; i++) { // +1 (i++ is executed each round)
        print(0); // +1
      }
    }
    ```

=== "Rỉ sét"

    ```rust title=""
    fn algorithm(n: i32) {
        let mut a = 1;   // +1
        a = a + 1;      // +1
        a = a * 2;      // +1

        // Loop n times
        for _ in 0..n { // +1 (i++ is executed each round)
            println!("{}", 0); // +1
        }
    }
    ```

=== "C"

    ```c title=""
    void algorithm(int n) {
        int a = 1;  // +1
        a = a + 1;  // +1
        a = a * 2;  // +1
        // Loop n times
        for (int i = 0; i < n; i++) {   // +1 (i++ is executed each round)
            printf("%d", 0);            // +1
        }
    }
    ```

=== "Kotlin"

    ```kotlin title=""
    fun algorithm(n: Int) {
        var a = 1 // +1
        a = a + 1 // +1
        a = a * 2 // +1
        // Loop n times
        for (i in 0..<n) { // +1 (i++ is executed each round)
            println(0) // +1
        }
    }
    ```

=== "Ruby"

    ```ruby title=""
    def algorithm(n)
        a = 1       # +1
        a = a + 1   # +1
        a = a * 2   # +1
        # Loop n times
        (0...n).each do # +1
            puts 0      # +1
        end
    end
    ```

Giả sử số lần thực hiện của thuật toán là hàm của kích thước dữ liệu đầu vào $n$, ký hiệu là $T(n)$. Khi đó số lần thực hiện của hàm trên là:

$$
T(n) = 3 + 2n
$$

$T(n)$ là một hàm tuyến tính, biểu thị rằng xu hướng tăng trưởng thời gian chạy của nó là tuyến tính và do đó độ phức tạp về thời gian của nó là bậc tuyến tính.

Chúng tôi biểu thị độ phức tạp về thời gian của thứ tự tuyến tính là $O(n)$. Ký hiệu toán học này được gọi là <u>ký hiệu big-$O$</u>, biểu thị <u>giới hạn tiệm cận trên</u> của hàm $T(n)$.

Phân tích độ phức tạp về thời gian về cơ bản tính toán giới hạn tiệm cận trên của "số phép toán $T(n)$", có định nghĩa toán học rõ ràng.

!!! lưu ý "Giới hạn trên tiệm cận của hàm số"

Nếu tồn tại các số thực dương $c$ và $n_0$ sao cho với mọi $n > n_0$, chúng ta có $T(n) \leq c \cdot f(n)$, thì $f(n)$ có thể được coi là cận trên tiệm cận của $T(n)$, ký hiệu là $T(n) = O(f(n))$.

Như thể hiện trong hình bên dưới, việc tính giới hạn trên tiệm cận là tìm một hàm $f(n)$ sao cho khi $n$ tiến tới vô cùng, $T(n)$ và $f(n)$ có cùng mức tăng trưởng, chỉ khác nhau một hệ số không đổi $c$.

![Asymptotic upper bound of a function](time_complexity.assets/asymptotic_upper_bound.png)

## Phương pháp phái sinh

Ý tưởng về giới hạn trên tiệm cận có phần mang tính toán học. Nếu bạn cảm thấy mình chưa hiểu hết về nó, đừng lo lắng. Trước tiên chúng ta có thể nắm vững phương pháp đạo hàm và dần dần nắm bắt được ý nghĩa toán học của nó thông qua thực hành liên tục.

Theo định nghĩa, sau khi xác định $f(n)$, chúng ta có thể thu được độ phức tạp thời gian $O(f(n))$. Vậy làm cách nào để xác định giới hạn trên tiệm cận $f(n)$? Nhìn chung, nó được chia thành hai bước: đầu tiên đếm số lượng thao tác, sau đó xác định giới hạn tiệm cận trên.

### Bước 1: Đếm Số Thao Tác

Đối với mã, đếm từ trên xuống dưới theo dòng. Tuy nhiên, vì hệ số không đổi $c$ trong $c \cdot f(n)$ ở trên có thể có kích thước bất kỳ, **các hệ số và số hạng không đổi trong số lượng phép toán $T(n)$ đều có thể bị bỏ qua**. Theo nguyên tắc này, có thể tóm tắt các kỹ thuật đơn giản hóa việc đếm sau đây.

1. **Bỏ qua các hằng số trong $T(n)$**. Vì chúng đều độc lập với $n$ nên chúng không ảnh hưởng đến độ phức tạp về thời gian.
2. **Bỏ qua tất cả các hệ số**. Ví dụ: lặp $2n$ lần, $5n + 1$ lần, v.v., tất cả đều có thể được đơn giản hóa thành $n$ lần, vì hệ số trước $n$ không ảnh hưởng đến độ phức tạp về thời gian.
3. **Sử dụng phép nhân cho các vòng lặp lồng nhau**. Tổng số thao tác bằng tích của số thao tác ở vòng lặp bên ngoài và vòng lặp bên trong, với mỗi lớp vòng lặp vẫn có thể áp dụng các kỹ thuật `1.` và `2.` riêng biệt.

Cho một hàm, chúng ta có thể sử dụng các kỹ thuật trên để đếm số lượng thao tác:

=== "Trăn"

    ```python title=""
    def algorithm(n: int):
        a = 1      # +0 (Technique 1)
        a = a + n  # +0 (Technique 1)
        # +n (Technique 2)
        for i in range(5 * n + 1):
            print(0)
        # +n*n (Technique 3)
        for i in range(2 * n):
            for j in range(n + 1):
                print(0)
    ```

=== "C++"

    ```cpp title=""
    void algorithm(int n) {
        int a = 1;  // +0 (Technique 1)
        a = a + n;  // +0 (Technique 1)
        // +n (Technique 2)
        for (int i = 0; i < 5 * n + 1; i++) {
            cout << 0 << endl;
        }
        // +n*n (Technique 3)
        for (int i = 0; i < 2 * n; i++) {
            for (int j = 0; j < n + 1; j++) {
                cout << 0 << endl;
            }
        }
    }
    ```

=== "Java"

    ```java title=""
    void algorithm(int n) {
        int a = 1;  // +0 (Technique 1)
        a = a + n;  // +0 (Technique 1)
        // +n (Technique 2)
        for (int i = 0; i < 5 * n + 1; i++) {
            System.out.println(0);
        }
        // +n*n (Technique 3)
        for (int i = 0; i < 2 * n; i++) {
            for (int j = 0; j < n + 1; j++) {
                System.out.println(0);
            }
        }
    }
    ```

=== "C#"

    ```csharp title=""
    void Algorithm(int n) {
        int a = 1;  // +0 (Technique 1)
        a = a + n;  // +0 (Technique 1)
        // +n (Technique 2)
        for (int i = 0; i < 5 * n + 1; i++) {
            Console.WriteLine(0);
        }
        // +n*n (Technique 3)
        for (int i = 0; i < 2 * n; i++) {
            for (int j = 0; j < n + 1; j++) {
                Console.WriteLine(0);
            }
        }
    }
    ```

=== "Đi"

    ```go title=""
    func algorithm(n int) {
        a := 1     // +0 (Technique 1)
        a = a + n  // +0 (Technique 1)
        // +n (Technique 2)
        for i := 0; i < 5 * n + 1; i++ {
            fmt.Println(0)
        }
        // +n*n (Technique 3)
        for i := 0; i < 2 * n; i++ {
            for j := 0; j < n + 1; j++ {
                fmt.Println(0)
            }
        }
    }
    ```

=== "Nhanh chóng"

    ```swift title=""
    func algorithm(n: Int) {
        var a = 1 // +0 (Technique 1)
        a = a + n // +0 (Technique 1)
        // +n (Technique 2)
        for _ in 0 ..< (5 * n + 1) {
            print(0)
        }
        // +n*n (Technique 3)
        for _ in 0 ..< (2 * n) {
            for _ in 0 ..< (n + 1) {
                print(0)
            }
        }
    }
    ```

=== "JS"

    ```javascript title=""
    function algorithm(n) {
        let a = 1;  // +0 (Technique 1)
        a = a + n;  // +0 (Technique 1)
        // +n (Technique 2)
        for (let i = 0; i < 5 * n + 1; i++) {
            console.log(0);
        }
        // +n*n (Technique 3)
        for (let i = 0; i < 2 * n; i++) {
            for (let j = 0; j < n + 1; j++) {
                console.log(0);
            }
        }
    }
    ```

=== "TS"

    ```typescript title=""
    function algorithm(n: number): void {
        let a = 1;  // +0 (Technique 1)
        a = a + n;  // +0 (Technique 1)
        // +n (Technique 2)
        for (let i = 0; i < 5 * n + 1; i++) {
            console.log(0);
        }
        // +n*n (Technique 3)
        for (let i = 0; i < 2 * n; i++) {
            for (let j = 0; j < n + 1; j++) {
                console.log(0);
            }
        }
    }
    ```

=== "Phi tiêu"

    ```dart title=""
    void algorithm(int n) {
      int a = 1; // +0 (Technique 1)
      a = a + n; // +0 (Technique 1)
      // +n (Technique 2)
      for (int i = 0; i < 5 * n + 1; i++) {
        print(0);
      }
      // +n*n (Technique 3)
      for (int i = 0; i < 2 * n; i++) {
        for (int j = 0; j < n + 1; j++) {
          print(0);
        }
      }
    }
    ```

=== "Rỉ sét"

    ```rust title=""
    fn algorithm(n: i32) {
        let mut a = 1;     // +0 (Technique 1)
        a = a + n;        // +0 (Technique 1)

        // +n (Technique 2)
        for i in 0..(5 * n + 1) {
            println!("{}", 0);
        }

        // +n*n (Technique 3)
        for i in 0..(2 * n) {
            for j in 0..(n + 1) {
                println!("{}", 0);
            }
        }
    }
    ```

=== "C"

    ```c title=""
    void algorithm(int n) {
        int a = 1;  // +0 (Technique 1)
        a = a + n;  // +0 (Technique 1)
        // +n (Technique 2)
        for (int i = 0; i < 5 * n + 1; i++) {
            printf("%d", 0);
        }
        // +n*n (Technique 3)
        for (int i = 0; i < 2 * n; i++) {
            for (int j = 0; j < n + 1; j++) {
                printf("%d", 0);
            }
        }
    }
    ```

=== "Kotlin"

    ```kotlin title=""
    fun algorithm(n: Int) {
        var a = 1   // +0 (Technique 1)
        a = a + n   // +0 (Technique 1)
        // +n (Technique 2)
        for (i in 0..<5 * n + 1) {
            println(0)
        }
        // +n*n (Technique 3)
        for (i in 0..<2 * n) {
            for (j in 0..<n + 1) {
                println(0)
            }
        }
    }
    ```

=== "Ruby"

    ```ruby title=""
    def algorithm(n)
        a = 1       # +0 (Technique 1)
        a = a + n   # +0 (Technique 1)
        # +n (Technique 2)
        (0...(5 * n + 1)).each do { puts 0 }
        # +n*n (Technique 3)
        (0...(2 * n)).each do
            (0...(n + 1)).each do { puts 0 }
        end
    end
    ```

Công thức sau đây thể hiện kết quả đếm trước và sau khi sử dụng các kỹ thuật trên; cả hai đều có độ phức tạp về thời gian là $O(n^2)$.

$$
\bắt đầu{căn chỉnh}
T(n) & = 2n(n + 1) + (5n + 1) + 2 & \text{Đếm đầy đủ (-.-|||)} \newline
& = 2n^2 + 7n + 3 \newline
T(n) & = n^2 + n & \text{Số đơn giản hóa (o.O)}
\end{căn chỉnh}
$$

### Bước 2: Xác định giới hạn tiệm cận trên

**Độ phức tạp về thời gian được xác định bởi số hạng có thứ tự cao nhất trong $T(n)$**. Điều này là do khi $n$ tiến tới vô cùng, số hạng bậc cao nhất sẽ đóng vai trò chủ đạo và ảnh hưởng của các số hạng khác có thể bị bỏ qua.

Bảng dưới đây trình bày một số ví dụ, trong đó một số giá trị phóng đại được sử dụng để nhấn mạnh kết luận rằng "các hệ số không thể làm lung lay trật tự". Khi $n$ tiến tới vô cùng, các hằng số này trở nên không có ý nghĩa.

<p align="center"> Table <id> &nbsp; Time complexities corresponding to different numbers of operations </p>

| Số lượng hoạt động $T(n)$ | Độ phức tạp thời gian $O(f(n))$ |
| ---------------------- | -------------------- |
| $100000$ | $O(1)$ |
| $3n + 2$ | $O(n)$ |
| $2n^2 + 3n + 2$ | $O(n^2)$ |
| $n^3 + 10000n^2$ | $O(n^3)$ |
| $2^n + 10000n^{10000}$ | $O(2^n)$ |

## Các loại phổ biến

Đặt kích thước dữ liệu đầu vào là $n$. Các loại độ phức tạp thời gian phổ biến được thể hiện trong hình bên dưới (sắp xếp theo thứ tự từ thấp đến cao).

$$
\bắt đầu{căn chỉnh}
& O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(2^n) < O(n!) \newline
& \text{Hằng số} < \text{Logarit} < \text{Tuyến tính} < \text{Số tuyến tính} < \text{Quadratic} < \text{Exentials} < \text{Factorial}
\end{căn chỉnh}
$$

![Common time complexity types](time_complexity.assets/time_complexity_common_types.png)

### Lệnh cố định $O(1)$

Số lượng thao tác theo thứ tự không đổi không phụ thuộc vào kích thước dữ liệu đầu vào $n$, nghĩa là nó không thay đổi khi $n$ thay đổi.

Trong hàm sau, mặc dù giá trị của `size` có thể lớn, nhưng nó độc lập với kích thước dữ liệu đầu vào $n$, do đó độ phức tạp về thời gian vẫn là $O(1)$:

```src
[file]{time_complexity}-[class]{}-[func]{constant}
```

### Thứ tự tuyến tính $O(n)$

Số lượng thao tác theo thứ tự tuyến tính tăng tuyến tính tương ứng với kích thước dữ liệu đầu vào $n$. Thứ tự tuyến tính thường xuất hiện trong các vòng lặp một lớp:

```src
[file]{time_complexity}-[class]{}-[func]{linear}
```

Các hoạt động như duyệt mảng và duyệt danh sách liên kết có độ phức tạp về thời gian là $O(n)$, trong đó $n$ là độ dài của mảng hoặc danh sách liên kết:

```src
[file]{time_complexity}-[class]{}-[func]{array_traversal}
```

Điều đáng lưu ý là **kích thước dữ liệu đầu vào $n$ phải được xác định theo loại dữ liệu đầu vào**. Ví dụ, trong ví dụ đầu tiên, biến $n$ là kích thước dữ liệu đầu vào; trong ví dụ thứ hai, độ dài mảng $n$ là kích thước dữ liệu.

### Thứ tự bậc hai $O(n^2)$

Số lượng phép toán theo thứ tự bậc hai tăng theo bậc hai tương ứng với kích thước dữ liệu đầu vào $n$. Thứ tự bậc hai thường xuất hiện trong các vòng lặp lồng nhau, trong đó cả vòng lặp bên ngoài và bên trong đều có độ phức tạp về thời gian là $O(n)$, dẫn đến độ phức tạp về thời gian tổng thể là $O(n^2)$:

```src
[file]{time_complexity}-[class]{}-[func]{quadratic}
```

Hình dưới đây so sánh độ phức tạp về thời gian của bậc không đổi, bậc tuyến tính và bậc hai.

![Time complexities of constant, linear, and quadratic orders](time_complexity.assets/time_complexity_constant_linear_quadratic.png)

Lấy tính năng sắp xếp bong bóng làm ví dụ, vòng lặp bên ngoài thực hiện $n - 1$ lần và vòng lặp bên trong thực hiện $n-1$, $n-2$, $\dots$, $2$, $1$ lần, trung bình là $n / 2$ lần, dẫn đến độ phức tạp về thời gian là $O((n - 1) n / 2) = O(n^2)$:

```src
[file]{time_complexity}-[class]{}-[func]{bubble_sort}
```

### Thứ tự hàm mũ $O(2^n)$

"Sự phân chia tế bào" sinh học là một ví dụ điển hình của sự tăng trưởng theo cấp số nhân: trạng thái ban đầu là ô $1$, sau một lần phân chia nó trở thành $2$, sau hai vòng nó trở thành $4$, v.v.; sau $n$ vòng chia sẽ có $2^n$ ô.

Hình bên dưới và đoạn mã sau mô phỏng quá trình phân chia ô, với độ phức tạp về thời gian là $O(2^n)$. Lưu ý rằng đầu vào $n$ biểu thị số vòng chia và giá trị trả về `count` biểu thị tổng số phép chia.

```src
[file]{time_complexity}-[class]{}-[func]{exponential}
```

![Time complexity of exponential order](time_complexity.assets/time_complexity_exponential.png)

Trong các thuật toán thực tế, bậc mũ thường xuất hiện ở các hàm đệ quy. Ví dụ: trong đoạn mã sau, nó chia đệ quy thành hai, dừng sau khi chia $n$:

```src
[file]{time_complexity}-[class]{}-[func]{exp_recur}
```

Tăng trưởng thứ tự theo cấp số nhân rất nhanh và phổ biến trong các phương pháp toàn diện (tìm kiếm vũ phu, quay lui, v.v.). Đối với các bài toán có quy mô dữ liệu lớn, thứ tự hàm mũ là không thể chấp nhận được và thường yêu cầu lập trình động hoặc thuật toán tham lam để giải.

### Thứ tự logarit $O(\log n)$

Ngược lại với thứ tự hàm mũ, thứ tự logarit phản ánh tình trạng “mỗi vòng giảm đi một nửa”. Đặt kích thước dữ liệu đầu vào là $n$. Vì mỗi vòng giảm xuống còn một nửa nên số vòng lặp là $\log_2 n$, đây là hàm nghịch đảo của $2^n$.

Hình bên dưới và đoạn mã sau mô phỏng quá trình "giảm xuống còn một nửa mỗi vòng", với độ phức tạp về thời gian là $O(\log_2 n)$, viết tắt là $O(\log n)$:

```src
[file]{time_complexity}-[class]{}-[func]{logarithmic}
```

![Time complexity of logarithmic order](time_complexity.assets/time_complexity_logarithmic.png)

Giống như cấp số mũ, cấp số logarit cũng thường xuất hiện trong các hàm đệ quy. Đoạn mã sau tạo thành một cây đệ quy có chiều cao $\log_2 n$:

```src
[file]{time_complexity}-[class]{}-[func]{log_recur}
```

Thứ tự logarit thường xuất hiện trong các thuật toán dựa trên chiến lược chia để trị, phản ánh ý tưởng liên tục chia tách một vấn đề và đơn giản hóa nó. Nó phát triển chậm và là độ phức tạp thời gian lý tưởng chỉ đứng sau thứ tự không đổi.

!!! mẹo "Cơ số của $O(\log n)$ là gì?"

Nói chính xác, "chia thành $m$" tương ứng với độ phức tạp về thời gian là $O(\log_m n)$. Và thông qua công thức thay đổi cơ số logarit, chúng ta có thể thu được độ phức tạp về thời gian với các cơ số khác nhau bằng nhau:

$$
    O(\log_m n) = O(\log_k n / \log_k m) = O(\log_k n)
    $$

Nghĩa là, cơ số $m$ có thể được chuyển đổi mà không ảnh hưởng đến độ phức tạp. Do đó, chúng ta thường bỏ qua cơ số $m$ và biểu thị bậc logarit đơn giản là $O(\log n)$.

### Thứ tự tuyến tính $O(n \log n)$

Thứ tự tuyến tính thường xuất hiện trong các vòng lặp lồng nhau, trong đó độ phức tạp về thời gian của hai lớp vòng lặp lần lượt là $O(\log n)$ và $O(n)$. Mã có liên quan như sau:

```src
[file]{time_complexity}-[class]{}-[func]{linear_log_recur}
```

Hình dưới đây cho thấy thứ tự tuyến tính được tạo ra như thế nào. Mỗi cấp độ của cây nhị phân có tổng cộng $n$ phép toán và cây có các cấp độ $\log_2 n + 1$, dẫn đến độ phức tạp về thời gian là $O(n \log n)$.

![Time complexity of linearithmic order](time_complexity.assets/time_complexity_logarithmic_linear.png)

Các thuật toán sắp xếp chính thống thường có độ phức tạp về thời gian là $O(n \log n)$, chẳng hạn như sắp xếp nhanh, sắp xếp hợp nhất và sắp xếp vùng heap.

### Thứ tự giai thừa $O(n!)$

Thứ tự giai thừa tương ứng với bài toán “hoán vị” toán học. Cho $n$ phần tử riêng biệt, tìm tất cả các sơ đồ hoán vị có thể có; số phương án là:

$$
n! = n \times (n - 1) \times (n - 2) \times \dots \times 2 \times 1
$$

Giai thừa thường được thực hiện bằng cách sử dụng đệ quy. Như được hiển thị trong hình bên dưới và đoạn mã sau, cấp độ đầu tiên chia thành các nhánh $n$, cấp độ thứ hai chia thành các nhánh $n - 1$, v.v., cho đến khi cấp $n$-th khi quá trình phân tách dừng lại:

```src
[file]{time_complexity}-[class]{}-[func]{factorial_recur}
```

![Time complexity of factorial order](time_complexity.assets/time_complexity_factorial.png)

Lưu ý rằng vì khi $n \geq 4$ chúng ta luôn có $n! > 2^n$, thứ tự giai thừa tăng nhanh hơn thứ tự hàm mũ và cũng không được chấp nhận đối với $n$ lớn.

## Độ phức tạp về thời gian tệ nhất, tốt nhất và trung bình

**Hiệu quả về thời gian của một thuật toán thường không cố định mà liên quan đến việc phân phối dữ liệu đầu vào**. Giả sử chúng ta nhập một mảng `nums` có độ dài $n$, trong đó `nums` bao gồm các số từ $1$ đến $n$, với mỗi số chỉ xuất hiện một lần, nhưng thứ tự phần tử được xáo trộn ngẫu nhiên. Nhiệm vụ là trả về chỉ mục của phần tử $1$. Chúng ta có thể rút ra kết luận sau đây.

- Khi `nums = [?, ?, ..., 1]`, tức là khi phần tử cuối cùng là $1$, nó yêu cầu duyệt toàn bộ mảng, **đạt độ phức tạp về thời gian trong trường hợp xấu nhất $O(n)$**.
- Khi `nums = [1, ?, ?, ...]`, tức là khi phần tử đầu tiên là $1$, bất kể mảng dài bao nhiêu, không cần tiếp tục duyệt, **đạt độ phức tạp thời gian trong trường hợp tốt nhất $\Omega(1)$**.

"Độ phức tạp về thời gian trong trường hợp xấu nhất" tương ứng với cận trên tiệm cận của hàm, được biểu thị bằng ký hiệu big-$O$. Tương ứng, "độ phức tạp thời gian trong trường hợp tốt nhất" tương ứng với cận dưới tiệm cận của hàm, được biểu thị bằng ký hiệu $\Omega$:

```src
[file]{worst_best_time_complexity}-[class]{}-[func]{find_one}
```

Điều đáng lưu ý là chúng ta hiếm khi sử dụng độ phức tạp về thời gian trong trường hợp tốt nhất trong thực tế, bởi vì nó thường chỉ có thể đạt được với xác suất rất nhỏ và có thể gây hiểu nhầm đôi chút. **Độ phức tạp về thời gian trong trường hợp xấu nhất thực tế hơn vì nó mang lại giá trị an toàn về hiệu quả**, cho phép chúng tôi sử dụng thuật toán một cách tự tin.

Từ ví dụ trên, chúng ta có thể thấy rằng cả độ phức tạp về thời gian trong trường hợp xấu nhất và trường hợp tốt nhất chỉ phát sinh dưới các phân phối đầu vào cụ thể, có thể xảy ra với xác suất rất thấp và có thể không phản ánh thực sự hiệu quả hoạt động của thuật toán. Ngược lại, **độ phức tạp về thời gian trung bình có thể phản ánh hiệu quả hoạt động của thuật toán trong dữ liệu đầu vào ngẫu nhiên**, được biểu thị bằng ký hiệu $\Theta$.

Đối với một số thuật toán, chúng ta có thể rút ra trường hợp trung bình một cách đơn giản theo phân phối dữ liệu ngẫu nhiên. Ví dụ: trong ví dụ trên, do mảng đầu vào bị xáo trộn nên xác suất phần tử $1$ xuất hiện ở bất kỳ chỉ mục nào là bằng nhau, do đó số vòng lặp trung bình của thuật toán bằng một nửa độ dài mảng $n / 2$, cho độ phức tạp thời gian trung bình là $\Theta(n / 2) = \Theta(n)$.

Nhưng đối với các thuật toán phức tạp hơn, việc tính toán độ phức tạp thời gian trung bình thường khá khó khăn, vì khó có thể phân tích kỳ vọng toán học tổng thể theo phân phối dữ liệu. Trong trường hợp này, chúng tôi thường sử dụng độ phức tạp về thời gian trong trường hợp xấu nhất làm tiêu chí để đánh giá hiệu quả của thuật toán.

!!! câu hỏi "Tại sao biểu tượng $\Theta$ hiếm khi được nhìn thấy?"

Điều này có thể là do ký hiệu $O$ quá bắt mắt nên chúng ta thường sử dụng nó để thể hiện độ phức tạp về thời gian trung bình. Nhưng nói đúng ra, cách thực hành này không phải là tiêu chuẩn. Trong cuốn sách này và các tài liệu khác, nếu bạn gặp những biểu thức như "độ phức tạp thời gian trung bình $O(n)$", vui lòng hiểu trực tiếp là $\Theta(n)$.
