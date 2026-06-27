# Lặp lại và đệ quy

Trong các thuật toán, việc thực hiện lặp đi lặp lại một tác vụ là rất phổ biến và liên quan chặt chẽ đến việc phân tích độ phức tạp. Do đó, trước khi giới thiệu độ phức tạp về thời gian và không gian, trước tiên chúng ta hãy hiểu cách triển khai thực hiện tác vụ lặp lại trong các chương trình, cụ thể là hai cấu trúc điều khiển chương trình cơ bản: lặp và đệ quy.

## Lặp lại

<u>Iteration</u> là một cơ chế điều khiển cho phép chương trình thực hiện một công việc nhiều lần. Chương trình sẽ lặp lại việc thực thi một đoạn mã khi điều kiện lặp còn đúng, và sẽ dừng lại khi điều kiện đó không còn đúng nữa.

### Vòng lặp For

Vòng lặp `for` là một trong những dạng lặp phổ biến nhất, **phù hợp để sử dụng khi biết trước số lần lặp**.

Hàm sau đây thực hiện phép tính tổng $1 + 2 + \dots + n$ bằng cách sử dụng vòng lặp `for`, với kết quả được lưu trong biến `res`. Lưu ý rằng trong Python, `range(a, b)` tương ứng với khoảng "đóng trái, mở phải", với phạm vi truyền tải là $a, a + 1, \dots, b-1$:

=== "Python"
    ```python title="iteration.py"
    def for_loop(n: int) -> int:
        """for loop"""
        res = 0
        # Sum 1, 2, ..., n-1, n
        for i in range(1, n + 1):
            res += i
        return res
    ```
=== "C++"
    ```cpp title="iteration.cpp"
    int forLoop(int n) {
        int res = 0;
        // Sum 1, 2, ..., n-1, n
        for (int i = 1; i <= n; ++i) {
            res += i;
        }
        return res;
    }
    ```
=== "Java"
    ```java title="iteration.java"
    static int forLoop(int n) {
            int res = 0;
            // Sum 1, 2, ..., n-1, n
            for (int i = 1; i <= n; i++) {
                res += i;
            }
            return res;
        }
    ```
=== "C#"
    ```csharp title="iteration.cs"
    int ForLoop(int n) {
            int res = 0;
            // Sum 1, 2, ..., n-1, n
            for (int i = 1; i <= n; i++) {
                res += i;
            }
            return res;
        }
    ```
=== "Go"
    ```go title="iteration.go"
    func forLoop(n int) int {
    	res := 0
    	// Sum 1, 2, ..., n-1, n
    	for i := 1; i <= n; i++ {
    		res += i
    	}
    	return res
    }
    ```
=== "Swift"
    ```swift title="iteration.swift"
    func forLoop(n: Int) -> Int {
        var res = 0
        // Sum 1, 2, ..., n-1, n
        for i in 1 ... n {
            res += i
        }
        return res
    }
    ```
=== "JS"
    ```javascript title="iteration.js"
    function forLoop(n) {
        let res = 0;
        // Sum 1, 2, ..., n-1, n
        for (let i = 1; i <= n; i++) {
            res += i;
        }
        return res;
    }
    ```
=== "TS"
    ```typescript title="iteration.ts"
    function forLoop(n: number): number {
        let res = 0;
        // Sum 1, 2, ..., n-1, n
        for (let i = 1; i <= n; i++) {
            res += i;
        }
        return res;
    }
    ```
=== "Dart"
    ```dart title="iteration.dart"
    int forLoop(int n) {
      int res = 0;
      // Sum 1, 2, ..., n-1, n
      for (int i = 1; i <= n; i++) {
        res += i;
      }
      return res;
    }
    ```
=== "Rust"
    ```rust title="iteration.rs"
    fn for_loop(n: i32) -> i32 {
        let mut res = 0;
        // Sum 1, 2, ..., n-1, n
        for i in 1..=n {
            res += i;
        }
        res
    }
    ```
=== "C"
    ```c title="iteration.c"
    int forLoop(int n) {
        int res = 0;
        // Sum 1, 2, ..., n-1, n
        for (int i = 1; i <= n; i++) {
            res += i;
        }
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="iteration.kt"
    fun forLoop(n: Int): Int {
        var res = 0
        // Sum 1, 2, ..., n-1, n
        for (i in 1..n) {
            res += i
        }
        return res
    }
    ```
=== "Ruby"
    ```ruby title="iteration.rb"
    ### for loop ###
    def for_loop(n)
      res = 0
    
      # Sum 1, 2, ..., n-1, n
      for i in 1..n
        res += i
      end
    
      res
    ```


Hình dưới đây cho thấy sơ đồ của hàm tính tổng này.

![Flowchart of the summation function](iteration_and_recursion.assets/iteration.png)

Số lượng thao tác trong hàm tính tổng này tỷ lệ thuận với kích thước dữ liệu đầu vào $n$ hoặc có "mối quan hệ tuyến tính". Trên thực tế, **độ phức tạp về thời gian mô tả chính xác "mối quan hệ tuyến tính" này**. Những nội dung liên quan sẽ được giới thiệu chi tiết ở phần tiếp theo.

### Vòng lặp while

Tương tự như vòng lặp `for`, vòng lặp `while` cũng là một phương thức để thực hiện phép lặp. Trong vòng lặp `while`, trước tiên chương trình sẽ kiểm tra điều kiện trong mỗi vòng; nếu điều kiện đúng thì tiếp tục thực hiện, nếu không thì kết thúc vòng lặp.

Dưới đây chúng tôi sử dụng vòng lặp `while` để thực hiện phép tính tổng $1 + 2 + \dots + n$:

=== "Python"
    ```python title="iteration.py"
    def while_loop(n: int) -> int:
        """while loop"""
        res = 0
        i = 1  # Initialize condition variable
        # Sum 1, 2, ..., n-1, n
        while i <= n:
            res += i
            i += 1  # Update condition variable
        return res
    ```
=== "C++"
    ```cpp title="iteration.cpp"
    int whileLoop(int n) {
        int res = 0;
        int i = 1; // Initialize condition variable
        // Sum 1, 2, ..., n-1, n
        while (i <= n) {
            res += i;
            i++; // Update condition variable
        }
        return res;
    }
    ```
=== "Java"
    ```java title="iteration.java"
    static int whileLoop(int n) {
            int res = 0;
            int i = 1; // Initialize condition variable
            // Sum 1, 2, ..., n-1, n
            while (i <= n) {
                res += i;
                i++; // Update condition variable
            }
            return res;
        }
    ```
