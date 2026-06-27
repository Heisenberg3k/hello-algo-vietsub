# Sắp xếp bong bóng

<u>Bubble sort</u> sorts an array by continuously comparing and swapping adjacent elements. This process resembles bubbles rising from the bottom to the top, hence the name bubble sort.

Như minh họa trong hình bên dưới, quá trình sủi bọt có thể được mô phỏng bằng cách sử dụng hoán đổi phần tử: bắt đầu từ đầu ngoài cùng bên trái của mảng và di chuyển sang bên phải, so sánh từng cặp phần tử liền kề và nếu "phần tử bên trái > phần tử bên phải", hãy hoán đổi chúng. Sau khi quá trình duyệt hoàn tất, phần tử lớn nhất sẽ được chuyển đến đầu ngoài cùng bên phải của mảng.

=== "<1>"
    ![Simulating bubble sort using element swaps](bubble_sort.assets/bubble_operation_step1.png)

=== "<2>"
    ![bubble_operation_step2](bubble_sort.assets/bubble_operation_step2.png)

=== "<3>"
    ![bubble_operation_step3](bubble_sort.assets/bubble_operation_step3.png)

=== "<4>"
    ![bubble_operation_step4](bubble_sort.assets/bubble_operation_step4.png)

=== "<5>"
    ![bubble_operation_step5](bubble_sort.assets/bubble_operation_step5.png)

=== "<6>"
    ![bubble_operation_step6](bubble_sort.assets/bubble_operation_step6.png)

=== "<7>"
    ![bubble_operation_step7](bubble_sort.assets/bubble_operation_step7.png)

## Luồng thuật toán

Giả sử mảng có độ dài $n$. Các bước sắp xếp bong bóng được thể hiện trong hình dưới đây.

1. Đầu tiên, thực hiện "sủi bọt" trên các phần tử $n$, **hoán đổi phần tử lớn nhất của mảng về đúng vị trí của nó**.
2. Tiếp theo, thực hiện "sủi bọt" trên các phần tử $n - 1$ còn lại, **hoán đổi phần tử lớn thứ hai về đúng vị trí của nó**.
3. Và vân vân. Sau $n - 1$ vòng "sủi bọt", **các phần tử $n - 1$ lớn nhất đều đã được hoán đổi về đúng vị trí của chúng**.
4. Phần tử duy nhất còn lại phải là phần tử nhỏ nhất, không cần sắp xếp thì việc sắp xếp mảng hoàn tất.

![Bubble sort flow](bubble_sort.assets/bubble_sort_overview.png)

Mã ví dụ như sau:

=== "Python"
    ```python title="bubble_sort.py"
    def bubble_sort(nums: list[int]):
        """Bubble sort"""
        n = len(nums)
        # Outer loop: unsorted interval is [0, i]
        for i in range(n - 1, 0, -1):
            # Inner loop: swap the largest element in the unsorted interval [0, i] to the rightmost end of the interval
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    # Swap nums[j] and nums[j + 1]
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
    ```
=== "C++"
    ```cpp title="bubble_sort.cpp"
    void bubbleSort(vector<int> &nums) {
        // Outer loop: unsorted range is [0, i]
        for (int i = nums.size() - 1; i > 0; i--) {
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (int j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    // Swap nums[j] and nums[j + 1]
                    // Using std::swap() function here
                    swap(nums[j], nums[j + 1]);
                }
            }
        }
    }
    ```
