# Mảng

<u>mảng</u> là cấu trúc dữ liệu tuyến tính lưu trữ các phần tử cùng loại trong không gian bộ nhớ liền kề. Vị trí của một phần tử trong mảng được gọi là <u>chỉ mục</u> của phần tử đó. Hình dưới đây minh họa các khái niệm chính và phương pháp lưu trữ của mảng.

![Array definition and storage method](array.assets/array_definition.png)

## Các thao tác mảng phổ biến

### Khởi tạo mảng

Chúng ta có thể chọn giữa hai phương pháp khởi tạo mảng dựa trên nhu cầu của mình: có hoặc không có giá trị ban đầu. Khi không có giá trị ban đầu nào được chỉ định, hầu hết các ngôn ngữ lập trình đều khởi tạo các phần tử mảng thành $0$:

=== "Trăn"

    ```python title="array.py"
    # Initialize array
    arr: list[int] = [0] * 5  # [ 0, 0, 0, 0, 0 ]
    nums: list[int] = [1, 3, 2, 5, 4]
    ```

=== "C++"

    ```cpp title="array.cpp"
    /* Initialize array */
    // Stored on stack
    int arr[5];
    int nums[5] = { 1, 3, 2, 5, 4 };
    // Stored on heap (requires manual memory release)
    int* arr1 = new int[5];
    int* nums1 = new int[5] { 1, 3, 2, 5, 4 };
    ```

=== "Java"

    ```java title="array.java"
    /* Initialize array */
    int[] arr = new int[5]; // { 0, 0, 0, 0, 0 }
    int[] nums = { 1, 3, 2, 5, 4 };
    ```

=== "C#"

    ```csharp title="array.cs"
    /* Initialize array */
    int[] arr = new int[5]; // [ 0, 0, 0, 0, 0 ]
    int[] nums = [1, 3, 2, 5, 4];
    ```

=== "Đi"

    ```go title="array.go"
    /* Initialize array */
    var arr [5]int
    // In Go, specifying length ([5]int) creates an array; not specifying length ([]int) creates a slice
    // Since Go's arrays are designed to have their length determined at compile time, only constants can be used to specify the length
    // For convenience in implementing the extend() method, slices are treated as arrays below
    nums := []int{1, 3, 2, 5, 4}
    ```

=== "Nhanh chóng"

    ```swift title="array.swift"
    /* Initialize array */
    let arr = Array(repeating: 0, count: 5) // [0, 0, 0, 0, 0]
    let nums = [1, 3, 2, 5, 4]
    ```

=== "JS"

    ```javascript title="array.js"
    /* Initialize array */
    var arr = new Array(5).fill(0);
    var nums = [1, 3, 2, 5, 4];
    ```

=== "TS"

    ```typescript title="array.ts"
    /* Initialize array */
    let arr: number[] = new Array(5).fill(0);
    let nums: number[] = [1, 3, 2, 5, 4];
    ```

=== "Phi tiêu"

    ```dart title="array.dart"
    /* Initialize array */
    List<int> arr = List.filled(5, 0); // [0, 0, 0, 0, 0]
    List<int> nums = [1, 3, 2, 5, 4];
    ```

=== "Rỉ sét"

    ```rust title="array.rs"
    /* Initialize array */
    let arr: [i32; 5] = [0; 5]; // [0, 0, 0, 0, 0]
    let slice: &[i32] = &[0; 5];
    // In Rust, specifying length ([i32; 5]) creates an array; not specifying length (&[i32]) creates a slice
    // Since Rust's arrays are designed to have their length determined at compile time, only constants can be used to specify the length
    // Vector is the type generally used as a dynamic array in Rust
    // For convenience in implementing the extend() method, vectors are treated as arrays below
    let nums: Vec<i32> = vec![1, 3, 2, 5, 4];
    ```

=== "C"

    ```c title="array.c"
    /* Initialize array */
    int arr[5] = { 0 }; // { 0, 0, 0, 0, 0 }
    int nums[5] = { 1, 3, 2, 5, 4 };
    ```

=== "Kotlin"

    ```kotlin title="array.kt"
    /* Initialize array */
    var arr = IntArray(5) // { 0, 0, 0, 0, 0 }
    var nums = intArrayOf(1, 3, 2, 5, 4)
    ```

=== "Ruby"

    ```ruby title="array.rb"
    # Initialize array
    arr = Array.new(5, 0)
    nums = [1, 3, 2, 5, 4]
    ```

??? pythontutor "Trực quan hóa mã"

https://pythontutor.com/render.html#code=%23%20%E5%88%9D%E5%A7%8B%E5%8C%96%E6%95%B0%E7% BB%84%0Aarr%20%3D%20%5B0%5D%20*%205%20%20%23%20%5B%200,%200,%200,%200,%200%20%5D%0Anums% 20%3D%20%5B1,%203,%202,%205,%204%5D&cumulative=false&curInstr=0&heapPrimitives=nvernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