=== "C#"
    ```csharp title="iteration.cs"
    int WhileLoop(int n) {
            int res = 0;
            int i = 1; // Initialize condition variable
            // Sum 1, 2, ..., n-1, n
            while (i <= n) {
                res += i;
                i += 1; // Update condition variable
            }
            return res;
        }
    ```
=== "Go"
    ```go title="iteration.go"
    func whileLoop(n int) int {
    	res := 0
    	// Initialize condition variable
    	i := 1
    	// Sum 1, 2, ..., n-1, n
    	for i <= n {
    		res += i
    		// Update condition variable
    		i++
    	}
    	return res
    }
    ```
=== "Swift"
    ```swift title="iteration.swift"
    func whileLoop(n: Int) -> Int {
        var res = 0
        var i = 1 // Initialize condition variable
        // Sum 1, 2, ..., n-1, n
        while i <= n {
            res += i
            i += 1 // Update condition variable
        }
        return res
    }
    ```
=== "JS"
    ```javascript title="iteration.js"
    function whileLoop(n) {
        let res = 0;
        let i = 1; // Initialize condition variable
        // Sum 1, 2, ..., n-1, n
        while (i <= n) {
            res += i;
            i++; // Update condition variable
        }
        return res;
    }
    ```
=== "TS"
    ```typescript title="iteration.ts"
    function whileLoop(n: number): number {
        let res = 0;
        let i = 1; // Initialize condition variable
        // Sum 1, 2, ..., n-1, n
        while (i <= n) {
            res += i;
            i++; // Update condition variable
        }
        return res;
    }
    ```
=== "Dart"
    ```dart title="iteration.dart"
    int whileLoop(int n) {
      int res = 0;
      int i = 1; // Initialize condition variable
      // Sum 1, 2, ..., n-1, n
      while (i <= n) {
        res += i;
        i++; // Update condition variable
      }
      return res;
    }
    ```
=== "Rust"
    ```rust title="iteration.rs"
    fn while_loop(n: i32) -> i32 {
        let mut res = 0;
        let mut i = 1; // Initialize condition variable
    
        // Sum 1, 2, ..., n-1, n
        while i <= n {
            res += i;
            i += 1; // Update condition variable
        }
        res
    }
    ```
=== "C"
    ```c title="iteration.c"
    int whileLoop(int n) {
        int res = 0;
        int i = 1; // Initialize condition variable
        // Sum 1, 2, ..., n-1, n
        while (i <= n) {
            res += i;
            i++; // Update condition variable
        }
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="iteration.kt"
    fun whileLoop(n: Int): Int {
        var res = 0
        var i = 1 // Initialize condition variable
        // Sum 1, 2, ..., n-1, n
        while (i <= n) {
            res += i
            i++ // Update condition variable
        }
        return res
    }
    ```
=== "Ruby"
    ```ruby title="iteration.rb"
    ### while loop ###
    def while_loop(n)
      res = 0
      i = 1 # Initialize condition variable
    
      # Sum 1, 2, ..., n-1, n
      while i <= n
        res += i
        i += 1 # Update condition variable
      end
    
      res
    ```


**Vòng lặp `while` có tính linh hoạt cao hơn vòng lặp `for`**. Trong vòng lặp `while`, chúng ta có thể thoải mái thiết kế các bước khởi tạo và cập nhật của biến điều kiện.

Ví dụ: trong đoạn mã sau, biến điều kiện $i$ được cập nhật hai lần mỗi vòng, điều này không thuận tiện khi triển khai bằng vòng lặp `for`:

=== "Python"
    ```python title="iteration.py"
    def while_loop_ii(n: int) -> int:
        """while loop (two updates)"""
        res = 0
        i = 1  # Initialize condition variable
        # Sum 1, 4, 10, ...
        while i <= n:
            res += i
            # Update condition variable
            i += 1
            i *= 2
        return res
    ```
=== "Rust"
    ```rust title="iteration.rs"
    fn while_loop_ii(n: i32) -> i32 {
        let mut res = 0;
        let mut i = 1; // Initialize condition variable
    
        // Sum 1, 4, 10, ...
        while i <= n {
            res += i;
            // Update condition variable
            i += 1;
            i *= 2;
        }
        res
    }
    ```
=== "Ruby"
    ```ruby title="iteration.rb"
    ### while loop (two updates) ###
    def while_loop_ii(n)
      res = 0
      i = 1 # Initialize condition variable
    
      # Sum 1, 4, 10, ...
      while i <= n
        res += i
        # Update condition variable
        i += 1
        i *= 2
      end
    
      res
    ```


Nhìn chung, vòng lặp **`for` có mã nhỏ gọn hơn, trong khi vòng lặp `while` linh hoạt hơn**; cả hai đều có thể thực hiện các cấu trúc lặp. Việc lựa chọn sử dụng cái nào phải được xác định dựa trên yêu cầu của vấn đề cụ thể.

### Vòng lặp lồng nhau

Chúng ta có thể lồng một cấu trúc vòng lặp vào bên trong một cấu trúc vòng lặp khác. Dưới đây là một ví dụ sử dụng vòng lặp `for`:

=== "Python"
    ```python title="iteration.py"
    def nested_for_loop(n: int) -> str:
        """Nested for loop"""
        res = ""
        # Loop i = 1, 2, ..., n-1, n
        for i in range(1, n + 1):
            # Loop j = 1, 2, ..., n-1, n
            for j in range(1, n + 1):
                res += f"({i}, {j}), "
        return res
    ```
=== "C++"
    ```cpp title="iteration.cpp"
    string nestedForLoop(int n) {
        ostringstream res;
        // Loop i = 1, 2, ..., n-1, n
        for (int i = 1; i <= n; ++i) {
            // Loop j = 1, 2, ..., n-1, n
            for (int j = 1; j <= n; ++j) {
                res << "(" << i << ", " << j << "), ";
            }
        }
        return res.str();
    }
    ```
=== "Java"
    ```java title="iteration.java"
    static String nestedForLoop(int n) {
            StringBuilder res = new StringBuilder();
            // Loop i = 1, 2, ..., n-1, n
            for (int i = 1; i <= n; i++) {
                // Loop j = 1, 2, ..., n-1, n
                for (int j = 1; j <= n; j++) {
                    res.append("(" + i + ", " + j + "), ");
                }
            }
            return res.toString();
        }
    ```
