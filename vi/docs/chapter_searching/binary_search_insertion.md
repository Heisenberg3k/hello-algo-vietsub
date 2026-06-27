# Điểm chèn tìm kiếm nhị phân

Tìm kiếm nhị phân có thể được sử dụng không chỉ để tìm kiếm phần tử đích mà còn để giải quyết nhiều vấn đề khác nhau, chẳng hạn như tìm vị trí chèn của phần tử đích.

## Trường hợp không có phần tử trùng lặp

!!! câu hỏi

Cho một mảng được sắp xếp `nums` có độ dài $n$ và một phần tử `target`, trong đó mảng không chứa các phần tử trùng lặp, hãy chèn `target` vào `nums` trong khi vẫn giữ nguyên thứ tự được sắp xếp của nó. Nếu `target` đã tồn tại trong mảng, hãy chèn nó vào bên trái. Trả về chỉ mục của `target` sau khi chèn. Một ví dụ được hiển thị dưới đây.

![Binary search insertion point example data](binary_search_insertion.assets/binary_search_insertion_example.png)

Nếu muốn sử dụng lại mã tìm kiếm nhị phân ở phần trước, chúng ta cần trả lời hai câu hỏi sau.

**Câu hỏi 1**: Khi mảng chứa `target`, chỉ mục điểm chèn có giống với chỉ mục của phần tử đó không?

Sự cố yêu cầu chèn `target` vào bên trái của các phần tử bằng nhau, có nghĩa là `target` mới được chèn sẽ thay thế vị trí của `target` ban đầu. Nói cách khác, **khi mảng chứa `target`, chỉ mục điểm chèn là chỉ mục của `target`** đó.

**Câu hỏi 2**: Khi mảng không chứa `target` thì chỉ số điểm chèn là gì?

Để phân tích điều này sâu hơn, hãy xem xét quá trình tìm kiếm nhị phân: khi `nums[m] < target`, $i$ di chuyển, nghĩa là con trỏ $i$ đang tiếp cận các phần tử lớn hơn hoặc bằng `target`. Tương tự, con trỏ $j$ luôn tiếp cận các phần tử nhỏ hơn hoặc bằng `target`.

Do đó, khi tìm kiếm nhị phân kết thúc, $i$ phải trỏ đến phần tử đầu tiên lớn hơn `target`, và $j$ phải trỏ đến phần tử đầu tiên nhỏ hơn `target`. **Theo sau đó, khi mảng không chứa `target`, chỉ mục chèn là $i$**. Mã được hiển thị dưới đây:

=== "Python"
    ```python title="binary_search_insertion.py"
    def binary_search_insertion_simple(nums: list[int], target: int) -> int:
        """Binary search for insertion point (no duplicate elements)"""
        i, j = 0, len(nums) - 1  # Initialize closed interval [0, n-1]
        while i <= j:
            m = (i + j) // 2  # Calculate midpoint index m
            if nums[m] < target:
                i = m + 1  # target is in the interval [m+1, j]
            elif nums[m] > target:
                j = m - 1  # target is in the interval [i, m-1]
            else:
                return m  # Found target, return insertion point m
        # Target not found, return insertion point i
        return i
    ```
=== "C++"
    ```cpp title="binary_search_insertion.cpp"
    int binarySearchInsertionSimple(vector<int> &nums, int target) {
        int i = 0, j = nums.size() - 1; // Initialize closed interval [0, n-1]
        while (i <= j) {
            int m = i + (j - i) / 2; // Calculate the midpoint index m
            if (nums[m] < target) {
                i = m + 1; // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                return m; // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i;
    }
    ```
=== "Java"
    ```java title="binary_search_insertion.java"
    static int binarySearchInsertionSimple(int[] nums, int target) {
            int i = 0, j = nums.length - 1; // Initialize closed interval [0, n-1]
            while (i <= j) {
                int m = i + (j - i) / 2; // Calculate the midpoint index m
                if (nums[m] < target) {
                    i = m + 1; // target is in the interval [m+1, j]
                } else if (nums[m] > target) {
                    j = m - 1; // target is in the interval [i, m-1]
                } else {
                    return m; // Found target, return insertion point m
                }
            }
            // Target not found, return insertion point i
            return i;
        }
    ```