=== "Java"
    ```java title="bubble_sort.java"
    public class bubble_sort {
        /* Bubble sort */
        static void bubbleSort(int[] nums) {
            // Outer loop: unsorted range is [0, i]
            for (int i = nums.length - 1; i > 0; i--) {
                // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
                for (int j = 0; j < i; j++) {
                    if (nums[j] > nums[j + 1]) {
                        // Swap nums[j] and nums[j + 1]
                        int tmp = nums[j];
                        nums[j] = nums[j + 1];
                        nums[j + 1] = tmp;
                    }
                }
            }
        }
    
        /* Bubble sort (flag optimization) */
        static void bubbleSortWithFlag(int[] nums) {
            // Outer loop: unsorted range is [0, i]
            for (int i = nums.length - 1; i > 0; i--) {
                boolean flag = false; // Initialize flag
                // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
                for (int j = 0; j < i; j++) {
                    if (nums[j] > nums[j + 1]) {
                        // Swap nums[j] and nums[j + 1]
                        int tmp = nums[j];
                        nums[j] = nums[j + 1];
                        nums[j + 1] = tmp;
                        flag = true; // Record element swap
                    }
                }
                if (!flag)
                    break; // No elements were swapped in this round of "bubbling", exit directly
            }
        }
    
        public static void main(String[] args) {
            int[] nums = { 4, 1, 3, 1, 5, 2 };
            bubbleSort(nums);
            System.out.println("After bubble sort completes, nums = " + Arrays.toString(nums));
    
            int[] nums1 = { 4, 1, 3, 1, 5, 2 };
            bubbleSortWithFlag(nums1);
            System.out.println("After bubble sort completes, nums1 = " + Arrays.toString(nums1));
        }
    }
    ```
=== "C#"
    ```csharp title="bubble_sort.cs"
    public class bubble_sort {
        /* Bubble sort */
        void BubbleSort(int[] nums) {
            // Outer loop: unsorted range is [0, i]
            for (int i = nums.Length - 1; i > 0; i--) {
                // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
                for (int j = 0; j < i; j++) {
                    if (nums[j] > nums[j + 1]) {
                        // Swap nums[j] and nums[j + 1]
                        (nums[j + 1], nums[j]) = (nums[j], nums[j + 1]);
                    }
                }
            }
        }
    
        /* Bubble sort (flag optimization) */
        void BubbleSortWithFlag(int[] nums) {
            // Outer loop: unsorted range is [0, i]
            for (int i = nums.Length - 1; i > 0; i--) {
                bool flag = false; // Initialize flag
                // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
                for (int j = 0; j < i; j++) {
                    if (nums[j] > nums[j + 1]) {
                        // Swap nums[j] and nums[j + 1]
                        (nums[j + 1], nums[j]) = (nums[j], nums[j + 1]);
                        flag = true;  // Record element swap
                    }
                }
                if (!flag) break;     // No elements were swapped in this round of "bubbling", exit directly
            }
        }
    
        [Test]
        public void Test() {
            int[] nums = [4, 1, 3, 1, 5, 2];
            BubbleSort(nums);
            Console.WriteLine("After bubble sort, nums = " + string.Join(",", nums));
    
            int[] nums1 = [4, 1, 3, 1, 5, 2];
            BubbleSortWithFlag(nums1);
            Console.WriteLine("After bubble sort completes, nums1 = " + string.Join(",", nums1));
        }
    }
    ```
=== "Go"
    ```go title="bubble_sort.go"
    func bubbleSort(nums []int) {
    	// Outer loop: unsorted range is [0, i]
    	for i := len(nums) - 1; i > 0; i-- {
    		// Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
    		for j := 0; j < i; j++ {
    			if nums[j] > nums[j+1] {
    				// Swap nums[j] and nums[j + 1]
    				nums[j], nums[j+1] = nums[j+1], nums[j]
    			}
    		}
    	}
    }
    ```
=== "Swift"
    ```swift title="bubble_sort.swift"
    func bubbleSort(nums: inout [Int]) {
        // Outer loop: unsorted range is [0, i]
        for i in nums.indices.dropFirst().reversed() {
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for j in 0 ..< i {
                if nums[j] > nums[j + 1] {
                    // Swap nums[j] and nums[j + 1]
                    nums.swapAt(j, j + 1)
                }
            }
        }
    }
    ```
=== "JS"
    ```javascript title="bubble_sort.js"
    function bubbleSort(nums) {
        // Outer loop: unsorted range is [0, i]
        for (let i = nums.length - 1; i > 0; i--) {
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (let j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    // Swap nums[j] and nums[j + 1]
                    let tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                }
            }
        }
    }
    ```
