# Bài toán tổng tập hợp con

## Không có phần tử trùng lặp

!!! câu hỏi

Cho một mảng số nguyên dương `nums` và một số nguyên dương mục tiêu `target`, hãy tìm tất cả các kết hợp có thể có trong đó tổng các phần tử trong kết hợp bằng `target`. Mảng đã cho không có phần tử trùng lặp và mỗi phần tử có thể được chọn nhiều lần. Trả về các kết hợp này ở dạng danh sách, trong đó danh sách không được chứa các kết hợp trùng lặp.

Ví dụ: với tập $\{3, 4, 5\}$ và số nguyên mục tiêu $9$, các nghiệm là $\{3, 3, 3\}, \{4, 5\}$. Lưu ý hai điểm sau:

- Các phần tử trong tập đầu vào có thể được chọn lặp lại không giới hạn.
- Tập con không phân biệt thứ tự phần tử; ví dụ: $\{4, 5\}$ và $\{5, 4\}$ là cùng một tập hợp con.

### Sử dụng Giải pháp hoán vị làm tài liệu tham khảo

Tương tự như bài toán hoán vị, chúng ta có thể xem quá trình tạo các tập con là kết quả của một loạt các lựa chọn và cập nhật tổng chạy trong quá trình lựa chọn. Khi tổng bằng `target`, chúng tôi ghi tập hợp con vào danh sách kết quả.

Không giống như bài toán hoán vị, **các phần tử trong bài toán này có thể được chọn bao nhiêu lần**, vì vậy chúng ta không cần sử dụng danh sách boolean `selected` để theo dõi xem một phần tử đã được chọn chưa. Với một vài thay đổi nhỏ đối với mã hoán vị, chúng ta thu được lời giải ban đầu:

=== "Python"
    ```python title="subset_sum_i_naive.py"
    def subset_sum_i_naive(nums: list[int], target: int) -> list[list[int]]:
        """Solve subset sum I (including duplicate subsets)"""
        state = []  # State (subset)
        total = 0  # Subset sum
        res = []  # Result list (subset list)
        backtrack(state, target, total, nums, res)
        return res
    ```
=== "C++"
    ```cpp title="subset_sum_i_naive.cpp"
    vector<vector<int>> subsetSumINaive(vector<int> &nums, int target) {
        vector<int> state;       // State (subset)
        int total = 0;           // Subset sum
        vector<vector<int>> res; // Result list (subset list)
        backtrack(state, target, total, nums, res);
        return res;
    }
    ```
=== "Java"
    ```java title="subset_sum_i_naive.java"
    public class subset_sum_i_naive {
        /* Backtracking algorithm: Subset sum I */
        static void backtrack(List<Integer> state, int target, int total, int[] choices, List<List<Integer>> res) {
            // When the subset sum equals target, record the solution
            if (total == target) {
                res.add(new ArrayList<>(state));
                return;
            }
            // Traverse all choices
            for (int i = 0; i < choices.length; i++) {
                // Pruning: if the subset sum exceeds target, skip this choice
                if (total + choices[i] > target) {
                    continue;
                }
                // Attempt: make choice, update element sum total
                state.add(choices[i]);
                // Proceed to the next round of selection
                backtrack(state, target, total + choices[i], choices, res);
                // Backtrack: undo choice, restore to previous state
                state.remove(state.size() - 1);
            }
        }
    
        /* Solve subset sum I (including duplicate subsets) */
        static List<List<Integer>> subsetSumINaive(int[] nums, int target) {
            List<Integer> state = new ArrayList<>(); // State (subset)
            int total = 0; // Subset sum
            List<List<Integer>> res = new ArrayList<>(); // Result list (subset list)
            backtrack(state, target, total, nums, res);
            return res;
        }
    
        public static void main(String[] args) {
            int[] nums = { 3, 4, 5 };
            int target = 9;
    
            List<List<Integer>> res = subsetSumINaive(nums, target);
    
            System.out.println("Input array nums = " + Arrays.toString(nums) + ", target = " + target);
            System.out.println("All subsets with sum equal to " + target + " are res = " + res);
            System.out.println("Please note that this method outputs results containing duplicate sets");
        }
    }
    ```
=== "C#"
    ```csharp title="subset_sum_i_naive.cs"
    public class subset_sum_i_naive {
        /* Backtracking algorithm: Subset sum I */
        void Backtrack(List<int> state, int target, int total, int[] choices, List<List<int>> res) {
            // When the subset sum equals target, record the solution
            if (total == target) {
                res.Add(new List<int>(state));
                return;
            }
            // Traverse all choices
            for (int i = 0; i < choices.Length; i++) {
                // Pruning: if the subset sum exceeds target, skip this choice
                if (total + choices[i] > target) {
                    continue;
                }
                // Attempt: make choice, update element sum total
                state.Add(choices[i]);
                // Proceed to the next round of selection
                Backtrack(state, target, total + choices[i], choices, res);
                // Backtrack: undo choice, restore to previous state
                state.RemoveAt(state.Count - 1);
            }
        }
    
        /* Solve subset sum I (including duplicate subsets) */
        List<List<int>> SubsetSumINaive(int[] nums, int target) {
            List<int> state = []; // State (subset)
            int total = 0; // Subset sum
            List<List<int>> res = []; // Result list (subset list)
            Backtrack(state, target, total, nums, res);
            return res;
        }
    
        [Test]
        public void Test() {
            int[] nums = [3, 4, 5];
            int target = 9;
            List<List<int>> res = SubsetSumINaive(nums, target);
            Console.WriteLine("Input array nums = " + string.Join(", ", nums) + ", target = " + target);
            Console.WriteLine("All subsets with sum equal to " + target + " are res = ");
            foreach (var subset in res) {
                PrintUtil.PrintList(subset);
            }
            Console.WriteLine("Please note that this method outputs results containing duplicate sets");
        }
    }
    ```