=== "C#"
    ```csharp title="binary_search_insertion.cs"
    public static int BinarySearchInsertionSimple(int[] nums, int target) {
            int i = 0, j = nums.Length - 1; // Initialize closed interval [0, n-1]
            while (i <= j) {
                int m = i + (j - i) / 2; // Calculate the midpoint index m
                if (nums[m] < target) {
                    i = m + 1; // target is in the interval [m+1, j]
                } else if (nums[m] > target) {
                    j = m - 1; // target is in the interval [i, m-1]
                } else {
                    return m; // Found target, return insertion point m
                }
            }
            // Target not found, return insertion point i
            return i;
        }
    ```
=== "Go"
    ```go title="binary_search_insertion.go"
    func binarySearchInsertionSimple(nums []int, target int) int {
    	// Initialize closed interval [0, n-1]
    	i, j := 0, len(nums)-1
    	for i <= j {
    		// Calculate the midpoint index m
    		m := i + (j-i)/2
    		if nums[m] < target {
    			// target is in the interval [m+1, j]
    			i = m + 1
    		} else if nums[m] > target {
    			// target is in the interval [i, m-1]
    			j = m - 1
    		} else {
    			// Found target, return insertion point m
    			return m
    		}
    	}
    	// Target not found, return insertion point i
    	return i
    }
    ```
=== "Swift"
    ```swift title="binary_search_insertion.swift"
    func binarySearchInsertionSimple(nums: [Int], target: Int) -> Int {
        // Initialize closed interval [0, n-1]
        var i = nums.startIndex
        var j = nums.endIndex - 1
        while i <= j {
            let m = i + (j - i) / 2 // Calculate the midpoint index m
            if nums[m] < target {
                i = m + 1 // target is in the interval [m+1, j]
            } else if nums[m] > target {
                j = m - 1 // target is in the interval [i, m-1]
            } else {
                return m // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i
    }
    ```
=== "JS"
    ```javascript title="binary_search_insertion.js"
    function binarySearchInsertionSimple(nums, target) {
        let i = 0,
            j = nums.length - 1; // Initialize closed interval [0, n-1]
        while (i <= j) {
            const m = Math.floor(i + (j - i) / 2); // Calculate midpoint index m, use Math.floor() to round down
            if (nums[m] < target) {
                i = m + 1; // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                return m; // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i;
    }
    ```
=== "TS"
    ```typescript title="binary_search_insertion.ts"
    function binarySearchInsertionSimple(
        nums: Array<number>,
        target: number
    ): number {
        let i = 0,
            j = nums.length - 1; // Initialize closed interval [0, n-1]
        while (i <= j) {
            const m = Math.floor(i + (j - i) / 2); // Calculate midpoint index m, use Math.floor() to round down
            if (nums[m] < target) {
                i = m + 1; // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                return m; // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i;
    }
    ```
=== "Dart"
    ```dart title="binary_search_insertion.dart"
    int binarySearchInsertionSimple(List<int> nums, int target) {
      int i = 0, j = nums.length - 1; // Initialize closed interval [0, n-1]
      while (i <= j) {
        int m = i + (j - i) ~/ 2; // Calculate the midpoint index m
        if (nums[m] < target) {
          i = m + 1; // target is in the interval [m+1, j]
        } else if (nums[m] > target) {
          j = m - 1; // target is in the interval [i, m-1]
        } else {
          return m; // Found target, return insertion point m
        }
      }
      // Target not found, return insertion point i
      return i;
    }
    ```
=== "Rust"
    ```rust title="binary_search_insertion.rs"
    fn binary_search_insertion_simple(nums: &[i32], target: i32) -> i32 {
        let (mut i, mut j) = (0, nums.len() as i32 - 1); // Initialize closed interval [0, n-1]
        while i <= j {
            let m = i + (j - i) / 2; // Calculate the midpoint index m
            if nums[m as usize] < target {
                i = m + 1; // target is in the interval [m+1, j]
            } else if nums[m as usize] > target {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                return m;
            }
        }
        // Target not found, return insertion point i
        i
    }
    ```
=== "C"
    ```c title="binary_search_insertion.c"
    int binarySearchInsertionSimple(int *nums, int numSize, int target) {
        int i = 0, j = numSize - 1; // Initialize closed interval [0, n-1]
        while (i <= j) {
            int m = i + (j - i) / 2; // Calculate the midpoint index m
            if (nums[m] < target) {
                i = m + 1; // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                return m; // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i;
    }
    ```
