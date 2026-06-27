# Đặc điểm của bài toán lập trình động

Trong phần trước, chúng ta đã tìm hiểu cách lập trình động giải quyết vấn đề ban đầu bằng cách phân tách nó thành các bài toán con. Trên thực tế, phân rã bài toán con là một cách tiếp cận thuật toán tổng quát, với các điểm nhấn khác nhau trong phân chia và chinh phục, lập trình động và quay lui.

- Thuật toán chia và chinh phục đệ quy chia bài toán ban đầu thành nhiều bài toán con độc lập cho đến khi đạt được bài toán con nhỏ nhất và hợp nhất lời giải của các bài toán con trong quá trình quay lui để cuối cùng thu được lời giải của bài toán con ban đầu.
- Lập trình động cũng phân rã đệ quy các bài toán, tuy nhiên điểm khác biệt chính so với thuật toán chia để trị là các bài toán con trong quy hoạch động phụ thuộc lẫn nhau và xuất hiện nhiều bài toán con chồng chéo trong quá trình phân rã.
- Thuật toán quay lui liệt kê tất cả các giải pháp có thể thông qua thử và sai, đồng thời tránh các nhánh tìm kiếm không cần thiết thông qua việc cắt tỉa. Lời giải của bài toán ban đầu bao gồm một loạt các bước quyết định và chúng ta có thể coi dãy con trước mỗi bước quyết định là một bài toán con.

Trên thực tế, quy hoạch động thường được sử dụng để giải các bài toán tối ưu hóa, chúng không chỉ chứa các bài toán con chồng chéo mà còn có hai đặc điểm chính khác: cấu trúc con tối ưu và không có hậu quả.

## Cấu trúc con tối ưu

Chúng tôi thực hiện một sửa đổi nhỏ cho bài toán leo cầu thang để làm cho nó phù hợp hơn trong việc thể hiện khái niệm kết cấu nền tối ưu.

!!! câu hỏi “Leo cầu thang với chi phí tối thiểu”

Với một cầu thang, bạn có thể leo từng bước $1$ hoặc $2$ một lần và mỗi bước được gắn nhãn bằng một số nguyên không âm biểu thị chi phí khi bước lên nó. Cho một mảng số nguyên không âm $cost$, trong đó $cost[i]$ biểu thị chi phí của bước $i$-th và $cost[0]$ là điểm cơ bản (điểm bắt đầu), chi phí tối thiểu cần thiết để đạt đến đỉnh là bao nhiêu?

Như được hiển thị trong hình bên dưới, nếu chi phí của các bước $1$st, $2$nd và $3$lần lượt là $1$, $10$ và $1$, thì việc leo từ mặt đất lên bước thứ $3$ yêu cầu chi phí tối thiểu là $2$.

![Minimum cost to climb to the 3rd step](dp_problem_features.assets/min_cost_cs_example.png)

Gọi $dp[i]$ là chi phí tích lũy để leo lên bước thứ $i$. Vì bước $i$-th chỉ có thể đến từ bước $i-1$-th hoặc $i-2$-th, nên $dp[i]$ chỉ có thể bằng $dp[i-1] + cost[i]$ hoặc $dp[i-2] + cost[i]$. Để giảm thiểu chi phí, chúng ta nên chọn cái nhỏ hơn trong hai cái:

$$
dp[i] = \min(dp[i-1], dp[i-2]) + chi phí[i]
$$

Điều này dẫn chúng ta đến ý nghĩa của cấu trúc con tối ưu: **lời giải tối ưu cho bài toán ban đầu được xây dựng từ lời giải tối ưu cho các bài toán con**.

Bài toán này rõ ràng có cấu trúc con tối ưu: chúng ta chọn cấu trúc con tốt hơn từ các lời giải tối ưu cho hai bài toán con $dp[i-1]$ và $dp[i-2]$, và sử dụng nó để xây dựng lời giải tối ưu cho bài toán ban đầu $dp[i]$.

Vậy bài toán leo cầu thang ở phần trước có cấu trúc phần dưới tối ưu không? Mục đích của nó là tìm ra số cách, tưởng chừng như là một bài toán đếm, nhưng nếu chúng ta đổi câu hỏi: "Tìm số cách tối đa". Chúng tôi ngạc nhiên phát hiện ra rằng **mặc dù vấn đề trước và sau khi sửa đổi là tương đương nhau, nhưng cấu trúc con tối ưu đã xuất hiện**: số cách tối đa cho bước $n$-th bằng tổng số cách tối đa cho các bước $n-1$-th và $n-2$-th. Vì vậy, việc giải thích cấu trúc con tối ưu khá linh hoạt và sẽ có ý nghĩa khác nhau trong các bài toán khác nhau.

