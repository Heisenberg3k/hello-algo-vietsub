# Ranh giới tìm kiếm nhị phân

## Tìm ranh giới bên trái

!!! câu hỏi

Cho một mảng được sắp xếp `nums` có độ dài $n$ có thể chứa các phần tử trùng lặp, trả về chỉ mục của lần xuất hiện ngoài cùng bên trái của `target`. Nếu mảng không chứa `target`, trả về $-1$.

Nhớ lại phương pháp tìm điểm chèn bằng tìm kiếm nhị phân. Sau khi tìm kiếm hoàn tất, $i$ trỏ đến `đích` ngoài cùng bên trái, **vì vậy việc tìm điểm chèn về cơ bản là tìm chỉ mục của `đích`** ngoài cùng bên trái.

Xem xét việc thực hiện tìm kiếm ranh giới bên trái bằng chức năng tìm điểm chèn. Lưu ý rằng mảng có thể không chứa `target`, điều này có thể dẫn đến hai trường hợp sau:

- Chỉ số điểm chèn $i$ nằm ngoài giới hạn.
- Phần tử `nums[i]` không bằng `target`.

Khi một trong những tình huống này xảy ra, chỉ cần trả về $-1$. Mã được hiển thị dưới đây:

=== "Python"
    ```python title="binary_search_edge.py"
    def binary_search_left_edge(nums: list[int], target: int) -> int:
        """Binary search for the leftmost target"""
        # Equivalent to finding the insertion point of target
        i = binary_search_insertion(nums, target)
        # Target not found, return -1
        if i == len(nums) or nums[i] != target:
            return -1
        # Found target, return index i
        return i
    ```
=== "C++"
    ```cpp title="binary_search_edge.cpp"
    int binarySearchLeftEdge(vector<int> &nums, int target) {
        // Equivalent to finding the insertion point of target
        int i = binarySearchInsertion(nums, target);
        // Target not found, return -1
        if (i == nums.size() || nums[i] != target) {
            return -1;
        }
        // Found target, return index i
        return i;
    }
    ```
=== "Java"
    ```java title="binary_search_edge.java"
    static int binarySearchLeftEdge(int[] nums, int target) {
            // Equivalent to finding the insertion point of target
            int i = binary_search_insertion.binarySearchInsertion(nums, target);
            // Target not found, return -1
            if (i == nums.length || nums[i] != target) {
                return -1;
            }
            // Found target, return index i
            return i;
        }
    ```
=== "C#"
    ```csharp title="binary_search_edge.cs"
    int BinarySearchLeftEdge(int[] nums, int target) {
            // Equivalent to finding the insertion point of target
            int i = binary_search_insertion.BinarySearchInsertion(nums, target);
            // Target not found, return -1
            if (i == nums.Length || nums[i] != target) {
                return -1;
            }
            // Found target, return index i
            return i;
        }
    ```
=== "Go"
    ```go title="binary_search_edge.go"
    func binarySearchLeftEdge(nums []int, target int) int {
    	// Equivalent to finding the insertion point of target
    	i := binarySearchInsertion(nums, target)
    	// Target not found, return -1
    	if i == len(nums) || nums[i] != target {
    		return -1
    	}
    	// Found target, return index i
    	return i
    }
    ```
=== "Swift"
    ```swift title="binary_search_edge.swift"
    func binarySearchLeftEdge(nums: [Int], target: Int) -> Int {
        // Equivalent to finding the insertion point of target
        let i = binarySearchInsertion(nums: nums, target: target)
        // Target not found, return -1
        if i == nums.endIndex || nums[i] != target {
            return -1
        }
        // Found target, return index i
        return i
    }
    ```
=== "JS"
    ```javascript title="binary_search_edge.js"
    function binarySearchLeftEdge(nums, target) {
        // Equivalent to finding the insertion point of target
        const i = binarySearchInsertion(nums, target);
        // Target not found, return -1
        if (i === nums.length || nums[i] !== target) {
            return -1;
        }
        // Found target, return index i
        return i;
    }
    ```
=== "TS"
    ```typescript title="binary_search_edge.ts"
    function binarySearchLeftEdge(nums: Array<number>, target: number): number {
        // Equivalent to finding the insertion point of target
        const i = binarySearchInsertion(nums, target);
        // Target not found, return -1
        if (i === nums.length || nums[i] !== target) {
            return -1;
        }
        // Found target, return index i
        return i;
    }
    ```
=== "Dart"
    ```dart title="binary_search_edge.dart"
    int binarySearchLeftEdge(List<int> nums, int target) {
      // Equivalent to finding the insertion point of target
      int i = binarySearchInsertion(nums, target);
      // Target not found, return -1
      if (i == nums.length || nums[i] != target) {
        return -1;
      }
      // Found target, return index i
      return i;
    }
    ```
=== "Rust"
    ```rust title="binary_search_edge.rs"
    fn binary_search_left_edge(nums: &[i32], target: i32) -> i32 {
        // Equivalent to finding the insertion point of target
        let i = binary_search_insertion(nums, target);
        // Target not found, return -1
        if i == nums.len() as i32 || nums[i as usize] != target {
            return -1;
        }
        // Found target, return index i
        i
    }
    ```
