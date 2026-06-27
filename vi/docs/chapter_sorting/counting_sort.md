# Đếm Sắp xếp

<u>Counting sort</u> sorts by counting the occurrences of elements and is typically applied to integer arrays.

## Thực hiện đơn giản

Hãy bắt đầu với một ví dụ đơn giản. Cho một mảng `nums` có độ dài $n$, trong đó các phần tử đều là "số nguyên không âm", quy trình sắp xếp tổng thể được hiển thị trong hình bên dưới.

1. Duyệt mảng để tìm số lớn nhất, ký hiệu là $m$, sau đó tạo mảng phụ `bộ đếm` có độ dài $m + 1$.
2. **Sử dụng `bộ đếm` để đếm số lần mỗi số xuất hiện trong `nums`**, trong đó `bộ đếm [num]` lưu trữ số lần xuất hiện của `num`. Điều này rất đơn giản: duyệt qua `nums` (biểu thị số hiện tại bằng `num`) và tăng `counter[num]` lên $1$ mỗi lần.
3. **Vì các chỉ số của `bộ đếm` được sắp xếp tự nhiên nên các số đã được sắp xếp một cách hiệu quả**. Tiếp theo, duyệt qua `bộ đếm` và viết các số trở lại thành `nums` theo thứ tự tăng dần theo số lần xuất hiện của chúng.

![Counting sort flow](counting_sort.assets/counting_sort_overview.png)

Mã này như sau:

=== "Python"
    ```python title="counting_sort.py"
    def counting_sort_naive(nums: list[int]):
        """Counting sort"""
        # Simple implementation, cannot be used for sorting objects
        # 1. Count the maximum element m in the array
        m = 0
        for num in nums:
            m = max(m, num)
        # 2. Count the occurrence of each number
        # counter[num] represents the occurrence of num
        counter = [0] * (m + 1)
        for num in nums:
            counter[num] += 1
        # 3. Traverse counter, filling each element back into the original array nums
        i = 0
        for num in range(m + 1):
            for _ in range(counter[num]):
                nums[i] = num
                i += 1
    ```
=== "C++"
    ```cpp title="counting_sort.cpp"
    // Simple implementation, cannot be used for sorting objects
    void countingSortNaive(vector<int> &nums) {
        // 1. Count the maximum element m in the array
        int m = 0;
        for (int num : nums) {
            m = max(m, num);
        }
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        vector<int> counter(m + 1, 0);
        for (int num : nums) {
            counter[num]++;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        int i = 0;
        for (int num = 0; num < m + 1; num++) {
            for (int j = 0; j < counter[num]; j++, i++) {
                nums[i] = num;
            }
        }
    }
    ```
=== "Java"
    ```java title="counting_sort.java"
    // Simple implementation, cannot be used for sorting objects
        static void countingSortNaive(int[] nums) {
            // 1. Count the maximum element m in the array
            int m = 0;
            for (int num : nums) {
                m = Math.max(m, num);
            }
            // 2. Count the occurrence of each number
            // counter[num] represents the occurrence of num
            int[] counter = new int[m + 1];
            for (int num : nums) {
                counter[num]++;
            }
            // 3. Traverse counter, filling each element back into the original array nums
            int i = 0;
            for (int num = 0; num < m + 1; num++) {
                for (int j = 0; j < counter[num]; j++, i++) {
                    nums[i] = num;
                }
            }
        }
    ```
=== "C#"
    ```csharp title="counting_sort.cs"
    // Simple implementation, cannot be used for sorting objects
        void CountingSortNaive(int[] nums) {
            // 1. Count the maximum element m in the array
            int m = 0;
            foreach (int num in nums) {
                m = Math.Max(m, num);
            }
            // 2. Count the occurrence of each number
            // counter[num] represents the occurrence of num
            int[] counter = new int[m + 1];
            foreach (int num in nums) {
                counter[num]++;
            }
            // 3. Traverse counter, filling each element back into the original array nums
            int i = 0;
            for (int num = 0; num < m + 1; num++) {
                for (int j = 0; j < counter[num]; j++, i++) {
                    nums[i] = num;
                }
            }
        }
    ```