=== "C#"
    ```csharp title="iteration.cs"
    string NestedForLoop(int n) {
            StringBuilder res = new();
            // Loop i = 1, 2, ..., n-1, n
            for (int i = 1; i <= n; i++) {
                // Loop j = 1, 2, ..., n-1, n
                for (int j = 1; j <= n; j++) {
                    res.Append($"({i}, {j}), ");
                }
            }
            return res.ToString();
        }
    ```
=== "Go"
    ```go title="iteration.go"
    func nestedForLoop(n int) string {
    	res := ""
    	// Loop i = 1, 2, ..., n-1, n
    	for i := 1; i <= n; i++ {
    		for j := 1; j <= n; j++ {
    			// Loop j = 1, 2, ..., n-1, n
    			res += fmt.Sprintf("(%d, %d), ", i, j)
    		}
    	}
    	return res
    }
    ```
=== "Swift"
    ```swift title="iteration.swift"
    func nestedForLoop(n: Int) -> String {
        var res = ""
        // Loop i = 1, 2, ..., n-1, n
        for i in 1 ... n {
            // Loop j = 1, 2, ..., n-1, n
            for j in 1 ... n {
                res.append("(\(i), \(j)), ")
            }
        }
        return res
    }
    ```
=== "JS"
    ```javascript title="iteration.js"
    function nestedForLoop(n) {
        let res = '';
        // Loop i = 1, 2, ..., n-1, n
        for (let i = 1; i <= n; i++) {
            // Loop j = 1, 2, ..., n-1, n
            for (let j = 1; j <= n; j++) {
                res += `(${i}, ${j}), `;
            }
        }
        return res;
    }
    ```
=== "TS"
    ```typescript title="iteration.ts"
    function nestedForLoop(n: number): string {
        let res = '';
        // Loop i = 1, 2, ..., n-1, n
        for (let i = 1; i <= n; i++) {
            // Loop j = 1, 2, ..., n-1, n
            for (let j = 1; j <= n; j++) {
                res += `(${i}, ${j}), `;
            }
        }
        return res;
    }
    ```
=== "Dart"
    ```dart title="iteration.dart"
    String nestedForLoop(int n) {
      String res = "";
      // Loop i = 1, 2, ..., n-1, n
      for (int i = 1; i <= n; i++) {
        // Loop j = 1, 2, ..., n-1, n
        for (int j = 1; j <= n; j++) {
          res += "($i, $j), ";
        }
      }
      return res;
    }
    ```
=== "Rust"
    ```rust title="iteration.rs"
    fn nested_for_loop(n: i32) -> String {
        let mut res = vec![];
        // Loop i = 1, 2, ..., n-1, n
        for i in 1..=n {
            // Loop j = 1, 2, ..., n-1, n
            for j in 1..=n {
                res.push(format!("({}, {}), ", i, j));
            }
        }
        res.join("")
    }
    ```
=== "C"
    ```c title="iteration.c"
    char *nestedForLoop(int n) {
        // n * n is the number of points, "(i, j), " string max length is 6+10*2, plus extra space for null character \0
        int size = n * n * 26 + 1;
        char *res = malloc(size * sizeof(char));
        // Loop i = 1, 2, ..., n-1, n
        for (int i = 1; i <= n; i++) {
            // Loop j = 1, 2, ..., n-1, n
            for (int j = 1; j <= n; j++) {
                char tmp[26];
                snprintf(tmp, sizeof(tmp), "(%d, %d), ", i, j);
                strncat(res, tmp, size - strlen(res) - 1);
            }
        }
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="iteration.kt"
    fun nestedForLoop(n: Int): String {
        val res = StringBuilder()
        // Loop i = 1, 2, ..., n-1, n
        for (i in 1..n) {
            // Loop j = 1, 2, ..., n-1, n
            for (j in 1..n) {
                res.append(" ($i, $j), ")
            }
        }
        return res.toString()
    }
    ```
=== "Ruby"
    ```ruby title="iteration.rb"
    ### Nested for loop ###
    def nested_for_loop(n)
      res = ""
    
      # Loop i = 1, 2, ..., n-1, n
      for i in 1..n
        # Loop j = 1, 2, ..., n-1, n
        for j in 1..n
          res += "(#{i}, #{j}), "
        end
      end
    
      res
    ```


Hình dưới đây cho thấy sơ đồ của vòng lặp lồng nhau này.

![Flowchart of nested loops](iteration_and_recursion.assets/nested_iteration.png)

Trong trường hợp này, số thao tác của hàm tỷ lệ thuận với $n^2$ hoặc thời gian chạy của thuật toán có "mối quan hệ bậc hai" với kích thước dữ liệu đầu vào $n$.

Chúng ta có thể tiếp tục thêm các vòng lặp lồng nhau, trong đó mỗi cấp độ lồng nhau bổ sung có thể được xem như là sự gia tăng về chiều, nâng độ phức tạp về thời gian lên "mối quan hệ bậc ba", "mối quan hệ bậc bốn", v.v.

##Đệ quy

<u>Recursion</u> là một chiến lược thuật toán giải quyết vấn đề bằng cách để một hàm tự gọi lại chính nó. Đệ quy chủ yếu bao gồm hai giai đoạn.

1. **Giảm dần**: Chương trình liên tục tự gọi mình sâu hơn, thường chuyển các tham số nhỏ hơn hoặc đơn giản hơn cho đến khi đạt đến "điều kiện kết thúc".
2. **Ascend**: Sau khi kích hoạt "điều kiện kết thúc", chương trình trả về từng lớp từ hàm đệ quy sâu nhất, tổng hợp kết quả của từng lớp.

Từ góc độ triển khai, mã đệ quy chủ yếu bao gồm ba phần tử.

1. **Điều kiện kết thúc**: Được sử dụng để xác định thời điểm chuyển từ "giảm dần" sang "tăng dần".
2. **Cuộc gọi đệ quy**: Tương ứng với "giảm dần", trong đó hàm gọi chính nó, thường có các tham số nhỏ hơn hoặc đơn giản hơn.
3. **Trả về kết quả**: Tương ứng với "tăng dần", trả kết quả của mức đệ quy hiện tại về lớp trước.

Quan sát đoạn mã sau. Chúng ta chỉ cần gọi hàm `recur(n)` để hoàn thành phép tính $1 + 2 + \dots + n$:

=== "Python"
    ```python title="recursion.py"
    def recur(n: int) -> int:
        """Recursion"""
        # Termination condition
        if n == 1:
            return 1
        # Recurse: recursive call
        res = recur(n - 1)
        # Return: return result
        return n + res
    ```
