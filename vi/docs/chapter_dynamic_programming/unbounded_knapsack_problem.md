# Vấn đề về chiếc ba lô không giới hạn

Trong phần này, trước tiên chúng ta giải một bài toán về chiếc ba lô phổ biến khác: chiếc ba lô không giới hạn, sau đó khám phá một trường hợp đặc biệt của nó: bài toán đổi xu.

## Vấn đề về chiếc ba lô không giới hạn

!!! câu hỏi

Cho $n$ vật phẩm, trong đó trọng lượng của vật phẩm thứ $i$ là $wgt[i-1]$ và giá trị của nó là $val[i-1]$, và một chiếc ba lô có sức chứa $cap$. **Mỗi mục có thể được chọn nhiều lần**. Giá trị tối đa có thể được đặt trong ba lô trong giới hạn sức chứa là bao nhiêu? Một ví dụ được hiển thị trong hình dưới đây.

![Example data for unbounded knapsack problem](unbounded_knapsack_problem.assets/unbounded_knapsack_example.png)

### Phương pháp lập trình động

Bài toán về chiếc ba lô không giới hạn rất giống với bài toán về chiếc ba lô 0-1, **chỉ khác ở chỗ không có giới hạn về số lần một vật phẩm có thể được chọn**.

- Trong bài toán ba lô 0-1, mỗi loại vật phẩm chỉ có một loại nên sau khi đặt vật phẩm $i$ vào trong ba lô, chúng ta chỉ được chọn từ các vật phẩm $i-1$ đầu tiên.
- Trong bài toán ba lô không giới hạn, số lượng của mỗi loại vật phẩm là không giới hạn nên sau khi đặt vật $i$ vào ba lô, **chúng ta vẫn có thể chọn từ các vật phẩm $i$ đầu tiên**.

Theo quy tắc của bài toán chiếc ba lô không giới hạn, sự thay đổi trạng thái $[i, c]$ được chia thành hai trường hợp.

- **Không đặt đồ vật $i$**: Tương tự như bài toán về chiếc ba lô 0-1, chuyển sang $[i-1, c]$.
- **Đặt đồ vật $i$**: Khác với bài toán về chiếc ba lô 0-1, chuyển sang $[i, c-wgt[i-1]]$.

Do đó, phương trình chuyển trạng thái trở thành:

$$
dp[i, c] = \max(dp[i-1, c], dp[i, c - wgt[i-1]] + val[i-1])
$$

### Triển khai mã

So sánh mã cho hai vấn đề, có một thay đổi trong quá trình chuyển đổi trạng thái từ $i-1$ sang $i$, với mọi thứ khác giống hệt nhau:

=== "Python"
    ```python title="unbounded_knapsack.py"
    def unbounded_knapsack_dp(wgt: list[int], val: list[int], cap: int) -> int:
        """Unbounded knapsack: Dynamic programming"""
        n = len(wgt)
        # Initialize dp table
        dp = [[0] * (cap + 1) for _ in range(n + 1)]
        # State transition
        for i in range(1, n + 1):
            for c in range(1, cap + 1):
                if wgt[i - 1] > c:
                    # If exceeds knapsack capacity, don't select item i
                    dp[i][c] = dp[i - 1][c]
                else:
                    # The larger value between not selecting and selecting item i
                    dp[i][c] = max(dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1])
        return dp[n][cap]
    ```
=== "Rust"
    ```rust title="unbounded_knapsack.rs"
    fn unbounded_knapsack_dp(wgt: &[i32], val: &[i32], cap: usize) -> i32 {
        let n = wgt.len();
        // Initialize dp table
        let mut dp = vec![vec![0; cap + 1]; n + 1];
        // State transition
        for i in 1..=n {
            for c in 1..=cap {
                if wgt[i - 1] > c as i32 {
                    // If exceeds knapsack capacity, don't select item i
                    dp[i][c] = dp[i - 1][c];
                } else {
                    // The larger value between not selecting and selecting item i
                    dp[i][c] = std::cmp::max(dp[i - 1][c], dp[i][c - wgt[i - 1] as usize] + val[i - 1]);
                }
            }
        }
        return dp[n][cap];
    }
    ```