### Truy cập các phần tử

Các phần tử mảng được lưu trữ trong không gian bộ nhớ liền kề, điều đó có nghĩa là việc tính toán địa chỉ bộ nhớ của các phần tử mảng rất dễ dàng. Cho địa chỉ bộ nhớ của mảng (địa chỉ bộ nhớ của phần tử đầu tiên) và chỉ mục của một phần tử, chúng ta có thể sử dụng công thức hiển thị trong hình bên dưới để tính địa chỉ bộ nhớ của phần tử và truy cập trực tiếp vào phần tử đó.

![Memory address calculation for array elements](array.assets/array_memory_location_calculation.png)

Quan sát hình trên, chúng ta thấy rằng phần tử đầu tiên của mảng có chỉ số là $0$, điều này có vẻ phản trực giác vì việc đếm từ $1$ sẽ tự nhiên hơn. Tuy nhiên, từ góc nhìn của công thức tính toán địa chỉ, **chỉ mục về cơ bản là phần chênh lệch so với địa chỉ bộ nhớ**. Độ lệch địa chỉ của phần tử đầu tiên là $0$, do đó, việc chỉ mục của nó là $0$ là hợp lý.

Việc truy cập các phần tử trong mảng có hiệu quả cao; chúng ta có thể truy cập ngẫu nhiên bất kỳ phần tử nào trong mảng trong thời gian $O(1)$.

=== "Python"
    ```python title="array.py"
    def random_access(nums: list[int]) -> int:
        """Random access to element"""
        # Randomly select a number from the interval [0, len(nums)-1]
        random_index = random.randint(0, len(nums) - 1)
        # Retrieve and return the random element
        random_num = nums[random_index]
        return random_num
    
    
    # Please note that Python's list is a dynamic array and can be extended directly
    # For learning purposes, this function treats the list as an array with immutable length
    ```
=== "C++"
    ```cpp title="array.cpp"
    int randomAccess(int *nums, int size) {
        // Randomly select a number from interval [0, size)
        int randomIndex = rand() % size;
        // Retrieve and return the random element
        int randomNum = nums[randomIndex];
        return randomNum;
    }
    ```
=== "Java"
    ```java title="array.java"
    static int randomAccess(int[] nums) {
            // Randomly select a number in the interval [0, nums.length)
            int randomIndex = ThreadLocalRandom.current().nextInt(0, nums.length);
            // Retrieve and return the random element
            int randomNum = nums[randomIndex];
            return randomNum;
        }
    ```
=== "C#"
    ```csharp title="array.cs"
    int RandomAccess(int[] nums) {
            Random random = new();
            // Randomly select a number in interval [0, nums.Length)
            int randomIndex = random.Next(nums.Length);
            // Retrieve and return the random element
            int randomNum = nums[randomIndex];
            return randomNum;
        }
    ```
=== "Go"
    ```go title="array.go"
    func randomAccess(nums []int) (randomNum int) {
    	// Randomly select a number in the interval [0, nums.length)
    	randomIndex := rand.Intn(len(nums))
    	// Retrieve and return the random element
    	randomNum = nums[randomIndex]
    	return
    }
    ```
=== "Swift"
    ```swift title="array.swift"
    func randomAccess(nums: [Int]) -> Int {
        // Randomly select a number in interval [0, nums.count)
        let randomIndex = nums.indices.randomElement()!
        // Retrieve and return the random element
        let randomNum = nums[randomIndex]
        return randomNum
    }
    ```
=== "JS"
    ```javascript title="array.js"
    function randomAccess(nums) {
        // Randomly select a number in the interval [0, nums.length)
        const random_index = Math.floor(Math.random() * nums.length);
        // Retrieve and return the random element
        const random_num = nums[random_index];
        return random_num;
    }
    ```
=== "TS"
    ```typescript title="array.ts"
    function randomAccess(nums: number[]): number {
        // Randomly select a number in the interval [0, nums.length)
        const random_index = Math.floor(Math.random() * nums.length);
        // Retrieve and return the random element
        const random_num = nums[random_index];
        return random_num;
    }
    ```
=== "Dart"
    ```dart title="array.dart"
    int randomAccess(List<int> nums) {
      // Randomly select a number in the interval [0, nums.length)
      int randomIndex = Random().nextInt(nums.length);
      // Retrieve and return the random element
      int randomNum = nums[randomIndex];
      return randomNum;
    }
    ```