=== "C++"
    ```cpp title="recursion.cpp"
    int recur(int n) {
        // Termination condition
        if (n == 1)
            return 1;
        // Recurse: recursive call
        int res = recur(n - 1);
        // Return: return result
        return n + res;
    }
    ```
=== "Java"
    ```java title="recursion.java"
    public class recursion {
        /* Recursion */
        static int recur(int n) {
            // Termination condition
            if (n == 1)
                return 1;
            // Recurse: recursive call
            int res = recur(n - 1);
            // Return: return result
            return n + res;
        }
    
        /* Simulate recursion using iteration */
        static int forLoopRecur(int n) {
            // Use an explicit stack to simulate the system call stack
            Stack<Integer> stack = new Stack<>();
            int res = 0;
            // Recurse: recursive call
            for (int i = n; i > 0; i--) {
                // Simulate "recurse" with "push"
                stack.push(i);
            }
            // Return: return result
            while (!stack.isEmpty()) {
                // Simulate "return" with "pop"
                res += stack.pop();
            }
            // res = 1+2+3+...+n
            return res;
        }
    
        /* Tail recursion */
        static int tailRecur(int n, int res) {
            // Termination condition
            if (n == 0)
                return res;
            // Tail recursive call
            return tailRecur(n - 1, res + n);
        }
    
        /* Fibonacci sequence: recursion */
        static int fib(int n) {
            // Termination condition f(1) = 0, f(2) = 1
            if (n == 1 || n == 2)
                return n - 1;
            // Recursive call f(n) = f(n-1) + f(n-2)
            int res = fib(n - 1) + fib(n - 2);
            // Return result f(n)
            return res;
        }
    
        /* Driver Code */
        public static void main(String[] args) {
            int n = 5;
            int res;
    
            res = recur(n);
            System.out.println("\nRecursive function sum result res = " + res);
    
            res = forLoopRecur(n);
            System.out.println("\nUsing iteration to simulate recursive sum result res = " + res);
    
            res = tailRecur(n, 0);
            System.out.println("\nTail recursive function sum result res = " + res);
    
            res = fib(n);
            System.out.println("\nThe " + n + "th term of the Fibonacci sequence is " + res);
        }
    }
    ```
=== "C#"
    ```csharp title="recursion.cs"
    public class recursion {
        /* Recursion */
        int Recur(int n) {
            // Termination condition
            if (n == 1)
                return 1;
            // Recurse: recursive call
            int res = Recur(n - 1);
            // Return: return result
            return n + res;
        }
    
        /* Simulate recursion using iteration */
        int ForLoopRecur(int n) {
            // Use an explicit stack to simulate the system call stack
            Stack<int> stack = new();
            int res = 0;
            // Recurse: recursive call
            for (int i = n; i > 0; i--) {
                // Simulate "recurse" with "push"
                stack.Push(i);
            }
            // Return: return result
            while (stack.Count > 0) {
                // Simulate "return" with "pop"
                res += stack.Pop();
            }
            // res = 1+2+3+...+n
            return res;
        }
    
        /* Tail recursion */
        int TailRecur(int n, int res) {
            // Termination condition
            if (n == 0)
                return res;
            // Tail recursive call
            return TailRecur(n - 1, res + n);
        }
    
        /* Fibonacci sequence: recursion */
        int Fib(int n) {
            // Termination condition f(1) = 0, f(2) = 1
            if (n == 1 || n == 2)
                return n - 1;
            // Recursive call f(n) = f(n-1) + f(n-2)
            int res = Fib(n - 1) + Fib(n - 2);
            // Return result f(n)
            return res;
        }
    
        /* Driver Code */
        [Test]
        public void Test() {
            int n = 5;
            int res;
    
            res = Recur(n);
            Console.WriteLine("\nRecursive function sum result res = " + res);
    
            res = ForLoopRecur(n);
            Console.WriteLine("\nUsing iteration to simulate recursive sum result res = " + res);
    
            res = TailRecur(n, 0);
            Console.WriteLine("\nTail recursive function sum result res = " + res);
    
            res = Fib(n);
            Console.WriteLine("\nThe " + n + "th term of the Fibonacci sequence is " + res);
        }
    }
    ```
=== "Go"
    ```go title="recursion.go"
    func recur(n int) int {
    	// Termination condition
    	if n == 1 {
    		return 1
    	}
    	// Recurse: recursive call
    	res := recur(n - 1)
    	// Return: return result
    	return n + res
    }
    ```
=== "Swift"
    ```swift title="recursion.swift"
    func recur(n: Int) -> Int {
        // Termination condition
        if n == 1 {
            return 1
        }
        // Recurse: recursive call
        let res = recur(n: n - 1)
        // Return: return result
        return n + res
    }
    ```
=== "JS"
    ```javascript title="recursion.js"
    function recur(n) {
        // Termination condition
        if (n === 1) return 1;
        // Recurse: recursive call
        const res = recur(n - 1);
        // Return: return result
        return n + res;
    }
    ```
=== "TS"
    ```typescript title="recursion.ts"
    function recur(n: number): number {
        // Termination condition
        if (n === 1) return 1;
        // Recurse: recursive call
        const res = recur(n - 1);
        // Return: return result
        return n + res;
    }
    ```
=== "Dart"
    ```dart title="recursion.dart"
    int recur(int n) {
      // Termination condition
      if (n == 1) return 1;
      // Recurse: recursive call
      int res = recur(n - 1);
      // Return: return result
      return n + res;
    }
    ```
=== "Rust"
    ```rust title="recursion.rs"
    fn recur(n: i32) -> i32 {
        // Termination condition
        if n == 1 {
            return 1;
        }
        // Recurse: recursive call
        let res = recur(n - 1);
        // Return: return result
        n + res
    }
    ```
=== "C"
    ```c title="recursion.c"
    int recur(int n) {
        // Termination condition
        if (n == 1)
            return 1;
        // Recurse: recursive call
        int res = recur(n - 1);
        // Return: return result
        return n + res;
    }
    ```
=== "Kotlin"
    ```kotlin title="recursion.kt"
    fun recur(n: Int): Int {
        // Termination condition
        if (n == 1)
            return 1
        // Descend: recursive call
        val res = recur(n - 1)
        // Return: return result
        return n + res
    }
    ```
=== "Ruby"
    ```ruby title="recursion.rb"
    ### Recursion ###
    def recur(n)
      # Termination condition
      return 1 if n == 1
      # Recurse: recursive call
      res = recur(n - 1)
      # Return: return result
      n + res
    ```