Theo phương trình chuyển trạng thái và các trạng thái ban đầu $dp[1] = cost[1]$ và $dp[2] = cost[2]$, chúng ta có thể thu được mã lập trình động:

=== "Python"
    ```python title="min_cost_climbing_stairs_dp.py"
    def min_cost_climbing_stairs_dp(cost: list[int]) -> int:
        """Minimum cost climbing stairs: Dynamic programming"""
        n = len(cost) - 1
        if n == 1 or n == 2:
            return cost[n]
        # Initialize dp table, used to store solutions to subproblems
        dp = [0] * (n + 1)
        # Initial state: preset the solution to the smallest subproblem
        dp[1], dp[2] = cost[1], cost[2]
        # State transition: gradually solve larger subproblems from smaller ones
        for i in range(3, n + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[n]
    ```
=== "C++"
    ```cpp title="min_cost_climbing_stairs_dp.cpp"
    * File: min_cost_climbing_stairs_dp.cpp
     * Created Time: 2023-06-30
     * Author: krahets (krahets@163.com)
     */
    
    #include "../utils/common.hpp"
    
    /* Minimum cost climbing stairs: Dynamic programming */
    int minCostClimbingStairsDP(vector<int> &cost) {
        int n = cost.size() - 1;
        if (n == 1 || n == 2)
            return cost[n];
        // Initialize dp table, used to store solutions to subproblems
        vector<int> dp(n + 1);
        // Initial state: preset the solution to the smallest subproblem
        dp[1] = cost[1];
        dp[2] = cost[2];
        // State transition: gradually solve larger subproblems from smaller ones
        for (int i = 3; i <= n; i++) {
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i];
        }
        return dp[n];
    }
    ```
=== "Java"
    ```java title="min_cost_climbing_stairs_dp.java"
    public class min_cost_climbing_stairs_dp {
        /* Minimum cost climbing stairs: Dynamic programming */
        public static int minCostClimbingStairsDP(int[] cost) {
            int n = cost.length - 1;
            if (n == 1 || n == 2)
                return cost[n];
            // Initialize dp table, used to store solutions to subproblems
            int[] dp = new int[n + 1];
            // Initial state: preset the solution to the smallest subproblem
            dp[1] = cost[1];
            dp[2] = cost[2];
            // State transition: gradually solve larger subproblems from smaller ones
            for (int i = 3; i <= n; i++) {
                dp[i] = Math.min(dp[i - 1], dp[i - 2]) + cost[i];
            }
            return dp[n];
        }
    
        /* Minimum cost climbing stairs: Space-optimized dynamic programming */
        public static int minCostClimbingStairsDPComp(int[] cost) {
            int n = cost.length - 1;
            if (n == 1 || n == 2)
                return cost[n];
            int a = cost[1], b = cost[2];
            for (int i = 3; i <= n; i++) {
                int tmp = b;
                b = Math.min(a, tmp) + cost[i];
                a = tmp;
            }
            return b;
        }
    
        public static void main(String[] args) {
            int[] cost = { 0, 1, 10, 1, 1, 1, 10, 1, 1, 10, 1 };
            System.out.println(String.format("Input staircase cost list is %s", Arrays.toString(cost)));
    
            int res = minCostClimbingStairsDP(cost);
            System.out.println(String.format("Minimum cost to climb staircase is %d", res));
    
            res = minCostClimbingStairsDPComp(cost);
            System.out.println(String.format("Minimum cost to climb staircase is %d", res));
        }
    }
    ```
=== "C#"
    ```csharp title="min_cost_climbing_stairs_dp.cs"
    public class min_cost_climbing_stairs_dp {
        /* Minimum cost climbing stairs: Dynamic programming */
        int MinCostClimbingStairsDP(int[] cost) {
            int n = cost.Length - 1;
            if (n == 1 || n == 2)
                return cost[n];
            // Initialize dp table, used to store solutions to subproblems
            int[] dp = new int[n + 1];
            // Initial state: preset the solution to the smallest subproblem
            dp[1] = cost[1];
            dp[2] = cost[2];
            // State transition: gradually solve larger subproblems from smaller ones
            for (int i = 3; i <= n; i++) {
                dp[i] = Math.Min(dp[i - 1], dp[i - 2]) + cost[i];
            }
            return dp[n];
        }
    
        /* Minimum cost climbing stairs: Space-optimized dynamic programming */
        int MinCostClimbingStairsDPComp(int[] cost) {
            int n = cost.Length - 1;
            if (n == 1 || n == 2)
                return cost[n];
            int a = cost[1], b = cost[2];
            for (int i = 3; i <= n; i++) {
                int tmp = b;
                b = Math.Min(a, tmp) + cost[i];
                a = tmp;
            }
            return b;
        }
    
        [Test]
        public void Test() {
            int[] cost = [0, 1, 10, 1, 1, 1, 10, 1, 1, 10, 1];
            Console.WriteLine("Input stair cost list is");
            PrintUtil.PrintList(cost);
    
            int res = MinCostClimbingStairsDP(cost);
            Console.WriteLine($"Minimum cost to climb stairs is {res}");
    
            res = MinCostClimbingStairsDPComp(cost);
            Console.WriteLine($"Minimum cost to climb stairs is {res}");
        }
    }
    ```