=== "Ruby"
    ```ruby title="unbounded_knapsack.rb"
    ### Unbounded knapsack: dynamic programming ###
    def unbounded_knapsack_dp(wgt, val, cap)
      n = wgt.length
      # Initialize dp table
      dp = Array.new(n + 1) { Array.new(cap + 1, 0) }
      # State transition
      for i in 1...(n + 1)
        for c in 1...(cap + 1)
          if wgt[i - 1] > c
            # If exceeds knapsack capacity, don't select item i
            dp[i][c] = dp[i - 1][c]
          else
            # The larger value between not selecting and selecting item i
            dp[i][c] = [dp[i - 1][c], dp[i][c - wgt[i - 1]] + val[i - 1]].max
          end
        end
      end
      dp[n][cap]
    ```


### Tối ưu hóa không gian

Vì trạng thái hiện tại được chuyển từ các trạng thái ở bên trái và phía trên, **sau khi tối ưu hóa không gian, mỗi hàng trong bảng $dp$ phải được duyệt theo thứ tự chuyển tiếp**.

Thứ tự di chuyển này hoàn toàn ngược lại với ba lô 0-1. Vui lòng tham khảo hình dưới đây để hiểu sự khác biệt giữa hai.

=== "<1>"
    ![Space-optimized dynamic programming process for unbounded knapsack problem](unbounded_knapsack_problem.assets/unbounded_knapsack_dp_comp_step1.png)

=== "<2>"
    ![unbounded_knapsack_dp_comp_step2](unbounded_knapsack_problem.assets/unbounded_knapsack_dp_comp_step2.png)

=== "<3>"
    ![unbounded_knapsack_dp_comp_step3](unbounded_knapsack_problem.assets/unbounded_knapsack_dp_comp_step3.png)

=== "<4>"
    ![unbounded_knapsack_dp_comp_step4](unbounded_knapsack_problem.assets/unbounded_knapsack_dp_comp_step4.png)

=== "<5>"
    ![unbounded_knapsack_dp_comp_step5](unbounded_knapsack_problem.assets/unbounded_knapsack_dp_comp_step5.png)

=== "<6>"
    ![unbounded_knapsack_dp_comp_step6](unbounded_knapsack_problem.assets/unbounded_knapsack_dp_comp_step6.png)

Việc thực hiện mã tương đối đơn giản, chỉ cần xóa chiều đầu tiên của mảng `dp`:

=== "Python"
    ```python title="unbounded_knapsack.py"
    def unbounded_knapsack_dp_comp(wgt: list[int], val: list[int], cap: int) -> int:
        """Unbounded knapsack: Space-optimized dynamic programming"""
        n = len(wgt)
        # Initialize dp table
        dp = [0] * (cap + 1)
        # State transition
        for i in range(1, n + 1):
            # Traverse in forward order
            for c in range(1, cap + 1):
                if wgt[i - 1] > c:
                    # If exceeds knapsack capacity, don't select item i
                    dp[c] = dp[c]
                else:
                    # The larger value between not selecting and selecting item i
                    dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
        return dp[cap]
    ```
=== "Rust"
    ```rust title="unbounded_knapsack.rs"
    fn unbounded_knapsack_dp_comp(wgt: &[i32], val: &[i32], cap: usize) -> i32 {
        let n = wgt.len();
        // Initialize dp table
        let mut dp = vec![0; cap + 1];
        // State transition
        for i in 1..=n {
            for c in 1..=cap {
                if wgt[i - 1] > c as i32 {
                    // If exceeds knapsack capacity, don't select item i
                    dp[c] = dp[c];
                } else {
                    // The larger value between not selecting and selecting item i
                    dp[c] = std::cmp::max(dp[c], dp[c - wgt[i - 1] as usize] + val[i - 1]);
                }
            }
        }
        dp[cap]
    }
    ```
=== "Ruby"
    ```ruby title="unbounded_knapsack.rb"
    ### Unbounded knapsack: space-optimized DP ###
    def unbounded_knapsack_dp_comp(wgt, val, cap)
      n = wgt.length
      # Initialize dp table
      dp = Array.new(cap + 1, 0)
      # State transition
      for i in 1...(n + 1)
        # Traverse in forward order
        for c in 1...(cap + 1)
          if wgt[i -1] > c
            # If exceeds knapsack capacity, don't select item i
            dp[c] = dp[c]
          else
            # The larger value between not selecting and selecting item i
            dp[c] = [dp[c], dp[c - wgt[i - 1]] + val[i - 1]].max
          end
        end
      end
      dp[cap]
    ```


## Vấn đề đổi xu

Bài toán chiếc ba lô đại diện cho một lớp lớn các bài toán quy hoạch động và có nhiều biến thể, chẳng hạn như bài toán đổi xu.

!!! câu hỏi

