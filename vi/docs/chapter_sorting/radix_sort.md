# Sắp xếp cơ số

Phần trước đã giới thiệu cách sắp xếp đếm, phù hợp khi số lượng phần tử $n$ lớn nhưng phạm vi giá trị $m$ nhỏ. Giả sử chúng ta cần sắp xếp $n = 10^6$ ID sinh viên, mỗi ID là một số có 8 chữ số. Khi đó phạm vi giá trị $m = 10^8$ là rất lớn. Sử dụng phương pháp sắp xếp đếm sẽ yêu cầu một lượng lớn bộ nhớ, trong khi phương pháp sắp xếp cơ số sẽ tránh được vấn đề này.

<u>Radix sort</u> is based on the same core idea as counting sort: it also sorts by counting occurrences. Building on this, radix sort exploits the positional relationship among digits and sorts them one digit at a time to obtain the final result.

## Luồng thuật toán

Lấy dữ liệu ID sinh viên làm ví dụ, giả sử chữ số thấp nhất là chữ số thứ $1$ và chữ số cao nhất là chữ số thứ $8$. Luồng sắp xếp cơ số được thể hiện trong hình bên dưới.

1. Khởi tạo chữ số $k = 1$.
2. Thực hiện "sắp xếp đếm" trên chữ số thứ $k$ của mã số học sinh. Sau khi hoàn thành, dữ liệu sẽ được sắp xếp từ nhỏ nhất đến lớn nhất theo chữ số thứ $k$.
3. Tăng $k$ lên $1$, sau đó quay lại bước `2.` và tiếp tục lặp lại cho đến khi tất cả các chữ số được sắp xếp, lúc đó quá trình kết thúc.

![Radix sort algorithm flow](radix_sort.assets/radix_sort_overview.png)

Tiếp theo, chúng ta hãy xem mã. Đối với một số $x$ trong cơ số $d$, $k$chữ số thứ $x_k$ của nó có thể thu được bằng công thức sau:

$$
x_k = \lfloor\frac{x}{d^{k-1}}\rfloor \bmod d
$$

Ở đây, $\lfloor a \rfloor$ biểu thị việc làm tròn số dấu phẩy động $a$ xuống và $\bmod \: d$ biểu thị việc lấy modulo $d$ còn lại. Đối với dữ liệu ID sinh viên, $d = 10$ và $k \in [1, 8]$.

Ngoài ra, chúng ta cần sửa đổi một chút mã sắp xếp đếm để sắp xếp nó dựa trên chữ số thứ $k$ của số:

=== "Python"
    ```python title="radix_sort.py"
    def radix_sort(nums: list[int]):
        """Radix sort"""
        # Get the maximum element of the array, used to determine the maximum number of digits
        m = max(nums)
        # Traverse from the lowest to the highest digit
        exp = 1
        while exp <= m:
            # Perform counting sort on the k-th digit of array elements
            # k = 1 -> exp = 1
            # k = 2 -> exp = 10
            # i.e., exp = 10^(k-1)
            counting_sort_digit(nums, exp)
            exp *= 10
    ```
=== "C++"
    ```cpp title="radix_sort.cpp"
    void radixSort(vector<int> &nums) {
        // Get the maximum element of the array, used to determine the maximum number of digits
        int m = *max_element(nums.begin(), nums.end());
        // Traverse from the lowest to the highest digit
        for (int exp = 1; exp <= m; exp *= 10)
            // Perform counting sort on the k-th digit of array elements
            // k = 1 -> exp = 1
            // k = 2 -> exp = 10
            // i.e., exp = 10^(k-1)
            countingSortDigit(nums, exp);
    }
    ```