=== "Go"
    ```go title="min_cost_climbing_stairs_dp.go"
    // File: min_cost_climbing_stairs_dp.go
    // Created Time: 2023-07-23
    // Author: Reanon (793584285@qq.com)
    
    package chapter_dynamic_programming
    
    /* Minimum cost climbing stairs: Dynamic programming */
    func minCostClimbingStairsDP(cost []int) int {
    	n := len(cost) - 1
    	if n == 1 || n == 2 {
    		return cost[n]
    	}
    	min := func(a, b int) int {
    		if a < b {
    			return a
    		}
    		return b
    	}
    	// Initialize dp table, used to store solutions to subproblems
    	dp := make([]int, n+1)
    	// Initial state: preset the solution to the smallest subproblem
    	dp[1] = cost[1]
    	dp[2] = cost[2]
    	// State transition: gradually solve larger subproblems from smaller ones
    	for i := 3; i <= n; i++ {
    		dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    	}
    	return dp[n]
    }
    ```
=== "Swift"
    ```swift title="min_cost_climbing_stairs_dp.swift"
    * File: min_cost_climbing_stairs_dp.swift
     * Created Time: 2023-07-15
     * Author: nuomi1 (nuomi1@qq.com)
     */
    
    /* Minimum cost climbing stairs: Dynamic programming */
    func minCostClimbingStairsDP(cost: [Int]) -> Int {
        let n = cost.count - 1
        if n == 1 || n == 2 {
            return cost[n]
        }
        // Initialize dp table, used to store solutions to subproblems
        var dp = Array(repeating: 0, count: n + 1)
        // Initial state: preset the solution to the smallest subproblem
        dp[1] = cost[1]
        dp[2] = cost[2]
        // State transition: gradually solve larger subproblems from smaller ones
        for i in 3 ... n {
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        }
        return dp[n]
    }
    ```
=== "JS"
    ```javascript title="min_cost_climbing_stairs_dp.js"
    * File: min_cost_climbing_stairs_dp.js
     * Created Time: 2023-08-23
     * Author: Gaofer Chou (gaofer-chou@qq.com)
     */
    
    /* Minimum cost climbing stairs: Dynamic programming */
    function minCostClimbingStairsDP(cost) {
        const n = cost.length - 1;
        if (n === 1 || n === 2) {
            return cost[n];
        }
        // Initialize dp table, used to store solutions to subproblems
        const dp = new Array(n + 1);
        // Initial state: preset the solution to the smallest subproblem
        dp[1] = cost[1];
        dp[2] = cost[2];
        // State transition: gradually solve larger subproblems from smaller ones
        for (let i = 3; i <= n; i++) {
            dp[i] = Math.min(dp[i - 1], dp[i - 2]) + cost[i];
        }
        return dp[n];
    }
    ```
=== "TS"
    ```typescript title="min_cost_climbing_stairs_dp.ts"
    * File: min_cost_climbing_stairs_dp.ts
     * Created Time: 2023-08-23
     * Author: Gaofer Chou (gaofer-chou@qq.com)
     */
    
    /* Minimum cost climbing stairs: Dynamic programming */
    function minCostClimbingStairsDP(cost: Array<number>): number {
        const n = cost.length - 1;
        if (n === 1 || n === 2) {
            return cost[n];
        }
        // Initialize dp table, used to store solutions to subproblems
        const dp = new Array(n + 1);
        // Initial state: preset the solution to the smallest subproblem
        dp[1] = cost[1];
        dp[2] = cost[2];
        // State transition: gradually solve larger subproblems from smaller ones
        for (let i = 3; i <= n; i++) {
            dp[i] = Math.min(dp[i - 1], dp[i - 2]) + cost[i];
        }
        return dp[n];
    }
    ```
=== "Dart"
    ```dart title="min_cost_climbing_stairs_dp.dart"
    * File: min_cost_climbing_stairs_dp.dart
     * Created Time: 2023-08-11
     * Author: liuyuxin (gvenusleo@gmail.com)
     */
    
    import 'dart:math';
    
    /* Minimum cost climbing stairs: Dynamic programming */
    int minCostClimbingStairsDP(List<int> cost) {
      int n = cost.length - 1;
      if (n == 1 || n == 2) return cost[n];
      // Initialize dp table, used to store solutions to subproblems
      List<int> dp = List.filled(n + 1, 0);
      // Initial state: preset the solution to the smallest subproblem
      dp[1] = cost[1];
      dp[2] = cost[2];
      // State transition: gradually solve larger subproblems from smaller ones
      for (int i = 3; i <= n; i++) {
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i];
      }
      return dp[n];
    }
    ```