=== "Go"
    ```go title="counting_sort.go"
    // Simple implementation, cannot be used for sorting objects
    func countingSortNaive(nums []int) {
    	// 1. Count the maximum element m in the array
    	m := 0
    	for _, num := range nums {
    		if num > m {
    			m = num
    		}
    	}
    	// 2. Count the occurrence of each number
    	// counter[num] represents the occurrence of num
    	counter := make([]int, m+1)
    	for _, num := range nums {
    		counter[num]++
    	}
    	// 3. Traverse counter, filling each element back into the original array nums
    	for i, num := 0, 0; num < m+1; num++ {
    		for j := 0; j < counter[num]; j++ {
    			nums[i] = num
    			i++
    		}
    	}
    }
    ```
=== "Swift"
    ```swift title="counting_sort.swift"
    // Simple implementation, cannot be used for sorting objects
    func countingSortNaive(nums: inout [Int]) {
        // 1. Count the maximum element m in the array
        let m = nums.max()!
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        var counter = Array(repeating: 0, count: m + 1)
        for num in nums {
            counter[num] += 1
        }
        // 3. Traverse counter, filling each element back into the original array nums
        var i = 0
        for num in 0 ..< m + 1 {
            for _ in 0 ..< counter[num] {
                nums[i] = num
                i += 1
            }
        }
    }
    ```
=== "JS"
    ```javascript title="counting_sort.js"
    // Simple implementation, cannot be used for sorting objects
    function countingSortNaive(nums) {
        // 1. Count the maximum element m in the array
        let m = Math.max(...nums);
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        const counter = new Array(m + 1).fill(0);
        for (const num of nums) {
            counter[num]++;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        let i = 0;
        for (let num = 0; num < m + 1; num++) {
            for (let j = 0; j < counter[num]; j++, i++) {
                nums[i] = num;
            }
        }
    }
    ```
=== "TS"
    ```typescript title="counting_sort.ts"
    // Simple implementation, cannot be used for sorting objects
    function countingSortNaive(nums: number[]): void {
        // 1. Count the maximum element m in the array
        let m: number = Math.max(...nums);
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        const counter: number[] = new Array<number>(m + 1).fill(0);
        for (const num of nums) {
            counter[num]++;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        let i = 0;
        for (let num = 0; num < m + 1; num++) {
            for (let j = 0; j < counter[num]; j++, i++) {
                nums[i] = num;
            }
        }
    }
    ```
=== "Dart"
    ```dart title="counting_sort.dart"
    // Simple implementation, cannot be used for sorting objects
    void countingSortNaive(List<int> nums) {
      // 1. Count the maximum element m in the array
      int m = 0;
      for (int _num in nums) {
        m = max(m, _num);
      }
      // 2. Count the occurrence of each number
      // counter[_num] represents occurrence count of _num
      List<int> counter = List.filled(m + 1, 0);
      for (int _num in nums) {
        counter[_num]++;
      }
      // 3. Traverse counter, filling each element back into the original array nums
      int i = 0;
      for (int _num = 0; _num < m + 1; _num++) {
        for (int j = 0; j < counter[_num]; j++, i++) {
          nums[i] = _num;
        }
      }
    }
    ```
=== "Rust"
    ```rust title="counting_sort.rs"
    // Simple implementation, cannot be used for sorting objects
    fn counting_sort_naive(nums: &mut [i32]) {
        // 1. Count the maximum element m in the array
        let m = *nums.iter().max().unwrap();
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        let mut counter = vec![0; m as usize + 1];
        for &num in nums.iter() {
            counter[num as usize] += 1;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        let mut i = 0;
        for num in 0..m + 1 {
            for _ in 0..counter[num as usize] {
                nums[i] = num;
                i += 1;
            }
        }
    }
    ```
=== "C"
    ```c title="counting_sort.c"
    // Simple implementation, cannot be used for sorting objects
    void countingSortNaive(int nums[], int size) {
        // 1. Count the maximum element m in the array
        int m = 0;
        for (int i = 0; i < size; i++) {
            if (nums[i] > m) {
                m = nums[i];
            }
        }
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        int *counter = calloc(m + 1, sizeof(int));
        for (int i = 0; i < size; i++) {
            counter[nums[i]]++;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        int i = 0;
        for (int num = 0; num < m + 1; num++) {
            for (int j = 0; j < counter[num]; j++, i++) {
                nums[i] = num;
            }
        }
        // 4. Free memory
        free(counter);
    }
    ```