=== "C"
    ```c title="binary_search_edge.c"
    int binarySearchLeftEdge(int *nums, int numSize, int target) {
        // Equivalent to finding the insertion point of target
        int i = binarySearchInsertion(nums, numSize, target);
        // Target not found, return -1
        if (i == numSize || nums[i] != target) {
            return -1;
        }
        // Found target, return index i
        return i;
    }
    ```
=== "Kotlin"
    ```kotlin title="binary_search_edge.kt"
    fun binarySearchLeftEdge(nums: IntArray, target: Int): Int {
        // Equivalent to finding the insertion point of target
        val i = binarySearchInsertion(nums, target)
        // Target not found, return -1
        if (i == nums.size || nums[i] != target) {
            return -1
        }
        // Found target, return index i
        return i
    }
    ```
=== "Ruby"
    ```ruby title="binary_search_edge.rb"
    ### Binary search leftmost target ###
    def binary_search_left_edge(nums, target)
      # Equivalent to finding the insertion point of target
      i = binary_search_insertion(nums, target)
    
      # Target not found, return -1
      return -1 if i == nums.length || nums[i] != target
    
      i # Found target, return index i
    ```


## Tìm ranh giới phù hợp

Vậy làm thế nào để chúng ta tìm được `mục tiêu` ngoài cùng bên phải? Cách tiếp cận trực tiếp nhất là sửa đổi mã và thay thế thao tác thu gọn con trỏ trong trường hợp `nums[m] == target`. Mã bị bỏ qua ở đây; bạn đọc quan tâm có thể tự mình thực hiện.

Dưới đây chúng tôi giới thiệu hai phương pháp thông minh hơn.

### Sử dụng lại tìm kiếm ranh giới bên trái

Trên thực tế, chúng ta có thể sử dụng hàm tìm `đích` ngoài cùng bên trái để tìm `mục tiêu` ngoài cùng bên phải. Phương pháp cụ thể là: **chuyển đổi việc tìm `target` ngoài cùng bên phải thành tìm `target + 1`** ngoài cùng bên trái.

Như được hiển thị trong hình bên dưới, sau khi tìm kiếm hoàn tất, con trỏ $i$ trỏ đến `target + 1` ngoài cùng bên trái (nếu nó tồn tại), trong khi $j$ trỏ đến `target` ngoài cùng bên phải, **vì vậy chúng ta có thể trả về $j$**.

![Converting right boundary search to left boundary search](binary_search_edge.assets/binary_search_right_edge_by_left_edge.png)

Lưu ý rằng điểm chèn được trả về là $i$, vì vậy chúng ta cần trừ $1$ từ nó để thu được $j$:

=== "Python"
    ```python title="binary_search_edge.py"
    def binary_search_right_edge(nums: list[int], target: int) -> int:
        """Binary search for the rightmost target"""
        # Convert to finding the leftmost target + 1
        i = binary_search_insertion(nums, target + 1)
        # j points to the rightmost target, i points to the first element greater than target
        j = i - 1
        # Target not found, return -1
        if j == -1 or nums[j] != target:
            return -1
        # Found target, return index j
        return j
    ```
=== "C++"
    ```cpp title="binary_search_edge.cpp"
    int binarySearchRightEdge(vector<int> &nums, int target) {
        // Convert to finding the leftmost target + 1
        int i = binarySearchInsertion(nums, target + 1);
        // j points to the rightmost target, i points to the first element greater than target
        int j = i - 1;
        // Target not found, return -1
        if (j == -1 || nums[j] != target) {
            return -1;
        }
        // Found target, return index j
        return j;
    }
    ```
=== "Java"
    ```java title="binary_search_edge.java"
    static int binarySearchRightEdge(int[] nums, int target) {
            // Convert to finding the leftmost target + 1
            int i = binary_search_insertion.binarySearchInsertion(nums, target + 1);
            // j points to the rightmost target, i points to the first element greater than target
            int j = i - 1;
            // Target not found, return -1
            if (j == -1 || nums[j] != target) {
                return -1;
            }
            // Found target, return index j
            return j;
        }
    ```
=== "C#"
    ```csharp title="binary_search_edge.cs"
    int BinarySearchRightEdge(int[] nums, int target) {
            // Convert to finding the leftmost target + 1
            int i = binary_search_insertion.BinarySearchInsertion(nums, target + 1);
            // j points to the rightmost target, i points to the first element greater than target
            int j = i - 1;
            // Target not found, return -1
            if (j == -1 || nums[j] != target) {
                return -1;
            }
            // Found target, return index j
            return j;
        }
    ```
=== "Go"
    ```go title="binary_search_edge.go"
    func binarySearchRightEdge(nums []int, target int) int {
    	// Convert to finding the leftmost target + 1
    	i := binarySearchInsertion(nums, target+1)
    	// j points to the rightmost target, i points to the first element greater than target
    	j := i - 1
    	// Target not found, return -1
    	if j == -1 || nums[j] != target {
    		return -1
    	}
    	// Found target, return index j
    	return j
    }
    ```