Hình dưới đây cho thấy quá trình đệ quy của hàm này.

![Recursive process of the summation function](iteration_and_recursion.assets/recursion_sum.png)

Mặc dù từ góc độ tính toán, phép lặp và đệ quy có thể đạt được kết quả như nhau, **chúng đại diện cho hai mô hình hoàn toàn khác nhau để suy nghĩ và giải quyết vấn đề**.

- **Lặp lại**: Giải quyết vấn đề "từ dưới lên". Bắt đầu từ những bước cơ bản nhất, các bước này sau đó được thực hiện lặp đi lặp lại hoặc tích lũy cho đến khi nhiệm vụ hoàn thành.
- **Đệ quy**: Giải bài toán "từ trên xuống". Bài toán ban đầu được phân tách thành các bài toán con nhỏ hơn có dạng giống như bài toán ban đầu. Các bài toán con này tiếp tục được phân tách thành các bài toán con thậm chí còn nhỏ hơn cho đến khi đạt được trường hợp cơ sở (trong đó lời giải đã được biết).

Lấy hàm tính tổng ở trên làm ví dụ, giả sử bài toán là $f(n) = 1 + 2 + \dots + n$.

- **Lặp**: Mô phỏng quá trình tính tổng trong một vòng lặp, duyệt từ $1$ đến $n$, thực hiện thao tác tính tổng trong mỗi vòng để thu được $f(n)$.
- **Đệ quy**: Phân rã bài toán thành bài toán con $f(n) = n + f(n-1)$, phân rã liên tục (đệ quy) cho đến khi dừng ở trường hợp cơ sở $f(1) = 1$.

### Ngăn xếp cuộc gọi

Mỗi khi một hàm đệ quy gọi chính nó, hệ thống sẽ cấp phát bộ nhớ cho hàm mới được gọi để lưu trữ các biến cục bộ, địa chỉ cuộc gọi và các thông tin khác. Điều này dẫn đến hai hậu quả.

- Dữ liệu ngữ cảnh của hàm được lưu trữ trong một vùng bộ nhớ gọi là “không gian khung ngăn xếp”, vùng này không được giải phóng cho đến khi hàm quay trở lại. Do đó, **đệ quy thường tiêu tốn nhiều dung lượng bộ nhớ hơn phép lặp**.
- Các lệnh gọi hàm đệ quy phải chịu thêm chi phí. **Do đó, đệ quy thường ít tiết kiệm thời gian hơn so với vòng lặp**.

Như được hiển thị trong hình bên dưới, trước khi điều kiện kết thúc được kích hoạt, có $n$ hàm đệ quy tồn tại đồng thời, với **độ sâu đệ quy là $n$**.

![Recursion call depth](iteration_and_recursion.assets/recursion_sum_depth.png)

Trong thực tế, độ sâu đệ quy mà các ngôn ngữ lập trình cho phép thường bị giới hạn và đệ quy quá sâu có thể dẫn đến lỗi tràn ngăn xếp.

### Đệ quy đuôi

Điều thú vị là **nếu một hàm thực hiện lệnh gọi đệ quy là bước cuối cùng trước khi quay trở lại**, trình biên dịch hoặc trình thông dịch có thể tối ưu hóa hàm đó để hiệu quả về không gian của nó tương đương với phép lặp. Trường hợp này được gọi là <u>đệ quy đuôi</u>.

- **Đệ quy thông thường**: Khi một hàm trở về cấp độ trước đó, nó cần tiếp tục thực thi mã, do đó hệ thống cần lưu ngữ cảnh lệnh gọi của lớp trước đó.
- **Đệ quy đuôi**: Lệnh gọi đệ quy là thao tác cuối cùng trước khi hàm trả về, nghĩa là sau khi quay về mức trước đó không cần tiếp tục thực hiện các thao tác khác nên hệ thống không cần lưu ngữ cảnh của hàm lớp trước.

Lấy phép tính $1 + 2 + \dots + n$ làm ví dụ, chúng ta có thể đặt biến kết quả `res` làm tham số hàm để thực hiện đệ quy đuôi:

=== "Python"
    ```python title="recursion.py"
    def tail_recur(n, res):
        """Tail recursion"""
        # Termination condition
        if n == 0:
            return res
        # Tail recursive call
        return tail_recur(n - 1, res + n)
    ```
=== "C++"
    ```cpp title="recursion.cpp"
    int tailRecur(int n, int res) {
        // Termination condition
        if (n == 0)
            return res;
        // Tail recursive call
        return tailRecur(n - 1, res + n);
    }
    ```
=== "Java"
    ```java title="recursion.java"
    static int tailRecur(int n, int res) {
            // Termination condition
            if (n == 0)
                return res;
            // Tail recursive call
            return tailRecur(n - 1, res + n);
        }
    ```
=== "C#"
    ```csharp title="recursion.cs"
    int TailRecur(int n, int res) {
            // Termination condition
            if (n == 0)
                return res;
            // Tail recursive call
            return TailRecur(n - 1, res + n);
        }
    ```
=== "Go"
    ```go title="recursion.go"
    func tailRecur(n int, res int) int {
    	// Termination condition
    	if n == 0 {
    		return res
    	}
    	// Tail recursive call
    	return tailRecur(n-1, res+n)
    }
    ```
=== "Swift"
    ```swift title="recursion.swift"
    func tailRecur(n: Int, res: Int) -> Int {
        // Termination condition
        if n == 0 {
            return res
        }
        // Tail recursive call
        return tailRecur(n: n - 1, res: res + n)
    }
    ```
=== "JS"
    ```javascript title="recursion.js"
    function tailRecur(n, res) {
        // Termination condition
        if (n === 0) return res;
        // Tail recursive call
        return tailRecur(n - 1, res + n);
    }
    ```
=== "TS"
    ```typescript title="recursion.ts"
    function tailRecur(n: number, res: number): number {
        // Termination condition
        if (n === 0) return res;
        // Tail recursive call
        return tailRecur(n - 1, res + n);
    }
    ```
=== "Dart"
    ```dart title="recursion.dart"
    int tailRecur(int n, int res) {
      // Termination condition
      if (n == 0) return res;
      // Tail recursive call
      return tailRecur(n - 1, res + n);
    }
    ```
=== "Rust"
    ```rust title="recursion.rs"
    fn tail_recur(n: i32, res: i32) -> i32 {
        // Termination condition
        if n == 0 {
            return res;
        }
        // Tail recursive call
        tail_recur(n - 1, res + n)
    }
    ```