Cho $n$ loại tiền, trong đó mệnh giá của loại tiền $i$-là $coins[i - 1]$, và số tiền mục tiêu là $amt$. **Mỗi loại xu có thể được chọn nhiều lần**. Số xu tối thiểu cần thiết để đạt được số tiền mục tiêu là bao nhiêu? Nếu không thể đạt được số tiền mục tiêu, hãy trả lại $-1$. Một ví dụ được hiển thị trong hình dưới đây.

![Example data for coin change problem](unbounded_knapsack_problem.assets/coin_change_example.png)

### Phương pháp lập trình động

**Bài toán đổi xu có thể xem là trường hợp đặc biệt của bài toán chiếc ba lô không giới hạn**, với những mối liên hệ và điểm khác biệt sau.

- Hai bài toán có thể quy đổi cho nhau: “vật phẩm” tương ứng với “xu”, “trọng lượng vật phẩm” tương ứng với “mệnh giá tiền xu”, và “sức chứa ba lô” tương ứng với “số lượng mục tiêu”.
- Mục tiêu tối ưu hóa thì ngược lại: bài toán ba lô không giới hạn nhằm mục đích tối đa hóa giá trị vật phẩm, trong khi bài toán đổi xu nhằm mục đích giảm thiểu số lượng xu.
- Bài toán chiếc ba lô không giới hạn tìm kiếm lời giải “không vượt quá” dung lượng của chiếc ba lô, trong khi bài toán đổi xu tìm lời giải “chính xác” bằng số lượng mục tiêu.

**Bước 1: Suy nghĩ về các quyết định trong mỗi vòng, xác định trạng thái và từ đó nhận được bảng $dp$**

Trạng thái $[i, a]$ tương ứng với bài toán con: **số lượng xu tối thiểu trong số các loại $i$ đầu tiên có thể tạo nên số tiền $a$**, ký hiệu là $dp[i, a]$.

Bảng $dp$ hai chiều có kích thước $(n+1) \times (amt+1)$.

**Bước 2: Xác định cấu trúc con tối ưu và sau đó rút ra phương trình chuyển trạng thái**

Bài toán này khác với bài toán chiếc ba lô không giới hạn ở hai khía cạnh sau đây liên quan đến phương trình chuyển trạng thái.

- Bài toán này tìm giá trị nhỏ nhất nên toán tử $\max()$ cần được đổi thành $\min()$.
- Mục tiêu tối ưu hóa là số lượng xu chứ không phải giá trị vật phẩm, vì vậy khi chọn một xu, chỉ cần thêm $1$.

$$
dp[i, a] = \min(dp[i-1, a], dp[i, a - coins[i-1]] + 1)
$$

**Bước 3: Xác định điều kiện biên và thứ tự chuyển trạng thái**

Khi số tiền mục tiêu là $0$, số xu tối thiểu cần thiết để tạo nên số tiền đó là $0$, vì vậy tất cả $dp[i, 0]$ trong cột đầu tiên bằng $0$.

Khi không có xu, **không thể bù đắp bất kỳ số tiền $> 0$** nào, đây là một giải pháp không hợp lệ. Để kích hoạt hàm $\min()$ trong phương trình chuyển đổi trạng thái nhằm xác định và lọc ra các giải pháp không hợp lệ, chúng tôi xem xét sử dụng $+ \infty$ để biểu thị chúng, tức là đặt tất cả $dp[0, a]$ ở hàng đầu tiên thành $+ \infty$.

### Triển khai mã

Hầu hết các ngôn ngữ lập trình không cung cấp biến $+ \infty$ và chỉ có thể sử dụng giá trị tối đa của loại số nguyên `int` để thay thế. Tuy nhiên, điều này có thể dẫn tới tràn số nguyên: phép toán $+1$ trong phương trình chuyển trạng thái có thể gây ra tràn.

Vì lý do này, chúng tôi sử dụng số $amt + 1$ để biểu thị các giải pháp không hợp lệ, vì số lượng xu tối đa cần thiết để tạo nên $amt$ nhiều nhất là $amt$. Trước khi quay lại, hãy kiểm tra xem $dp[n, amt]$ có bằng $amt + 1$; nếu vậy, hãy trả về $-1$, cho biết rằng số tiền mục tiêu không thể đạt được. Mã này như sau:

=== "Python"
    ```python title="coin_change.py"
    def coin_change_dp(coins: list[int], amt: int) -> int:
        """Coin change: Dynamic programming"""
        n = len(coins)
        MAX = amt + 1
        # Initialize dp table
        dp = [[0] * (amt + 1) for _ in range(n + 1)]
        # State transition: first row and first column
        for a in range(1, amt + 1):
            dp[0][a] = MAX
        # State transition: rest of the rows and columns
        for i in range(1, n + 1):
            for a in range(1, amt + 1):
                if coins[i - 1] > a:
                    # If exceeds target amount, don't select coin i
                    dp[i][a] = dp[i - 1][a]
                else:
                    # The smaller value between not selecting and selecting coin i
                    dp[i][a] = min(dp[i - 1][a], dp[i][a - coins[i - 1]] + 1)
        return dp[n][amt] if dp[n][amt] != MAX else -1
    ```
=== "Rust"
    ```rust title="coin_change.rs"
    fn coin_change_dp(coins: &[i32], amt: usize) -> i32 {
        let n = coins.len();
        let max = amt + 1;
        // Initialize dp table
        let mut dp = vec![vec![0; amt + 1]; n + 1];
        // State transition: first row and first column
        for a in 1..=amt {
            dp[0][a] = max;
        }
        // State transition: rest of the rows and columns
        for i in 1..=n {
            for a in 1..=amt {
                if coins[i - 1] > a as i32 {
                    // If exceeds target amount, don't select coin i
                    dp[i][a] = dp[i - 1][a];
                } else {
                    // The smaller value between not selecting and selecting coin i
                    dp[i][a] = std::cmp::min(dp[i - 1][a], dp[i][a - coins[i - 1] as usize] + 1);
                }
            }
        }
        if dp[n][amt] != max {
            return dp[n][amt] as i32;
        } else {
            -1
        }
    }
    ```
=== "Ruby"
    ```ruby title="coin_change.rb"
    ### Coin change: dynamic programming ###
    def coin_change_dp(coins, amt)
      n = coins.length
      _MAX = amt + 1
      # Initialize dp table
      dp = Array.new(n + 1) { Array.new(amt + 1, 0) }
      # State transition: first row and first column
      (1...(amt + 1)).each { |a| dp[0][a] = _MAX }
      # State transition: rest of the rows and columns
      for i in 1...(n + 1)
        for a in 1...(amt + 1)
          if coins[i - 1] > a
            # If exceeds target amount, don't select coin i
            dp[i][a] = dp[i - 1][a]
          else
            # The smaller value between not selecting and selecting coin i
            dp[i][a] = [dp[i - 1][a], dp[i][a - coins[i - 1]] + 1].min
          end
        end
      end
      dp[n][amt] != _MAX ? dp[n][amt] : -1
    ```


Hình dưới đây cho thấy quy trình lập trình động để đổi xu, rất giống với bài toán chiếc ba lô không giới hạn.

=== "<1>"
    ![Dynamic programming process for coin change problem](unbounded_knapsack_problem.assets/coin_change_dp_step1.png)

=== "<2>"
    ![coin_change_dp_step2](unbounded_knapsack_problem.assets/coin_change_dp_step2.png)

=== "<3>"
    ![coin_change_dp_step3](unbounded_knapsack_problem.assets/coin_change_dp_step3.png)

=== "<4>"
    ![coin_change_dp_step4](unbounded_knapsack_problem.assets/coin_change_dp_step4.png)

=== "<5>"
    ![coin_change_dp_step5](unbounded_knapsack_problem.assets/coin_change_dp_step5.png)

=== "<6>"
    ![coin_change_dp_step6](unbounded_knapsack_problem.assets/coin_change_dp_step6.png)

=== "<7>"
    ![coin_change_dp_step7](unbounded_knapsack_problem.assets/coin_change_dp_step7.png)

=== "<8>"
    ![coin_change_dp_step8](unbounded_knapsack_problem.assets/coin_change_dp_step8.png)

=== "<9>"
    ![coin_change_dp_step9](unbounded_knapsack_problem.assets/coin_change_dp_step9.png)

=== "<10>"
    ![coin_change_dp_step10](unbounded_knapsack_problem.assets/coin_change_dp_step10.png)

=== "<11>"
    ![coin_change_dp_step11](unbounded_knapsack_problem.assets/coin_change_dp_step11.png)

=== "<12>"
    ![coin_change_dp_step12](unbounded_knapsack_problem.assets/coin_change_dp_step12.png)

=== "<13>"
    ![coin_change_dp_step13](unbounded_knapsack_problem.assets/coin_change_dp_step13.png)

=== "<14>"
    ![coin_change_dp_step14](unbounded_knapsack_problem.assets/coin_change_dp_step14.png)

