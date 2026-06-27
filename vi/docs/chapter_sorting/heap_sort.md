# Sắp xếp đống

!!! mẹo

Trước khi đọc phần này, hãy đảm bảo bạn đã hoàn thành chương "Heap".

<u>Heap sort</u> is an efficient sorting algorithm based on the heap data structure. We can implement heap sort using the heap construction and element removal operations introduced earlier.

1. Nhập mảng và xây dựng vùng heap tối thiểu, tại đó phần tử nhỏ nhất nằm ở đỉnh heap.
2. Thực hiện liên tục các thao tác loại bỏ phần tử và ghi lại các phần tử bị loại bỏ để có được thứ tự sắp xếp tăng dần.

Mặc dù phương pháp trên khả thi nhưng nó yêu cầu một mảng bổ sung để lưu các phần tử được bật ra, điều này khá lãng phí dung lượng. Trong thực tế, chúng tôi thường sử dụng một phương pháp triển khai tinh tế hơn.

## Luồng thuật toán

Giả sử độ dài mảng là $n$. Luồng sắp xếp đống được hiển thị trong hình bên dưới.

1. Nhập mảng và xây dựng vùng heap tối đa. Sau khi hoàn thành, phần tử lớn nhất nằm ở đỉnh heap.
2. Hoán đổi phần tử trên cùng của heap (phần tử đầu tiên) với phần tử dưới cùng của heap (phần tử cuối cùng). Sau khi hoán đổi hoàn tất, hãy giảm độ dài vùng heap xuống $1$ và tăng số lượng phần tử được sắp xếp thêm $1$.
3. Bắt đầu từ phần tử trên cùng của heap, thực hiện thao tác heapify từ trên xuống dưới (sàng lọc xuống). Sau khi heapify hoàn tất, thuộc tính heap được khôi phục.
4. Lặp lại các bước `2.` và `3.` Sau $n - 1$ vòng, mảng được sắp xếp.

!!! mẹo

Trên thực tế, thao tác loại bỏ phần tử còn bao gồm các bước `2.` và `3.`, có thêm bước loại bỏ phần tử.

=== "<1>"
    ![Heap sort steps](heap_sort.assets/heap_sort_step1.png)

=== "<2>"
    ![heap_sort_step2](heap_sort.assets/heap_sort_step2.png)

=== "<3>"
    ![heap_sort_step3](heap_sort.assets/heap_sort_step3.png)

=== "<4>"
    ![heap_sort_step4](heap_sort.assets/heap_sort_step4.png)

=== "<5>"
    ![heap_sort_step5](heap_sort.assets/heap_sort_step5.png)

=== "<6>"
    ![heap_sort_step6](heap_sort.assets/heap_sort_step6.png)

=== "<7>"
    ![heap_sort_step7](heap_sort.assets/heap_sort_step7.png)

=== "<8>"
    ![heap_sort_step8](heap_sort.assets/heap_sort_step8.png)

=== "<9>"
    ![heap_sort_step9](heap_sort.assets/heap_sort_step9.png)

=== "<10>"
    ![heap_sort_step10](heap_sort.assets/heap_sort_step10.png)

=== "<11>"
    ![heap_sort_step11](heap_sort.assets/heap_sort_step11.png)

=== "<12>"
    ![heap_sort_step12](heap_sort.assets/heap_sort_step12.png)

Trong đoạn mã bên dưới, chúng ta sử dụng cùng hàm `sift_down()` để tạo đống dữ liệu từ trên xuống dưới như trong chương "Heap". Điều đáng chú ý là do độ dài heap giảm khi phần tử lớn nhất được trích xuất, chúng ta cần thêm tham số độ dài $n$ vào `sift_down()` để chỉ định độ dài hiệu dụng hiện tại của heap. Mã này như sau:

=== "Python"
    ```python title="heap_sort.py"
    def heap_sort(nums: list[int]):
        """Heap sort"""
        # Build heap operation: heapify all nodes except leaves
        for i in range(len(nums) // 2 - 1, -1, -1):
            sift_down(nums, len(nums), i)
        # Extract the largest element from the heap and repeat for n-1 rounds
        for i in range(len(nums) - 1, 0, -1):
            # Swap the root node with the rightmost leaf node (swap the first element with the last element)
            nums[0], nums[i] = nums[i], nums[0]
            # Start heapifying the root node, from top to bottom
            sift_down(nums, i, 0)
    ```
=== "C++"
    ```cpp title="heap_sort.cpp"
    void heapSort(vector<int> &nums) {
        // Build heap operation: heapify all nodes except leaves
        for (int i = nums.size() / 2 - 1; i >= 0; --i) {
            siftDown(nums, nums.size(), i);
        }
        // Extract the largest element from the heap and repeat for n-1 rounds
        for (int i = nums.size() - 1; i > 0; --i) {
            // Delete node
            swap(nums[0], nums[i]);
            // Start heapifying the root node, from top to bottom
            siftDown(nums, i, 0);
        }
    }
    ```