=== "Rust"
    ```rust title="array.rs"
    fn random_access(nums: &[i32]) -> i32 {
        // Randomly select a number in interval [0, nums.len())
        let random_index = rand::thread_rng().gen_range(0..nums.len());
        // Retrieve and return the random element
        let random_num = nums[random_index];
        random_num
    }
    ```
=== "C"
    ```c title="array.c"
    int randomAccess(int *nums, int size) {
        // Randomly select a number from interval [0, size)
        int randomIndex = rand() % size;
        // Retrieve and return the random element
        int randomNum = nums[randomIndex];
        return randomNum;
    }
    ```
=== "Kotlin"
    ```kotlin title="array.kt"
    fun randomAccess(nums: IntArray): Int {
        // Randomly select a number in interval [0, nums.size)
        val randomIndex = ThreadLocalRandom.current().nextInt(0, nums.size)
        // Retrieve and return the random element
        val randomNum = nums[randomIndex]
        return randomNum
    }
    ```
=== "Ruby"
    ```ruby title="array.rb"
    ### Random access element ###
    def random_access(nums)
      # Randomly select a number in the interval [0, nums.length)
      random_index = Random.rand(0...nums.length)
    
      # Retrieve and return the random element
      nums[random_index]
    ```


### Chèn phần tử

Các phần tử mảng được đóng gói chặt chẽ với nhau trong bộ nhớ, không có khoảng trống giữa chúng để dành cho dữ liệu bổ sung. Như trong hình bên dưới, nếu muốn chèn một phần tử vào giữa mảng, chúng ta cần dịch chuyển tất cả các phần tử tiếp theo sang phải một vị trí rồi gán giá trị tại chỉ mục đó.

![Example of inserting an element into an array](array.assets/array_insert_element.png)

Điều đáng chú ý là vì độ dài của mảng là cố định nên việc chèn một phần tử chắc chắn sẽ đẩy phần tử cuối cùng ra khỏi mảng. Chúng ta sẽ để lại giải pháp cho vấn đề này để thảo luận trong chương "Danh sách".

=== "Python"
    ```python title="array.py"
    def insert(nums: list[int], num: int, index: int):
        """Insert element num at index index in the array"""
        # Move all elements at and after index index backward by one position
        for i in range(len(nums) - 1, index, -1):
            nums[i] = nums[i - 1]
        # Assign num to the element at index index
        nums[index] = num
    ```
=== "C++"
    ```cpp title="array.cpp"
    void insert(int *nums, int size, int num, int index) {
        // Move all elements at and after index index backward by one position
        for (int i = size - 1; i > index; i--) {
            nums[i] = nums[i - 1];
        }
        // Assign num to the element at index index
        nums[index] = num;
    }
    ```
=== "Java"
    ```java title="array.java"
    static void insert(int[] nums, int num, int index) {
            // Move all elements at and after index index backward by one position
            for (int i = nums.length - 1; i > index; i--) {
                nums[i] = nums[i - 1];
            }
            // Assign num to the element at index index
            nums[index] = num;
        }
    ```
=== "C#"
    ```csharp title="array.cs"
    void Insert(int[] nums, int num, int index) {
            // Move all elements at and after index index backward by one position
            for (int i = nums.Length - 1; i > index; i--) {
                nums[i] = nums[i - 1];
            }
            // Assign num to the element at index index
            nums[index] = num;
        }
    ```
=== "Go"
    ```go title="array.go"
    func insert(nums []int, num int, index int) {
    	// Move all elements at and after index index backward by one position
    	for i := len(nums) - 1; i > index; i-- {
    		nums[i] = nums[i-1]
    	}
    	// Assign num to the element at index index
    	nums[index] = num
    }
    ```
=== "Swift"
    ```swift title="array.swift"
    func insert(nums: inout [Int], num: Int, index: Int) {
        // Move all elements at and after index index backward by one position
        for i in nums.indices.dropFirst(index).reversed() {
            nums[i] = nums[i - 1]
        }
        // Assign num to the element at index index
        nums[index] = num
    }
    ```
=== "JS"
    ```javascript title="array.js"
    function insert(nums, num, index) {
        // Move all elements at and after index index backward by one position
        for (let i = nums.length - 1; i > index; i--) {
            nums[i] = nums[i - 1];
        }
        // Assign num to the element at index index
        nums[index] = num;
    }
    ```
=== "TS"
    ```typescript title="array.ts"
    function insert(nums: number[], num: number, index: number): void {
        // Move all elements at and after index index backward by one position
        for (let i = nums.length - 1; i > index; i--) {
            nums[i] = nums[i - 1];
        }
        // Assign num to the element at index index
        nums[index] = num;
    }
    ```
=== "Dart"
    ```dart title="array.dart"
    void insert(List<int> nums, int _num, int index) {
      // Move all elements at and after index index backward by one position
      for (var i = nums.length - 1; i > index; i--) {
        nums[i] = nums[i - 1];
      }
      // Assign _num to element at index
      nums[index] = _num;
    }
    ```
