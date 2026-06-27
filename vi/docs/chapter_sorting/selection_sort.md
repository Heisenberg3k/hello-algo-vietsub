# Sắp xếp lựa chọn

<u>Selection sort</u> works very simply: in each round, it selects the smallest element from the unsorted interval and places it at the end of the sorted interval.

Giả sử mảng có độ dài $n$. Quy trình sắp xếp lựa chọn được thể hiện trong hình dưới đây.

1. Ban đầu, tất cả các phần tử đều chưa được sắp xếp, tức là khoảng (chỉ mục) chưa được sắp xếp là $[0, n-1]$.
2. Chọn phần tử nhỏ nhất trong khoảng $[0, n-1]$ và hoán đổi nó với phần tử ở chỉ số $0$. Sau khi hoàn thành, phần tử đầu tiên của mảng được sắp xếp.
3. Chọn phần tử nhỏ nhất trong khoảng $[1, n-1]$ và hoán đổi nó với phần tử ở chỉ số $1$. Sau khi hoàn thành, 2 phần tử đầu tiên của mảng được sắp xếp.
4. Và vân vân. Sau $n - 1$ vòng lựa chọn và hoán đổi, các phần tử $n - 1$ đầu tiên của mảng được sắp xếp.
5. Phần tử duy nhất còn lại phải là phần tử lớn nhất, do đó không cần sắp xếp thêm và mảng đã được sắp xếp.

=== "<1>"
    ![Selection sort steps](selection_sort.assets/selection_sort_step1.png)

=== "<2>"
    ![selection_sort_step2](selection_sort.assets/selection_sort_step2.png)

=== "<3>"
    ![selection_sort_step3](selection_sort.assets/selection_sort_step3.png)

=== "<4>"
    ![selection_sort_step4](selection_sort.assets/selection_sort_step4.png)

=== "<5>"
    ![selection_sort_step5](selection_sort.assets/selection_sort_step5.png)

=== "<6>"
    ![selection_sort_step6](selection_sort.assets/selection_sort_step6.png)

=== "<7>"
    ![selection_sort_step7](selection_sort.assets/selection_sort_step7.png)

=== "<8>"
    ![selection_sort_step8](selection_sort.assets/selection_sort_step8.png)

=== "<9>"
    ![selection_sort_step9](selection_sort.assets/selection_sort_step9.png)

=== "<10>"
    ![selection_sort_step10](selection_sort.assets/selection_sort_step10.png)

=== "<11>"
    ![selection_sort_step11](selection_sort.assets/selection_sort_step11.png)

Trong mã, chúng tôi sử dụng $k$ để theo dõi phần tử nhỏ nhất trong khoảng chưa được sắp xếp:

=== "Python"
    ```python title="selection_sort.py"
    def selection_sort(nums: list[int]):
        """Selection sort"""
        n = len(nums)
        # Outer loop: unsorted interval is [i, n-1]
        for i in range(n - 1):
            # Inner loop: find the smallest element within the unsorted interval
            k = i
            for j in range(i + 1, n):
                if nums[j] < nums[k]:
                    k = j  # Record the index of the smallest element
            # Swap the smallest element with the first element of the unsorted interval
            nums[i], nums[k] = nums[k], nums[i]
    ```
=== "C++"
    ```cpp title="selection_sort.cpp"
    void selectionSort(vector<int> &nums) {
        int n = nums.size();
        // Outer loop: unsorted interval is [i, n-1]
        for (int i = 0; i < n - 1; i++) {
            // Inner loop: find the smallest element within the unsorted interval
            int k = i;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] < nums[k])
                    k = j; // Record the index of the smallest element
            }
            // Swap the smallest element with the first element of the unsorted interval
            swap(nums[i], nums[k]);
        }
    }
    ```