=== "Go"
    ```go title="subset_sum_i_naive.go"
    func backtrackSubsetSumINaive(total, target int, state, choices *[]int, res *[][]int) {
    	// When the subset sum equals target, record the solution
    	if target == total {
    		newState := append([]int{}, *state...)
    		*res = append(*res, newState)
    		return
    	}
    	// Traverse all choices
    	for i := 0; i < len(*choices); i++ {
    		// Pruning: if the subset sum exceeds target, skip this choice
    		if total+(*choices)[i] > target {
    			continue
    		}
    		// Attempt: make choice, update element sum total
    		*state = append(*state, (*choices)[i])
    		// Proceed to the next round of selection
    		backtrackSubsetSumINaive(total+(*choices)[i], target, state, choices, res)
    		// Backtrack: undo choice, restore to previous state
    		*state = (*state)[:len(*state)-1]
    	}
    }
    ```
=== "Swift"
    ```swift title="subset_sum_i_naive.swift"
    func subsetSumINaive(nums: [Int], target: Int) -> [[Int]] {
        var state: [Int] = [] // State (subset)
        let total = 0 // Subset sum
        var res: [[Int]] = [] // Result list (subset list)
        backtrack(state: &state, target: target, total: total, choices: nums, res: &res)
        return res
    }
    ```
=== "JS"
    ```javascript title="subset_sum_i_naive.js"
    function subsetSumINaive(nums, target) {
        const state = []; // State (subset)
        const total = 0; // Subset sum
        const res = []; // Result list (subset list)
        backtrack(state, target, total, nums, res);
        return res;
    }
    ```
=== "TS"
    ```typescript title="subset_sum_i_naive.ts"
    function subsetSumINaive(nums: number[], target: number): number[][] {
        const state = []; // State (subset)
        const total = 0; // Subset sum
        const res = []; // Result list (subset list)
        backtrack(state, target, total, nums, res);
        return res;
    }
    ```
=== "Dart"
    ```dart title="subset_sum_i_naive.dart"
    List<List<int>> subsetSumINaive(List<int> nums, int target) {
      List<int> state = []; // State (subset)
      int total = 0; // Sum of elements
      List<List<int>> res = []; // Result list (subset list)
      backtrack(state, target, total, nums, res);
      return res;
    }
    ```
=== "Rust"
    ```rust title="subset_sum_i_naive.rs"
    fn subset_sum_i_naive(nums: &[i32], target: i32) -> Vec<Vec<i32>> {
        let mut state = Vec::new(); // State (subset)
        let total = 0; // Subset sum
        let mut res = Vec::new(); // Result list (subset list)
        backtrack(&mut state, target, total, nums, &mut res);
        res
    }
    ```
=== "C"
    ```c title="subset_sum_i_naive.c"
    void subsetSumINaive(int *nums, int numsSize, int target) {
        resSize = 0; // Initialize solution count to 0
        backtrack(target, 0, nums, numsSize);
    }
    ```
=== "Kotlin"
    ```kotlin title="subset_sum_i_naive.kt"
    fun subsetSumINaive(nums: IntArray, target: Int): MutableList<MutableList<Int>?> {
        val state = mutableListOf<Int>() // State (subset)
        val total = 0 // Subset sum
        val res = mutableListOf<MutableList<Int>?>() // Result list (subset list)
        backtrack(state, target, total, nums, res)
        return res
    }
    ```
=== "Ruby"
    ```ruby title="subset_sum_i_naive.rb"
    ### Solve subset sum I (with duplicate subsets) ###
    def subset_sum_i_naive(nums, target)
      state = [] # State (subset)
      total = 0 # Subset sum
      res = [] # Result list (subset list)
      backtrack(state, target, total, nums, res)
      res
    ```


Chạy đoạn mã trên trên mảng $[3, 4, 5]$ với giá trị đích $9$ sẽ tạo ra $[3, 3, 3], [4, 5], [5, 4]$. **Mặc dù chúng tôi đã tìm thành công tất cả các tập hợp con có tổng bằng $9$, nhưng vẫn có các tập hợp con trùng lặp $[4, 5]$ và $[5, 4]$**.

Điều này là do quá trình tìm kiếm phân biệt thứ tự các lựa chọn, nhưng các tập hợp con không phân biệt thứ tự lựa chọn. Như minh họa trong hình bên dưới, việc chọn 4 trước rồi đến 5 so với chọn 5 trước rồi 4 là các nhánh khác nhau, nhưng chúng tương ứng với cùng một tập hợp con.