=== "Rust"
    ```rust title="array.rs"
    fn insert(nums: &mut [i32], num: i32, index: usize) {
        // Move all elements at and after index index backward by one position
        for i in (index + 1..nums.len()).rev() {
            nums[i] = nums[i - 1];
        }
        // Assign num to the element at index index
        nums[index] = num;
    }
    ```
=== "C"
    ```c title="array.c"
    void insert(int *nums, int size, int num, int index) {
        // Move all elements at and after index index backward by one position
        for (int i = size - 1; i > index; i--) {
            nums[i] = nums[i - 1];
        }
        // Assign num to the element at index index
        nums[index] = num;
    }
    ```
=== "Kotlin"
    ```kotlin title="array.kt"
    fun insert(nums: IntArray, num: Int, index: Int) {
        // Move all elements at and after index index backward by one position
        for (i in nums.size - 1 downTo index + 1) {
            nums[i] = nums[i - 1]
        }
        // Assign num to the element at index index
        nums[index] = num
    }
    ```
=== "Ruby"
    ```ruby title="array.rb"
    ### Insert element num at index in array ###
    def insert(nums, num, index)
      # Move all elements at and after index index backward by one position
      for i in (nums.length - 1).downto(index + 1)
        nums[i] = nums[i - 1]
      end
    
      # Assign num to the element at index index
      nums[index] = num
    ```


### Xóa phần tử

Tương tự, như trong hình bên dưới, để xóa phần tử tại chỉ mục $i$, chúng ta cần dịch chuyển tất cả các phần tử sau chỉ mục $i$ về phía trước một vị trí.

![Example of removing an element from an array](array.assets/array_remove_element.png)

Lưu ý rằng sau khi xóa xong, phần tử cuối cùng ban đầu không còn ý nghĩa nữa nên chúng ta không cần phải sửa đổi nó một cách rõ ràng.

=== "Python"
    ```python title="array.py"
    def remove(nums: list[int], index: int):
        """Remove the element at index index"""
        # Move all elements after index index forward by one position
        for i in range(index, len(nums) - 1):
            nums[i] = nums[i + 1]
    ```
=== "C++"
    ```cpp title="array.cpp"
    void remove(int *nums, int size, int index) {
        // Move all elements after index index forward by one position
        for (int i = index; i < size - 1; i++) {
            nums[i] = nums[i + 1];
        }
    }
    ```
=== "Java"
    ```java title="array.java"
    static void remove(int[] nums, int index) {
            // Move all elements after index index forward by one position
            for (int i = index; i < nums.length - 1; i++) {
                nums[i] = nums[i + 1];
            }
        }
    ```
=== "C#"
    ```csharp title="array.cs"
    void Remove(int[] nums, int index) {
            // Move all elements after index index forward by one position
            for (int i = index; i < nums.Length - 1; i++) {
                nums[i] = nums[i + 1];
            }
        }
    ```
=== "Go"
    ```go title="array.go"
    func remove(nums []int, index int) {
    	// Move all elements after index index forward by one position
    	for i := index; i < len(nums)-1; i++ {
    		nums[i] = nums[i+1]
    	}
    }
    ```
=== "Swift"
    ```swift title="array.swift"
    func remove(nums: inout [Int], index: Int) {
        // Move all elements after index index forward by one position
        for i in nums.indices.dropFirst(index).dropLast() {
            nums[i] = nums[i + 1]
        }
    }
    ```
=== "JS"
    ```javascript title="array.js"
    function remove(nums, index) {
        // Move all elements after index index forward by one position
        for (let i = index; i < nums.length - 1; i++) {
            nums[i] = nums[i + 1];
        }
    }
    ```
=== "TS"
    ```typescript title="array.ts"
    function remove(nums: number[], index: number): void {
        // Move all elements after index index forward by one position
        for (let i = index; i < nums.length - 1; i++) {
            nums[i] = nums[i + 1];
        }
    }
    ```
=== "Dart"
    ```dart title="array.dart"
    void remove(List<int> nums, int index) {
      // Move all elements after index index forward by one position
      for (var i = index; i < nums.length - 1; i++) {
        nums[i] = nums[i + 1];
      }
    }
    ```
=== "Rust"
    ```rust title="array.rs"
    fn remove(nums: &mut [i32], index: usize) {
        // Move all elements after index index forward by one position
        for i in index..nums.len() - 1 {
            nums[i] = nums[i + 1];
        }
    }
    ```