=== "Java"
    ```java title="selection_sort.java"
    public class selection_sort {
        /* Selection sort */
        public static void selectionSort(int[] nums) {
            int n = nums.length;
            // Outer loop: unsorted interval is [i, n-1]
            for (int i = 0; i < n - 1; i++) {
                // Inner loop: find the smallest element within the unsorted interval
                int k = i;
                for (int j = i + 1; j < n; j++) {
                    if (nums[j] < nums[k])
                        k = j; // Record the index of the smallest element
                }
                // Swap the smallest element with the first element of the unsorted interval
                int temp = nums[i];
                nums[i] = nums[k];
                nums[k] = temp;
            }
        }
    
        public static void main(String[] args) {
            int[] nums = { 4, 1, 3, 1, 5, 2 };
            selectionSort(nums);
            System.out.println("After selection sort completes, nums = " + Arrays.toString(nums));
        }
    }
    ```
=== "C#"
    ```csharp title="selection_sort.cs"
    public class selection_sort {
        /* Selection sort */
        void SelectionSort(int[] nums) {
            int n = nums.Length;
            // Outer loop: unsorted interval is [i, n-1]
            for (int i = 0; i < n - 1; i++) {
                // Inner loop: find the smallest element within the unsorted interval
                int k = i;
                for (int j = i + 1; j < n; j++) {
                    if (nums[j] < nums[k])
                        k = j; // Record the index of the smallest element
                }
                // Swap the smallest element with the first element of the unsorted interval
                (nums[k], nums[i]) = (nums[i], nums[k]);
            }
        }
    
        [Test]
        public void Test() {
            int[] nums = [4, 1, 3, 1, 5, 2];
            SelectionSort(nums);
            Console.WriteLine("After selection sort completes, nums = " + string.Join(" ", nums));
        }
    }
    ```
=== "Go"
    ```go title="selection_sort.go"
    func selectionSort(nums []int) {
    	n := len(nums)
    	// Outer loop: unsorted interval is [i, n-1]
    	for i := 0; i < n-1; i++ {
    		// Inner loop: find the smallest element within the unsorted interval
    		k := i
    		for j := i + 1; j < n; j++ {
    			if nums[j] < nums[k] {
    				// Record the index of the smallest element
    				k = j
    			}
    		}
    		// Swap the smallest element with the first element of the unsorted interval
    		nums[i], nums[k] = nums[k], nums[i]
    
    	}
    }
    ```
=== "Swift"
    ```swift title="selection_sort.swift"
    func selectionSort(nums: inout [Int]) {
        // Outer loop: unsorted interval is [i, n-1]
        for i in nums.indices.dropLast() {
            // Inner loop: find the smallest element within the unsorted interval
            var k = i
            for j in nums.indices.dropFirst(i + 1) {
                if nums[j] < nums[k] {
                    k = j // Record the index of the smallest element
                }
            }
            // Swap the smallest element with the first element of the unsorted interval
            nums.swapAt(i, k)
        }
    }
    ```
=== "JS"
    ```javascript title="selection_sort.js"
    function selectionSort(nums) {
        let n = nums.length;
        // Outer loop: unsorted interval is [i, n-1]
        for (let i = 0; i < n - 1; i++) {
            // Inner loop: find the smallest element within the unsorted interval
            let k = i;
            for (let j = i + 1; j < n; j++) {
                if (nums[j] < nums[k]) {
                    k = j; // Record the index of the smallest element
                }
            }
            // Swap the smallest element with the first element of the unsorted interval
            [nums[i], nums[k]] = [nums[k], nums[i]];
        }
    }
    ```
=== "TS"
    ```typescript title="selection_sort.ts"
    function selectionSort(nums: number[]): void {
        let n = nums.length;
        // Outer loop: unsorted interval is [i, n-1]
        for (let i = 0; i < n - 1; i++) {
            // Inner loop: find the smallest element within the unsorted interval
            let k = i;
            for (let j = i + 1; j < n; j++) {
                if (nums[j] < nums[k]) {
                    k = j; // Record the index of the smallest element
                }
            }
            // Swap the smallest element with the first element of the unsorted interval
            [nums[i], nums[k]] = [nums[k], nums[i]];
        }
    }
    ```