=== "C"
    ```c title="recursion.c"
    int tailRecur(int n, int res) {
        // Termination condition
        if (n == 0)
            return res;
        // Tail recursive call
        return tailRecur(n - 1, res + n);
    }
    ```
=== "Kotlin"
    ```kotlin title="recursion.kt"
    tailrec fun tailRecur(n: Int, res: Int): Int {
        // Add tailrec keyword to enable tail recursion optimization
        // Termination condition
        if (n == 0)
            return res
        // Tail recursive call
        return tailRecur(n - 1, res + n)
    }
    ```
=== "Ruby"
    ```ruby title="recursion.rb"
    ### Tail recursion ###
    def tail_recur(n, res)
      # Termination condition
      return res if n == 0
      # Tail recursive call
      tail_recur(n - 1, res + n)
    ```


Quá trình thực hiện đệ quy đuôi được thể hiện trong hình bên dưới. So sánh đệ quy thông thường và đệ quy đuôi, phép tính tổng được thực hiện ở các điểm khác nhau.

- **Đệ quy thông thường**: Thao tác tính tổng được thực hiện trong quá trình "tăng dần", yêu cầu thao tác tính tổng bổ sung sau mỗi lớp quay trở lại.
- **Đệ quy đuôi**: Phép tính tổng được thực hiện trong quá trình "giảm dần"; quá trình "tăng dần" chỉ cần trả về từng lớp.

![Tail recursion process](iteration_and_recursion.assets/tail_recursion_sum.png)

!!! mẹo

Xin lưu ý rằng nhiều trình biên dịch hoặc trình thông dịch không hỗ trợ tối ưu hóa đệ quy đuôi. Ví dụ: Python không hỗ trợ tối ưu hóa đệ quy đuôi theo mặc định, vì vậy ngay cả khi một hàm ở dạng đệ quy đuôi, nó vẫn có thể gặp phải sự cố tràn ngăn xếp.

### Cây đệ quy

Khi giải quyết các vấn đề thuật toán liên quan đến "phân chia và chinh phục", đệ quy thường cung cấp cách tiếp cận trực quan hơn và mã dễ đọc hơn so với phép lặp. Lấy "chuỗi Fibonacci" làm ví dụ.

!!! câu hỏi

Cho dãy Fibonacci $0, 1, 1, 2, 3, 5, 8, 13, \dots$, tìm số thứ $n$ trong dãy.

Đặt số $n$-th của dãy Fibonacci là $f(n)$. Có thể dễ dàng rút ra được hai kết luận.

- Hai số đầu tiên của dãy là $f(1) = 0$ và $f(2) = 1$.
- Mỗi số trong dãy là tổng của hai số trước đó, tức là $f(n) = f(n - 1) + f(n - 2)$.

Theo quan hệ truy hồi để thực hiện lệnh gọi đệ quy, với hai số đầu tiên làm điều kiện kết thúc, chúng ta có thể viết mã đệ quy. Gọi `fib(n)` sẽ cho chúng ta số $n$-th của dãy Fibonacci:

=== "Python"
    ```python title="recursion.py"
    def fib(n: int) -> int:
        """Fibonacci sequence: recursion"""
        # Termination condition f(1) = 0, f(2) = 1
        if n == 1 or n == 2:
            return n - 1
        # Recursive call f(n) = f(n-1) + f(n-2)
        res = fib(n - 1) + fib(n - 2)
        # Return result f(n)
        return res
    ```
=== "C++"
    ```cpp title="recursion.cpp"
    int fib(int n) {
        // Termination condition f(1) = 0, f(2) = 1
        if (n == 1 || n == 2)
            return n - 1;
        // Recursive call f(n) = f(n-1) + f(n-2)
        int res = fib(n - 1) + fib(n - 2);
        // Return result f(n)
        return res;
    }
    ```
=== "Java"
    ```java title="recursion.java"
    static int fib(int n) {
            // Termination condition f(1) = 0, f(2) = 1
            if (n == 1 || n == 2)
                return n - 1;
            // Recursive call f(n) = f(n-1) + f(n-2)
            int res = fib(n - 1) + fib(n - 2);
            // Return result f(n)
            return res;
        }
    ```
=== "C#"
    ```csharp title="recursion.cs"
    int Fib(int n) {
            // Termination condition f(1) = 0, f(2) = 1
            if (n == 1 || n == 2)
                return n - 1;
            // Recursive call f(n) = f(n-1) + f(n-2)
            int res = Fib(n - 1) + Fib(n - 2);
            // Return result f(n)
            return res;
        }
    ```
=== "Go"
    ```go title="recursion.go"
    func fib(n int) int {
    	// Termination condition f(1) = 0, f(2) = 1
    	if n == 1 || n == 2 {
    		return n - 1
    	}
    	// Recursive call f(n) = f(n-1) + f(n-2)
    	res := fib(n-1) + fib(n-2)
    	// Return result f(n)
    	return res
    }
    ```
=== "Swift"
    ```swift title="recursion.swift"
    func fib(n: Int) -> Int {
        // Termination condition f(1) = 0, f(2) = 1
        if n == 1 || n == 2 {
            return n - 1
        }
        // Recursive call f(n) = f(n-1) + f(n-2)
        let res = fib(n: n - 1) + fib(n: n - 2)
        // Return result f(n)
        return res
    }
    ```
=== "JS"
    ```javascript title="recursion.js"
    function fib(n) {
        // Termination condition f(1) = 0, f(2) = 1
        if (n === 1 || n === 2) return n - 1;
        // Recursive call f(n) = f(n-1) + f(n-2)
        const res = fib(n - 1) + fib(n - 2);
        // Return result f(n)
        return res;
    }
    ```
=== "TS"
    ```typescript title="recursion.ts"
    function fib(n: number): number {
        // Termination condition f(1) = 0, f(2) = 1
        if (n === 1 || n === 2) return n - 1;
        // Recursive call f(n) = f(n-1) + f(n-2)
        const res = fib(n - 1) + fib(n - 2);
        // Return result f(n)
        return res;
    }
    ```
=== "Dart"
    ```dart title="recursion.dart"
    int fib(int n) {
      // Termination condition f(1) = 0, f(2) = 1
      if (n == 1 || n == 2) return n - 1;
      // Recursive call f(n) = f(n-1) + f(n-2)
      int res = fib(n - 1) + fib(n - 2);
      // Return result f(n)
      return res;
    }
    ```