=== "Rust"
    ```rust title="min_cost_climbing_stairs_dp.rs"
    fn min_cost_climbing_stairs_dp(cost: &[i32]) -> i32 {
        let n = cost.len() - 1;
        if n == 1 || n == 2 {
            return cost[n];
        }
        // Initialize dp table, used to store solutions to subproblems
        let mut dp = vec![-1; n + 1];
        // Initial state: preset the solution to the smallest subproblem
        dp[1] = cost[1];
        dp[2] = cost[2];
        // State transition: gradually solve larger subproblems from smaller ones
        for i in 3..=n {
            dp[i] = cmp::min(dp[i - 1], dp[i - 2]) + cost[i];
        }
        dp[n]
    }
    ```
=== "C"
    ```c title="min_cost_climbing_stairs_dp.c"
    * File: min_cost_climbing_stairs_dp.c
     * Created Time: 2023-10-02
     * Author: Zuoxun (845242523@qq.com)
     */
    
    #include "../utils/common.h"
    
    /* Find minimum value */
    int myMin(int a, int b) {
        return a < b ? a : b;
    }
    ```
=== "Kotlin"
    ```kotlin title="min_cost_climbing_stairs_dp.kt"
    * File: min_cost_climbing_stairs_dp.kt
     * Created Time: 2024-01-25
     * Author: curtishd (1023632660@qq.com)
     */
    
    package chapter_dynamic_programming
    
    import kotlin.math.min
    
    /* Minimum cost climbing stairs: Dynamic programming */
    fun minCostClimbingStairsDP(cost: IntArray): Int {
        val n = cost.size - 1
        if (n == 1 || n == 2) return cost[n]
        // Initialize dp table, used to store solutions to subproblems
        val dp = IntArray(n + 1)
        // Initial state: preset the solution to the smallest subproblem
        dp[1] = cost[1]
        dp[2] = cost[2]
        // State transition: gradually solve larger subproblems from smaller ones
        for (i in 3..n) {
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        }
        return dp[n]
    }
    ```
=== "Ruby"
    ```ruby title="min_cost_climbing_stairs_dp.rb"
    ### Minimum cost climbing stairs: DP ###
    def min_cost_climbing_stairs_dp(cost)
      n = cost.length - 1
      return cost[n] if n == 1 || n == 2
      # Initialize dp table, used to store solutions to subproblems
      dp = Array.new(n + 1, 0)
      # Initial state: preset the solution to the smallest subproblem
      dp[1], dp[2] = cost[1], cost[2]
      # State transition: gradually solve larger subproblems from smaller ones
      (3...(n + 1)).each { |i| dp[i] = [dp[i - 1], dp[i - 2]].min + cost[i] }
      dp[n]
    ```


Hình dưới đây thể hiện quy trình lập trình động cho đoạn mã trên.

![Dynamic programming process for climbing stairs with minimum cost](dp_problem_features.assets/min_cost_cs_dp.png)

Vấn đề này cũng có thể được tối ưu hóa không gian, nén từ một chiều về 0, giảm độ phức tạp của không gian từ $O(n)$ xuống $O(1)$:

=== "Python"
    ```python title="min_cost_climbing_stairs_dp.py"
    def min_cost_climbing_stairs_dp_comp(cost: list[int]) -> int:
        """Minimum cost climbing stairs: Space-optimized dynamic programming"""
        n = len(cost) - 1
        if n == 1 or n == 2:
            return cost[n]
        a, b = cost[1], cost[2]
        for i in range(3, n + 1):
            a, b = b, min(a, b) + cost[i]
        return b
    ```
=== "Rust"
    ```rust title="min_cost_climbing_stairs_dp.rs"
    fn min_cost_climbing_stairs_dp_comp(cost: &[i32]) -> i32 {
        let n = cost.len() - 1;
        if n == 1 || n == 2 {
            return cost[n];
        };
        let (mut a, mut b) = (cost[1], cost[2]);
        for i in 3..=n {
            let tmp = b;
            b = cmp::min(a, tmp) + cost[i];
            a = tmp;
        }
        b
    }
    ```
