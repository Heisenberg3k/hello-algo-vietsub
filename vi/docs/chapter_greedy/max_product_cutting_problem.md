# Vấn đề cắt giảm sản phẩm tối đa

!!! câu hỏi

Cho một số nguyên dương $n$, chia nó thành tổng của ít nhất hai số nguyên dương và tìm tích lớn nhất của các số nguyên thu được, như minh họa trong hình bên dưới.

![Problem definition of max product cutting](max_product_cutting_problem.assets/max_product_cutting_definition.png)

Giả sử chúng ta chia $n$ thành $m$ thừa số nguyên, trong đó thừa số $i$-th được ký hiệu là $n_i$, nghĩa là

$$
n = \sum_{i=1}^{m}n_i
$$

Mục tiêu của bài toán này là tìm tích lớn nhất của tất cả các thừa số nguyên, cụ thể là

$$
\max(\prod_{i=1}^{m}n_i)
$$

Chúng ta cần xác định nên có bao nhiêu phần $m$ và mỗi phần $n_i$ nên là bao nhiêu.

### Xác định chiến lược tham lam

Theo nguyên tắc chung, tích của hai số nguyên thường lớn hơn tổng của chúng. Giả sử chúng ta tách hệ số $2$ khỏi $n$; sản phẩm thu được là $2(n-2)$. Chúng tôi so sánh sản phẩm này với $n$:

$$
\begin{aligned}
2(n-2) & \geq n \newline
2n - n - 4 & \geq 0 \newline
n & \geq 4
\end{aligned}
$$

Như được hiển thị trong hình bên dưới, khi $n \geq 4$, việc tách $2$ sẽ làm tăng tích, **điều này cho biết rằng các số nguyên lớn hơn hoặc bằng $4$ đều phải được chia**.

**Chiến lược tham lam thứ nhất**: Nếu sơ đồ phân tách chứa hệ số $\geq 4$, thì cần phân chia thêm. Sơ đồ phân tách cuối cùng chỉ nên chứa các thừa số $1$, $2$ và $3$.

![Splitting causes product to increase](max_product_cutting_problem.assets/max_product_cutting_greedy_infer1.png)

Tiếp theo, hãy xem xét yếu tố nào là tối ưu. Trong ba thừa số $1$, $2$ và $3$, rõ ràng $1$ là tệ nhất, vì $1 \times (n-1) < n$ luôn giữ nguyên, nghĩa là việc tách $1$ thực tế sẽ làm giảm tích số.

Như thể hiện trong hình bên dưới, khi $n = 6$, chúng ta có $3 \times 3 > 2 \times 2 \times 2$. **Điều này có nghĩa là việc chia $3$ sẽ tốt hơn việc tách $2$**.

**Chiến lược tham lam hai**: Trong sơ đồ chia tách, chỉ nên có tối đa hai $2$, vì ba $2$ luôn có thể được thay thế bằng hai $3$ để có được sản phẩm lớn hơn.

![Optimal splitting factor](max_product_cutting_problem.assets/max_product_cutting_greedy_infer2.png)

Tóm lại, có thể rút ra các chiến lược tham lam sau đây.

1. Nhập số nguyên $n$, chia liên tục thừa số $3$ cho đến khi còn lại là $0$, $1$, hoặc $2$.
2. Khi số dư là $0$, điều đó có nghĩa là $n$ là bội số của $3$, do đó không cần thực hiện thêm hành động nào.
3. Khi còn lại $2$ thì không chia thêm; giữ nó như cũ.
4. Khi số dư là $1$, vì $2 \times 2 > 1 \times 3$, hãy thay thế $3$ cuối cùng và $1$ còn lại bằng hai $2$s.

### Triển khai mã

Như thể hiện trong hình bên dưới, chúng ta không cần vòng lặp để chia số nguyên. Thay vào đó, chúng ta sử dụng phép chia số nguyên để thu được số $3$s, ký hiệu là $a$, và phép toán modulo để thu được số $b$ còn lại, cho:

$$
n = 3 a + b
$$

Xin lưu ý rằng đối với trường hợp cạnh của $n \leq 3$, $1$ phải được tách ra, với tích $1 \times (n - 1)$.

=== "Python"
    ```python title="max_product_cutting.py"
    def max_product_cutting(n: int) -> int:
        """Max product cutting: Greedy algorithm"""
        # When n <= 3, must cut out a 1
        if n <= 3:
            return 1 * (n - 1)
        # Greedily cut out 3, a is the number of 3s, b is the remainder
        a, b = n // 3, n % 3
        if b == 1:
            # When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
            return int(math.pow(3, a - 1)) * 2 * 2
        if b == 2:
            # When the remainder is 2, do nothing
            return int(math.pow(3, a)) * 2
        # When the remainder is 0, do nothing
        return int(math.pow(3, a))
    ```