![Subset search and boundary pruning](subset_sum_problem.assets/subset_sum_i_naive.png)

Để loại bỏ các tập hợp con trùng lặp, **một ý tưởng đơn giản là loại bỏ danh sách kết quả trùng lặp**. Tuy nhiên, phương pháp này rất kém hiệu quả vì hai lý do:

- Khi có nhiều phần tử mảng, đặc biệt khi `target` lớn, quá trình tìm kiếm sẽ tạo ra nhiều tập con trùng lặp.
- Việc so sánh các tập con (mảng) rất tốn thời gian, đòi hỏi phải sắp xếp các mảng trước, sau đó so sánh từng phần tử trong mảng.

### Cắt bớt các tập hợp con trùng lặp

**Chúng tôi xem xét việc loại bỏ trùng lặp thông qua việc cắt bớt trong quá trình tìm kiếm**. Quan sát hình bên dưới, các tập hợp con trùng lặp xảy ra khi các phần tử mảng được chọn theo các thứ tự khác nhau, như trong các trường hợp sau:

1. Khi vòng đầu tiên và vòng thứ hai chọn $3$ và $4$ tương ứng, tất cả các tập con chứa hai phần tử này sẽ được tạo, ký hiệu là $[3, 4, \dots]$.
2. Sau đó, khi vòng đầu tiên chọn $4$, **vòng thứ hai sẽ bỏ qua $3$**, vì tập hợp con $[4, 3, \dots]$ được tạo bởi lựa chọn này là bản sao chính xác của tập hợp con được tạo ở bước `1.`

Trong quá trình tìm kiếm, các lựa chọn của mỗi cấp độ sẽ được thử từ trái sang phải nên các nhánh ngoài cùng bên phải sẽ được lược bỏ nhiều hơn.

1. Hai vòng đầu tiên chọn $3$ và $5$, tạo tập con $[3, 5, \dots]$.
2. Hai vòng đầu tiên chọn $4$ và $5$, tạo tập con $[4, 5, \dots]$.
3. Nếu vòng đầu tiên chọn $5$, **vòng thứ hai sẽ bỏ qua $3$ và $4$**, vì các tập hợp con $[5, 3, \dots]$ và $[5, 4, \dots]$ là bản sao chính xác của các tập hợp con được mô tả trong bước `1.` và `2.`

![Different selection orders leading to duplicate subsets](subset_sum_problem.assets/subset_sum_i_pruning.png)

Tóm lại, với mảng đầu vào $[x_1, x_2, \dots, x_n]$, hãy đặt chuỗi lựa chọn trong quá trình tìm kiếm là $[x_{i_1}, x_{i_2}, \dots, x_{i_m}]$. Trình tự lựa chọn này phải thỏa mãn $i_1 \leq i_2 \leq \dots \leq i_m$; **bất kỳ chuỗi lựa chọn nào không thỏa mãn điều kiện này sẽ gây ra sự trùng lặp và cần được cắt bớt**.

### Triển khai mã

Để thực hiện việc cắt tỉa này, chúng ta khởi tạo một biến `start` để chỉ ra điểm bắt đầu của quá trình truyền tải. **Sau khi thực hiện lựa chọn $x_{i}$, hãy đặt vòng tiếp theo để bắt đầu truyền tải từ chỉ mục $i$**. Điều này đảm bảo rằng chuỗi lựa chọn thỏa mãn $i_1 \leq i_2 \leq \dots \leq i_m$, đảm bảo tính duy nhất của tập hợp con.

Ngoài ra, chúng tôi đã thực hiện hai tối ưu hóa sau cho mã:

- Trước khi bắt đầu tìm kiếm, đầu tiên hãy sắp xếp mảng `nums`. Khi duyệt qua tất cả các lựa chọn, **kết thúc vòng lặp ngay lập tức khi tổng tập hợp con vượt quá `target`**, vì các phần tử tiếp theo lớn hơn và tổng tập hợp con của chúng phải vượt quá `target`.
- Bỏ qua biến tổng phần tử `total` và **sử dụng phép trừ trên `target` để theo dõi tổng các phần tử**. Ghi lại lời giải khi `target` bằng $0$.

=== "Python"
    ```python title="subset_sum_i.py"
    def subset_sum_i(nums: list[int], target: int) -> list[list[int]]:
        """Solve subset sum I"""
        state = []  # State (subset)
        nums.sort()  # Sort nums
        start = 0  # Start point for traversal
        res = []  # Result list (subset list)
        backtrack(state, target, nums, start, res)
        return res
    ```
=== "C++"
    ```cpp title="subset_sum_i.cpp"
    vector<vector<int>> subsetSumI(vector<int> &nums, int target) {
        vector<int> state;              // State (subset)
        sort(nums.begin(), nums.end()); // Sort nums
        int start = 0;                  // Start point for traversal
        vector<vector<int>> res;        // Result list (subset list)
        backtrack(state, target, nums, start, res);
        return res;
    }
    ```