=== "Java"
    ```java title="heap_sort.java"
    public class heap_sort {
        /* Heap length is n, start heapifying node i, from top to bottom */
        public static void siftDown(int[] nums, int n, int i) {
            while (true) {
                // If node i is largest or indices l, r are out of bounds, no need to continue heapify, break
                int l = 2 * i + 1;
                int r = 2 * i + 2;
                int ma = i;
                if (l < n && nums[l] > nums[ma])
                    ma = l;
                if (r < n && nums[r] > nums[ma])
                    ma = r;
                // Swap two nodes
                if (ma == i)
                    break;
                // Swap two nodes
                int temp = nums[i];
                nums[i] = nums[ma];
                nums[ma] = temp;
                // Loop downwards heapification
                i = ma;
            }
        }
    
        /* Heap sort */
        public static void heapSort(int[] nums) {
            // Build heap operation: heapify all nodes except leaves
            for (int i = nums.length / 2 - 1; i >= 0; i--) {
                siftDown(nums, nums.length, i);
            }
            // Extract the largest element from the heap and repeat for n-1 rounds
            for (int i = nums.length - 1; i > 0; i--) {
                // Delete node
                int tmp = nums[0];
                nums[0] = nums[i];
                nums[i] = tmp;
                // Start heapifying the root node, from top to bottom
                siftDown(nums, i, 0);
            }
        }
    
        public static void main(String[] args) {
            int[] nums = { 4, 1, 3, 1, 5, 2 };
            heapSort(nums);
            System.out.println("After heap sort completes, nums = " + Arrays.toString(nums));
        }
    }
    ```
=== "C#"
    ```csharp title="heap_sort.cs"
    public class heap_sort {
        /* Heap length is n, start heapifying node i, from top to bottom */
        void SiftDown(int[] nums, int n, int i) {
            while (true) {
                // If node i is largest or indices l, r are out of bounds, no need to continue heapify, break
                int l = 2 * i + 1;
                int r = 2 * i + 2;
                int ma = i;
                if (l < n && nums[l] > nums[ma])
                    ma = l;
                if (r < n && nums[r] > nums[ma])
                    ma = r;
                // Swap two nodes
                if (ma == i)
                    break;
                // Swap two nodes
                (nums[ma], nums[i]) = (nums[i], nums[ma]);
                // Loop downwards heapification
                i = ma;
            }
        }
    
        /* Heap sort */
        void HeapSort(int[] nums) {
            // Build heap operation: heapify all nodes except leaves
            for (int i = nums.Length / 2 - 1; i >= 0; i--) {
                SiftDown(nums, nums.Length, i);
            }
            // Extract the largest element from the heap and repeat for n-1 rounds
            for (int i = nums.Length - 1; i > 0; i--) {
                // Delete node
                (nums[i], nums[0]) = (nums[0], nums[i]);
                // Start heapifying the root node, from top to bottom
                SiftDown(nums, i, 0);
            }
        }
    
        [Test]
        public void Test() {
            int[] nums = [4, 1, 3, 1, 5, 2];
            HeapSort(nums);
            Console.WriteLine("After heap sort completes, nums = " + string.Join(" ", nums));
        }
    }
    ```
=== "Go"
    ```go title="heap_sort.go"
    func heapSort(nums *[]int) {
    	// Build heap operation: heapify all nodes except leaves
    	for i := len(*nums)/2 - 1; i >= 0; i-- {
    		siftDown(nums, len(*nums), i)
    	}
    	// Extract the largest element from the heap and repeat for n-1 rounds
    	for i := len(*nums) - 1; i > 0; i-- {
    		// Delete node
    		(*nums)[0], (*nums)[i] = (*nums)[i], (*nums)[0]
    		// Start heapifying the root node, from top to bottom
    		siftDown(nums, i, 0)
    	}
    }
    ```
=== "Swift"
    ```swift title="heap_sort.swift"
    func heapSort(nums: inout [Int]) {
        // Build heap operation: heapify all nodes except leaves
        for i in stride(from: nums.count / 2 - 1, through: 0, by: -1) {
            siftDown(nums: &nums, n: nums.count, i: i)
        }
        // Extract the largest element from the heap and repeat for n-1 rounds
        for i in nums.indices.dropFirst().reversed() {
            // Delete node
            nums.swapAt(0, i)
            // Start heapifying the root node, from top to bottom
            siftDown(nums: &nums, n: i, i: 0)
        }
    }
    ```