=== "C++"
    ```cpp title="max_product_cutting.cpp"
    int maxProductCutting(int n) {
        // When n <= 3, must cut out a 1
        if (n <= 3) {
            return 1 * (n - 1);
        }
        // Greedily cut out 3, a is the number of 3s, b is the remainder
        int a = n / 3;
        int b = n % 3;
        if (b == 1) {
            // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
            return (int)pow(3, a - 1) * 2 * 2;
        }
        if (b == 2) {
            // When the remainder is 2, do nothing
            return (int)pow(3, a) * 2;
        }
        // When the remainder is 0, do nothing
        return (int)pow(3, a);
    }
    ```
=== "Java"
    ```java title="max_product_cutting.java"
    public class max_product_cutting {
        /* Max product cutting: Greedy algorithm */
        public static int maxProductCutting(int n) {
            // When n <= 3, must cut out a 1
            if (n <= 3) {
                return 1 * (n - 1);
            }
            // Greedily cut out 3, a is the number of 3s, b is the remainder
            int a = n / 3;
            int b = n % 3;
            if (b == 1) {
                // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
                return (int) Math.pow(3, a - 1) * 2 * 2;
            }
            if (b == 2) {
                // When the remainder is 2, do nothing
                return (int) Math.pow(3, a) * 2;
            }
            // When the remainder is 0, do nothing
            return (int) Math.pow(3, a);
        }
    
        public static void main(String[] args) {
            int n = 58;
    
            // Greedy algorithm
            int res = maxProductCutting(n);
            System.out.println("Maximum cutting product is " + res);
        }
    }
    ```
=== "C#"
    ```csharp title="max_product_cutting.cs"
    public class max_product_cutting {
        /* Max product cutting: Greedy algorithm */
        int MaxProductCutting(int n) {
            // When n <= 3, must cut out a 1
            if (n <= 3) {
                return 1 * (n - 1);
            }
            // Greedily cut out 3, a is the number of 3s, b is the remainder
            int a = n / 3;
            int b = n % 3;
            if (b == 1) {
                // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
                return (int)Math.Pow(3, a - 1) * 2 * 2;
            }
            if (b == 2) {
                // When the remainder is 2, do nothing
                return (int)Math.Pow(3, a) * 2;
            }
            // When the remainder is 0, do nothing
            return (int)Math.Pow(3, a);
        }
    
        [Test]
        public void Test() {
            int n = 58;
    
            // Greedy algorithm
            int res = MaxProductCutting(n);
            Console.WriteLine("Maximum cutting product is" + res);
        }
    }
    ```
=== "Go"
    ```go title="max_product_cutting.go"
    func maxProductCutting(n int) int {
    	// When n <= 3, must cut out a 1
    	if n <= 3 {
    		return 1 * (n - 1)
    	}
    	// Greedily cut out 3, a is the number of 3s, b is the remainder
    	a := n / 3
    	b := n % 3
    	if b == 1 {
    		// When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
    		return int(math.Pow(3, float64(a-1))) * 2 * 2
    	}
    	if b == 2 {
    		// When the remainder is 2, do nothing
    		return int(math.Pow(3, float64(a))) * 2
    	}
    	// When the remainder is 0, do nothing
    	return int(math.Pow(3, float64(a)))
    }
    ```
=== "Swift"
    ```swift title="max_product_cutting.swift"
    func maxProductCutting(n: Int) -> Int {
        // When n <= 3, must cut out a 1
        if n <= 3 {
            return 1 * (n - 1)
        }
        // Greedily cut out 3, a is the number of 3s, b is the remainder
        let a = n / 3
        let b = n % 3
        if b == 1 {
            // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
            return pow(3, a - 1) * 2 * 2
        }
        if b == 2 {
            // When the remainder is 2, do nothing
            return pow(3, a) * 2
        }
        // When the remainder is 0, do nothing
        return pow(3, a)
    }
    ```
=== "JS"
    ```javascript title="max_product_cutting.js"
    function maxProductCutting(n) {
        // When n <= 3, must cut out a 1
        if (n <= 3) {
            return 1 * (n - 1);
        }
        // Greedily cut out 3, a is the number of 3s, b is the remainder
        let a = Math.floor(n / 3);
        let b = n % 3;
        if (b === 1) {
            // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
            return Math.pow(3, a - 1) * 2 * 2;
        }
        if (b === 2) {
            // When the remainder is 2, do nothing
            return Math.pow(3, a) * 2;
        }
        // When the remainder is 0, do nothing
        return Math.pow(3, a);
    }
    ```
=== "TS"
    ```typescript title="max_product_cutting.ts"
    function maxProductCutting(n: number): number {
        // When n <= 3, must cut out a 1
        if (n <= 3) {
            return 1 * (n - 1);
        }
        // Greedily cut out 3, a is the number of 3s, b is the remainder
        let a: number = Math.floor(n / 3);
        let b: number = n % 3;
        if (b === 1) {
            // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
            return Math.pow(3, a - 1) * 2 * 2;
        }
        if (b === 2) {
            // When the remainder is 2, do nothing
            return Math.pow(3, a) * 2;
        }
        // When the remainder is 0, do nothing
        return Math.pow(3, a);
    }
    ```