=== "C"
    ```c title="array.c"
    // Note: stdio.h occupies the remove keyword
    void removeItem(int *nums, int size, int index) {
        // Move all elements after index index forward by one position
        for (int i = index; i < size - 1; i++) {
            nums[i] = nums[i + 1];
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="array.kt"
    fun remove(nums: IntArray, index: Int) {
        // Move all elements after index index forward by one position
        for (i in index..<nums.size - 1) {
            nums[i] = nums[i + 1]
        }
    }
    ```
=== "Ruby"
    ```ruby title="array.rb"
    ### Delete element at index ###
    def remove(nums, index)
      # Move all elements after index index forward by one position
      for i in index...(nums.length - 1)
        nums[i] = nums[i + 1]
      end
    ```


Nhìn chung, các thao tác chèn và xóa mảng có những nhược điểm sau:

- **Độ phức tạp về thời gian cao**: Độ phức tạp về thời gian trung bình cho cả việc chèn và xóa trong mảng là $O(n)$, trong đó $n$ là độ dài của mảng.
- **Mất phần tử**: Vì độ dài của mảng là không thay đổi nên sau khi chèn phần tử vào, các phần tử vượt quá độ dài của mảng sẽ bị mất.
- **Lãng phí bộ nhớ**: Chúng ta có thể khởi tạo một mảng tương đối dài và chỉ sử dụng phần trước, do đó mọi phần tử đuôi bị ghi đè chỉ là phần giữ chỗ không được sử dụng, nhưng điều này sẽ lãng phí một số dung lượng bộ nhớ.

### Duyệt mảng

Trong hầu hết các ngôn ngữ lập trình, chúng ta có thể duyệt mảng theo chỉ mục hoặc bằng cách lặp trực tiếp qua từng phần tử trong mảng:

=== "Python"
    ```python title="array.py"
    def traverse(nums: list[int]):
        """Traverse array"""
        count = 0
        # Traverse array by index
        for i in range(len(nums)):
            count += nums[i]
        # Direct traversal of array elements
        for num in nums:
            count += num
        # Traverse simultaneously data index and elements
        for i, num in enumerate(nums):
            count += nums[i]
            count += num
    ```
=== "C++"
    ```cpp title="array.cpp"
    void traverse(int *nums, int size) {
        int count = 0;
        // Traverse array by index
        for (int i = 0; i < size; i++) {
            count += nums[i];
        }
    }
    ```
=== "Java"
    ```java title="array.java"
    static void traverse(int[] nums) {
            int count = 0;
            // Traverse array by index
            for (int i = 0; i < nums.length; i++) {
                count += nums[i];
            }
            // Direct traversal of array elements
            for (int num : nums) {
                count += num;
            }
        }
    ```
=== "C#"
    ```csharp title="array.cs"
    void Traverse(int[] nums) {
            int count = 0;
            // Traverse array by index
            for (int i = 0; i < nums.Length; i++) {
                count += nums[i];
            }
            // Direct traversal of array elements
            foreach (int num in nums) {
                count += num;
            }
        }
    ```
=== "Go"
    ```go title="array.go"
    func traverse(nums []int) {
    	count := 0
    	// Traverse array by index
    	for i := 0; i < len(nums); i++ {
    		count += nums[i]
    	}
    	count = 0
    	// Direct traversal of array elements
    	for _, num := range nums {
    		count += num
    	}
    	// Traverse simultaneously data index and elements
    	for i, num := range nums {
    		count += nums[i]
    		count += num
    	}
    }
    ```
=== "Swift"
    ```swift title="array.swift"
    func traverse(nums: [Int]) {
        var count = 0
        // Traverse array by index
        for i in nums.indices {
            count += nums[i]
        }
        // Direct traversal of array elements
        for num in nums {
            count += num
        }
        // Traverse simultaneously data index and elements
        for (i, num) in nums.enumerated() {
            count += nums[i]
            count += num
        }
    }
    ```
=== "JS"
    ```javascript title="array.js"
    function traverse(nums) {
        let count = 0;
        // Traverse array by index
        for (let i = 0; i < nums.length; i++) {
            count += nums[i];
        }
        // Direct traversal of array elements
        for (const num of nums) {
            count += num;
        }
    }
    ```
=== "TS"
    ```typescript title="array.ts"
    function traverse(nums: number[]): void {
        let count = 0;
        // Traverse array by index
        for (let i = 0; i < nums.length; i++) {
            count += nums[i];
        }
        // Direct traversal of array elements
        for (const num of nums) {
            count += num;
        }
    }
    ```
=== "Dart"
    ```dart title="array.dart"
    void traverse(List<int> nums) {
      int count = 0;
      // Traverse array by index
      for (var i = 0; i < nums.length; i++) {
        count += nums[i];
      }
      // Direct traversal of array elements
      for (int _num in nums) {
        count += _num;
      }
      // Traverse array using forEach method
      nums.forEach((_num) {
        count += _num;
      });
    }
    ```