=== "Java"
    ```java title="radix_sort.java"
    public class radix_sort {
        /* Get the k-th digit of element num, where exp = 10^(k-1) */
        static int digit(int num, int exp) {
            // Passing exp instead of k can avoid repeated expensive exponentiation here
            return (num / exp) % 10;
        }
    
        /* Counting sort (based on nums k-th digit) */
        static void countingSortDigit(int[] nums, int exp) {
            // Decimal digit range is 0~9, therefore need a bucket array of length 10
            int[] counter = new int[10];
            int n = nums.length;
            // Count the occurrence of digits 0~9
            for (int i = 0; i < n; i++) {
                int d = digit(nums[i], exp); // Get the k-th digit of nums[i], noted as d
                counter[d]++;                // Count the occurrence of digit d
            }
            // Calculate prefix sum, converting "occurrence count" into "array index"
            for (int i = 1; i < 10; i++) {
                counter[i] += counter[i - 1];
            }
            // Traverse in reverse, based on bucket statistics, place each element into res
            int[] res = new int[n];
            for (int i = n - 1; i >= 0; i--) {
                int d = digit(nums[i], exp);
                int j = counter[d] - 1; // Get the index j for d in the array
                res[j] = nums[i];       // Place the current element at index j
                counter[d]--;           // Decrease the count of d by 1
            }
            // Use result to overwrite the original array nums
            for (int i = 0; i < n; i++)
                nums[i] = res[i];
        }
    
        /* Radix sort */
        static void radixSort(int[] nums) {
            // Get the maximum element of the array, used to determine the maximum number of digits
            int m = Integer.MIN_VALUE;
            for (int num : nums)
                if (num > m)
                    m = num;
            // Traverse from the lowest to the highest digit
            for (int exp = 1; exp <= m; exp *= 10) {
                // Perform counting sort on the k-th digit of array elements
                // k = 1 -> exp = 1
                // k = 2 -> exp = 10
                // i.e., exp = 10^(k-1)
                countingSortDigit(nums, exp);
            }
        }
    
        public static void main(String[] args) {
            // Radix sort
            int[] nums = { 10546151, 35663510, 42865989, 34862445, 81883077,
                           88906420, 72429244, 30524779, 82060337, 63832996 };
            radixSort(nums);
            System.out.println("After radix sort completes, nums = " + Arrays.toString(nums));
        }
    }
    ```
=== "C#"
    ```csharp title="radix_sort.cs"
    public class radix_sort {
        /* Get the k-th digit of element num, where exp = 10^(k-1) */
        int Digit(int num, int exp) {
            // Passing exp instead of k can avoid repeated expensive exponentiation here
            return (num / exp) % 10;
        }
    
        /* Counting sort (based on nums k-th digit) */
        void CountingSortDigit(int[] nums, int exp) {
            // Decimal digit range is 0~9, therefore need a bucket array of length 10
            int[] counter = new int[10];
            int n = nums.Length;
            // Count the occurrence of digits 0~9
            for (int i = 0; i < n; i++) {
                int d = Digit(nums[i], exp); // Get the k-th digit of nums[i], noted as d
                counter[d]++;                // Count the occurrence of digit d
            }
            // Calculate prefix sum, converting "occurrence count" into "array index"
            for (int i = 1; i < 10; i++) {
                counter[i] += counter[i - 1];
            }
            // Traverse in reverse, based on bucket statistics, place each element into res
            int[] res = new int[n];
            for (int i = n - 1; i >= 0; i--) {
                int d = Digit(nums[i], exp);
                int j = counter[d] - 1; // Get the index j for d in the array
                res[j] = nums[i];       // Place the current element at index j
                counter[d]--;           // Decrease the count of d by 1
            }
            // Use result to overwrite the original array nums
            for (int i = 0; i < n; i++) {
                nums[i] = res[i];
            }
        }
    
        /* Radix sort */
        void RadixSort(int[] nums) {
            // Get the maximum element of the array, used to determine the maximum number of digits
            int m = int.MinValue;
            foreach (int num in nums) {
                if (num > m) m = num;
            }
            // Traverse from the lowest to the highest digit
            for (int exp = 1; exp <= m; exp *= 10) {
                // Perform counting sort on the k-th digit of array elements
                // k = 1 -> exp = 1
                // k = 2 -> exp = 10
                // i.e., exp = 10^(k-1)
                CountingSortDigit(nums, exp);
            }
        }
    
        [Test]
        public void Test() {
            // Radix sort
            int[] nums = [ 10546151, 35663510, 42865989, 34862445, 81883077,
                88906420, 72429244, 30524779, 82060337, 63832996 ];
            RadixSort(nums);
            Console.WriteLine("After radix sort completes, nums = " + string.Join(" ", nums));
        }
    }
    ```