=== "Kotlin"
    ```kotlin title="binary_search_insertion.kt"
    fun binarySearchInsertionSimple(nums: IntArray, target: Int): Int {
        var i = 0
        var j = nums.size - 1 // Initialize closed interval [0, n-1]
        while (i <= j) {
            val m = i + (j - i) / 2 // Calculate the midpoint index m
            if (nums[m] < target) {
                i = m + 1 // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1 // target is in the interval [i, m-1]
            } else {
                return m // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i
    }
    ```
=== "Ruby"
    ```ruby title="binary_search_insertion.rb"
    ### Binary search insertion point (no duplicates) ###
    def binary_search_insertion_simple(nums, target)
      # Initialize closed interval [0, n-1]
      i, j = 0, nums.length - 1
    
      while i <= j
        # Calculate the midpoint index m
        m = (i + j) / 2
    
        if nums[m] < target
          i = m + 1 # target is in the interval [m+1, j]
        elsif nums[m] > target
          j = m - 1 # target is in the interval [i, m-1]
        else
          return m  # Found target, return insertion point m
        end
      end
    
      i # Target not found, return insertion point i
    ```


## Trường hợp có phần tử trùng lặp

!!! câu hỏi

Dựa trên vấn đề trước đó, giả sử mảng có thể chứa các phần tử trùng lặp, còn mọi thứ khác vẫn giữ nguyên.

Giả sử có nhiều phần tử `target` trong mảng. Tìm kiếm nhị phân thông thường chỉ có thể trả về chỉ mục của một `đích`, **và không thể xác định có bao nhiêu phần tử `đích` ở bên trái và bên phải của phần tử đó**.

Bài toán yêu cầu chèn phần tử đích vào vị trí ngoài cùng bên trái **vì vậy chúng ta cần tìm chỉ mục của `target` ngoài cùng bên trái trong mảng**. Cách tiếp cận ban đầu đơn giản là làm theo các bước được hiển thị trong hình bên dưới:

1. Thực hiện tìm kiếm nhị phân để lấy chỉ mục của bất kỳ `đích` nào, ký hiệu là $k$.
2. Bắt đầu từ chỉ mục $k$, thực hiện duyệt tuyến tính sang trái và quay lại khi tìm thấy `đích` ngoài cùng bên trái.

![Linear search for insertion point of duplicate elements](binary_search_insertion.assets/binary_search_insertion_naive.png)

Mặc dù phương pháp này hoạt động nhưng nó bao gồm tìm kiếm tuyến tính, dẫn đến độ phức tạp về thời gian là $O(n)$. Khi mảng chứa nhiều phần tử `target` trùng lặp, phương pháp này rất kém hiệu quả.

Bây giờ hãy xem xét việc mở rộng mã tìm kiếm nhị phân. Như được hiển thị trong hình bên dưới, quy trình tổng thể vẫn không thay đổi: trong mỗi lần lặp, trước tiên chúng tôi tính chỉ số trung điểm $m$, sau đó so sánh `target` với `nums[m]`, dẫn đến các trường hợp sau:

- Khi `nums[m] < target` hoặc `nums[m] > target`, điều đó có nghĩa là `target` chưa được tìm thấy, vì vậy hãy sử dụng thao tác thu nhỏ khoảng tiêu chuẩn của tìm kiếm nhị phân để **di chuyển con trỏ $i$ và $j$ đến gần `target`**.
- Khi `nums[m] == target`, có nghĩa là các phần tử nhỏ hơn `target` nằm trong khoảng $[i, m - 1]$, vì vậy hãy sử dụng $j = m - 1$ để thu hẹp khoảng, từ đó **di chuyển con trỏ $j$ đến gần các phần tử nhỏ hơn `target`**.

Sau khi vòng lặp hoàn thành, $i$ trỏ đến `target` ngoài cùng bên trái và $j$ trỏ đến phần tử đầu tiên nhỏ hơn `target`, **vì vậy chỉ mục $i$ là điểm chèn**.

=== "<1>"
    ![Steps for binary search insertion point of duplicate elements](binary_search_insertion.assets/binary_search_insertion_step1.png)

=== "<2>"
    ![binary_search_insertion_step2](binary_search_insertion.assets/binary_search_insertion_step2.png)