=== "Rust"
    ```rust title="array.rs"
    fn traverse(nums: &[i32]) {
        let mut _count = 0;
        // Traverse array by index
        for i in 0..nums.len() {
            _count += nums[i];
        }
        // Direct traversal of array elements
        _count = 0;
        for &num in nums {
            _count += num;
        }
    }
    ```
=== "C"
    ```c title="array.c"
    void traverse(int *nums, int size) {
        int count = 0;
        // Traverse array by index
        for (int i = 0; i < size; i++) {
            count += nums[i];
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="array.kt"
    fun traverse(nums: IntArray) {
        var count = 0
        // Traverse array by index
        for (i in nums.indices) {
            count += nums[i]
        }
        // Direct traversal of array elements
        for (j in nums) {
            count += j
        }
    }
    ```
=== "Ruby"
    ```ruby title="array.rb"
    ### Traverse array ###
    def traverse(nums)
      count = 0
    
      # Traverse array by index
      for i in 0...nums.length
        count += nums[i]
      end
    
      # Direct traversal of array elements
      for num in nums
        count += num
      end
    ```


### Tìm phần tử

Việc tìm kiếm một phần tử được chỉ định trong một mảng yêu cầu duyệt qua mảng và kiểm tra xem giá trị phần tử có khớp trong mỗi lần lặp hay không; nếu nó khớp, xuất chỉ mục tương ứng.

Vì mảng là cấu trúc dữ liệu tuyến tính nên thao tác tìm kiếm ở trên được gọi là "tìm kiếm tuyến tính".

=== "Python"
    ```python title="array.py"
    def find(nums: list[int], target: int) -> int:
        """Find the specified element in the array"""
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    ```
=== "C++"
    ```cpp title="array.cpp"
    int find(int *nums, int size, int target) {
        for (int i = 0; i < size; i++) {
            if (nums[i] == target)
                return i;
        }
        return -1;
    }
    ```
=== "Java"
    ```java title="array.java"
    static int find(int[] nums, int target) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == target)
                    return i;
            }
            return -1;
        }
    ```
=== "C#"
    ```csharp title="array.cs"
    int Find(int[] nums, int target) {
            for (int i = 0; i < nums.Length; i++) {
                if (nums[i] == target)
                    return i;
            }
            return -1;
        }
    ```
=== "Go"
    ```go title="array.go"
    func find(nums []int, target int) (index int) {
    	index = -1
    	for i := 0; i < len(nums); i++ {
    		if nums[i] == target {
    			index = i
    			break
    		}
    	}
    	return
    }
    ```
=== "Swift"
    ```swift title="array.swift"
    func find(nums: [Int], target: Int) -> Int {
        for i in nums.indices {
            if nums[i] == target {
                return i
            }
        }
        return -1
    }
    ```
=== "JS"
    ```javascript title="array.js"
    function find(nums, target) {
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === target) return i;
        }
        return -1;
    }
    ```
=== "TS"
    ```typescript title="array.ts"
    function find(nums: number[], target: number): number {
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === target) {
                return i;
            }
        }
        return -1;
    }
    ```
=== "Dart"
    ```dart title="array.dart"
    int find(List<int> nums, int target) {
      for (var i = 0; i < nums.length; i++) {
        if (nums[i] == target) return i;
      }
      return -1;
    }
    ```
=== "Rust"
    ```rust title="array.rs"
    fn find(nums: &[i32], target: i32) -> Option<usize> {
        for i in 0..nums.len() {
            if nums[i] == target {
                return Some(i);
            }
        }
        None
    }
    ```
=== "C"
    ```c title="array.c"
    int find(int *nums, int size, int target) {
        for (int i = 0; i < size; i++) {
            if (nums[i] == target)
                return i;
        }
        return -1;
    }
    ```
=== "Kotlin"
    ```kotlin title="array.kt"
    fun find(nums: IntArray, target: Int): Int {
        for (i in nums.indices) {
            if (nums[i] == target)
                return i
        }
        return -1
    }
    ```
=== "Ruby"
    ```ruby title="array.rb"
    ### Find specified element in array ###
    def find(nums, target)
      for i in 0...nums.length
        return i if nums[i] == target
      end
    
      -1
    ```


### Mở rộng mảng

Trong môi trường hệ thống phức tạp, các chương trình không thể đảm bảo rằng không gian bộ nhớ sau một mảng có sẵn, khiến việc mở rộng dung lượng của mảng trở nên không an toàn. Do đó, trong hầu hết các ngôn ngữ lập trình, **độ dài của mảng là không thay đổi**.