=== "Java"
    ```java title="subset_sum_i.java"
    public class subset_sum_i {
        /* Backtracking algorithm: Subset sum I */
        static void backtrack(List<Integer> state, int target, int[] choices, int start, List<List<Integer>> res) {
            // When the subset sum equals target, record the solution
            if (target == 0) {
                res.add(new ArrayList<>(state));
                return;
            }
            // Traverse all choices
            // Pruning 2: start traversing from start to avoid generating duplicate subsets
            for (int i = start; i < choices.length; i++) {
                // Pruning 1: if the subset sum exceeds target, end the loop directly
                // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
                if (target - choices[i] < 0) {
                    break;
                }
                // Attempt: make choice, update target, start
                state.add(choices[i]);
                // Proceed to the next round of selection
                backtrack(state, target - choices[i], choices, i, res);
                // Backtrack: undo choice, restore to previous state
                state.remove(state.size() - 1);
            }
        }
    
        /* Solve subset sum I */
        static List<List<Integer>> subsetSumI(int[] nums, int target) {
            List<Integer> state = new ArrayList<>(); // State (subset)
            Arrays.sort(nums); // Sort nums
            int start = 0; // Start point for traversal
            List<List<Integer>> res = new ArrayList<>(); // Result list (subset list)
            backtrack(state, target, nums, start, res);
            return res;
        }
    
        public static void main(String[] args) {
            int[] nums = { 3, 4, 5 };
            int target = 9;
    
            List<List<Integer>> res = subsetSumI(nums, target);
    
            System.out.println("Input array nums = " + Arrays.toString(nums) + ", target = " + target);
            System.out.println("All subsets with sum equal to " + target + " are res = " + res);
        }
    }
    ```
=== "C#"
    ```csharp title="subset_sum_i.cs"
    public class subset_sum_i {
        /* Backtracking algorithm: Subset sum I */
        void Backtrack(List<int> state, int target, int[] choices, int start, List<List<int>> res) {
            // When the subset sum equals target, record the solution
            if (target == 0) {
                res.Add(new List<int>(state));
                return;
            }
            // Traverse all choices
            // Pruning 2: start traversing from start to avoid generating duplicate subsets
            for (int i = start; i < choices.Length; i++) {
                // Pruning 1: if the subset sum exceeds target, end the loop directly
                // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
                if (target - choices[i] < 0) {
                    break;
                }
                // Attempt: make choice, update target, start
                state.Add(choices[i]);
                // Proceed to the next round of selection
                Backtrack(state, target - choices[i], choices, i, res);
                // Backtrack: undo choice, restore to previous state
                state.RemoveAt(state.Count - 1);
            }
        }
    
        /* Solve subset sum I */
        List<List<int>> SubsetSumI(int[] nums, int target) {
            List<int> state = []; // State (subset)
            Array.Sort(nums); // Sort nums
            int start = 0; // Start point for traversal
            List<List<int>> res = []; // Result list (subset list)
            Backtrack(state, target, nums, start, res);
            return res;
        }
    
        [Test]
        public void Test() {
            int[] nums = [3, 4, 5];
            int target = 9;
            List<List<int>> res = SubsetSumI(nums, target);
            Console.WriteLine("Input array nums = " + string.Join(", ", nums) + ", target = " + target);
            Console.WriteLine("All subsets with sum equal to " + target + " are res = ");
            foreach (var subset in res) {
                PrintUtil.PrintList(subset);
            }
        }
    }
    ```
=== "Go"
    ```go title="subset_sum_i.go"
    func backtrackSubsetSumI(start, target int, state, choices *[]int, res *[][]int) {
    	// When the subset sum equals target, record the solution
    	if target == 0 {
    		newState := append([]int{}, *state...)
    		*res = append(*res, newState)
    		return
    	}
    	// Traverse all choices
    	// Pruning 2: start traversing from start to avoid generating duplicate subsets
    	for i := start; i < len(*choices); i++ {
    		// Pruning 1: if the subset sum exceeds target, end the loop directly
    		// This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
    		if target-(*choices)[i] < 0 {
    			break
    		}
    		// Attempt: make choice, update target, start
    		*state = append(*state, (*choices)[i])
    		// Proceed to the next round of selection
    		backtrackSubsetSumI(i, target-(*choices)[i], state, choices, res)
    		// Backtrack: undo choice, restore to previous state
    		*state = (*state)[:len(*state)-1]
    	}
    }
    ```
=== "Swift"
    ```swift title="subset_sum_i.swift"
    func subsetSumI(nums: [Int], target: Int) -> [[Int]] {
        var state: [Int] = [] // State (subset)
        let nums = nums.sorted() // Sort nums
        let start = 0 // Start point for traversal
        var res: [[Int]] = [] // Result list (subset list)
        backtrack(state: &state, target: target, choices: nums, start: start, res: &res)
        return res
    }
    ```
=== "JS"
    ```javascript title="subset_sum_i.js"
    function subsetSumI(nums, target) {
        const state = []; // State (subset)
        nums.sort((a, b) => a - b); // Sort nums
        const start = 0; // Start point for traversal
        const res = []; // Result list (subset list)
        backtrack(state, target, nums, start, res);
        return res;
    }
    ```