=== "<3>"
    ![binary_search_insertion_step3](binary_search_insertion.assets/binary_search_insertion_step3.png)

=== "<4>"
    ![binary_search_insertion_step4](binary_search_insertion.assets/binary_search_insertion_step4.png)

=== "<5>"
    ![binary_search_insertion_step5](binary_search_insertion.assets/binary_search_insertion_step5.png)

=== "<6>"
    ![binary_search_insertion_step6](binary_search_insertion.assets/binary_search_insertion_step6.png)

=== "<7>"
    ![binary_search_insertion_step7](binary_search_insertion.assets/binary_search_insertion_step7.png)

=== "<8>"
    ![binary_search_insertion_step8](binary_search_insertion.assets/binary_search_insertion_step8.png)

Hãy quan sát đoạn mã sau: các nhánh `nums[m] > target` và `nums[m] == target` thực hiện cùng một thao tác, để chúng có thể được hợp nhất.

Mặc dù vậy, chúng ta vẫn có thể mở rộng các nhánh có điều kiện vì logic rõ ràng và dễ đọc hơn.

=== "Python"
    ```python title="binary_search_insertion.py"
    def binary_search_insertion_simple(nums: list[int], target: int) -> int:
        """Binary search for insertion point (no duplicate elements)"""
        i, j = 0, len(nums) - 1  # Initialize closed interval [0, n-1]
        while i <= j:
            m = (i + j) // 2  # Calculate midpoint index m
            if nums[m] < target:
                i = m + 1  # target is in the interval [m+1, j]
            elif nums[m] > target:
                j = m - 1  # target is in the interval [i, m-1]
            else:
                return m  # Found target, return insertion point m
        # Target not found, return insertion point i
        return i
    ```
=== "C++"
    ```cpp title="binary_search_insertion.cpp"
    int binarySearchInsertionSimple(vector<int> &nums, int target) {
        int i = 0, j = nums.size() - 1; // Initialize closed interval [0, n-1]
        while (i <= j) {
            int m = i + (j - i) / 2; // Calculate the midpoint index m
            if (nums[m] < target) {
                i = m + 1; // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                return m; // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i;
    }
    ```
=== "Java"
    ```java title="binary_search_insertion.java"
    class binary_search_insertion {
        /* Binary search for insertion point (no duplicate elements) */
        static int binarySearchInsertionSimple(int[] nums, int target) {
            int i = 0, j = nums.length - 1; // Initialize closed interval [0, n-1]
            while (i <= j) {
                int m = i + (j - i) / 2; // Calculate the midpoint index m
                if (nums[m] < target) {
                    i = m + 1; // target is in the interval [m+1, j]
                } else if (nums[m] > target) {
                    j = m - 1; // target is in the interval [i, m-1]
                } else {
                    return m; // Found target, return insertion point m
                }
            }
            // Target not found, return insertion point i
            return i;
        }
    
        /* Binary search for insertion point (with duplicate elements) */
        static int binarySearchInsertion(int[] nums, int target) {
            int i = 0, j = nums.length - 1; // Initialize closed interval [0, n-1]
            while (i <= j) {
                int m = i + (j - i) / 2; // Calculate the midpoint index m
                if (nums[m] < target) {
                    i = m + 1; // target is in the interval [m+1, j]
                } else if (nums[m] > target) {
                    j = m - 1; // target is in the interval [i, m-1]
                } else {
                    j = m - 1; // The first element less than target is in the interval [i, m-1]
                }
            }
            // Return insertion point i
            return i;
        }
    
        public static void main(String[] args) {
            // Array without duplicate elements
            int[] nums = { 1, 3, 6, 8, 12, 15, 23, 26, 31, 35 };
            System.out.println("\nArray nums = " + java.util.Arrays.toString(nums));
            // Binary search for insertion point
            for (int target : new int[] { 6, 9 }) {
                int index = binarySearchInsertionSimple(nums, target);
                System.out.println("Insertion point index for element " + target + " is " + index);
            }
    
            // Array with duplicate elements
            nums = new int[] { 1, 3, 6, 6, 6, 6, 6, 10, 12, 15 };
            System.out.println("\nArray nums = " + java.util.Arrays.toString(nums));
            // Binary search for insertion point
            for (int target : new int[] { 2, 6, 20 }) {
                int index = binarySearchInsertion(nums, target);
                System.out.println("Insertion point index for element " + target + " is " + index);
            }
        }
    }
    ```