=== "Go"
    ```go title="radix_sort.go"
    func radixSort(nums []int) {
    	// Get the maximum element of the array, used to determine the maximum number of digits
    	max := math.MinInt
    	for _, num := range nums {
    		if num > max {
    			max = num
    		}
    	}
    	// Traverse from the lowest to the highest digit
    	for exp := 1; max >= exp; exp *= 10 {
    		// Perform counting sort on the k-th digit of array elements
    		// k = 1 -> exp = 1
    		// k = 2 -> exp = 10
    		// i.e., exp = 10^(k-1)
    		countingSortDigit(nums, exp)
    	}
    }
    ```
=== "Swift"
    ```swift title="radix_sort.swift"
    func radixSort(nums: inout [Int]) {
        // Get the maximum element of the array, used to determine the maximum number of digits
        var m = Int.min
        for num in nums {
            if num > m {
                m = num
            }
        }
        // Traverse from the lowest to the highest digit
        for exp in sequence(first: 1, next: { m >= ($0 * 10) ? $0 * 10 : nil }) {
            // Perform counting sort on the k-th digit of array elements
            // k = 1 -> exp = 1
            // k = 2 -> exp = 10
            // i.e., exp = 10^(k-1)
            countingSortDigit(nums: &nums, exp: exp)
        }
    }
    ```
=== "JS"
    ```javascript title="radix_sort.js"
    function radixSort(nums) {
        // Get the maximum element of the array, used to determine the maximum number of digits
        let m = Math.max(... nums);
        // Traverse from the lowest to the highest digit
        for (let exp = 1; exp <= m; exp *= 10) {
            // Perform counting sort on the k-th digit of array elements
            // k = 1 -> exp = 1
            // k = 2 -> exp = 10
            // i.e., exp = 10^(k-1)
            countingSortDigit(nums, exp);
        }
    }
    ```
=== "TS"
    ```typescript title="radix_sort.ts"
    function radixSort(nums: number[]): void {
        // Get the maximum element of the array, used to determine the maximum number of digits
        let m: number = Math.max(... nums);
        // Traverse from the lowest to the highest digit
        for (let exp = 1; exp <= m; exp *= 10) {
            // Perform counting sort on the k-th digit of array elements
            // k = 1 -> exp = 1
            // k = 2 -> exp = 10
            // i.e., exp = 10^(k-1)
            countingSortDigit(nums, exp);
        }
    }
    ```
=== "Dart"
    ```dart title="radix_sort.dart"
    void radixSort(List<int> nums) {
      // Get the maximum element of the array, used to determine the maximum number of digits
      // In Dart, int length is 64 bits
      int m = -1 << 63;
      for (int _num in nums) if (_num > m) m = _num;
      // Traverse from the lowest to the highest digit
      for (int exp = 1; exp <= m; exp *= 10)
        // Perform counting sort on the k-th digit of array elements
        // k = 1 -> exp = 1
        // k = 2 -> exp = 10
        // i.e., exp = 10^(k-1)
        countingSortDigit(nums, exp);
    }
    ```
=== "Rust"
    ```rust title="radix_sort.rs"
    fn radix_sort(nums: &mut [i32]) {
        // Get the maximum element of the array, used to determine the maximum number of digits
        let m = *nums.into_iter().max().unwrap();
        // Traverse from the lowest to the highest digit
        let mut exp = 1;
        while exp <= m {
            counting_sort_digit(nums, exp);
            exp *= 10;
        }
    }
    ```