=== "TS"
    ```typescript title="subset_sum_i.ts"
    function subsetSumI(nums: number[], target: number): number[][] {
        const state = []; // State (subset)
        nums.sort((a, b) => a - b); // Sort nums
        const start = 0; // Start point for traversal
        const res = []; // Result list (subset list)
        backtrack(state, target, nums, start, res);
        return res;
    }
    ```
=== "Dart"
    ```dart title="subset_sum_i.dart"
    List<List<int>> subsetSumI(List<int> nums, int target) {
      List<int> state = []; // State (subset)
      nums.sort(); // Sort nums
      int start = 0; // Start point for traversal
      List<List<int>> res = []; // Result list (subset list)
      backtrack(state, target, nums, start, res);
      return res;
    }
    ```
=== "Rust"
    ```rust title="subset_sum_i.rs"
    fn subset_sum_i(nums: &mut [i32], target: i32) -> Vec<Vec<i32>> {
        let mut state = Vec::new(); // State (subset)
        nums.sort(); // Sort nums
        let start = 0; // Start point for traversal
        let mut res = Vec::new(); // Result list (subset list)
        backtrack(&mut state, target, nums, start, &mut res);
        res
    }
    ```
=== "C"
    ```c title="subset_sum_i.c"
    void subsetSumI(int *nums, int numsSize, int target) {
        qsort(nums, numsSize, sizeof(int), cmp); // Sort nums
        int start = 0;                           // Start point for traversal
        backtrack(target, nums, numsSize, start);
    }
    ```
=== "Kotlin"
    ```kotlin title="subset_sum_i.kt"
    fun subsetSumI(nums: IntArray, target: Int): MutableList<MutableList<Int>?> {
        val state = mutableListOf<Int>() // State (subset)
        nums.sort() // Sort nums
        val start = 0 // Start point for traversal
        val res = mutableListOf<MutableList<Int>?>() // Result list (subset list)
        backtrack(state, target, nums, start, res)
        return res
    }
    ```
=== "Ruby"
    ```ruby title="subset_sum_i.rb"
    ### Solve subset sum I ###
    def subset_sum_i(nums, target)
      state = [] # State (subset)
      nums.sort! # Sort nums
      start = 0 # Start point for traversal
      res = [] # Result list (subset list)
      backtrack(state, target, nums, start, res)
      res
    ```


Hình bên dưới cho thấy quá trình quay lui hoàn chỉnh được tạo ra bằng cách chạy đoạn mã trên trên mảng $[3, 4, 5]$ với giá trị đích $9$.

![Subset-sum I backtracking process](subset_sum_problem.assets/subset_sum_i.png)

## Với các phần tử trùng lặp trong mảng

!!! câu hỏi

Cho một mảng số nguyên dương `nums` và một số nguyên dương mục tiêu `target`, hãy tìm tất cả các kết hợp có thể có trong đó tổng các phần tử trong kết hợp bằng `target`. **Mảng đã cho có thể chứa các phần tử trùng lặp và mỗi phần tử chỉ có thể được chọn nhiều nhất một lần**. Trả về các kết hợp này ở dạng danh sách, trong đó danh sách không được chứa các kết hợp trùng lặp.

So với bài toán trước, **mảng đầu vào trong bài toán này có thể chứa các phần tử trùng lặp**, điều này gây ra một vấn đề mới. Ví dụ: cho mảng $[4, \hat{4}, 5]$ và giá trị đích $9$, đầu ra của mã hiện tại là $[4, 5], [\hat{4}, 5]$, chứa các tập hợp con trùng lặp.

**Lý do trùng lặp này là các phần tử bằng nhau được chọn nhiều lần trong một vòng nhất định**. Trong hình bên dưới, vòng đầu tiên có ba lựa chọn, hai trong số đó là $4$, tạo ra hai nhánh tìm kiếm trùng lặp tạo ra các tập hợp con trùng lặp. Tương tự, hai $4$ ở vòng thứ hai cũng tạo ra các tập con trùng lặp.

![Duplicate subsets caused by equal elements](subset_sum_problem.assets/subset_sum_ii_repeat.png)

### Cắt tỉa các phần tử bằng nhau

Để giải quyết vấn đề này, **chúng ta cần giới hạn các phần tử bằng nhau chỉ được chọn một lần trong mỗi vòng**. Việc triển khai khá thông minh: vì mảng đã được sắp xếp nên các phần tử bằng nhau nằm liền kề nhau. Điều này có nghĩa là trong một vòng lựa chọn nhất định, nếu phần tử hiện tại bằng phần tử ở bên trái của nó thì giá trị tương tự đã được chọn trong vòng này, vì vậy chúng ta trực tiếp bỏ qua phần tử hiện tại.

Đồng thời, **vấn đề này chỉ rõ mỗi phần tử mảng chỉ được chọn một lần**. May mắn thay, chúng ta cũng có thể sử dụng biến `start` để thỏa mãn ràng buộc này: sau khi đưa ra lựa chọn $x_{i}$, hãy đặt vòng tiếp theo để bắt đầu truyền tải từ chỉ mục $i + 1$ trở đi. Điều này vừa loại bỏ các tập hợp con trùng lặp vừa tránh việc chọn các phần tử nhiều lần.

### Triển khai mã