=== "Ruby"
    ```ruby title="min_cost_climbing_stairs_dp.rb"
    # Minimum cost climbing stairs: Space-optimized dynamic programming
    def min_cost_climbing_stairs_dp_comp(cost)
      n = cost.length - 1
      return cost[n] if n == 1 || n == 2
      a, b = cost[1], cost[2]
      (3...(n + 1)).each { |i| a, b = b, [a, b].min + cost[i] }
      b
    ```


## Không có hậu quả

Không có hậu quả là một trong những đặc điểm quan trọng cho phép lập trình động giải quyết vấn đề một cách hiệu quả. Định nghĩa của nó là: **với một trạng thái nhất định, sự phát triển trong tương lai của nó chỉ liên quan đến trạng thái hiện tại và không liên quan gì đến tất cả các trạng thái trong quá khứ**.

Lấy bài toán leo cầu thang làm ví dụ, với trạng thái $i$, nó sẽ phát triển thành các trạng thái $i+1$ và $i+2$, tương ứng với việc nhảy bước $1$ và nhảy bước $2$. Khi thực hiện hai lựa chọn này, chúng ta không cần xem xét các trạng thái trước trạng thái $i$, vì chúng không ảnh hưởng gì đến tương lai của trạng thái $i$.

Tuy nhiên, nếu chúng ta thêm một ràng buộc cho bài toán leo cầu thang thì tình hình sẽ thay đổi.

!!! Câu hỏi “Leo cầu thang có hạn chế”

Cho một cầu thang có $n$ bậc, trong đó bạn có thể leo lên các bậc $1$ hoặc $2$ cùng một lúc, **nhưng bạn không thể nhảy bước $1$ trong hai vòng liên tiếp**. Có bao nhiêu cách để leo lên đỉnh?

Như được minh họa trong hình bên dưới, chỉ có những cách khả thi $2$ để leo lên bước thứ $3$. Đường đi có ba bước nhảy $1$ liên tiếp không thỏa mãn ràng buộc và do đó bị loại bỏ.

![Number of ways to climb to the 3rd step with constraint](dp_problem_features.assets/climbing_stairs_constraint_example.png)

Trong bài toán này, nếu vòng trước là bước nhảy $1$ thì vòng tiếp theo phải nhảy bước $2$. Điều này có nghĩa là **lựa chọn tiếp theo không thể chỉ được xác định bởi trạng thái hiện tại (số bước cầu thang hiện tại) mà còn phụ thuộc vào trạng thái trước đó (số bước cầu thang từ vòng trước)**.

Không khó để thấy rằng vấn đề này không còn thỏa mãn không có hậu quả, và phương trình chuyển đổi trạng thái $dp[i] = dp[i-1] + dp[i-2]$ cũng thất bại, bởi vì $dp[i-1]$ thể hiện việc nhảy $1$ trong vòng này, nhưng nó bao gồm nhiều giải pháp trong đó "vòng trước là bước nhảy $1$", không thể tính trực tiếp bằng $dp[i]$ để thỏa mãn ràng buộc.

Vì lý do này, chúng ta cần mở rộng định nghĩa trạng thái: **state $[i, j]$ thể hiện đang ở bước $i$-th với vòng trước đã nhảy $j$ bước**, trong đó $j \in \{1, 2\}$. Định nghĩa trạng thái này phân biệt một cách hiệu quả liệu vòng trước đó là bước nhảy $1$ hay bước $2$, cho phép chúng tôi xác định trạng thái hiện tại đến từ đâu.

- Khi vòng trước nhảy $1$, vòng trước đó chỉ được chọn nhảy $2$, tức là $dp[i, 1]$ chỉ có thể chuyển từ $dp[i-1, 2]$.
- Khi vòng trước nhảy $2$ bước, vòng trước đó có thể chọn nhảy $1$ bước hoặc $2$ bước, tức là $dp[i, 2]$ có thể chuyển từ $dp[i-2, 1]$ hoặc $dp[i-2, 2]$.

Như được hiển thị trong hình bên dưới, theo định nghĩa này, $dp[i, j]$ biểu thị số cách để chuyển sang trạng thái $[i, j]$. Khi đó phương trình chuyển trạng thái sẽ là:

$$
\bắt đầu{trường hợp}
dp[i, 1] = dp[i-1, 2] \\
dp[i, 2] = dp[i-2, 1] + dp[i-2, 2]
\end{trường hợp}
$$

![Recurrence relation considering constraints](dp_problem_features.assets/climbing_stairs_constraint_state_transfer.png)

Cuối cùng, trả về $dp[n, 1] + dp[n, 2]$, trong đó tổng của hai đại diện cho tổng số cách để leo lên bước $n$-th:

=== "Python"
    ```python title="climbing_stairs_constraint_dp.py"
    def climbing_stairs_constraint_dp(n: int) -> int:
        """Climbing stairs with constraint: Dynamic programming"""
        if n == 1 or n == 2:
            return 1
        # Initialize dp table, used to store solutions to subproblems
        dp = [[0] * 3 for _ in range(n + 1)]
        # Initial state: preset the solution to the smallest subproblem
        dp[1][1], dp[1][2] = 1, 0
        dp[2][1], dp[2][2] = 0, 1
        # State transition: gradually solve larger subproblems from smaller ones
        for i in range(3, n + 1):
            dp[i][1] = dp[i - 1][2]
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
        return dp[n][1] + dp[n][2]
    ```
=== "C++"
    ```cpp title="climbing_stairs_constraint_dp.cpp"
    * File: climbing_stairs_constraint_dp.cpp
     * Created Time: 2023-07-01
     * Author: krahets (krahets@163.com)
     */
    
    #include "../utils/common.hpp"
    
    /* Climbing stairs with constraint: Dynamic programming */
    int climbingStairsConstraintDP(int n) {
        if (n == 1 || n == 2) {
            return 1;
        }
        // Initialize dp table, used to store solutions to subproblems
        vector<vector<int>> dp(n + 1, vector<int>(3, 0));
        // Initial state: preset the solution to the smallest subproblem
        dp[1][1] = 1;
        dp[1][2] = 0;
        dp[2][1] = 0;
        dp[2][2] = 1;
        // State transition: gradually solve larger subproblems from smaller ones
        for (int i = 3; i <= n; i++) {
            dp[i][1] = dp[i - 1][2];
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
        }
        return dp[n][1] + dp[n][2];
    }
    ```
=== "Java"
    ```java title="climbing_stairs_constraint_dp.java"
    public class climbing_stairs_constraint_dp {
        /* Climbing stairs with constraint: Dynamic programming */
        static int climbingStairsConstraintDP(int n) {
            if (n == 1 || n == 2) {
                return 1;
            }
            // Initialize dp table, used to store solutions to subproblems
            int[][] dp = new int[n + 1][3];
            // Initial state: preset the solution to the smallest subproblem
            dp[1][1] = 1;
            dp[1][2] = 0;
            dp[2][1] = 0;
            dp[2][2] = 1;
            // State transition: gradually solve larger subproblems from smaller ones
            for (int i = 3; i <= n; i++) {
                dp[i][1] = dp[i - 1][2];
                dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
            }
            return dp[n][1] + dp[n][2];
        }
    
        public static void main(String[] args) {
            int n = 9;
    
            int res = climbingStairsConstraintDP(n);
            System.out.println(String.format("Climbing %d stairs has %d solutions", n, res));
        }
    }
    ```
=== "C#"
    ```csharp title="climbing_stairs_constraint_dp.cs"
    public class climbing_stairs_constraint_dp {
        /* Climbing stairs with constraint: Dynamic programming */
        int ClimbingStairsConstraintDP(int n) {
            if (n == 1 || n == 2) {
                return 1;
            }
            // Initialize dp table, used to store solutions to subproblems
            int[,] dp = new int[n + 1, 3];
            // Initial state: preset the solution to the smallest subproblem
            dp[1, 1] = 1;
            dp[1, 2] = 0;
            dp[2, 1] = 0;
            dp[2, 2] = 1;
            // State transition: gradually solve larger subproblems from smaller ones
            for (int i = 3; i <= n; i++) {
                dp[i, 1] = dp[i - 1, 2];
                dp[i, 2] = dp[i - 2, 1] + dp[i - 2, 2];
            }
            return dp[n, 1] + dp[n, 2];
        }
    
        [Test]
        public void Test() {
            int n = 9;
            int res = ClimbingStairsConstraintDP(n);
            Console.WriteLine($"Climbing {n} stairs has {res} solutions");
        }
    }
    ```
=== "Go"
    ```go title="climbing_stairs_constraint_dp.go"
    // File: climbing_stairs_constraint_dp.go
    // Created Time: 2023-07-18
    // Author: Reanon (793584285@qq.com)
    
    package chapter_dynamic_programming
    
    /* Climbing stairs with constraint: Dynamic programming */
    func climbingStairsConstraintDP(n int) int {
    	if n == 1 || n == 2 {
    		return 1
    	}
    	// Initialize dp table, used to store solutions to subproblems
    	dp := make([][3]int, n+1)
    	// Initial state: preset the solution to the smallest subproblem
    	dp[1][1] = 1
    	dp[1][2] = 0
    	dp[2][1] = 0
    	dp[2][2] = 1
    	// State transition: gradually solve larger subproblems from smaller ones
    	for i := 3; i <= n; i++ {
    		dp[i][1] = dp[i-1][2]
    		dp[i][2] = dp[i-2][1] + dp[i-2][2]
    	}
    	return dp[n][1] + dp[n][2]
    }
    ```
