# Sắp xếp chèn

<u>Insertion sort</u> is a simple sorting algorithm that works very similarly to the process of manually sorting a deck of cards.

Cụ thể, chúng tôi chọn một phần tử cơ sở từ phần chưa được sắp xếp, so sánh từng phần tử đó với các phần tử trong phần được sắp xếp ở bên trái của nó và chèn nó vào đúng vị trí.

Hình dưới đây minh họa cách chèn một phần tử vào một mảng. Đặt phần tử cơ sở là `base`. Chúng ta cần dịch chuyển tất cả các phần tử giữa chỉ mục đích và `base` một vị trí sang phải, sau đó gán `base` cho chỉ mục đích.

![Single insertion operation](insertion_sort.assets/insertion_operation.png)

## Luồng thuật toán

Luồng sắp xếp chèn tổng thể được hiển thị trong hình bên dưới.

1. Ban đầu, phần tử đầu tiên của mảng đã được sắp xếp.
2. Chọn phần tử thứ hai của mảng làm `base`, và sau khi chèn nó vào đúng vị trí, **2 phần tử đầu tiên của mảng được sắp xếp**.
3. Chọn phần tử thứ ba làm `base`, và sau khi chèn nó vào đúng vị trí, **3 phần tử đầu tiên của mảng được sắp xếp**.
4. Và vân vân. Ở vòng cuối cùng, chọn phần tử cuối cùng làm `base` và sau khi chèn nó vào đúng vị trí, **tất cả các phần tử được sắp xếp**.

![Insertion sort flow](insertion_sort.assets/insertion_sort_overview.png)

Mã ví dụ như sau:

=== "Python"
    ```python title="insertion_sort.py"
    def insertion_sort(nums: list[int]):
        """Insertion sort"""
        # Outer loop: sorted interval is [0, i-1]
        for i in range(1, len(nums)):
            base = nums[i]
            j = i - 1
            # Inner loop: insert base into the correct position within the sorted interval [0, i-1]
            while j >= 0 and nums[j] > base:
                nums[j + 1] = nums[j]  # Move nums[j] to the right by one position
                j -= 1
            nums[j + 1] = base  # Assign base to the correct position
    ```
=== "C++"
    ```cpp title="insertion_sort.cpp"
    void insertionSort(vector<int> &nums) {
        // Outer loop: sorted interval is [0, i-1]
        for (int i = 1; i < nums.size(); i++) {
            int base = nums[i], j = i - 1;
            // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
            while (j >= 0 && nums[j] > base) {
                nums[j + 1] = nums[j]; // Move nums[j] to the right by one position
                j--;
            }
            nums[j + 1] = base; // Assign base to the correct position
        }
    }
    ```
=== "Java"
    ```java title="insertion_sort.java"
    public class insertion_sort {
        /* Insertion sort */
        static void insertionSort(int[] nums) {
            // Outer loop: sorted interval is [0, i-1]
            for (int i = 1; i < nums.length; i++) {
                int base = nums[i], j = i - 1;
                // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
                while (j >= 0 && nums[j] > base) {
                    nums[j + 1] = nums[j]; // Move nums[j] to the right by one position
                    j--;
                }
                nums[j + 1] = base;        // Assign base to the correct position
            }
        }
    
        public static void main(String[] args) {
            int[] nums = { 4, 1, 3, 1, 5, 2 };
            insertionSort(nums);
            System.out.println("After insertion sort completes, nums = " + Arrays.toString(nums));
        }
    }
    ```
=== "C#"
    ```csharp title="insertion_sort.cs"
    public class insertion_sort {
        /* Insertion sort */
        void InsertionSort(int[] nums) {
            // Outer loop: sorted interval is [0, i-1]
            for (int i = 1; i < nums.Length; i++) {
                int bas = nums[i], j = i - 1;
                // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
                while (j >= 0 && nums[j] > bas) {
                    nums[j + 1] = nums[j]; // Move nums[j] to the right by one position
                    j--;
                }
                nums[j + 1] = bas;         // Assign base to the correct position
            }
        }
    
        [Test]
        public void Test() {
            int[] nums = [4, 1, 3, 1, 5, 2];
            InsertionSort(nums);
            Console.WriteLine("After insertion sort completes, nums = " + string.Join(",", nums));
        }
    }
    ```