=== "Python"
    ```python title="subset_sum_ii.py"
    def subset_sum_ii(nums: list[int], target: int) -> list[list[int]]:
        """Solve subset sum II"""
        state = []  # State (subset)
        nums.sort()  # Sort nums
        start = 0  # Start point for traversal
        res = []  # Result list (subset list)
        backtrack(state, target, nums, start, res)
        return res
    ```
=== "C++"
    ```cpp title="subset_sum_ii.cpp"
    * File: subset_sum_ii.cpp
     * Created Time: 2023-06-21
     * Author: krahets (krahets@163.com)
     */
    
    #include "../utils/common.hpp"
    
    /* Backtracking algorithm: Subset sum II */
    void backtrack(vector<int> &state, int target, vector<int> &choices, int start, vector<vector<int>> &res) {
        // When the subset sum equals target, record the solution
        if (target == 0) {
            res.push_back(state);
            return;
        }
        // Traverse all choices
        // Pruning 2: start traversing from start to avoid generating duplicate subsets
        // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
        for (int i = start; i < choices.size(); i++) {
            // Pruning 1: if the subset sum exceeds target, end the loop directly
            // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
            if (target - choices[i] < 0) {
                break;
            }
            // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
            if (i > start && choices[i] == choices[i - 1]) {
                continue;
            }
            // Attempt: make choice, update target, start
            state.push_back(choices[i]);
            // Proceed to the next round of selection
            backtrack(state, target - choices[i], choices, i + 1, res);
            // Backtrack: undo choice, restore to previous state
            state.pop_back();
        }
    }
    ```
=== "Java"
    ```java title="subset_sum_ii.java"
    public class subset_sum_ii {
        /* Backtracking algorithm: Subset sum II */
        static void backtrack(List<Integer> state, int target, int[] choices, int start, List<List<Integer>> res) {
            // When the subset sum equals target, record the solution
            if (target == 0) {
                res.add(new ArrayList<>(state));
                return;
            }
            // Traverse all choices
            // Pruning 2: start traversing from start to avoid generating duplicate subsets
            // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
            for (int i = start; i < choices.length; i++) {
                // Pruning 1: if the subset sum exceeds target, end the loop directly
                // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
                if (target - choices[i] < 0) {
                    break;
                }
                // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
                if (i > start && choices[i] == choices[i - 1]) {
                    continue;
                }
                // Attempt: make choice, update target, start
                state.add(choices[i]);
                // Proceed to the next round of selection
                backtrack(state, target - choices[i], choices, i + 1, res);
                // Backtrack: undo choice, restore to previous state
                state.remove(state.size() - 1);
            }
        }
    
        /* Solve subset sum II */
        static List<List<Integer>> subsetSumII(int[] nums, int target) {
            List<Integer> state = new ArrayList<>(); // State (subset)
            Arrays.sort(nums); // Sort nums
            int start = 0; // Start point for traversal
            List<List<Integer>> res = new ArrayList<>(); // Result list (subset list)
            backtrack(state, target, nums, start, res);
            return res;
        }
    
        public static void main(String[] args) {
            int[] nums = { 4, 4, 5 };
            int target = 9;
    
            List<List<Integer>> res = subsetSumII(nums, target);
    
            System.out.println("Input array nums = " + Arrays.toString(nums) + ", target = " + target);
            System.out.println("All subsets with sum equal to " + target + " are res = " + res);
        }
    }
    ```
=== "C#"
    ```csharp title="subset_sum_ii.cs"
    public class subset_sum_ii {
        /* Backtracking algorithm: Subset sum II */
        void Backtrack(List<int> state, int target, int[] choices, int start, List<List<int>> res) {
            // When the subset sum equals target, record the solution
            if (target == 0) {
                res.Add(new List<int>(state));
                return;
            }
            // Traverse all choices
            // Pruning 2: start traversing from start to avoid generating duplicate subsets
            // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
            for (int i = start; i < choices.Length; i++) {
                // Pruning 1: if the subset sum exceeds target, end the loop directly
                // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
                if (target - choices[i] < 0) {
                    break;
                }
                // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
                if (i > start && choices[i] == choices[i - 1]) {
                    continue;
                }
                // Attempt: make choice, update target, start
                state.Add(choices[i]);
                // Proceed to the next round of selection
                Backtrack(state, target - choices[i], choices, i + 1, res);
                // Backtrack: undo choice, restore to previous state
                state.RemoveAt(state.Count - 1);
            }
        }
    
        /* Solve subset sum II */
        List<List<int>> SubsetSumII(int[] nums, int target) {
            List<int> state = []; // State (subset)
            Array.Sort(nums); // Sort nums
            int start = 0; // Start point for traversal
            List<List<int>> res = []; // Result list (subset list)
            Backtrack(state, target, nums, start, res);
            return res;
        }
    
        [Test]
        public void Test() {
            int[] nums = [4, 4, 5];
            int target = 9;
            List<List<int>> res = SubsetSumII(nums, target);
            Console.WriteLine("Input array nums = " + string.Join(", ", nums) + ", target = " + target);
            Console.WriteLine("All subsets with sum equal to " + target + " are res = ");
            foreach (var subset in res) {
                PrintUtil.PrintList(subset);
            }
        }
    }
    ```