Nếu muốn mở rộng một mảng, chúng ta cần tạo một mảng mới, lớn hơn rồi sao chép từng phần tử mảng ban đầu sang mảng mới. Đây là thao tác $O(n)$, rất tốn thời gian khi mảng lớn. Mã được hiển thị dưới đây:

=== "Python"
    ```python title="array.py"
    # Please note that Python's list is a dynamic array and can be extended directly
    # For learning purposes, this function treats the list as an array with immutable length
    def extend(nums: list[int], enlarge: int) -> list[int]:
        """Extend array length"""
        # Initialize an array with extended length
        res = [0] * (len(nums) + enlarge)
        # Copy all elements from the original array to the new array
        for i in range(len(nums)):
            res[i] = nums[i]
        # Return the extended new array
        return res
    ```
=== "C++"
    ```cpp title="array.cpp"
    int *extend(int *nums, int size, int enlarge) {
        // Initialize an array with extended length
        int *res = new int[size + enlarge];
        // Copy all elements from the original array to the new array
        for (int i = 0; i < size; i++) {
            res[i] = nums[i];
        }
        // Free memory
        delete[] nums;
        // Return the extended new array
        return res;
    }
    ```
=== "Java"
    ```java title="array.java"
    static int[] extend(int[] nums, int enlarge) {
            // Initialize an array with extended length
            int[] res = new int[nums.length + enlarge];
            // Copy all elements from the original array to the new array
            for (int i = 0; i < nums.length; i++) {
                res[i] = nums[i];
            }
            // Return the extended new array
            return res;
        }
    ```
=== "C#"
    ```csharp title="array.cs"
    int[] Extend(int[] nums, int enlarge) {
            // Initialize an array with extended length
            int[] res = new int[nums.Length + enlarge];
            // Copy all elements from the original array to the new array
            for (int i = 0; i < nums.Length; i++) {
                res[i] = nums[i];
            }
            // Return the extended new array
            return res;
        }
    ```
=== "Go"
    ```go title="array.go"
    func extend(nums []int, enlarge int) []int {
    	// Initialize an array with extended length
    	res := make([]int, len(nums)+enlarge)
    	// Copy all elements from the original array to the new array
    	for i, num := range nums {
    		res[i] = num
    	}
    	// Return the extended new array
    	return res
    }
    ```
=== "Swift"
    ```swift title="array.swift"
    func extend(nums: [Int], enlarge: Int) -> [Int] {
        // Initialize an array with extended length
        var res = Array(repeating: 0, count: nums.count + enlarge)
        // Copy all elements from the original array to the new array
        for i in nums.indices {
            res[i] = nums[i]
        }
        // Return the extended new array
        return res
    }
    ```
=== "JS"
    ```javascript title="array.js"
    // Note: JavaScript's Array is dynamic array, can be directly expanded
    // For learning purposes, this function treats Array as fixed-length array
    function extend(nums, enlarge) {
        // Initialize an array with extended length
        const res = new Array(nums.length + enlarge).fill(0);
        // Copy all elements from the original array to the new array
        for (let i = 0; i < nums.length; i++) {
            res[i] = nums[i];
        }
        // Return the extended new array
        return res;
    }
    ```
=== "TS"
    ```typescript title="array.ts"
    // Note: TypeScript's Array is dynamic array, can be directly expanded
    // For learning purposes, this function treats Array as fixed-length array
    function extend(nums: number[], enlarge: number): number[] {
        // Initialize an array with extended length
        const res = new Array(nums.length + enlarge).fill(0);
        // Copy all elements from the original array to the new array
        for (let i = 0; i < nums.length; i++) {
            res[i] = nums[i];
        }
        // Return the extended new array
        return res;
    }
    ```
=== "Dart"
    ```dart title="array.dart"
    List<int> extend(List<int> nums, int enlarge) {
      // Initialize an array with extended length
      List<int> res = List.filled(nums.length + enlarge, 0);
      // Copy all elements from the original array to the new array
      for (var i = 0; i < nums.length; i++) {
        res[i] = nums[i];
      }
      // Return the extended new array
      return res;
    }
    ```
=== "Rust"
    ```rust title="array.rs"
    fn extend(nums: &[i32], enlarge: usize) -> Vec<i32> {
        // Initialize an array with extended length
        let mut res: Vec<i32> = vec![0; nums.len() + enlarge];
        // Copy all elements from original array to new
        res[0..nums.len()].copy_from_slice(nums);
    
        // Return the extended new array
        res
    }
    ```