=== "Go"
    ```go title="insertion_sort.go"
    func insertionSort(nums []int) {
    	// Outer loop: sorted interval is [0, i-1]
    	for i := 1; i < len(nums); i++ {
    		base := nums[i]
    		j := i - 1
    		// Inner loop: insert base into the correct position within the sorted interval [0, i-1]
    		for j >= 0 && nums[j] > base {
    			nums[j+1] = nums[j] // Move nums[j] to the right by one position
    			j--
    		}
    		nums[j+1] = base // Assign base to the correct position
    	}
    }
    ```
=== "Swift"
    ```swift title="insertion_sort.swift"
    func insertionSort(nums: inout [Int]) {
        // Outer loop: sorted interval is [0, i-1]
        for i in nums.indices.dropFirst() {
            let base = nums[i]
            var j = i - 1
            // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
            while j >= 0, nums[j] > base {
                nums[j + 1] = nums[j] // Move nums[j] to the right by one position
                j -= 1
            }
            nums[j + 1] = base // Assign base to the correct position
        }
    }
    ```
=== "JS"
    ```javascript title="insertion_sort.js"
    function insertionSort(nums) {
        // Outer loop: sorted interval is [0, i-1]
        for (let i = 1; i < nums.length; i++) {
            let base = nums[i],
                j = i - 1;
            // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
            while (j >= 0 && nums[j] > base) {
                nums[j + 1] = nums[j]; // Move nums[j] to the right by one position
                j--;
            }
            nums[j + 1] = base; // Assign base to the correct position
        }
    }
    ```
=== "TS"
    ```typescript title="insertion_sort.ts"
    function insertionSort(nums: number[]): void {
        // Outer loop: sorted interval is [0, i-1]
        for (let i = 1; i < nums.length; i++) {
            const base = nums[i];
            let j = i - 1;
            // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
            while (j >= 0 && nums[j] > base) {
                nums[j + 1] = nums[j]; // Move nums[j] to the right by one position
                j--;
            }
            nums[j + 1] = base; // Assign base to the correct position
        }
    }
    ```
=== "Dart"
    ```dart title="insertion_sort.dart"
    void insertionSort(List<int> nums) {
      // Outer loop: sorted interval is [0, i-1]
      for (int i = 1; i < nums.length; i++) {
        int base = nums[i], j = i - 1;
        // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
        while (j >= 0 && nums[j] > base) {
          nums[j + 1] = nums[j]; // Move nums[j] to the right by one position
          j--;
        }
        nums[j + 1] = base; // Assign base to the correct position
      }
    }
    ```
=== "Rust"
    ```rust title="insertion_sort.rs"
    fn insertion_sort(nums: &mut [i32]) {
        // Outer loop: sorted interval is [0, i-1]
        for i in 1..nums.len() {
            let (base, mut j) = (nums[i], (i - 1) as i32);
            // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
            while j >= 0 && nums[j as usize] > base {
                nums[(j + 1) as usize] = nums[j as usize]; // Move nums[j] to the right by one position
                j -= 1;
            }
            nums[(j + 1) as usize] = base; // Assign base to the correct position
        }
    }
    ```
=== "C"
    ```c title="insertion_sort.c"
    void insertionSort(int nums[], int size) {
        // Outer loop: sorted interval is [0, i-1]
        for (int i = 1; i < size; i++) {
            int base = nums[i], j = i - 1;
            // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
            while (j >= 0 && nums[j] > base) {
                // Move nums[j] to the right by one position
                nums[j + 1] = nums[j];
                j--;
            }
            // Assign base to the correct position
            nums[j + 1] = base;
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="insertion_sort.kt"
    fun insertionSort(nums: IntArray) {
        // Outer loop: sorted elements are 1, 2, ..., n
        for (i in nums.indices) {
            val base = nums[i]
            var j = i - 1
            // Inner loop: insert base into the correct position within the sorted interval [0, i-1]
            while (j >= 0 && nums[j] > base) {
                nums[j + 1] = nums[j] // Move nums[j] to the right by one position
                j--
            }
            nums[j + 1] = base        // Assign base to the correct position
        }
    }
    ```