=== "C#"
    ```csharp title="binary_search_insertion.cs"
    public class binary_search_insertion {
        /* Binary search for insertion point (no duplicate elements) */
        public static int BinarySearchInsertionSimple(int[] nums, int target) {
            int i = 0, j = nums.Length - 1; // Initialize closed interval [0, n-1]
            while (i <= j) {
                int m = i + (j - i) / 2; // Calculate the midpoint index m
                if (nums[m] < target) {
                    i = m + 1; // target is in the interval [m+1, j]
                } else if (nums[m] > target) {
                    j = m - 1; // target is in the interval [i, m-1]
                } else {
                    return m; // Found target, return insertion point m
                }
            }
            // Target not found, return insertion point i
            return i;
        }
    
        /* Binary search for insertion point (with duplicate elements) */
        public static int BinarySearchInsertion(int[] nums, int target) {
            int i = 0, j = nums.Length - 1; // Initialize closed interval [0, n-1]
            while (i <= j) {
                int m = i + (j - i) / 2; // Calculate the midpoint index m
                if (nums[m] < target) {
                    i = m + 1; // target is in the interval [m+1, j]
                } else if (nums[m] > target) {
                    j = m - 1; // target is in the interval [i, m-1]
                } else {
                    j = m - 1; // The first element less than target is in the interval [i, m-1]
                }
            }
            // Return insertion point i
            return i;
        }
    
        [Test]
        public void Test() {
            // Array without duplicate elements
            int[] nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35];
            Console.WriteLine("\nArray nums = " + nums.PrintList());
            // Binary search for insertion point
            foreach (int target in new int[] { 6, 9 }) {
                int index = BinarySearchInsertionSimple(nums, target);
                Console.WriteLine("Element " + target + "'s insertion point index is " + index);
            }
    
            // Array with duplicate elements
            nums = [1, 3, 6, 6, 6, 6, 6, 10, 12, 15];
            Console.WriteLine("\nArray nums = " + nums.PrintList());
            // Binary search for insertion point
            foreach (int target in new int[] { 2, 6, 20 }) {
                int index = BinarySearchInsertion(nums, target);
                Console.WriteLine("Element " + target + "'s insertion point index is " + index);
            }
        }
    }
    ```
=== "Go"
    ```go title="binary_search_insertion.go"
    func binarySearchInsertionSimple(nums []int, target int) int {
    	// Initialize closed interval [0, n-1]
    	i, j := 0, len(nums)-1
    	for i <= j {
    		// Calculate the midpoint index m
    		m := i + (j-i)/2
    		if nums[m] < target {
    			// target is in the interval [m+1, j]
    			i = m + 1
    		} else if nums[m] > target {
    			// target is in the interval [i, m-1]
    			j = m - 1
    		} else {
    			// Found target, return insertion point m
    			return m
    		}
    	}
    	// Target not found, return insertion point i
    	return i
    }
    ```
=== "Swift"
    ```swift title="binary_search_insertion.swift"
    func binarySearchInsertionSimple(nums: [Int], target: Int) -> Int {
        // Initialize closed interval [0, n-1]
        var i = nums.startIndex
        var j = nums.endIndex - 1
        while i <= j {
            let m = i + (j - i) / 2 // Calculate the midpoint index m
            if nums[m] < target {
                i = m + 1 // target is in the interval [m+1, j]
            } else if nums[m] > target {
                j = m - 1 // target is in the interval [i, m-1]
            } else {
                return m // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i
    }
    ```
=== "JS"
    ```javascript title="binary_search_insertion.js"
    function binarySearchInsertion(nums, target) {
        let i = 0,
            j = nums.length - 1; // Initialize closed interval [0, n-1]
        while (i <= j) {
            const m = Math.floor(i + (j - i) / 2); // Calculate midpoint index m, use Math.floor() to round down
            if (nums[m] < target) {
                i = m + 1; // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                j = m - 1; // The first element less than target is in the interval [i, m-1]
            }
        }
        // Return insertion point i
        return i;
    }
    ```