=== "Rust"
    ```rust title="recursion.rs"
    fn fib(n: i32) -> i32 {
        // Termination condition f(1) = 0, f(2) = 1
        if n == 1 || n == 2 {
            return n - 1;
        }
        // Recursive call f(n) = f(n-1) + f(n-2)
        let res = fib(n - 1) + fib(n - 2);
        // Return result
        res
    }
    ```
=== "C"
    ```c title="recursion.c"
    int fib(int n) {
        // Termination condition f(1) = 0, f(2) = 1
        if (n == 1 || n == 2)
            return n - 1;
        // Recursive call f(n) = f(n-1) + f(n-2)
        int res = fib(n - 1) + fib(n - 2);
        // Return result f(n)
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="recursion.kt"
    fun fib(n: Int): Int {
        // Termination condition f(1) = 0, f(2) = 1
        if (n == 1 || n == 2)
            return n - 1
        // Recursive call f(n) = f(n-1) + f(n-2)
        val res = fib(n - 1) + fib(n - 2)
        // Return result f(n)
        return res
    }
    ```
=== "Ruby"
    ```ruby title="recursion.rb"
    ### Fibonacci sequence: recursion ###
    def fib(n)
      # Termination condition f(1) = 0, f(2) = 1
      return n - 1 if n == 1 || n == 2
      # Recursive call f(n) = f(n-1) + f(n-2)
      res = fib(n - 1) + fib(n - 2)
      # Return result f(n)
      res
    ```


Quan sát đoạn mã trên, chúng ta thực hiện hai lệnh gọi đệ quy trong hàm, **có nghĩa là một lệnh gọi tạo ra hai nhánh lệnh gọi**. Như được hiển thị trong hình bên dưới, việc gọi đệ quy lặp đi lặp lại này cuối cùng sẽ tạo ra một <u>cây đệ quy</u> với các mức $n$.

![Recursion tree of the Fibonacci sequence](iteration_and_recursion.assets/recursion_tree.png)

Về cơ bản, đệ quy thể hiện mô hình "phân tách một vấn đề thành các bài toán con nhỏ hơn" và chiến lược phân chia để chinh phục này rất quan trọng.

- Từ góc độ thuật toán, nhiều chiến lược thuật toán quan trọng như tìm kiếm, sắp xếp, quay lui, chia để trị, lập trình động áp dụng trực tiếp hoặc gián tiếp cách suy nghĩ này.
- Từ góc độ cấu trúc dữ liệu, đệ quy đương nhiên phù hợp để xử lý các vấn đề liên quan đến danh sách, cây và biểu đồ liên kết, vì chúng rất phù hợp để phân tích bằng tư duy chia để trị.

## So sánh hai

Tóm tắt nội dung trên, như được hiển thị trong bảng bên dưới, phép lặp và đệ quy khác nhau về cách triển khai, hiệu suất và khả năng áp dụng.

<p align="center"> Table <id> &nbsp; Comparison of iteration and recursion characteristics </p>

|                | Lặp lại | Đệ quy |
| -------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Thực hiện | Cấu trúc vòng lặp | Hàm tự gọi chính nó |
| Hiệu quả về thời gian | Nói chung là hiệu quả hơn, không cần gọi hàm | Mỗi lệnh gọi hàm đều phát sinh chi phí |
| Sử dụng bộ nhớ | Thường sử dụng một lượng không gian bộ nhớ cố định | Các cuộc gọi hàm tích lũy có thể sử dụng một lượng lớn không gian khung ngăn xếp |
| Vấn đề phù hợp | Thích hợp cho các tác vụ vòng lặp đơn giản, với mã trực quan và dễ đọc | Thích hợp cho việc phân rã bài toán con, chẳng hạn như cây, đồ thị, chia để trị, quay lui, v.v., với cấu trúc mã ngắn gọn và rõ ràng |

!!! mẹo

Nếu bạn thấy nội dung sau khó hiểu, bạn có thể xem lại sau khi đọc chương “Stack”.

Mối quan hệ nội tại giữa phép lặp và đệ quy là gì? Lấy hàm đệ quy ở trên làm ví dụ, phép tính tổng được thực hiện trong giai đoạn đệ quy "tăng dần". Điều này có nghĩa là hàm được gọi đầu tiên thực sự hoàn thành thao tác tính tổng của nó sau cùng, **và cơ chế hoạt động này tương tự như nguyên tắc "vào sau, ra trước" của ngăn xếp**.

Trong thực tế, thuật ngữ đệ quy như "ngăn xếp cuộc gọi" và "không gian khung ngăn xếp" đã gợi ý về mối quan hệ chặt chẽ giữa đệ quy và ngăn xếp.

1. **Giảm dần**: Khi một hàm được gọi, hệ thống sẽ phân bổ một khung ngăn xếp mới trên "ngăn xếp cuộc gọi" cho hàm đó để lưu trữ các biến cục bộ, tham số, địa chỉ trả về và dữ liệu khác của hàm.
2. **Ascend**: Khi hàm hoàn thành việc thực thi và trả về, khung ngăn xếp tương ứng sẽ bị xóa khỏi "ngăn xếp lệnh gọi", khôi phục môi trường thực thi của hàm trước đó.

Do đó, **chúng ta có thể sử dụng một ngăn xếp rõ ràng để mô phỏng hành vi của ngăn xếp cuộc gọi**, do đó chuyển đệ quy thành dạng lặp:

=== "Python"
    ```python title="recursion.py"
    def for_loop_recur(n: int) -> int:
        """Simulate recursion using iteration"""
        # Use an explicit stack to simulate the system call stack
        stack = []
        res = 0
        # Recurse: recursive call
        for i in range(n, 0, -1):
            # Simulate "recurse" with "push"
            stack.append(i)
        # Return: return result
        while stack:
            # Simulate "return" with "pop"
            res += stack.pop()
        # res = 1+2+3+...+n
        return res
    ```
=== "C++"
    ```cpp title="recursion.cpp"
    int forLoopRecur(int n) {
        // Use an explicit stack to simulate the system call stack
        stack<int> stack;
        int res = 0;
        // Recurse: recursive call
        for (int i = n; i > 0; i--) {
            // Simulate "recurse" with "push"
            stack.push(i);
        }
        // Return: return result
        while (!stack.empty()) {
            // Simulate "return" with "pop"
            res += stack.top();
            stack.pop();
        }
        // res = 1+2+3+...+n
        return res;
    }
    ```