=== "C"
    ```c title="radix_sort.c"
    void radixSort(int nums[], int size) {
        // Get the maximum element of the array, used to determine the maximum number of digits
        int max = INT32_MIN;
        for (int i = 0; i < size; i++) {
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        // Traverse from the lowest to the highest digit
        for (int exp = 1; max >= exp; exp *= 10)
            // Perform counting sort on the k-th digit of array elements
            // k = 1 -> exp = 1
            // k = 2 -> exp = 10
            // i.e., exp = 10^(k-1)
            countingSortDigit(nums, size, exp);
    }
    ```
=== "Kotlin"
    ```kotlin title="radix_sort.kt"
    fun radixSort(nums: IntArray) {
        // Get the maximum element of the array, used to determine the maximum number of digits
        var m = Int.MIN_VALUE
        for (num in nums) if (num > m) m = num
        var exp = 1
        // Traverse from the lowest to the highest digit
        while (exp <= m) {
            // Perform counting sort on the k-th digit of array elements
            // k = 1 -> exp = 1
            // k = 2 -> exp = 10
            // i.e., exp = 10^(k-1)
            countingSortDigit(nums, exp)
            exp *= 10
        }
    }
    ```
=== "Ruby"
    ```ruby title="radix_sort.rb"
    ### Radix sort ###
    def radix_sort(nums)
      # Get the maximum element of the array, used to determine the maximum number of digits
      m = nums.max
      # Traverse from the lowest to the highest digit
      exp = 1
      while exp <= m
        # Perform counting sort on the k-th digit of array elements
        # k = 1 -> exp = 1
        # k = 2 -> exp = 10
        # i.e., exp = 10^(k-1)
        counting_sort_digit(nums, exp)
        exp *= 10
      end
    ```


!!! câu hỏi "Tại sao bắt đầu sắp xếp từ chữ số thấp nhất?"

Trong các lần sắp xếp liên tiếp, lần sắp xếp sau sẽ ghi đè kết quả của lần sắp xếp trước đó. Ví dụ: nếu lần đầu tiên mang lại $a < b$ nhưng lần thứ hai mang lại $a > b$, thì kết quả của lần thứ hai sẽ chiếm ưu thế. Vì các chữ số có thứ tự cao hơn có mức độ ưu tiên cao hơn các chữ số có thứ tự thấp hơn nên chúng ta nên sắp xếp các chữ số có thứ tự thấp hơn trước rồi đến các chữ số có thứ tự cao hơn.

## Đặc điểm thuật toán

So với sắp xếp đếm, sắp xếp cơ số phù hợp với phạm vi giá trị lớn hơn, **nhưng chỉ khi dữ liệu có thể được biểu diễn bằng một số chữ số cố định và số chữ số đó không quá lớn**. Ví dụ: các số có dấu phẩy động không phù hợp lắm với kiểu sắp xếp cơ số vì số lượng chữ số $k$ có thể quá lớn, có khả năng dẫn đến độ phức tạp về thời gian $O(nk) \gg O(n^2)$.

- **Độ phức tạp về thời gian của $O(nk)$, sắp xếp không thích ứng**: Đặt số lượng mục là $n$, đặt các giá trị được biểu diễn dưới dạng cơ sở $d$ và đặt số chữ số tối đa là $k$. Việc sắp xếp đếm trên một chữ số mất $O(n + d)$ thời gian, do đó việc sắp xếp tất cả $k$ chữ số mất $O((n + d)k)$ thời gian. Trong thực tế, $d$ và $k$ thường tương đối nhỏ, do đó độ phức tạp về thời gian tổng thể đạt tới $O(n)$.
- **Độ phức tạp về không gian của $O(n + d)$, sắp xếp không tại chỗ**: Giống như sắp xếp đếm, sắp xếp cơ số yêu cầu các mảng phụ `res` và `counter` có độ dài $n$ và $d$.
- **Sắp xếp ổn định**: Khi sắp xếp đếm ổn định, sắp xếp cơ số cũng ổn định; khi sắp xếp đếm không ổn định, sắp xếp cơ số không thể đảm bảo kết quả sắp xếp chính xác.