=== "Swift"
    ```swift title="climbing_stairs_constraint_dp.swift"
    * File: climbing_stairs_constraint_dp.swift
     * Created Time: 2023-07-15
     * Author: nuomi1 (nuomi1@qq.com)
     */
    
    /* Climbing stairs with constraint: Dynamic programming */
    func climbingStairsConstraintDP(n: Int) -> Int {
        if n == 1 || n == 2 {
            return 1
        }
        // Initialize dp table, used to store solutions to subproblems
        var dp = Array(repeating: Array(repeating: 0, count: 3), count: n + 1)
        // Initial state: preset the solution to the smallest subproblem
        dp[1][1] = 1
        dp[1][2] = 0
        dp[2][1] = 0
        dp[2][2] = 1
        // State transition: gradually solve larger subproblems from smaller ones
        for i in 3 ... n {
            dp[i][1] = dp[i - 1][2]
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
        }
        return dp[n][1] + dp[n][2]
    }
    ```
=== "JS"
    ```javascript title="climbing_stairs_constraint_dp.js"
    * File: climbing_stairs_constraint_dp.js
     * Created Time: 2023-08-23
     * Author: Gaofer Chou (gaofer-chou@qq.com)
     */
    
    /* Climbing stairs with constraint: Dynamic programming */
    function climbingStairsConstraintDP(n) {
        if (n === 1 || n === 2) {
            return 1;
        }
        // Initialize dp table, used to store solutions to subproblems
        const dp = Array.from(new Array(n + 1), () => new Array(3));
        // Initial state: preset the solution to the smallest subproblem
        dp[1][1] = 1;
        dp[1][2] = 0;
        dp[2][1] = 0;
        dp[2][2] = 1;
        // State transition: gradually solve larger subproblems from smaller ones
        for (let i = 3; i <= n; i++) {
            dp[i][1] = dp[i - 1][2];
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
        }
        return dp[n][1] + dp[n][2];
    }
    ```
=== "TS"
    ```typescript title="climbing_stairs_constraint_dp.ts"
    * File: climbing_stairs_constraint_dp.ts
     * Created Time: 2023-08-23
     * Author: Gaofer Chou (gaofer-chou@qq.com)
     */
    
    /* Climbing stairs with constraint: Dynamic programming */
    function climbingStairsConstraintDP(n: number): number {
        if (n === 1 || n === 2) {
            return 1;
        }
        // Initialize dp table, used to store solutions to subproblems
        const dp = Array.from({ length: n + 1 }, () => new Array(3));
        // Initial state: preset the solution to the smallest subproblem
        dp[1][1] = 1;
        dp[1][2] = 0;
        dp[2][1] = 0;
        dp[2][2] = 1;
        // State transition: gradually solve larger subproblems from smaller ones
        for (let i = 3; i <= n; i++) {
            dp[i][1] = dp[i - 1][2];
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
        }
        return dp[n][1] + dp[n][2];
    }
    ```
=== "Dart"
    ```dart title="climbing_stairs_constraint_dp.dart"
    * File: climbing_stairs_constraint_dp.dart
     * Created Time: 2023-08-11
     * Author: liuyuxin (gvenusleo@gmail.com)
     */
    
    /* Climbing stairs with constraint: Dynamic programming */
    int climbingStairsConstraintDP(int n) {
      if (n == 1 || n == 2) {
        return 1;
      }
      // Initialize dp table, used to store solutions to subproblems
      List<List<int>> dp = List.generate(n + 1, (index) => List.filled(3, 0));
      // Initial state: preset the solution to the smallest subproblem
      dp[1][1] = 1;
      dp[1][2] = 0;
      dp[2][1] = 0;
      dp[2][2] = 1;
      // State transition: gradually solve larger subproblems from smaller ones
      for (int i = 3; i <= n; i++) {
        dp[i][1] = dp[i - 1][2];
        dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
      }
      return dp[n][1] + dp[n][2];
    }
    ```
=== "Rust"
    ```rust title="climbing_stairs_constraint_dp.rs"
    fn climbing_stairs_constraint_dp(n: usize) -> i32 {
        if n == 1 || n == 2 {
            return 1;
        };
        // Initialize dp table, used to store solutions to subproblems
        let mut dp = vec![vec![-1; 3]; n + 1];
        // Initial state: preset the solution to the smallest subproblem
        dp[1][1] = 1;
        dp[1][2] = 0;
        dp[2][1] = 0;
        dp[2][2] = 1;
        // State transition: gradually solve larger subproblems from smaller ones
        for i in 3..=n {
            dp[i][1] = dp[i - 1][2];
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
        }
        dp[n][1] + dp[n][2]
    }
    ```