=== "TS"
    ```typescript title="binary_search_insertion.ts"
    function binarySearchInsertion(nums: Array<number>, target: number): number {
        let i = 0,
            j = nums.length - 1; // Initialize closed interval [0, n-1]
        while (i <= j) {
            const m = Math.floor(i + (j - i) / 2); // Calculate midpoint index m, use Math.floor() to round down
            if (nums[m] < target) {
                i = m + 1; // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                j = m - 1; // The first element less than target is in the interval [i, m-1]
            }
        }
        // Return insertion point i
        return i;
    }
    ```
=== "Dart"
    ```dart title="binary_search_insertion.dart"
    int binarySearchInsertionSimple(List<int> nums, int target) {
      int i = 0, j = nums.length - 1; // Initialize closed interval [0, n-1]
      while (i <= j) {
        int m = i + (j - i) ~/ 2; // Calculate the midpoint index m
        if (nums[m] < target) {
          i = m + 1; // target is in the interval [m+1, j]
        } else if (nums[m] > target) {
          j = m - 1; // target is in the interval [i, m-1]
        } else {
          return m; // Found target, return insertion point m
        }
      }
      // Target not found, return insertion point i
      return i;
    }
    ```
=== "Rust"
    ```rust title="binary_search_insertion.rs"
    fn binary_search_insertion_simple(nums: &[i32], target: i32) -> i32 {
        let (mut i, mut j) = (0, nums.len() as i32 - 1); // Initialize closed interval [0, n-1]
        while i <= j {
            let m = i + (j - i) / 2; // Calculate the midpoint index m
            if nums[m as usize] < target {
                i = m + 1; // target is in the interval [m+1, j]
            } else if nums[m as usize] > target {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                return m;
            }
        }
        // Target not found, return insertion point i
        i
    }
    ```
=== "C"
    ```c title="binary_search_insertion.c"
    int binarySearchInsertionSimple(int *nums, int numSize, int target) {
        int i = 0, j = numSize - 1; // Initialize closed interval [0, n-1]
        while (i <= j) {
            int m = i + (j - i) / 2; // Calculate the midpoint index m
            if (nums[m] < target) {
                i = m + 1; // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1; // target is in the interval [i, m-1]
            } else {
                return m; // Found target, return insertion point m
            }
        }
        // Target not found, return insertion point i
        return i;
    }
    ```
=== "Kotlin"
    ```kotlin title="binary_search_insertion.kt"
    fun binarySearchInsertion(nums: IntArray, target: Int): Int {
        var i = 0
        var j = nums.size - 1 // Initialize closed interval [0, n-1]
        while (i <= j) {
            val m = i + (j - i) / 2 // Calculate the midpoint index m
            if (nums[m] < target) {
                i = m + 1 // target is in the interval [m+1, j]
            } else if (nums[m] > target) {
                j = m - 1 // target is in the interval [i, m-1]
            } else {
                j = m - 1 // The first element less than target is in the interval [i, m-1]
            }
        }
        // Return insertion point i
        return i
    }
    ```
=== "Ruby"
    ```ruby title="binary_search_insertion.rb"
    ### Binary search insertion point (no duplicates) ###
    def binary_search_insertion_simple(nums, target)
      # Initialize closed interval [0, n-1]
      i, j = 0, nums.length - 1
    
      while i <= j
        # Calculate the midpoint index m
        m = (i + j) / 2
    
        if nums[m] < target
          i = m + 1 # target is in the interval [m+1, j]
        elsif nums[m] > target
          j = m - 1 # target is in the interval [i, m-1]
        else
          return m  # Found target, return insertion point m
        end
      end
    
      i # Target not found, return insertion point i
    ```


!!! mẹo

Đoạn mã trong phần này sử dụng toàn bộ cách tiếp cận "khoảng đóng". Bạn đọc quan tâm có thể tự mình thực hiện phương pháp “đóng trái, mở phải”.

Nhìn chung, tìm kiếm nhị phân chỉ đơn giản là vấn đề thiết lập các mục tiêu tìm kiếm riêng biệt cho các con trỏ $i$ và $j$. Mục tiêu có thể là một phần tử cụ thể (chẳng hạn như `target`) hoặc một phạm vi phần tử (chẳng hạn như các phần tử nhỏ hơn `target`).

Với mỗi lần lặp lại tìm kiếm nhị phân, các con trỏ $i$ và $j$ dần dần tiếp cận các mục tiêu đặt trước của chúng. Cuối cùng, họ tìm ra câu trả lời hoặc dừng lại sau khi vượt qua ranh giới.