=== "Swift"
    ```swift title="binary_search_edge.swift"
    func binarySearchRightEdge(nums: [Int], target: Int) -> Int {
        // Convert to finding the leftmost target + 1
        let i = binarySearchInsertion(nums: nums, target: target + 1)
        // j points to the rightmost target, i points to the first element greater than target
        let j = i - 1
        // Target not found, return -1
        if j == -1 || nums[j] != target {
            return -1
        }
        // Found target, return index j
        return j
    }
    ```
=== "JS"
    ```javascript title="binary_search_edge.js"
    function binarySearchRightEdge(nums, target) {
        // Convert to finding the leftmost target + 1
        const i = binarySearchInsertion(nums, target + 1);
        // j points to the rightmost target, i points to the first element greater than target
        const j = i - 1;
        // Target not found, return -1
        if (j === -1 || nums[j] !== target) {
            return -1;
        }
        // Found target, return index j
        return j;
    }
    ```
=== "TS"
    ```typescript title="binary_search_edge.ts"
    function binarySearchRightEdge(nums: Array<number>, target: number): number {
        // Convert to finding the leftmost target + 1
        const i = binarySearchInsertion(nums, target + 1);
        // j points to the rightmost target, i points to the first element greater than target
        const j = i - 1;
        // Target not found, return -1
        if (j === -1 || nums[j] !== target) {
            return -1;
        }
        // Found target, return index j
        return j;
    }
    ```
=== "Dart"
    ```dart title="binary_search_edge.dart"
    int binarySearchRightEdge(List<int> nums, int target) {
      // Convert to finding the leftmost target + 1
      int i = binarySearchInsertion(nums, target + 1);
      // j points to the rightmost target, i points to the first element greater than target
      int j = i - 1;
      // Target not found, return -1
      if (j == -1 || nums[j] != target) {
        return -1;
      }
      // Found target, return index j
      return j;
    }
    ```
=== "Rust"
    ```rust title="binary_search_edge.rs"
    fn binary_search_right_edge(nums: &[i32], target: i32) -> i32 {
        // Convert to finding the leftmost target + 1
        let i = binary_search_insertion(nums, target + 1);
        // j points to the rightmost target, i points to the first element greater than target
        let j = i - 1;
        // Target not found, return -1
        if j == -1 || nums[j as usize] != target {
            return -1;
        }
        // Found target, return index j
        j
    }
    ```
=== "C"
    ```c title="binary_search_edge.c"
    int binarySearchRightEdge(int *nums, int numSize, int target) {
        // Convert to finding the leftmost target + 1
        int i = binarySearchInsertion(nums, numSize, target + 1);
        // j points to the rightmost target, i points to the first element greater than target
        int j = i - 1;
        // Target not found, return -1
        if (j == -1 || nums[j] != target) {
            return -1;
        }
        // Found target, return index j
        return j;
    }
    ```
=== "Kotlin"
    ```kotlin title="binary_search_edge.kt"
    fun binarySearchRightEdge(nums: IntArray, target: Int): Int {
        // Convert to finding the leftmost target + 1
        val i = binarySearchInsertion(nums, target + 1)
        // j points to the rightmost target, i points to the first element greater than target
        val j = i - 1
        // Target not found, return -1
        if (j == -1 || nums[j] != target) {
            return -1
        }
        // Found target, return index j
        return j
    }
    ```
=== "Ruby"
    ```ruby title="binary_search_edge.rb"
    ### Binary search rightmost target ###
    def binary_search_right_edge(nums, target)
      # Convert to finding the leftmost target + 1
      i = binary_search_insertion(nums, target + 1)
    
      # j points to the rightmost target, i points to the first element greater than target
      j = i - 1
    
      # Target not found, return -1
      return -1 if j == -1 || nums[j] != target
    
      j # Found target, return index j
    ```


### Chuyển đổi sang Tìm kiếm phần tử

Chúng ta biết rằng khi mảng không chứa `target`, $i$ và $j$ cuối cùng sẽ lần lượt trỏ đến các phần tử đầu tiên lớn hơn và nhỏ hơn `target`.

Do đó, như trong hình bên dưới, chúng ta có thể xây dựng một phần tử không tồn tại trong mảng để tìm ranh giới bên trái và bên phải.

- Tìm `target` ngoài cùng bên trái: Có thể chuyển đổi thành tìm `target - 0.5` và trả về con trỏ $i$.
- Tìm `target` ngoài cùng bên phải: Có thể chuyển đổi thành tìm `target + 0.5` và trả về con trỏ $j$.

![Converting boundary search to element search](binary_search_edge.assets/binary_search_edge_by_element.png)

Mã bị bỏ qua ở đây, nhưng có hai điểm sau đáng chú ý:

- Vì mảng đã cho không chứa giá trị thập phân nên chúng ta không cần lo lắng về cách xử lý đẳng thức.
- Vì phương thức này đưa vào số thập phân nên biến `target` trong hàm cần được đổi thành kiểu dấu phẩy động (Python không yêu cầu thay đổi này).