=== "JS"
    ```javascript title="heap_sort.js"
    function heapSort(nums) {
        // Build heap operation: heapify all nodes except leaves
        for (let i = Math.floor(nums.length / 2) - 1; i >= 0; i--) {
            siftDown(nums, nums.length, i);
        }
        // Extract the largest element from the heap and repeat for n-1 rounds
        for (let i = nums.length - 1; i > 0; i--) {
            // Delete node
            [nums[0], nums[i]] = [nums[i], nums[0]];
            // Start heapifying the root node, from top to bottom
            siftDown(nums, i, 0);
        }
    }
    ```
=== "TS"
    ```typescript title="heap_sort.ts"
    function heapSort(nums: number[]): void {
        // Build heap operation: heapify all nodes except leaves
        for (let i = Math.floor(nums.length / 2) - 1; i >= 0; i--) {
            siftDown(nums, nums.length, i);
        }
        // Extract the largest element from the heap and repeat for n-1 rounds
        for (let i = nums.length - 1; i > 0; i--) {
            // Delete node
            [nums[0], nums[i]] = [nums[i], nums[0]];
            // Start heapifying the root node, from top to bottom
            siftDown(nums, i, 0);
        }
    }
    ```
=== "Dart"
    ```dart title="heap_sort.dart"
    void heapSort(List<int> nums) {
      // Build heap operation: heapify all nodes except leaves
      for (int i = nums.length ~/ 2 - 1; i >= 0; i--) {
        siftDown(nums, nums.length, i);
      }
      // Extract the largest element from the heap and repeat for n-1 rounds
      for (int i = nums.length - 1; i > 0; i--) {
        // Delete node
        int tmp = nums[0];
        nums[0] = nums[i];
        nums[i] = tmp;
        // Start heapifying the root node, from top to bottom
        siftDown(nums, i, 0);
      }
    }
    ```
=== "Rust"
    ```rust title="heap_sort.rs"
    fn heap_sort(nums: &mut [i32]) {
        // Build heap operation: heapify all nodes except leaves
        for i in (0..nums.len() / 2).rev() {
            sift_down(nums, nums.len(), i);
        }
        // Extract the largest element from the heap and repeat for n-1 rounds
        for i in (1..nums.len()).rev() {
            // Delete node
            nums.swap(0, i);
            // Start heapifying the root node, from top to bottom
            sift_down(nums, i, 0);
        }
    }
    ```
=== "C"
    ```c title="heap_sort.c"
    void heapSort(int nums[], int n) {
        // Build heap operation: heapify all nodes except leaves
        for (int i = n / 2 - 1; i >= 0; --i) {
            siftDown(nums, n, i);
        }
        // Extract the largest element from the heap and repeat for n-1 rounds
        for (int i = n - 1; i > 0; --i) {
            // Delete node
            int tmp = nums[0];
            nums[0] = nums[i];
            nums[i] = tmp;
            // Start heapifying the root node, from top to bottom
            siftDown(nums, i, 0);
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="heap_sort.kt"
    fun heapSort(nums: IntArray) {
        // Build heap operation: heapify all nodes except leaves
        for (i in nums.size / 2 - 1 downTo 0) {
            siftDown(nums, nums.size, i)
        }
        // Extract the largest element from the heap and repeat for n-1 rounds
        for (i in nums.size - 1 downTo 1) {
            // Delete node
            val temp = nums[0]
            nums[0] = nums[i]
            nums[i] = temp
            // Start heapifying the root node, from top to bottom
            siftDown(nums, i, 0)
        }
    }
    ```
=== "Ruby"
    ```ruby title="heap_sort.rb"
    ### Heap sort ###
    def heap_sort(nums)
      # Build heap operation: heapify all nodes except leaves
      (nums.length / 2 - 1).downto(0) do |i|
        sift_down(nums, nums.length, i)
      end
      # Extract the largest element from the heap and repeat for n-1 rounds
      (nums.length - 1).downto(1) do |i|
        # Delete node
        nums[0], nums[i] = nums[i], nums[0]
        # Start heapifying the root node, from top to bottom
        sift_down(nums, i, 0)
      end
    ```


## Đặc điểm thuật toán

- **Độ phức tạp về thời gian là $O(n \log n)$; Sắp xếp heap không thích ứng**: Quá trình xây dựng heap mất $O(n)$ thời gian. Việc trích xuất phần tử lớn nhất từ ​​heap mất $O(\log n)$ thời gian và việc này được lặp lại với tổng số vòng $n - 1$.
- **Độ phức tạp của không gian là $O(1)$; Sắp xếp heap được thực hiện đúng chỗ**: Một vài biến con trỏ sử dụng khoảng trắng $O(1)$. Hoán đổi phần tử và heapify đều được thực hiện trên mảng ban đầu.
- **Sắp xếp không ổn định**: Khi hoán đổi phần tử trên cùng và phần tử dưới cùng của heap, vị trí tương đối của các phần tử bằng nhau có thể thay đổi.