=== "Go"
    ```go title="subset_sum_ii.go"
    // File: subset_sum_ii.go
    // Created Time: 2023-06-24
    // Author: Reanon (793584285@qq.com)
    
    package chapter_backtracking
    
    import "sort"
    
    /* Backtracking algorithm: Subset sum II */
    func backtrackSubsetSumII(start, target int, state, choices *[]int, res *[][]int) {
    	// When the subset sum equals target, record the solution
    	if target == 0 {
    		newState := append([]int{}, *state...)
    		*res = append(*res, newState)
    		return
    	}
    	// Traverse all choices
    	// Pruning 2: start traversing from start to avoid generating duplicate subsets
    	// Pruning 3: start traversing from start to avoid repeatedly selecting the same element
    	for i := start; i < len(*choices); i++ {
    		// Pruning 1: if the subset sum exceeds target, end the loop directly
    		// This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
    		if target-(*choices)[i] < 0 {
    			break
    		}
    		// Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
    		if i > start && (*choices)[i] == (*choices)[i-1] {
    			continue
    		}
    		// Attempt: make choice, update target, start
    		*state = append(*state, (*choices)[i])
    		// Proceed to the next round of selection
    		backtrackSubsetSumII(i+1, target-(*choices)[i], state, choices, res)
    		// Backtrack: undo choice, restore to previous state
    		*state = (*state)[:len(*state)-1]
    	}
    }
    ```
=== "Swift"
    ```swift title="subset_sum_ii.swift"
    * File: subset_sum_ii.swift
     * Created Time: 2023-07-02
     * Author: nuomi1 (nuomi1@qq.com)
     */
    
    /* Backtracking algorithm: Subset sum II */
    func backtrack(state: inout [Int], target: Int, choices: [Int], start: Int, res: inout [[Int]]) {
        // When the subset sum equals target, record the solution
        if target == 0 {
            res.append(state)
            return
        }
        // Traverse all choices
        // Pruning 2: start traversing from start to avoid generating duplicate subsets
        // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
        for i in choices.indices.dropFirst(start) {
            // Pruning 1: if the subset sum exceeds target, end the loop directly
            // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
            if target - choices[i] < 0 {
                break
            }
            // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
            if i > start, choices[i] == choices[i - 1] {
                continue
            }
            // Attempt: make choice, update target, start
            state.append(choices[i])
            // Proceed to the next round of selection
            backtrack(state: &state, target: target - choices[i], choices: choices, start: i + 1, res: &res)
            // Backtrack: undo choice, restore to previous state
            state.removeLast()
        }
    }
    ```
=== "JS"
    ```javascript title="subset_sum_ii.js"
    * File: subset_sum_ii.js
     * Created Time: 2023-07-30
     * Author: yuan0221 (yl1452491917@gmail.com)
     */
    
    /* Backtracking algorithm: Subset sum II */
    function backtrack(state, target, choices, start, res) {
        // When the subset sum equals target, record the solution
        if (target === 0) {
            res.push([...state]);
            return;
        }
        // Traverse all choices
        // Pruning 2: start traversing from start to avoid generating duplicate subsets
        // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
        for (let i = start; i < choices.length; i++) {
            // Pruning 1: if the subset sum exceeds target, end the loop directly
            // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
            if (target - choices[i] < 0) {
                break;
            }
            // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
            if (i > start && choices[i] === choices[i - 1]) {
                continue;
            }
            // Attempt: make choice, update target, start
            state.push(choices[i]);
            // Proceed to the next round of selection
            backtrack(state, target - choices[i], choices, i + 1, res);
            // Backtrack: undo choice, restore to previous state
            state.pop();
        }
    }
    ```
=== "TS"
    ```typescript title="subset_sum_ii.ts"
    * File: subset_sum_ii.ts
     * Created Time: 2023-07-30
     * Author: yuan0221 (yl1452491917@gmail.com)
     */
    
    /* Backtracking algorithm: Subset sum II */
    function backtrack(
        state: number[],
        target: number,
        choices: number[],
        start: number,
        res: number[][]
    ): void {
        // When the subset sum equals target, record the solution
        if (target === 0) {
            res.push([...state]);
            return;
        }
        // Traverse all choices
        // Pruning 2: start traversing from start to avoid generating duplicate subsets
        // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
        for (let i = start; i < choices.length; i++) {
            // Pruning 1: if the subset sum exceeds target, end the loop directly
            // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
            if (target - choices[i] < 0) {
                break;
            }
            // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
            if (i > start && choices[i] === choices[i - 1]) {
                continue;
            }
            // Attempt: make choice, update target, start
            state.push(choices[i]);
            // Proceed to the next round of selection
            backtrack(state, target - choices[i], choices, i + 1, res);
            // Backtrack: undo choice, restore to previous state
            state.pop();
        }
    }
    ```