=== "C"
    ```c title="array.c"
    int *extend(int *nums, int size, int enlarge) {
        // Initialize an array with extended length
        int *res = (int *)malloc(sizeof(int) * (size + enlarge));
        // Copy all elements from the original array to the new array
        for (int i = 0; i < size; i++) {
            res[i] = nums[i];
        }
        // Initialize expanded space
        for (int i = size; i < size + enlarge; i++) {
            res[i] = 0;
        }
        // Return the extended new array
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="array.kt"
    fun extend(nums: IntArray, enlarge: Int): IntArray {
        // Initialize an array with extended length
        val res = IntArray(nums.size + enlarge)
        // Copy all elements from the original array to the new array
        for (i in nums.indices) {
            res[i] = nums[i]
        }
        // Return the extended new array
        return res
    }
    ```
=== "Ruby"
    ```ruby title="array.rb"
    ### Extend array length ###
    # Note: Ruby's Array is dynamic array, can be directly expanded
    # For learning purposes, this function treats Array as fixed-length array
    def extend(nums, enlarge)
      # Initialize an array with extended length
      res = Array.new(nums.length + enlarge, 0)
    
      # Copy all elements from the original array to the new array
      for i in 0...nums.length
        res[i] = nums[i]
      end
    
      # Return the extended new array
      res
    ```


## Ưu điểm và hạn chế của mảng

Mảng được lưu trữ trong không gian bộ nhớ liền kề với các phần tử cùng loại. Cách tiếp cận này chứa thông tin phong phú trước đó mà hệ thống có thể sử dụng để tối ưu hóa hiệu quả hoạt động của cấu trúc dữ liệu.

- **Hiệu quả không gian cao**: Mảng phân bổ các khối bộ nhớ liền kề cho dữ liệu mà không cần thêm chi phí cấu trúc.
- **Hỗ trợ truy cập ngẫu nhiên**: Mảng cho phép truy cập bất kỳ phần tử nào trong thời gian $O(1)$.
- **Cục bộ nhớ đệm**: Khi truy cập các phần tử mảng, máy tính không chỉ tải phần tử đó mà còn lưu vào bộ nhớ đệm các dữ liệu xung quanh, từ đó tận dụng bộ nhớ đệm để cải thiện tốc độ thực thi các thao tác tiếp theo.

Lưu trữ không gian liền kề là con dao hai lưỡi với những hạn chế sau:

- **Hiệu suất chèn và xóa thấp**: Khi một mảng có nhiều phần tử, các thao tác chèn và xóa đòi hỏi phải dịch chuyển một số lượng lớn các phần tử.
- **Độ dài bất biến**: Sau khi khởi tạo một mảng, độ dài của mảng sẽ cố định. Việc mở rộng mảng yêu cầu sao chép tất cả dữ liệu sang một mảng mới, việc này rất tốn kém.
- **Lãng phí không gian**: Nếu kích thước được phân bổ của một mảng vượt quá mức thực sự cần thiết thì không gian bổ sung sẽ bị lãng phí.

## Ứng dụng điển hình của mảng

Mảng là một cấu trúc dữ liệu cơ bản và phổ biến, thường được sử dụng trong các thuật toán khác nhau và để triển khai các cấu trúc dữ liệu phức tạp khác nhau.

- **Truy cập ngẫu nhiên**: Nếu muốn lấy mẫu ngẫu nhiên một số mục, chúng ta có thể sử dụng một mảng để lưu trữ chúng và tạo ra một chuỗi ngẫu nhiên để triển khai lấy mẫu ngẫu nhiên dựa trên các chỉ số.
- **Sắp xếp và tìm kiếm**: Mảng là cấu trúc dữ liệu được sử dụng phổ biến nhất cho các thuật toán sắp xếp và tìm kiếm. Sắp xếp nhanh, sắp xếp hợp nhất, tìm kiếm nhị phân và các thứ khác chủ yếu được thực hiện trên mảng.
- **Bảng tra cứu**: Khi cần tìm nhanh một phần tử hoặc mối quan hệ tương ứng của nó, chúng ta có thể sử dụng mảng làm bảng tra cứu. Ví dụ: nếu chúng ta muốn triển khai ánh xạ từ các ký tự sang mã ASCII, chúng ta có thể sử dụng giá trị mã ASCII của một ký tự làm chỉ mục, với phần tử tương ứng được lưu trữ ở vị trí đó trong mảng.
- **Học máy**: Mạng thần kinh sử dụng rộng rãi các phép toán đại số tuyến tính giữa vectơ, ma trận và tensor, tất cả đều được xây dựng dưới dạng mảng. Mảng là cấu trúc dữ liệu được sử dụng phổ biến nhất trong lập trình mạng nơ-ron.
- **Triển khai cấu trúc dữ liệu**: Mảng có thể được sử dụng để triển khai ngăn xếp, hàng đợi, bảng băm, vùng heap, biểu đồ và các cấu trúc dữ liệu khác. Ví dụ, biểu diễn ma trận kề của đồ thị về cơ bản là một mảng hai chiều.