=== "C"
    ```c title="climbing_stairs_constraint_dp.c"
    * File: climbing_stairs_constraint_dp.c
     * Created Time: 2023-10-02
     * Author: Zuoxun (845242523@qq.com)
     */
    
    #include "../utils/common.h"
    
    /* Climbing stairs with constraint: Dynamic programming */
    int climbingStairsConstraintDP(int n) {
        if (n == 1 || n == 2) {
            return 1;
        }
        // Initialize dp table, used to store solutions to subproblems
        int **dp = malloc((n + 1) * sizeof(int *));
        for (int i = 0; i <= n; i++) {
            dp[i] = calloc(3, sizeof(int));
        }
        // Initial state: preset the solution to the smallest subproblem
        dp[1][1] = 1;
        dp[1][2] = 0;
        dp[2][1] = 0;
        dp[2][2] = 1;
        // State transition: gradually solve larger subproblems from smaller ones
        for (int i = 3; i <= n; i++) {
            dp[i][1] = dp[i - 1][2];
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
        }
        int res = dp[n][1] + dp[n][2];
        // Free memory
        for (int i = 0; i <= n; i++) {
            free(dp[i]);
        }
        free(dp);
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="climbing_stairs_constraint_dp.kt"
    * File: climbing_stairs_constraint_dp.kt
     * Created Time: 2024-01-25
     * Author: curtishd (1023632660@qq.com)
     */
    
    package chapter_dynamic_programming
    
    /* Climbing stairs with constraint: Dynamic programming */
    fun climbingStairsConstraintDP(n: Int): Int {
        if (n == 1 || n == 2) {
            return 1
        }
        // Initialize dp table, used to store solutions to subproblems
        val dp = Array(n + 1) { IntArray(3) }
        // Initial state: preset the solution to the smallest subproblem
        dp[1][1] = 1
        dp[1][2] = 0
        dp[2][1] = 0
        dp[2][2] = 1
        // State transition: gradually solve larger subproblems from smaller ones
        for (i in 3..n) {
            dp[i][1] = dp[i - 1][2]
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
        }
        return dp[n][1] + dp[n][2]
    }
    ```
=== "Ruby"
    ```ruby title="climbing_stairs_constraint_dp.rb"
    ### Climbing stairs with constraint: DP ###
    def climbing_stairs_constraint_dp(n)
      return 1 if n == 1 || n == 2
    
      # Initialize dp table, used to store solutions to subproblems
      dp = Array.new(n + 1) { Array.new(3, 0) }
      # Initial state: preset the solution to the smallest subproblem
      dp[1][1], dp[1][2] = 1, 0
      dp[2][1], dp[2][2] = 0, 1
      # State transition: gradually solve larger subproblems from smaller ones
      for i in 3...(n + 1)
        dp[i][1] = dp[i - 1][2]
        dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
      end
    
      dp[n][1] + dp[n][2]
    ```


Trong trường hợp trên, vì chỉ cần xét thêm một trạng thái trước đó nên chúng ta vẫn có thể làm cho bài toán thỏa mãn không có hậu quả bằng cách mở rộng định nghĩa trạng thái. Tuy nhiên, một số vấn đề có “hậu quả” rất nghiêm trọng.

!!! Câu hỏi "Leo cầu thang có tạo chướng ngại vật"

Cho một cầu thang có $n$ bậc, trong đó bạn có thể leo từng bậc $1$ hoặc $2$ một lần. **Bất cứ khi nào bạn đạt đến bước $i$-th, hệ thống sẽ tự động đặt chướng ngại vật ở bước $2i$-th và không vòng tiếp theo nào được phép chuyển sang bước $2i$-th**. Ví dụ: nếu hai vòng đầu tiên chuyển sang bước thứ $2$ và $3$, thì sau đó bạn không thể chuyển sang bước thứ $4$ và $6$. Có bao nhiêu cách để leo lên đỉnh?

Trong bài toán này, lần nhảy tiếp theo phụ thuộc vào tất cả các trạng thái trong quá khứ, bởi vì mỗi lần nhảy sẽ đặt chướng ngại vật ở các bước cao hơn, ảnh hưởng đến các lần nhảy trong tương lai. Đối với những bài toán như vậy, quy hoạch động thường khó giải quyết.

Trên thực tế, nhiều bài toán tối ưu hóa tổ hợp phức tạp (chẳng hạn như bài toán người bán hàng du lịch) không thỏa mãn bất kỳ hậu quả nào. Đối với những vấn đề như vậy, chúng ta thường sử dụng các phương pháp khác, chẳng hạn như tìm kiếm heuristic, thuật toán di truyền và học tăng cường, để thu được các giải pháp tối ưu cục bộ có thể sử dụng được trong một thời gian giới hạn.