=== "Dart"
    ```dart title="selection_sort.dart"
    void selectionSort(List<int> nums) {
      int n = nums.length;
      // Outer loop: unsorted interval is [i, n-1]
      for (int i = 0; i < n - 1; i++) {
        // Inner loop: find the smallest element within the unsorted interval
        int k = i;
        for (int j = i + 1; j < n; j++) {
          if (nums[j] < nums[k]) k = j; // Record the index of the smallest element
        }
        // Swap the smallest element with the first element of the unsorted interval
        int temp = nums[i];
        nums[i] = nums[k];
        nums[k] = temp;
      }
    }
    ```
=== "Rust"
    ```rust title="selection_sort.rs"
    fn selection_sort(nums: &mut [i32]) {
        if nums.is_empty() {
            return;
        }
        let n = nums.len();
        // Outer loop: unsorted interval is [i, n-1]
        for i in 0..n - 1 {
            // Inner loop: find the smallest element within the unsorted interval
            let mut k = i;
            for j in i + 1..n {
                if nums[j] < nums[k] {
                    k = j; // Record the index of the smallest element
                }
            }
            // Swap the smallest element with the first element of the unsorted interval
            nums.swap(i, k);
        }
    }
    ```
=== "C"
    ```c title="selection_sort.c"
    void selectionSort(int nums[], int n) {
        // Outer loop: unsorted interval is [i, n-1]
        for (int i = 0; i < n - 1; i++) {
            // Inner loop: find the smallest element within the unsorted interval
            int k = i;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] < nums[k])
                    k = j; // Record the index of the smallest element
            }
            // Swap the smallest element with the first element of the unsorted interval
            int temp = nums[i];
            nums[i] = nums[k];
            nums[k] = temp;
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="selection_sort.kt"
    fun selectionSort(nums: IntArray) {
        val n = nums.size
        // Outer loop: unsorted interval is [i, n-1]
        for (i in 0..<n - 1) {
            var k = i
            // Inner loop: find the smallest element within the unsorted interval
            for (j in i + 1..<n) {
                if (nums[j] < nums[k])
                    k = j // Record the index of the smallest element
            }
            // Swap the smallest element with the first element of the unsorted interval
            val temp = nums[i]
            nums[i] = nums[k]
            nums[k] = temp
        }
    }
    ```
=== "Ruby"
    ```ruby title="selection_sort.rb"
    ### Selection sort ###
    def selection_sort(nums)
      n = nums.length
      # Outer loop: unsorted interval is [i, n-1]
      for i in 0...(n - 1)
        # Inner loop: find the smallest element within the unsorted interval
        k = i
        for j in (i + 1)...n
          if nums[j] < nums[k]
            k = j # Record the index of the smallest element
          end
        end
        # Swap the smallest element with the first element of the unsorted interval
        nums[i], nums[k] = nums[k], nums[i]
      end
    ```


## Đặc điểm thuật toán

- **Độ phức tạp về thời gian $O(n^2)$, sắp xếp không thích ứng**: Vòng lặp bên ngoài có tổng cộng $n - 1$ vòng. Độ dài của khoảng chưa sắp xếp ở vòng đầu tiên là $n$ và độ dài của khoảng chưa sắp xếp ở vòng cuối cùng là $2$. Nghĩa là, các vòng của vòng lặp bên ngoài chứa các vòng lặp bên trong với các lần lặp $n$, $n - 1$, $\dots$, $3$ và $2$, tổng cộng là $\frac{(n - 1)(n + 2)}{2}$.
- **Độ phức tạp của không gian $O(1)$, sắp xếp tại chỗ**: Con trỏ $i$ và $j$ sử dụng một lượng không gian bổ sung không đổi.
- **Sắp xếp không ổn định**: Như minh họa trong hình bên dưới, phần tử `nums[i]` có thể bị hoán đổi sang bên phải của phần tử bằng nó, gây ra sự thay đổi về thứ tự tương đối của chúng.

![Selection sort non-stability example](selection_sort.assets/selection_sort_instability.png)