=== "Dart"
    ```dart title="subset_sum_ii.dart"
    * File: subset_sum_ii.dart
     * Created Time: 2023-08-10
     * Author: liuyuxin (gvenusleo@gmail.com)
     */
    
    /* Backtracking algorithm: Subset sum II */
    void backtrack(
      List<int> state,
      int target,
      List<int> choices,
      int start,
      List<List<int>> res,
    ) {
      // When the subset sum equals target, record the solution
      if (target == 0) {
        res.add(List.from(state));
        return;
      }
      // Traverse all choices
      // Pruning 2: start traversing from start to avoid generating duplicate subsets
      // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
      for (int i = start; i < choices.length; i++) {
        // Pruning 1: if the subset sum exceeds target, end the loop directly
        // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
        if (target - choices[i] < 0) {
          break;
        }
        // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
        if (i > start && choices[i] == choices[i - 1]) {
          continue;
        }
        // Attempt: make choice, update target, start
        state.add(choices[i]);
        // Proceed to the next round of selection
        backtrack(state, target - choices[i], choices, i + 1, res);
        // Backtrack: undo choice, restore to previous state
        state.removeLast();
      }
    }
    ```
=== "Rust"
    ```rust title="subset_sum_ii.rs"
    fn subset_sum_ii(nums: &mut [i32], target: i32) -> Vec<Vec<i32>> {
        let mut state = Vec::new(); // State (subset)
        nums.sort(); // Sort nums
        let start = 0; // Start point for traversal
        let mut res = Vec::new(); // Result list (subset list)
        backtrack(&mut state, target, nums, start, &mut res);
        res
    }
    ```
=== "C"
    ```c title="subset_sum_ii.c"
    * File: subset_sum_ii.c
     * Created Time: 2023-07-29
     * Author: Gonglja (glj0@outlook.com)
     */
    
    #include "../utils/common.h"
    
    #define MAX_SIZE 100
    #define MAX_RES_SIZE 100
    
    // State (subset)
    int state[MAX_SIZE];
    int stateSize = 0;
    
    // Result list (subset list)
    int res[MAX_RES_SIZE][MAX_SIZE];
    int resColSizes[MAX_RES_SIZE];
    int resSize = 0;
    
    /* Backtracking algorithm: Subset sum II */
    void backtrack(int target, int *choices, int choicesSize, int start) {
        // When the subset sum equals target, record the solution
        if (target == 0) {
            for (int i = 0; i < stateSize; i++) {
                res[resSize][i] = state[i];
            }
            resColSizes[resSize++] = stateSize;
            return;
        }
        // Traverse all choices
        // Pruning 2: start traversing from start to avoid generating duplicate subsets
        // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
        for (int i = start; i < choicesSize; i++) {
            // Pruning 1: Skip if subset sum exceeds target
            if (target - choices[i] < 0) {
                continue;
            }
            // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
            if (i > start && choices[i] == choices[i - 1]) {
                continue;
            }
            // Attempt: make choice, update target, start
            state[stateSize] = choices[i];
            stateSize++;
            // Proceed to the next round of selection
            backtrack(target - choices[i], choices, choicesSize, i + 1);
            // Backtrack: undo choice, restore to previous state
            stateSize--;
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="subset_sum_ii.kt"
    * File: subset_sum_ii.kt
     * Created Time: 2024-01-25
     * Author: curtishd (1023632660@qq.com)
     */
    
    package chapter_backtracking.subset_sum_ii
    
    /* Backtracking algorithm: Subset sum II */
    fun backtrack(
        state: MutableList<Int>,
        target: Int,
        choices: IntArray,
        start: Int,
        res: MutableList<MutableList<Int>?>
    ) {
        // When the subset sum equals target, record the solution
        if (target == 0) {
            res.add(state.toMutableList())
            return
        }
        // Traverse all choices
        // Pruning 2: start traversing from start to avoid generating duplicate subsets
        // Pruning 3: start traversing from start to avoid repeatedly selecting the same element
        for (i in start..<choices.size) {
            // Pruning 1: if the subset sum exceeds target, end the loop directly
            // This is because the array is sorted, and later elements are larger, so the subset sum will definitely exceed target
            if (target - choices[i] < 0) {
                break
            }
            // Pruning 4: if this element equals the left element, it means this search branch is duplicate, skip it directly
            if (i > start && choices[i] == choices[i - 1]) {
                continue
            }
            // Attempt: make choice, update target, start
            state.add(choices[i])
            // Proceed to the next round of selection
            backtrack(state, target - choices[i], choices, i + 1, res)
            // Backtrack: undo choice, restore to previous state
            state.removeAt(state.size - 1)
        }
    }
    ```
=== "Ruby"
    ```ruby title="subset_sum_ii.rb"
    ### Solve subset sum II ###
    def subset_sum_ii(nums, target)
      state = [] # State (subset)
      nums.sort! # Sort nums
      start = 0 # Start point for traversal
      res = [] # Result list (subset list)
      backtrack(state, target, nums, start, res)
      res
    ```


Hình dưới đây cho thấy quá trình quay lui cho mảng $[4, 4, 5]$ với giá trị mục tiêu $9$, bao gồm bốn loại hoạt động cắt tỉa. Kết hợp hình minh họa với chú thích mã để hiểu toàn bộ quá trình tìm kiếm và cách hoạt động của từng thao tác cắt tỉa.

![Subset-sum II backtracking process](subset_sum_problem.assets/subset_sum_ii.png)