=== "<15>"
    ![coin_change_dp_step15](unbounded_knapsack_problem.assets/coin_change_dp_step15.png)

### Tối ưu hóa không gian

Việc tối ưu hóa không gian cho bài toán đổi xu được xử lý tương tự như bài toán chiếc ba lô không giới hạn:

=== "Python"
    ```python title="coin_change.py"
    def coin_change_dp_comp(coins: list[int], amt: int) -> int:
        """Coin change: Space-optimized dynamic programming"""
        n = len(coins)
        MAX = amt + 1
        # Initialize dp table
        dp = [MAX] * (amt + 1)
        dp[0] = 0
        # State transition
        for i in range(1, n + 1):
            # Traverse in forward order
            for a in range(1, amt + 1):
                if coins[i - 1] > a:
                    # If exceeds target amount, don't select coin i
                    dp[a] = dp[a]
                else:
                    # The smaller value between not selecting and selecting coin i
                    dp[a] = min(dp[a], dp[a - coins[i - 1]] + 1)
        return dp[amt] if dp[amt] != MAX else -1
    ```
=== "Rust"
    ```rust title="coin_change.rs"
    fn coin_change_dp_comp(coins: &[i32], amt: usize) -> i32 {
        let n = coins.len();
        let max = amt + 1;
        // Initialize dp table
        let mut dp = vec![0; amt + 1];
        dp.fill(max);
        dp[0] = 0;
        // State transition
        for i in 1..=n {
            for a in 1..=amt {
                if coins[i - 1] > a as i32 {
                    // If exceeds target amount, don't select coin i
                    dp[a] = dp[a];
                } else {
                    // The smaller value between not selecting and selecting coin i
                    dp[a] = std::cmp::min(dp[a], dp[a - coins[i - 1] as usize] + 1);
                }
            }
        }
        if dp[amt] != max {
            return dp[amt] as i32;
        } else {
            -1
        }
    }
    ```
=== "Ruby"
    ```ruby title="coin_change.rb"
    ### Coin change: space-optimized DP ###
    def coin_change_dp_comp(coins, amt)
      n = coins.length
      _MAX = amt + 1
      # Initialize dp table
      dp = Array.new(amt + 1, _MAX)
      dp[0] = 0
      # State transition
      for i in 1...(n + 1)
        # Traverse in forward order
        for a in 1...(amt + 1)
          if coins[i - 1] > a
            # If exceeds target amount, don't select coin i
            dp[a] = dp[a]
          else
            # The smaller value between not selecting and selecting coin i
            dp[a] = [dp[a], dp[a - coins[i - 1]] + 1].min
          end
        end
      end
      dp[amt] != _MAX ? dp[amt] : -1
    ```


## Vấn đề đổi xu II

!!! câu hỏi

Cho $n$ loại tiền, trong đó mệnh giá của loại tiền $i$-là $coins[i - 1]$, và số tiền mục tiêu là $amt$. Mỗi loại xu có thể được chọn nhiều lần. **Số lượng kết hợp xu có thể tạo nên số tiền mục tiêu là bao nhiêu?** Một ví dụ được hiển thị trong hình bên dưới.

![Example data for coin change problem II](unbounded_knapsack_problem.assets/coin_change_ii_example.png)

### Phương pháp lập trình động

So với bài toán trước, mục tiêu của bài toán này là tìm số tổ hợp, do đó bài toán con trở thành: **số tổ hợp giữa các loại $i$ đầu tiên có thể tạo thành số tiền $a$**. Bảng $dp$ vẫn là một ma trận hai chiều có kích thước $(n+1) \times (amt + 1)$.

Số lượng kết hợp cho trạng thái hiện tại bằng tổng các kết hợp từ việc không chọn đồng xu hiện tại đến chọn đồng xu hiện tại. Phương trình chuyển trạng thái là:

$$
dp[i, a] = dp[i-1, a] + dp[i, a - coins[i-1]]
$$

Khi số tiền mục tiêu là $0$, không cần chọn đồng xu nào để tạo nên số tiền mục tiêu, vì vậy tất cả $dp[i, 0]$ trong cột đầu tiên phải được khởi tạo thành $1$. Khi không có xu, không thể tạo ra bất kỳ số tiền $>0$ nào, vì vậy tất cả $dp[0, a]$ ở hàng đầu tiên đều bằng $0$.

### Triển khai mã