=== "TS"
    ```typescript title="bubble_sort.ts"
    function bubbleSort(nums: number[]): void {
        // Outer loop: unsorted range is [0, i]
        for (let i = nums.length - 1; i > 0; i--) {
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (let j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    // Swap nums[j] and nums[j + 1]
                    let tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                }
            }
        }
    }
    ```
=== "Dart"
    ```dart title="bubble_sort.dart"
    void bubbleSort(List<int> nums) {
      // Outer loop: unsorted range is [0, i]
      for (int i = nums.length - 1; i > 0; i--) {
        // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
        for (int j = 0; j < i; j++) {
          if (nums[j] > nums[j + 1]) {
            // Swap nums[j] and nums[j + 1]
            int tmp = nums[j];
            nums[j] = nums[j + 1];
            nums[j + 1] = tmp;
          }
        }
      }
    }
    ```
=== "Rust"
    ```rust title="bubble_sort.rs"
    fn bubble_sort(nums: &mut [i32]) {
        // Outer loop: unsorted range is [0, i]
        for i in (1..nums.len()).rev() {
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for j in 0..i {
                if nums[j] > nums[j + 1] {
                    // Swap nums[j] and nums[j + 1]
                    nums.swap(j, j + 1);
                }
            }
        }
    }
    ```
=== "C"
    ```c title="bubble_sort.c"
    void bubbleSort(int nums[], int size) {
        // Outer loop: unsorted range is [0, i]
        for (int i = size - 1; i > 0; i--) {
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (int j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                }
            }
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="bubble_sort.kt"
    fun bubbleSort(nums: IntArray) {
        // Outer loop: unsorted range is [0, i]
        for (i in nums.size - 1 downTo 1) {
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (j in 0..<i) {
                if (nums[j] > nums[j + 1]) {
                    // Swap nums[j] and nums[j + 1]
                    val temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
                }
            }
        }
    }
    ```
=== "Ruby"
    ```ruby title="bubble_sort.rb"
    ### Bubble sort ###
    def bubble_sort(nums)
      n = nums.length
      # Outer loop: unsorted range is [0, i]
      for i in (n - 1).downto(1)
        # Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
        for j in 0...i
          if nums[j] > nums[j + 1]
            # Swap nums[j] and nums[j + 1]
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
          end
        end
      end
    ```


## Tối ưu hóa hiệu quả

Chúng ta có thể quan sát thấy rằng nếu không có sự hoán đổi nào xảy ra trong một vòng "sủi bọt", thì mảng đã được sắp xếp và thuật toán có thể trả về ngay lập tức. Do đó, chúng ta có thể thêm cờ `flag` để phát hiện tình trạng này và chấm dứt ngay khi nó xảy ra.

Sau lần tối ưu hóa này, độ phức tạp về thời gian trong trường hợp xấu nhất và trường hợp trung bình của sắp xếp bong bóng vẫn là $O(n^2)$; tuy nhiên, khi mảng đầu vào đã được sắp xếp, độ phức tạp về thời gian trong trường hợp tốt nhất sẽ trở thành $O(n)$.

=== "Python"
    ```python title="bubble_sort.py"
    def bubble_sort_with_flag(nums: list[int]):
        """Bubble sort (flag optimization)"""
        n = len(nums)
        # Outer loop: unsorted interval is [0, i]
        for i in range(n - 1, 0, -1):
            flag = False  # Initialize flag
            # Inner loop: swap the largest element in the unsorted interval [0, i] to the rightmost end of the interval
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    # Swap nums[j] and nums[j + 1]
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True  # Record element swap
            if not flag:
                break  # No elements were swapped in this round of "bubbling", exit directly
    ```