=== "Java"
    ```java title="recursion.java"
    static int forLoopRecur(int n) {
            // Use an explicit stack to simulate the system call stack
            Stack<Integer> stack = new Stack<>();
            int res = 0;
            // Recurse: recursive call
            for (int i = n; i > 0; i--) {
                // Simulate "recurse" with "push"
                stack.push(i);
            }
            // Return: return result
            while (!stack.isEmpty()) {
                // Simulate "return" with "pop"
                res += stack.pop();
            }
            // res = 1+2+3+...+n
            return res;
        }
    ```
=== "C#"
    ```csharp title="recursion.cs"
    int ForLoopRecur(int n) {
            // Use an explicit stack to simulate the system call stack
            Stack<int> stack = new();
            int res = 0;
            // Recurse: recursive call
            for (int i = n; i > 0; i--) {
                // Simulate "recurse" with "push"
                stack.Push(i);
            }
            // Return: return result
            while (stack.Count > 0) {
                // Simulate "return" with "pop"
                res += stack.Pop();
            }
            // res = 1+2+3+...+n
            return res;
        }
    ```
=== "Go"
    ```go title="recursion.go"
    func forLoopRecur(n int) int {
    	// Use an explicit stack to simulate the system call stack
    	stack := list.New()
    	res := 0
    	// Recurse: recursive call
    	for i := n; i > 0; i-- {
    		// Simulate "recurse" with "push"
    		stack.PushBack(i)
    	}
    	// Return: return result
    	for stack.Len() != 0 {
    		// Simulate "return" with "pop"
    		res += stack.Back().Value.(int)
    		stack.Remove(stack.Back())
    	}
    	// res = 1+2+3+...+n
    	return res
    }
    ```
=== "Swift"
    ```swift title="recursion.swift"
    func forLoopRecur(n: Int) -> Int {
        // Use an explicit stack to simulate the system call stack
        var stack: [Int] = []
        var res = 0
        // Recurse: recursive call
        for i in (1 ... n).reversed() {
            // Simulate "recurse" with "push"
            stack.append(i)
        }
        // Return: return result
        while !stack.isEmpty {
            // Simulate "return" with "pop"
            res += stack.removeLast()
        }
        // res = 1+2+3+...+n
        return res
    }
    ```
=== "JS"
    ```javascript title="recursion.js"
    function forLoopRecur(n) {
        // Use an explicit stack to simulate the system call stack
        const stack = [];
        let res = 0;
        // Recurse: recursive call
        for (let i = n; i > 0; i--) {
            // Simulate "recurse" with "push"
            stack.push(i);
        }
        // Return: return result
        while (stack.length) {
            // Simulate "return" with "pop"
            res += stack.pop();
        }
        // res = 1+2+3+...+n
        return res;
    }
    ```
=== "TS"
    ```typescript title="recursion.ts"
    function forLoopRecur(n: number): number {
        // Use an explicit stack to simulate the system call stack
        const stack: number[] = [];
        let res: number = 0;
        // Recurse: recursive call
        for (let i = n; i > 0; i--) {
            // Simulate "recurse" with "push"
            stack.push(i);
        }
        // Return: return result
        while (stack.length) {
            // Simulate "return" with "pop"
            res += stack.pop();
        }
        // res = 1+2+3+...+n
        return res;
    }
    ```
=== "Dart"
    ```dart title="recursion.dart"
    int forLoopRecur(int n) {
      // Use an explicit stack to simulate the system call stack
      List<int> stack = [];
      int res = 0;
      // Recurse: recursive call
      for (int i = n; i > 0; i--) {
        // Simulate "recurse" with "push"
        stack.add(i);
      }
      // Return: return result
      while (!stack.isEmpty) {
        // Simulate "return" with "pop"
        res += stack.removeLast();
      }
      // res = 1+2+3+...+n
      return res;
    }
    ```
=== "Rust"
    ```rust title="recursion.rs"
    fn for_loop_recur(n: i32) -> i32 {
        // Use an explicit stack to simulate the system call stack
        let mut stack = Vec::new();
        let mut res = 0;
        // Recurse: recursive call
        for i in (1..=n).rev() {
            // Simulate "recurse" with "push"
            stack.push(i);
        }
        // Return: return result
        while !stack.is_empty() {
            // Simulate "return" with "pop"
            res += stack.pop().unwrap();
        }
        // res = 1+2+3+...+n
        res
    }
    ```
=== "C"
    ```c title="recursion.c"
    int forLoopRecur(int n) {
        int stack[1000]; // Use a large array to simulate stack
        int top = -1;    // Stack top index
        int res = 0;
        // Recurse: recursive call
        for (int i = n; i > 0; i--) {
            // Simulate "recurse" with "push"
            stack[1 + top++] = i;
        }
        // Return: return result
        while (top >= 0) {
            // Simulate "return" with "pop"
            res += stack[top--];
        }
        // res = 1+2+3+...+n
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="recursion.kt"
    fun forLoopRecur(n: Int): Int {
        // Use an explicit stack to simulate the system call stack
        val stack = Stack<Int>()
        var res = 0
        // Descend: recursive call
        for (i in n downTo 0) {
            // Simulate "recurse" with "push"
            stack.push(i)
        }
        // Return: return result
        while (stack.isNotEmpty()) {
            // Simulate "return" with "pop"
            res += stack.pop()
        }
        // res = 1+2+3+...+n
        return res
    }
    ```
=== "Ruby"
    ```ruby title="recursion.rb"
    ### Use iteration to simulate recursion ###
    def for_loop_recur(n)
      # Use an explicit stack to simulate the system call stack
      stack = []
      res = 0
    
      # Recurse: recursive call
      for i in n.downto(0)
        # Simulate "recurse" with "push"
        stack << i
      end
      # Return: return result
      while !stack.empty?
        res += stack.pop
      end
    
      # res = 1+2+3+...+n
      res
    ```


Quan sát đoạn mã trên, khi chuyển đệ quy thành phép lặp, mã trở nên phức tạp hơn. Mặc dù phép lặp và đệ quy có thể được chuyển đổi lẫn nhau trong nhiều trường hợp, nhưng việc làm đó có thể không đáng giá vì hai lý do sau.

- Mã được chuyển đổi có thể khó hiểu và khó đọc hơn.
- Đối với một số vấn đề phức tạp, việc mô phỏng hành vi của ngăn xếp lệnh gọi hệ thống có thể rất khó khăn.

Tóm lại, **việc lựa chọn giữa phép lặp và đệ quy phụ thuộc vào bản chất của vấn đề cụ thể**. Trong thực hành lập trình, điều quan trọng là phải cân nhắc ưu và nhược điểm của cả hai và chọn phương pháp phù hợp dựa trên ngữ cảnh.