=== "Ruby"
    ```ruby title="insertion_sort.rb"
    ### Insertion sort ###
    def insertion_sort(nums)
      n = nums.length
      # Outer loop: sorted interval is [0, i-1]
      for i in 1...n
        base = nums[i]
        j = i - 1
        # Inner loop: insert base into the correct position within the sorted interval [0, i-1]
        while j >= 0 && nums[j] > base
          nums[j + 1] = nums[j] # Move nums[j] to the right by one position
          j -= 1
        end
        nums[j + 1] = base # Assign base to the correct position
      end
    ```


## Đặc điểm thuật toán

- **Độ phức tạp về thời gian của $O(n^2)$, sắp xếp thích ứng**: Trong trường hợp xấu nhất, các thao tác chèn yêu cầu lần lặp $n - 1$, $n-2$, $\dots$, $2$ và $1$, tổng cộng là $(n - 1) n / 2$, do đó độ phức tạp về thời gian là $O(n^2)$. Khi dữ liệu đã được sắp xếp, mỗi thao tác chèn sẽ kết thúc sớm. Khi mảng đầu vào được sắp xếp hoàn toàn, kiểu sắp xếp chèn đạt được độ phức tạp về thời gian trong trường hợp tốt nhất là $O(n)$.
- **Độ phức tạp về không gian của $O(1)$, sắp xếp tại chỗ**: Con trỏ $i$ và $j$ sử dụng một lượng không gian bổ sung không đổi.
- **Sắp xếp ổn định**: Trong quá trình chèn, chúng ta đặt các phần tử ở bên phải các phần tử bằng nhau nên thứ tự tương đối của chúng không thay đổi.

## Ưu điểm của sắp xếp chèn

Độ phức tạp về thời gian của sắp xếp chèn là $O(n^2)$, trong khi độ phức tạp về thời gian của sắp xếp nhanh, mà chúng ta sẽ tìm hiểu tiếp theo, là $O(n \log n)$. Mặc dù sắp xếp chèn có độ phức tạp về thời gian cao hơn, **nó thường nhanh hơn trên các tập dữ liệu nhỏ**.

Kết luận này tương tự như kết luận về việc áp dụng tìm kiếm tuyến tính và tìm kiếm nhị phân. Các thuật toán như sắp xếp nhanh, với độ phức tạp $O(n \log n)$, là các thuật toán sắp xếp chia để trị và thường liên quan đến các hoạt động nguyên thủy hơn. Khi tập dữ liệu nhỏ, các giá trị của $n^2$ và $n \log n$ tương đối gần nhau, do đó độ phức tạp tiệm cận không chiếm ưu thế; thay vào đó, số lượng thao tác nguyên thủy trong mỗi vòng trở thành yếu tố quyết định.

Trên thực tế, các hàm sắp xếp tích hợp của nhiều ngôn ngữ lập trình (chẳng hạn như Java) sử dụng tính năng sắp xếp chèn. Ý tưởng chung là: đối với các mảng lớn, hãy sử dụng các thuật toán sắp xếp chia để trị như sắp xếp nhanh; đối với mảng ngắn, hãy sử dụng tính năng sắp xếp chèn trực tiếp.

Mặc dù sắp xếp nổi bọt, sắp xếp lựa chọn và sắp xếp chèn đều có độ phức tạp về thời gian là $O(n^2)$, nhưng trong các tình huống thực tế, **sắp xếp chèn được sử dụng thường xuyên hơn đáng kể so với sắp xếp bong bóng và sắp xếp lựa chọn**, chủ yếu vì những lý do sau.

- Sắp xếp bong bóng được thực hiện thông qua hoán đổi phần tử, yêu cầu một biến tạm thời và bao gồm 3 thao tác nguyên thủy; sắp xếp chèn được thực hiện thông qua việc gán phần tử và chỉ yêu cầu 1 thao tác nguyên thủy. Do đó, **sắp xếp bong bóng thường có chi phí tính toán cao hơn so với sắp xếp chèn**.
- Sắp xếp lựa chọn có độ phức tạp về thời gian là $O(n^2)$ trong mọi trường hợp. **Nếu được cung cấp một tập hợp dữ liệu được sắp xếp một phần, sắp xếp chèn thường hiệu quả hơn sắp xếp chọn**.
- Sắp xếp lựa chọn không ổn định và không thể áp dụng cho sắp xếp đa cấp.