=== "Python"
    ```python title="coin_change_ii.py"
    def coin_change_ii_dp(coins: list[int], amt: int) -> int:
        """Coin change II: Dynamic programming"""
        n = len(coins)
        # Initialize dp table
        dp = [[0] * (amt + 1) for _ in range(n + 1)]
        # Initialize first column
        for i in range(n + 1):
            dp[i][0] = 1
        # State transition
        for i in range(1, n + 1):
            for a in range(1, amt + 1):
                if coins[i - 1] > a:
                    # If exceeds target amount, don't select coin i
                    dp[i][a] = dp[i - 1][a]
                else:
                    # Sum of the two options: not selecting and selecting coin i
                    dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]
        return dp[n][amt]
    ```
=== "Rust"
    ```rust title="coin_change_ii.rs"
    fn coin_change_ii_dp(coins: &[i32], amt: usize) -> i32 {
        let n = coins.len();
        // Initialize dp table
        let mut dp = vec![vec![0; amt + 1]; n + 1];
        // Initialize first column
        for i in 0..=n {
            dp[i][0] = 1;
        }
        // State transition
        for i in 1..=n {
            for a in 1..=amt {
                if coins[i - 1] > a as i32 {
                    // If exceeds target amount, don't select coin i
                    dp[i][a] = dp[i - 1][a];
                } else {
                    // Sum of the two options: not selecting and selecting coin i
                    dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1] as usize];
                }
            }
        }
        dp[n][amt]
    }
    ```
=== "Ruby"
    ```ruby title="coin_change_ii.rb"
    ### Coin change II: dynamic programming ###
    def coin_change_ii_dp(coins, amt)
      n = coins.length
      # Initialize dp table
      dp = Array.new(n + 1) { Array.new(amt + 1, 0) }
      # Initialize first column
      (0...(n + 1)).each { |i| dp[i][0] = 1 }
      # State transition
      for i in 1...(n + 1)
        for a in 1...(amt + 1)
          if coins[i - 1] > a
            # If exceeds target amount, don't select coin i
            dp[i][a] = dp[i - 1][a]
          else
            # Sum of the two options: not selecting and selecting coin i
            dp[i][a] = dp[i - 1][a] + dp[i][a - coins[i - 1]]
          end
        end
      end
      dp[n][amt]
    ```


### Tối ưu hóa không gian

Việc tối ưu hóa không gian được xử lý theo cách tương tự, chỉ cần xóa kích thước đồng xu:

=== "Python"
    ```python title="coin_change_ii.py"
    def coin_change_ii_dp_comp(coins: list[int], amt: int) -> int:
        """Coin change II: Space-optimized dynamic programming"""
        n = len(coins)
        # Initialize dp table
        dp = [0] * (amt + 1)
        dp[0] = 1
        # State transition
        for i in range(1, n + 1):
            # Traverse in forward order
            for a in range(1, amt + 1):
                if coins[i - 1] > a:
                    # If exceeds target amount, don't select coin i
                    dp[a] = dp[a]
                else:
                    # Sum of the two options: not selecting and selecting coin i
                    dp[a] = dp[a] + dp[a - coins[i - 1]]
        return dp[amt]
    ```
=== "Rust"
    ```rust title="coin_change_ii.rs"
    fn coin_change_ii_dp_comp(coins: &[i32], amt: usize) -> i32 {
        let n = coins.len();
        // Initialize dp table
        let mut dp = vec![0; amt + 1];
        dp[0] = 1;
        // State transition
        for i in 1..=n {
            for a in 1..=amt {
                if coins[i - 1] > a as i32 {
                    // If exceeds target amount, don't select coin i
                    dp[a] = dp[a];
                } else {
                    // Sum of the two options: not selecting and selecting coin i
                    dp[a] = dp[a] + dp[a - coins[i - 1] as usize];
                }
            }
        }
        dp[amt]
    }
    ```
=== "Ruby"
    ```ruby title="coin_change_ii.rb"
    ### Coin change II: space-optimized DP ###
    def coin_change_ii_dp_comp(coins, amt)
      n = coins.length
      # Initialize dp table
      dp = Array.new(amt + 1, 0)
      dp[0] = 1
      # State transition
      for i in 1...(n + 1)
        # Traverse in forward order
        for a in 1...(amt + 1)
          if coins[i - 1] > a
            # If exceeds target amount, don't select coin i
            dp[a] = dp[a]
          else
            # Sum of the two options: not selecting and selecting coin i
            dp[a] = dp[a] + dp[a - coins[i - 1]]
          end
        end
      end
      dp[amt]
    ```