=== "C++"
    ```cpp title="bubble_sort.cpp"
    void bubbleSortWithFlag(vector<int> &nums) {
        // Outer loop: unsorted range is [0, i]
        for (int i = nums.size() - 1; i > 0; i--) {
            bool flag = false; // Initialize flag
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (int j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    // Swap nums[j] and nums[j + 1]
                    // Using std::swap() function here
                    swap(nums[j], nums[j + 1]);
                    flag = true; // Record element swap
                }
            }
            if (!flag)
                break; // No elements were swapped in this round of "bubbling", exit directly
        }
    }
    ```
=== "Java"
    ```java title="bubble_sort.java"
    static void bubbleSortWithFlag(int[] nums) {
            // Outer loop: unsorted range is [0, i]
            for (int i = nums.length - 1; i > 0; i--) {
                boolean flag = false; // Initialize flag
                // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
                for (int j = 0; j < i; j++) {
                    if (nums[j] > nums[j + 1]) {
                        // Swap nums[j] and nums[j + 1]
                        int tmp = nums[j];
                        nums[j] = nums[j + 1];
                        nums[j + 1] = tmp;
                        flag = true; // Record element swap
                    }
                }
                if (!flag)
                    break; // No elements were swapped in this round of "bubbling", exit directly
            }
        }
    ```
=== "C#"
    ```csharp title="bubble_sort.cs"
    void BubbleSortWithFlag(int[] nums) {
            // Outer loop: unsorted range is [0, i]
            for (int i = nums.Length - 1; i > 0; i--) {
                bool flag = false; // Initialize flag
                // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
                for (int j = 0; j < i; j++) {
                    if (nums[j] > nums[j + 1]) {
                        // Swap nums[j] and nums[j + 1]
                        (nums[j + 1], nums[j]) = (nums[j], nums[j + 1]);
                        flag = true;  // Record element swap
                    }
                }
                if (!flag) break;     // No elements were swapped in this round of "bubbling", exit directly
            }
        }
    ```
=== "Go"
    ```go title="bubble_sort.go"
    func bubbleSortWithFlag(nums []int) {
    	// Outer loop: unsorted range is [0, i]
    	for i := len(nums) - 1; i > 0; i-- {
    		flag := false // Initialize flag
    		// Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
    		for j := 0; j < i; j++ {
    			if nums[j] > nums[j+1] {
    				// Swap nums[j] and nums[j + 1]
    				nums[j], nums[j+1] = nums[j+1], nums[j]
    				flag = true // Record element swap
    			}
    		}
    		if flag == false { // No elements were swapped in this round of "bubbling", exit directly
    			break
    		}
    	}
    }
    ```
=== "Swift"
    ```swift title="bubble_sort.swift"
    func bubbleSortWithFlag(nums: inout [Int]) {
        // Outer loop: unsorted range is [0, i]
        for i in nums.indices.dropFirst().reversed() {
            var flag = false // Initialize flag
            for j in 0 ..< i {
                if nums[j] > nums[j + 1] {
                    // Swap nums[j] and nums[j + 1]
                    nums.swapAt(j, j + 1)
                    flag = true // Record element swap
                }
            }
            if !flag { // No elements were swapped in this round of "bubbling", exit directly
                break
            }
        }
    }
    ```
=== "JS"
    ```javascript title="bubble_sort.js"
    function bubbleSortWithFlag(nums) {
        // Outer loop: unsorted range is [0, i]
        for (let i = nums.length - 1; i > 0; i--) {
            let flag = false; // Initialize flag
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (let j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    // Swap nums[j] and nums[j + 1]
                    let tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                    flag = true; // Record element swap
                }
            }
            if (!flag) break; // No elements were swapped in this round of "bubbling", exit directly
        }
    }
    ```
=== "TS"
    ```typescript title="bubble_sort.ts"
    function bubbleSortWithFlag(nums: number[]): void {
        // Outer loop: unsorted range is [0, i]
        for (let i = nums.length - 1; i > 0; i--) {
            let flag = false; // Initialize flag
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (let j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    // Swap nums[j] and nums[j + 1]
                    let tmp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = tmp;
                    flag = true; // Record element swap
                }
            }
            if (!flag) break; // No elements were swapped in this round of "bubbling", exit directly
        }
    }
    ```