=== "Kotlin"
    ```kotlin title="counting_sort.kt"
    // Simple implementation, cannot be used for sorting objects
    fun countingSortNaive(nums: IntArray) {
        // 1. Count the maximum element m in the array
        var m = 0
        for (num in nums) {
            m = max(m, num)
        }
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        val counter = IntArray(m + 1)
        for (num in nums) {
            counter[num]++
        }
        // 3. Traverse counter, filling each element back into the original array nums
        var i = 0
        for (num in 0..<m + 1) {
            var j = 0
            while (j < counter[num]) {
                nums[i] = num
                j++
                i++
            }
        }
    }
    ```
=== "Ruby"
    ```ruby title="counting_sort.rb"
    ### Counting sort ###
    def counting_sort_naive(nums)
      # Simple implementation, cannot be used for sorting objects
      # 1. Count the maximum element m in the array
      m = 0
      nums.each { |num| m = [m, num].max }
      # 2. Count the occurrence of each number
      # counter[num] represents the occurrence of num
      counter = Array.new(m + 1, 0)
      nums.each { |num| counter[num] += 1 }
      # 3. Traverse counter, filling each element back into the original array nums
      i = 0
      for num in 0...(m + 1)
        (0...counter[num]).each do
          nums[i] = num
          i += 1
        end
      end
    ```


!!! lưu ý "Kết nối giữa sắp xếp đếm và sắp xếp nhóm"

Từ góc độ sắp xếp nhóm, mỗi chỉ mục của mảng đếm `bộ đếm` có thể được xem dưới dạng một nhóm và quá trình đếm có thể được xem như là phân phối các phần tử vào các nhóm tương ứng của chúng. Về cơ bản, sắp xếp đếm là trường hợp đặc biệt của sắp xếp nhóm cho dữ liệu số nguyên.

## Thực hiện hoàn chỉnh

Những độc giả tinh ý có thể nhận thấy rằng **nếu dữ liệu đầu vào bao gồm các đối tượng thì bước `3.` ở trên không còn hiệu quả**. Giả sử đầu vào bao gồm các đối tượng sản phẩm và chúng ta muốn sắp xếp chúng theo giá (một biến thành viên của lớp); thuật toán trên chỉ có thể tự tạo ra thứ tự sắp xếp của giá.

Vậy làm thế nào chúng ta có thể có được thứ tự sắp xếp của dữ liệu gốc? Đầu tiên chúng ta tính tổng tiền tố của `counter`. Như tên gợi ý, tổng tiền tố tại chỉ mục `i`, `prefix[i]`, bằng tổng của các phần tử từ chỉ mục `0` đến `i`:

$$
\text{tiền tố[i] = \sum_{j=0}^i \text{counter[j]}
$$

**Tổng tiền tố có cách hiểu rõ ràng: `tiền tố[num] - 1` đưa ra chỉ số lần xuất hiện cuối cùng của phần tử `num` trong mảng kết quả `res`**. Thông tin này rất quan trọng vì nó cho chúng ta biết vị trí của từng phần tử trong mảng kết quả. Tiếp theo, chúng ta duyệt ngược lại mảng `nums` ban đầu và đối với mỗi phần tử `num`, hãy thực hiện hai bước sau.

1. Đặt `num` tại chỉ mục `tiền tố[num] - 1` của mảng `res`.
2. Giảm tổng tiền tố `prefix[num]` xuống $1$ để lấy chỉ mục cho vị trí tiếp theo của `num`.

Sau khi quá trình truyền tải hoàn tất, mảng `res` chứa kết quả được sắp xếp và cuối cùng `res` được sử dụng để ghi đè lên mảng `nums` ban đầu. Luồng sắp xếp đếm hoàn chỉnh được hiển thị trong hình bên dưới.

=== "<1>"
    ![Counting sort steps](counting_sort.assets/counting_sort_step1.png)

=== "<2>"
    ![counting_sort_step2](counting_sort.assets/counting_sort_step2.png)

=== "<3>"
    ![counting_sort_step3](counting_sort.assets/counting_sort_step3.png)

=== "<4>"
    ![counting_sort_step4](counting_sort.assets/counting_sort_step4.png)

=== "<5>"
    ![counting_sort_step5](counting_sort.assets/counting_sort_step5.png)

=== "<6>"
    ![counting_sort_step6](counting_sort.assets/counting_sort_step6.png)

=== "<7>"
    ![counting_sort_step7](counting_sort.assets/counting_sort_step7.png)

=== "<8>"
    ![counting_sort_step8](counting_sort.assets/counting_sort_step8.png)

Việc thực hiện sắp xếp đếm được hiển thị dưới đây:

=== "Python"
    ```python title="counting_sort.py"
    def counting_sort_naive(nums: list[int]):
        """Counting sort"""
        # Simple implementation, cannot be used for sorting objects
        # 1. Count the maximum element m in the array
        m = 0
        for num in nums:
            m = max(m, num)
        # 2. Count the occurrence of each number
        # counter[num] represents the occurrence of num
        counter = [0] * (m + 1)
        for num in nums:
            counter[num] += 1
        # 3. Traverse counter, filling each element back into the original array nums
        i = 0
        for num in range(m + 1):
            for _ in range(counter[num]):
                nums[i] = num
                i += 1
    ```
=== "C++"
    ```cpp title="counting_sort.cpp"
    // Simple implementation, cannot be used for sorting objects
    void countingSortNaive(vector<int> &nums) {
        // 1. Count the maximum element m in the array
        int m = 0;
        for (int num : nums) {
            m = max(m, num);
        }
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        vector<int> counter(m + 1, 0);
        for (int num : nums) {
            counter[num]++;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        int i = 0;
        for (int num = 0; num < m + 1; num++) {
            for (int j = 0; j < counter[num]; j++, i++) {
                nums[i] = num;
            }
        }
    }
    ```
=== "Java"
    ```java title="counting_sort.java"
    public class counting_sort {
        /* Counting sort */
        // Simple implementation, cannot be used for sorting objects
        static void countingSortNaive(int[] nums) {
            // 1. Count the maximum element m in the array
            int m = 0;
            for (int num : nums) {
                m = Math.max(m, num);
            }
            // 2. Count the occurrence of each number
            // counter[num] represents the occurrence of num
            int[] counter = new int[m + 1];
            for (int num : nums) {
                counter[num]++;
            }
            // 3. Traverse counter, filling each element back into the original array nums
            int i = 0;
            for (int num = 0; num < m + 1; num++) {
                for (int j = 0; j < counter[num]; j++, i++) {
                    nums[i] = num;
                }
            }
        }
    
        /* Counting sort */
        // Complete implementation, can sort objects and is a stable sort
        static void countingSort(int[] nums) {
            // 1. Count the maximum element m in the array
            int m = 0;
            for (int num : nums) {
                m = Math.max(m, num);
            }
            // 2. Count the occurrence of each number
            // counter[num] represents the occurrence of num
            int[] counter = new int[m + 1];
            for (int num : nums) {
                counter[num]++;
            }
            // 3. Calculate the prefix sum of counter, converting "occurrence count" to "tail index"
            // counter[num]-1 is the last index where num appears in res
            for (int i = 0; i < m; i++) {
                counter[i + 1] += counter[i];
            }
            // 4. Traverse nums in reverse order, placing each element into the result array res
            // Initialize the array res to record results
            int n = nums.length;
            int[] res = new int[n];
            for (int i = n - 1; i >= 0; i--) {
                int num = nums[i];
                res[counter[num] - 1] = num; // Place num at the corresponding index
                counter[num]--; // Decrement the prefix sum by 1, getting the next index to place num
            }
            // Use result array res to overwrite the original array nums
            for (int i = 0; i < n; i++) {
                nums[i] = res[i];
            }
        }
    
        public static void main(String[] args) {
            int[] nums = { 1, 0, 1, 2, 0, 4, 0, 2, 2, 4 };
            countingSortNaive(nums);
            System.out.println("After counting sort (cannot sort objects) completes, nums = " + Arrays.toString(nums));
    
            int[] nums1 = { 1, 0, 1, 2, 0, 4, 0, 2, 2, 4 };
            countingSort(nums1);
            System.out.println("After counting sort completes, nums1 = " + Arrays.toString(nums1));
        }
    }
    ```
=== "C#"
    ```csharp title="counting_sort.cs"
    public class counting_sort {
        /* Counting sort */
        // Simple implementation, cannot be used for sorting objects
        void CountingSortNaive(int[] nums) {
            // 1. Count the maximum element m in the array
            int m = 0;
            foreach (int num in nums) {
                m = Math.Max(m, num);
            }
            // 2. Count the occurrence of each number
            // counter[num] represents the occurrence of num
            int[] counter = new int[m + 1];
            foreach (int num in nums) {
                counter[num]++;
            }
            // 3. Traverse counter, filling each element back into the original array nums
            int i = 0;
            for (int num = 0; num < m + 1; num++) {
                for (int j = 0; j < counter[num]; j++, i++) {
                    nums[i] = num;
                }
            }
        }
    
        /* Counting sort */
        // Complete implementation, can sort objects and is a stable sort
        void CountingSort(int[] nums) {
            // 1. Count the maximum element m in the array
            int m = 0;
            foreach (int num in nums) {
                m = Math.Max(m, num);
            }
            // 2. Count the occurrence of each number
            // counter[num] represents the occurrence of num
            int[] counter = new int[m + 1];
            foreach (int num in nums) {
                counter[num]++;
            }
            // 3. Calculate the prefix sum of counter, converting "occurrence count" to "tail index"
            // counter[num]-1 is the last index where num appears in res
            for (int i = 0; i < m; i++) {
                counter[i + 1] += counter[i];
            }
            // 4. Traverse nums in reverse order, placing each element into the result array res
            // Initialize the array res to record results
            int n = nums.Length;
            int[] res = new int[n];
            for (int i = n - 1; i >= 0; i--) {
                int num = nums[i];
                res[counter[num] - 1] = num; // Place num at the corresponding index
                counter[num]--; // Decrement the prefix sum by 1, getting the next index to place num
            }
            // Use result array res to overwrite the original array nums
            for (int i = 0; i < n; i++) {
                nums[i] = res[i];
            }
        }
    
        [Test]
        public void Test() {
            int[] nums = [1, 0, 1, 2, 0, 4, 0, 2, 2, 4];
            CountingSortNaive(nums);
            Console.WriteLine("After counting sort (cannot sort objects) completes, nums = " + string.Join(" ", nums));
    
            int[] nums1 = [1, 0, 1, 2, 0, 4, 0, 2, 2, 4];
            CountingSort(nums1);
            Console.WriteLine("After counting sort completes, nums1 = " + string.Join(" ", nums));
        }
    }
    ```
=== "Go"
    ```go title="counting_sort.go"
    // Simple implementation, cannot be used for sorting objects
    func countingSortNaive(nums []int) {
    	// 1. Count the maximum element m in the array
    	m := 0
    	for _, num := range nums {
    		if num > m {
    			m = num
    		}
    	}
    	// 2. Count the occurrence of each number
    	// counter[num] represents the occurrence of num
    	counter := make([]int, m+1)
    	for _, num := range nums {
    		counter[num]++
    	}
    	// 3. Traverse counter, filling each element back into the original array nums
    	for i, num := 0, 0; num < m+1; num++ {
    		for j := 0; j < counter[num]; j++ {
    			nums[i] = num
    			i++
    		}
    	}
    }
    ```
=== "Swift"
    ```swift title="counting_sort.swift"
    // Simple implementation, cannot be used for sorting objects
    func countingSortNaive(nums: inout [Int]) {
        // 1. Count the maximum element m in the array
        let m = nums.max()!
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        var counter = Array(repeating: 0, count: m + 1)
        for num in nums {
            counter[num] += 1
        }
        // 3. Traverse counter, filling each element back into the original array nums
        var i = 0
        for num in 0 ..< m + 1 {
            for _ in 0 ..< counter[num] {
                nums[i] = num
                i += 1
            }
        }
    }
    ```
=== "JS"
    ```javascript title="counting_sort.js"
    // Complete implementation, can sort objects and is a stable sort
    function countingSort(nums) {
        // 1. Count the maximum element m in the array
        let m = Math.max(...nums);
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        const counter = new Array(m + 1).fill(0);
        for (const num of nums) {
            counter[num]++;
        }
        // 3. Calculate the prefix sum of counter, converting "occurrence count" to "tail index"
        // counter[num]-1 is the last index where num appears in res
        for (let i = 0; i < m; i++) {
            counter[i + 1] += counter[i];
        }
        // 4. Traverse nums in reverse order, placing each element into the result array res
        // Initialize the array res to record results
        const n = nums.length;
        const res = new Array(n);
        for (let i = n - 1; i >= 0; i--) {
            const num = nums[i];
            res[counter[num] - 1] = num; // Place num at the corresponding index
            counter[num]--; // Decrement the prefix sum by 1, getting the next index to place num
        }
        // Use result array res to overwrite the original array nums
        for (let i = 0; i < n; i++) {
            nums[i] = res[i];
        }
    }
    ```
=== "TS"
    ```typescript title="counting_sort.ts"
    // Simple implementation, cannot be used for sorting objects
    function countingSortNaive(nums: number[]): void {
        // 1. Count the maximum element m in the array
        let m: number = Math.max(...nums);
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        const counter: number[] = new Array<number>(m + 1).fill(0);
        for (const num of nums) {
            counter[num]++;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        let i = 0;
        for (let num = 0; num < m + 1; num++) {
            for (let j = 0; j < counter[num]; j++, i++) {
                nums[i] = num;
            }
        }
    }
    ```
=== "Dart"
    ```dart title="counting_sort.dart"
    // Simple implementation, cannot be used for sorting objects
    void countingSortNaive(List<int> nums) {
      // 1. Count the maximum element m in the array
      int m = 0;
      for (int _num in nums) {
        m = max(m, _num);
      }
      // 2. Count the occurrence of each number
      // counter[_num] represents occurrence count of _num
      List<int> counter = List.filled(m + 1, 0);
      for (int _num in nums) {
        counter[_num]++;
      }
      // 3. Traverse counter, filling each element back into the original array nums
      int i = 0;
      for (int _num = 0; _num < m + 1; _num++) {
        for (int j = 0; j < counter[_num]; j++, i++) {
          nums[i] = _num;
        }
      }
    }
    ```
=== "Rust"
    ```rust title="counting_sort.rs"
    // Simple implementation, cannot be used for sorting objects
    fn counting_sort_naive(nums: &mut [i32]) {
        // 1. Count the maximum element m in the array
        let m = *nums.iter().max().unwrap();
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        let mut counter = vec![0; m as usize + 1];
        for &num in nums.iter() {
            counter[num as usize] += 1;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        let mut i = 0;
        for num in 0..m + 1 {
            for _ in 0..counter[num as usize] {
                nums[i] = num;
                i += 1;
            }
        }
    }
    ```
=== "C"
    ```c title="counting_sort.c"
    // Simple implementation, cannot be used for sorting objects
    void countingSortNaive(int nums[], int size) {
        // 1. Count the maximum element m in the array
        int m = 0;
        for (int i = 0; i < size; i++) {
            if (nums[i] > m) {
                m = nums[i];
            }
        }
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        int *counter = calloc(m + 1, sizeof(int));
        for (int i = 0; i < size; i++) {
            counter[nums[i]]++;
        }
        // 3. Traverse counter, filling each element back into the original array nums
        int i = 0;
        for (int num = 0; num < m + 1; num++) {
            for (int j = 0; j < counter[num]; j++, i++) {
                nums[i] = num;
            }
        }
        // 4. Free memory
        free(counter);
    }
    ```
=== "Kotlin"
    ```kotlin title="counting_sort.kt"
    // Complete implementation, can sort objects and is a stable sort
    fun countingSort(nums: IntArray) {
        // 1. Count the maximum element m in the array
        var m = 0
        for (num in nums) {
            m = max(m, num)
        }
        // 2. Count the occurrence of each number
        // counter[num] represents the occurrence of num
        val counter = IntArray(m + 1)
        for (num in nums) {
            counter[num]++
        }
        // 3. Calculate the prefix sum of counter, converting "occurrence count" to "tail index"
        // counter[num]-1 is the last index where num appears in res
        for (i in 0..<m) {
            counter[i + 1] += counter[i]
        }
        // 4. Traverse nums in reverse order, placing each element into the result array res
        // Initialize the array res to record results
        val n = nums.size
        val res = IntArray(n)
        for (i in n - 1 downTo 0) {
            val num = nums[i]
            res[counter[num] - 1] = num // Place num at the corresponding index
            counter[num]-- // Decrement the prefix sum by 1, getting the next index to place num
        }
        // Use result array res to overwrite the original array nums
        for (i in 0..<n) {
            nums[i] = res[i]
        }
    }
    ```
=== "Ruby"
    ```ruby title="counting_sort.rb"
    ### Counting sort ###
    def counting_sort_naive(nums)
      # Simple implementation, cannot be used for sorting objects
      # 1. Count the maximum element m in the array
      m = 0
      nums.each { |num| m = [m, num].max }
      # 2. Count the occurrence of each number
      # counter[num] represents the occurrence of num
      counter = Array.new(m + 1, 0)
      nums.each { |num| counter[num] += 1 }
      # 3. Traverse counter, filling each element back into the original array nums
      i = 0
      for num in 0...(m + 1)
        (0...counter[num]).each do
          nums[i] = num
          i += 1
        end
      end
    ```


## Đặc điểm thuật toán

- **Độ phức tạp về thời gian là $O(n + m)$ và cách sắp xếp đếm không thích ứng**: Việc duyệt `nums` và `counter` đều mất thời gian tuyến tính. Nói chung, khi $n \gg m$, độ phức tạp về thời gian tiến tới $O(n)$.
- **Độ phức tạp về không gian của $O(n + m)$, sắp xếp không tại chỗ**: Sử dụng mảng `res` và `counter` có độ dài tương ứng là $n$ và $m$.
- **Sắp xếp ổn định**: Vì các phần tử được điền vào `res` theo thứ tự "từ phải sang trái", việc duyệt ngược lại `nums` có thể tránh thay đổi vị trí tương đối của các phần tử bằng nhau, từ đó đạt được sự sắp xếp ổn định. Trên thực tế, việc duyệt qua `nums` theo thứ tự thuận cũng có thể mang lại kết quả sắp xếp chính xác, nhưng kết quả sẽ không ổn định.

## Hạn chế

Tại thời điểm này, bạn có thể nghĩ việc sắp xếp đếm khá khéo léo vì nó đạt được sự sắp xếp hiệu quả chỉ bằng cách đếm số lần xuất hiện. Tuy nhiên, các điều kiện tiên quyết để sử dụng tính năng sắp xếp đếm khá hạn chế.

**Sắp xếp đếm chỉ áp dụng cho số nguyên không âm**. Để áp dụng nó cho các loại dữ liệu khác, bạn phải đảm bảo rằng chúng có thể được chuyển đổi thành số nguyên không âm mà không thay đổi thứ tự tương đối của các phần tử. Ví dụ: đối với một mảng số nguyên chứa số âm, trước tiên bạn có thể thêm hằng số vào mỗi số để chuyển chúng sang phạm vi không âm, sau đó chuyển chúng trở lại sau khi sắp xếp.

**Sắp xếp đếm rất phù hợp với các trường hợp có nhiều phần tử nhưng phạm vi giá trị nhỏ**. Ví dụ: trong kịch bản trên, $m$ không thể quá lớn; nếu không, nó tiêu tốn quá nhiều không gian. Và khi $n \ll m$, việc sắp xếp việc đếm mất $O(m)$ thời gian, có thể chậm hơn so với các thuật toán sắp xếp có độ phức tạp về thời gian $O(n \log n)$.