=== "Dart"
    ```dart title="max_product_cutting.dart"
    int maxProductCutting(int n) {
      // When n <= 3, must cut out a 1
      if (n <= 3) {
        return 1 * (n - 1);
      }
      // Greedily cut out 3, a is the number of 3s, b is the remainder
      int a = n ~/ 3;
      int b = n % 3;
      if (b == 1) {
        // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
        return (pow(3, a - 1) * 2 * 2).toInt();
      }
      if (b == 2) {
        // When the remainder is 2, do nothing
        return (pow(3, a) * 2).toInt();
      }
      // When the remainder is 0, do nothing
      return pow(3, a).toInt();
    }
    ```
=== "Rust"
    ```rust title="max_product_cutting.rs"
    fn max_product_cutting(n: i32) -> i32 {
        // When n <= 3, must cut out a 1
        if n <= 3 {
            return 1 * (n - 1);
        }
        // Greedily cut out 3, a is the number of 3s, b is the remainder
        let a = n / 3;
        let b = n % 3;
        if b == 1 {
            // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
            3_i32.pow(a as u32 - 1) * 2 * 2
        } else if b == 2 {
            // When the remainder is 2, do nothing
            3_i32.pow(a as u32) * 2
        } else {
            // When the remainder is 0, do nothing
            3_i32.pow(a as u32)
        }
    }
    ```
=== "C"
    ```c title="max_product_cutting.c"
    int maxProductCutting(int n) {
        // When n <= 3, must cut out a 1
        if (n <= 3) {
            return 1 * (n - 1);
        }
        // Greedily cut out 3, a is the number of 3s, b is the remainder
        int a = n / 3;
        int b = n % 3;
        if (b == 1) {
            // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
            return pow(3, a - 1) * 2 * 2;
        }
        if (b == 2) {
            // When the remainder is 2, do nothing
            return pow(3, a) * 2;
        }
        // When the remainder is 0, do nothing
        return pow(3, a);
    }
    ```
=== "Kotlin"
    ```kotlin title="max_product_cutting.kt"
    fun maxProductCutting(n: Int): Int {
        // When n <= 3, must cut out a 1
        if (n <= 3) {
            return 1 * (n - 1)
        }
        // Greedily cut out 3, a is the number of 3s, b is the remainder
        val a = n / 3
        val b = n % 3
        if (b == 1) {
            // When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
            return 3.0.pow((a - 1)).toInt() * 2 * 2
        }
        if (b == 2) {
            // When the remainder is 2, do nothing
            return 3.0.pow(a).toInt() * 2 * 2
        }
        // When the remainder is 0, do nothing
        return 3.0.pow(a).toInt()
    }
    ```
=== "Ruby"
    ```ruby title="max_product_cutting.rb"
    ### Maximum cutting product: greedy ###
    def max_product_cutting(n)
      # When n <= 3, must cut out a 1
      return 1 * (n - 1) if n <= 3
      # Greedily cut out 3, a is the number of 3s, b is the remainder
      a, b = n / 3, n % 3
      # When the remainder is 1, convert a pair of 1 * 3 to 2 * 2
      return (3.pow(a - 1) * 2 * 2).to_i if b == 1
      # When the remainder is 2, do nothing
      return (3.pow(a) * 2).to_i if b == 2
      # When the remainder is 0, do nothing
      3.pow(a).to_i
    ```


![Calculation method for max product cutting](max_product_cutting_problem.assets/max_product_cutting_greedy_calculation.png)

**Độ phức tạp về thời gian phụ thuộc vào cách thực hiện phép lũy thừa trong ngôn ngữ lập trình**. Lấy Python làm ví dụ, có ba cách thường được sử dụng để tính lũy thừa.

- Cả toán tử `**` và hàm `pow()` đều có độ phức tạp về thời gian $O(\log⁡ a)$.
- Hàm `math.pow()` gọi nội bộ hàm `pow()` của thư viện C, hàm này thực hiện phép tính lũy thừa dấu phẩy động, với độ phức tạp về thời gian $O(1)$.

Các biến $a$ và $b$ sử dụng một lượng không gian bổ sung không đổi, **do đó độ phức tạp của không gian là $O(1)$**.

### Bằng chứng về tính đúng đắn

Chúng ta sử dụng chứng minh phản chứng và chỉ xét trường hợp $n \geq 4$.

1. **Tất cả các thừa số $\leq 3$**: Giả sử sơ đồ phân chia tối ưu bao gồm một thừa số $x \geq 4$. Sau đó, nó có thể được chia tiếp thành $2(x-2)$ để thu được tích lớn hơn (hoặc bằng). Điều này mâu thuẫn với giả định.
2. **Kế hoạch phân tách không chứa $1$**: Giả sử sơ đồ phân tách tối ưu bao gồm hệ số $1$. Sau đó, nó có thể được hợp nhất vào một yếu tố khác để có được sản phẩm lớn hơn. Điều này mâu thuẫn với giả định.
3. **Kế hoạch phân tách chứa tối đa hai $2$s**: Giả sử sơ đồ phân tách tối ưu bao gồm ba $2$s. Sau đó, chúng có thể được thay thế bằng hai $3$, mang lại sản phẩm lớn hơn. Điều này mâu thuẫn với giả định.