=== "Dart"
    ```dart title="bubble_sort.dart"
    void bubbleSortWithFlag(List<int> nums) {
      // Outer loop: unsorted range is [0, i]
      for (int i = nums.length - 1; i > 0; i--) {
        bool flag = false; // Initialize flag
        // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
        for (int j = 0; j < i; j++) {
          if (nums[j] > nums[j + 1]) {
            // Swap nums[j] and nums[j + 1]
            int tmp = nums[j];
            nums[j] = nums[j + 1];
            nums[j + 1] = tmp;
            flag = true; // Record element swap
          }
        }
        if (!flag) break; // No elements were swapped in this round of "bubbling", exit directly
      }
    }
    ```
=== "Rust"
    ```rust title="bubble_sort.rs"
    fn bubble_sort_with_flag(nums: &mut [i32]) {
        // Outer loop: unsorted range is [0, i]
        for i in (1..nums.len()).rev() {
            let mut flag = false; // Initialize flag
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for j in 0..i {
                if nums[j] > nums[j + 1] {
                    // Swap nums[j] and nums[j + 1]
                    nums.swap(j, j + 1);
                    flag = true; // Record element swap
                }
            }
            if !flag {
                break; // No elements were swapped in this round of "bubbling", exit directly
            };
        }
    }
    ```
=== "C"
    ```c title="bubble_sort.c"
    void bubbleSortWithFlag(int nums[], int size) {
        // Outer loop: unsorted range is [0, i]
        for (int i = size - 1; i > 0; i--) {
            bool flag = false;
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (int j = 0; j < i; j++) {
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j];
                    nums[j] = nums[j + 1];
                    nums[j + 1] = temp;
                    flag = true;
                }
            }
            if (!flag)
                break;
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="bubble_sort.kt"
    fun bubbleSortWithFlag(nums: IntArray) {
        // Outer loop: unsorted range is [0, i]
        for (i in nums.size - 1 downTo 1) {
            var flag = false // Initialize flag
            // Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
            for (j in 0..<i) {
                if (nums[j] > nums[j + 1]) {
                    // Swap nums[j] and nums[j + 1]
                    val temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
                    flag = true // Record element swap
                }
            }
            if (!flag) break // No elements were swapped in this round of "bubbling", exit directly
        }
    }
    ```
=== "Ruby"
    ```ruby title="bubble_sort.rb"
    ### Bubble sort (flag optimization) ###
    def bubble_sort_with_flag(nums)
      n = nums.length
      # Outer loop: unsorted range is [0, i]
      for i in (n - 1).downto(1)
        flag = false # Initialize flag
    
        # Inner loop: swap the largest element in the unsorted range [0, i] to the rightmost end of that range
        for j in 0...i
          if nums[j] > nums[j + 1]
            # Swap nums[j] and nums[j + 1]
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            flag = true # Record element swap
          end
        end
    
        break unless flag # No elements were swapped in this round of "bubbling", exit directly
      end
    ```


## Đặc điểm thuật toán

- **Độ phức tạp về thời gian là $O(n^2)$; thích ứng**: Trong các vòng "sủi bọt" liên tiếp, phần duyệt của mảng có độ dài $n - 1$, $n - 2$, $\dots$, $2$, $1$, với tổng độ dài là $(n - 1) n / 2$. Sau khi giới thiệu tính năng tối ưu hóa `flag`, độ phức tạp về thời gian trong trường hợp tốt nhất có thể đạt tới $O(n)$.
- **Độ phức tạp về không gian của $O(1)$, sắp xếp tại chỗ**: Con trỏ $i$ và $j$ sử dụng một lượng không gian bổ sung không đổi.
- **Sắp xếp ổn định**: Các phần tử bằng nhau không bị hoán đổi trong quá trình "sủi bọt".
