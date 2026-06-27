# Danh sách

<u>danh sách</u> là một khái niệm cấu trúc dữ liệu trừu tượng thể hiện một tập hợp các phần tử có thứ tự, hỗ trợ các hoạt động như truy cập phần tử, sửa đổi, chèn, xóa và truyền tải mà không yêu cầu người dùng xem xét các giới hạn dung lượng. Danh sách có thể được triển khai dựa trên danh sách hoặc mảng được liên kết.

- Danh sách liên kết có thể được xem một cách tự nhiên dưới dạng danh sách: nó hỗ trợ chèn, xóa, tìm kiếm, cập nhật và có thể phát triển linh hoạt khi cần thiết.
- Mảng cũng hỗ trợ chèn, xóa, tìm kiếm, cập nhật nhưng do có độ dài cố định nên chỉ có thể coi là danh sách có giới hạn dung lượng.

Khi một danh sách được triển khai bằng một mảng, **độ dài cố định của nó sẽ khiến nó ít thực tế hơn**. Điều này là do chúng ta thường không thể xác định trước lượng dữ liệu cần lưu trữ, gây khó khăn cho việc lựa chọn dung lượng phù hợp. Nếu công suất quá nhỏ có thể không đáp ứng được nhu cầu của chúng ta; nếu nó quá lớn, dung lượng bộ nhớ sẽ bị lãng phí.

Để giải quyết vấn đề này, chúng ta có thể sử dụng <u>mảng động</u> để triển khai danh sách. Nó kế thừa tất cả các ưu điểm của mảng đồng thời hỗ trợ thay đổi kích thước động trong quá trình thực hiện chương trình.

Trên thực tế, **các loại danh sách do thư viện chuẩn của nhiều ngôn ngữ lập trình cung cấp được triển khai bằng mảng động**, chẳng hạn như `list` trong Python, `ArrayList` trong Java, `vector` trong C++ và `List` trong C#. Trong phần thảo luận sau đây, chúng ta sẽ coi "danh sách" và "mảng động" là các khái niệm tương đương.

## Các thao tác danh sách chung

### Khởi tạo danh sách

Chúng tôi thường khởi tạo danh sách theo một trong hai cách: trống hoặc với các giá trị được xác định trước:

=== "Trăn"

    ```python title="list.py"
    # Initialize a list
    # Without initial values
    nums1: list[int] = []
    # With initial values
    nums: list[int] = [1, 3, 2, 5, 4]
    ```

=== "C++"

    ```cpp title="list.cpp"
    /* Initialize a list */
    // Note that vector in C++ is equivalent to nums as described in this article
    // Without initial values
    vector<int> nums1;
    // With initial values
    vector<int> nums = { 1, 3, 2, 5, 4 };
    ```

=== "Java"

    ```java title="list.java"
    /* Initialize a list */
    // Without initial values
    List<Integer> nums1 = new ArrayList<>();
    // With initial values (note that array elements should use the wrapper class Integer[] instead of int[])
    Integer[] numbers = new Integer[] { 1, 3, 2, 5, 4 };
    List<Integer> nums = new ArrayList<>(Arrays.asList(numbers));
    ```

=== "C#"

    ```csharp title="list.cs"
    /* Initialize a list */
    // Without initial values
    List<int> nums1 = [];
    // With initial values
    int[] numbers = [1, 3, 2, 5, 4];
    List<int> nums = [.. numbers];
    ```

=== "Đi"

    ```go title="list_test.go"
    /* Initialize a list */
    // Without initial values
    nums1 := []int{}
    // With initial values
    nums := []int{1, 3, 2, 5, 4}
    ```

=== "Nhanh chóng"

    ```swift title="list.swift"
    /* Initialize a list */
    // Without initial values
    let nums1: [Int] = []
    // With initial values
    var nums = [1, 3, 2, 5, 4]
    ```

=== "JS"

    ```javascript title="list.js"
    /* Initialize a list */
    // Without initial values
    const nums1 = [];
    // With initial values
    const nums = [1, 3, 2, 5, 4];
    ```

=== "TS"

    ```typescript title="list.ts"
    /* Initialize a list */
    // Without initial values
    const nums1: number[] = [];
    // With initial values
    const nums: number[] = [1, 3, 2, 5, 4];
    ```

=== "Phi tiêu"

    ```dart title="list.dart"
    /* Initialize a list */
    // Without initial values
    List<int> nums1 = [];
    // With initial values
    List<int> nums = [1, 3, 2, 5, 4];
    ```

=== "Rỉ sét"

    ```rust title="list.rs"
    /* Initialize a list */
    // Without initial values
    let nums1: Vec<i32> = Vec::new();
    // With initial values
    let nums: Vec<i32> = vec![1, 3, 2, 5, 4];
    ```

=== "C"

    ```c title="list.c"
    // C does not provide built-in dynamic arrays
    ```

=== "Kotlin"

    ```kotlin title="list.kt"
    /* Initialize a list */
    // Without initial values
    var nums1 = listOf<Int>()
    // With initial values
    var numbers = arrayOf(1, 3, 2, 5, 4)
    var nums = numbers.toMutableList()
    ```

=== "Ruby"

    ```ruby title="list.rb"
    # Initialize a list
    # Without initial values
    nums1 = []
    # With initial values
    nums = [1, 3, 2, 5, 4]
    ```

??? pythontutor "Trực quan hóa mã"

https://pythontutor.com/render.html#code=%22%22%22Driver%20Code%22%22%22%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%2 0%23%20%E5%88%9D%E5%A7%8B%E5%8C%96%E5%88%97%E8%A1%A8%0A%20%20%20%2 0%23%20%E6%97%A0%E5%88%9D%E5%A7%8B%E5%80%BC%0A%20%20%20%20nums1%20 %3D%20%5B%5D%0A%20%20%20%20%23%20%E6%9C%89%E5%88%9D%E5%A7%8B%E5%80 %BC%0A%20%20%20%20nums%20%3D%20%5B1,%203,%202,%205,%204%5D&tích lũy ive=false&curInstr=4&heapPrimitives=neverrest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

### Các phần tử truy cập

Vì danh sách về cơ bản là một mảng nên chúng ta có thể truy cập và cập nhật các phần tử với độ phức tạp về thời gian $O(1)$, điều này rất hiệu quả.

=== "Trăn"

    ```python title="list.py"
    # Access an element
    num: int = nums[1]  # Access element at index 1

    # Update an element
    nums[1] = 0    # Update element at index 1 to 0
    ```

=== "C++"

    ```cpp title="list.cpp"
    /* Access an element */
    int num = nums[1];  // Access element at index 1

    /* Update an element */
    nums[1] = 0;  // Update element at index 1 to 0
    ```

=== "Java"

    ```java title="list.java"
    /* Access an element */
    int num = nums.get(1);  // Access element at index 1

    /* Update an element */
    nums.set(1, 0);  // Update element at index 1 to 0
    ```

=== "C#"

    ```csharp title="list.cs"
    /* Access an element */
    int num = nums[1];  // Access element at index 1

    /* Update an element */
    nums[1] = 0;  // Update element at index 1 to 0
    ```

=== "Đi"

    ```go title="list_test.go"
    /* Access an element */
    num := nums[1]  // Access element at index 1

    /* Update an element */
    nums[1] = 0     // Update element at index 1 to 0
    ```

=== "Nhanh chóng"

    ```swift title="list.swift"
    /* Access an element */
    let num = nums[1] // Access element at index 1

    /* Update an element */
    nums[1] = 0 // Update element at index 1 to 0
    ```

=== "JS"

    ```javascript title="list.js"
    /* Access an element */
    const num = nums[1];  // Access element at index 1

    /* Update an element */
    nums[1] = 0;  // Update element at index 1 to 0
    ```

=== "TS"

    ```typescript title="list.ts"
    /* Access an element */
    const num: number = nums[1];  // Access element at index 1

    /* Update an element */
    nums[1] = 0;  // Update element at index 1 to 0
    ```

=== "Phi tiêu"

    ```dart title="list.dart"
    /* Access an element */
    int num = nums[1];  // Access element at index 1

    /* Update an element */
    nums[1] = 0;  // Update element at index 1 to 0
    ```

=== "Rỉ sét"

    ```rust title="list.rs"
    /* Access an element */
    let num: i32 = nums[1];  // Access element at index 1
    /* Update an element */
    nums[1] = 0;             // Update element at index 1 to 0
    ```

=== "C"

    ```c title="list.c"
    // C does not provide built-in dynamic arrays
    ```

=== "Kotlin"

    ```kotlin title="list.kt"
    /* Access an element */
    val num = nums[1]       // Access element at index 1
    /* Update an element */
    nums[1] = 0             // Update element at index 1 to 0
    ```

=== "Ruby"

    ```ruby title="list.rb"
    # Access an element
    num = nums[1] # Access element at index 1
    # Update an element
    nums[1] = 0 # Update element at index 1 to 0
    ```

??? pythontutor "Trực quan hóa mã"

https://pythontutor.com/render.html#code=%22%22%22Driver%20Code%22%22%22%0Aif%20__name__%20%3D%3D %20%22__main__%22%3A%0A%20%20%20%20%23%20%E5%88%9D%E5%A7%8B%E5%8C%96%E5%88%97%E8%A1%A8%0A%20%20%20 %20nums%20%3D%20%5B1,%203,%202,%205,%204%5D%0A%0A%20%20%20%20%23%20%E8%AE%BF%E9%97%AE%E5%85%83%E7% B4%A0%0A%20%20%20%20num%20%3D%20nums%5B1%5D%20%20%23%20%E8%AE%BF%E9%97%AE%E7%B4%A2%E5%BC%95%201%20 %E5%A4%84%E7%9A%84%E5%85%83%E7%B4%A0%0A%0A%20%20%20%20%23%20%E6%9B%B4%E6%96%B0%E5%85%83%E7%B4%A0% 0A%20%20%20%20nums%5B1%5D%20%3D%200%20%20%20%20%23%20%E5%B0%86%E7%B4%A2%E5%BC%95%201%20%E5%A4%84%E 7%9A%84%E5%85%83%E7%B4%A0%E6%9B%B4%E6%96%B0%E4%B8%BA%200&cumulative=false&curInstr=3&heapPrimitive s=nvernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

### Chèn và xóa phần tử

So với mảng, danh sách có thể tự do thêm và xóa các phần tử. Việc thêm một phần tử vào cuối danh sách có độ phức tạp về thời gian là $O(1)$, nhưng việc chèn và xóa các phần tử vẫn có hiệu quả tương tự như mảng, với độ phức tạp về thời gian là $O(n)$.

=== "Trăn"

    ```python title="list.py"
    # Clear the list
    nums.clear()

    # Add elements at the end
    nums.append(1)
    nums.append(3)
    nums.append(2)
    nums.append(5)
    nums.append(4)

    # Insert an element in the middle
    nums.insert(3, 6)  # Insert number 6 at index 3

    # Delete an element
    nums.pop(3)        # Delete element at index 3
    ```

=== "C++"

    ```cpp title="list.cpp"
    /* Clear the list */
    nums.clear();

    /* Add elements at the end */
    nums.push_back(1);
    nums.push_back(3);
    nums.push_back(2);
    nums.push_back(5);
    nums.push_back(4);

    /* Insert an element in the middle */
    nums.insert(nums.begin() + 3, 6);  // Insert number 6 at index 3

    /* Delete an element */
    nums.erase(nums.begin() + 3);      // Delete element at index 3
    ```

=== "Java"

    ```java title="list.java"
    /* Clear the list */
    nums.clear();

    /* Add elements at the end */
    nums.add(1);
    nums.add(3);
    nums.add(2);
    nums.add(5);
    nums.add(4);

    /* Insert an element in the middle */
    nums.add(3, 6);  // Insert number 6 at index 3

    /* Delete an element */
    nums.remove(3);  // Delete element at index 3
    ```

=== "C#"

    ```csharp title="list.cs"
    /* Clear the list */
    nums.Clear();

    /* Add elements at the end */
    nums.Add(1);
    nums.Add(3);
    nums.Add(2);
    nums.Add(5);
    nums.Add(4);

    /* Insert an element in the middle */
    nums.Insert(3, 6);  // Insert number 6 at index 3

    /* Delete an element */
    nums.RemoveAt(3);  // Delete element at index 3
    ```

=== "Đi"

    ```go title="list_test.go"
    /* Clear the list */
    nums = nil

    /* Add elements at the end */
    nums = append(nums, 1)
    nums = append(nums, 3)
    nums = append(nums, 2)
    nums = append(nums, 5)
    nums = append(nums, 4)

    /* Insert an element in the middle */
    nums = append(nums[:3], append([]int{6}, nums[3:]...)...) // Insert number 6 at index 3

    /* Delete an element */
    nums = append(nums[:3], nums[4:]...) // Delete element at index 3
    ```

=== "Nhanh chóng"

    ```swift title="list.swift"
    /* Clear the list */
    nums.removeAll()

    /* Add elements at the end */
    nums.append(1)
    nums.append(3)
    nums.append(2)
    nums.append(5)
    nums.append(4)

    /* Insert an element in the middle */
    nums.insert(6, at: 3) // Insert number 6 at index 3

    /* Delete an element */
    nums.remove(at: 3) // Delete element at index 3
    ```

=== "JS"

    ```javascript title="list.js"
    /* Clear the list */
    nums.length = 0;

    /* Add elements at the end */
    nums.push(1);
    nums.push(3);
    nums.push(2);
    nums.push(5);
    nums.push(4);

    /* Insert an element in the middle */
    nums.splice(3, 0, 6); // Insert number 6 at index 3

    /* Delete an element */
    nums.splice(3, 1);  // Delete element at index 3
    ```

=== "TS"

    ```typescript title="list.ts"
    /* Clear the list */
    nums.length = 0;

    /* Add elements at the end */
    nums.push(1);
    nums.push(3);
    nums.push(2);
    nums.push(5);
    nums.push(4);

    /* Insert an element in the middle */
    nums.splice(3, 0, 6); // Insert number 6 at index 3

    /* Delete an element */
    nums.splice(3, 1);  // Delete element at index 3
    ```

=== "Phi tiêu"

    ```dart title="list.dart"
    /* Clear the list */
    nums.clear();

    /* Add elements at the end */
    nums.add(1);
    nums.add(3);
    nums.add(2);
    nums.add(5);
    nums.add(4);

    /* Insert an element in the middle */
    nums.insert(3, 6); // Insert number 6 at index 3

    /* Delete an element */
    nums.removeAt(3); // Delete element at index 3
    ```

=== "Rỉ sét"

    ```rust title="list.rs"
    /* Clear the list */
    nums.clear();

    /* Add elements at the end */
    nums.push(1);
    nums.push(3);
    nums.push(2);
    nums.push(5);
    nums.push(4);

    /* Insert an element in the middle */
    nums.insert(3, 6);  // Insert number 6 at index 3

    /* Delete an element */
    nums.remove(3);    // Delete element at index 3
    ```

=== "C"

    ```c title="list.c"
    // C does not provide built-in dynamic arrays
    ```

=== "Kotlin"

    ```kotlin title="list.kt"
    /* Clear the list */
    nums.clear();

    /* Add elements at the end */
    nums.add(1);
    nums.add(3);
    nums.add(2);
    nums.add(5);
    nums.add(4);

    /* Insert an element in the middle */
    nums.add(3, 6);  // Insert number 6 at index 3

    /* Delete an element */
    nums.remove(3);  // Delete element at index 3
    ```

=== "Ruby"

    ```ruby title="list.rb"
    # Clear the list
    nums.clear

    # Add elements at the end
    nums << 1
    nums << 3
    nums << 2
    nums << 5
    nums << 4

    # Insert an element in the middle
    nums.insert(3, 6) # Insert number 6 at index 3

    # Delete an element
    nums.delete_at(3) # Delete element at index 3
    ```

??? pythontutor "Trực quan hóa mã"

https://pythontutor.com/render.html#code=%22%22%22Driver%20Code%22%22%22%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20%23%20%E6%9C%89 %E5%88%9D%E5%A7%8B%E5%80%BC%0A%20%20%20%20nums%20%3D%20%5B1,%203,%202,%20 5,%204%5D%0A%20%20%20%20%0A%20%20%20%20%23%20%E6%B8%85%E7%A9%BA%E5%88%97%E 8%A1%A8%0A%20%20%20%20nums.clear%28%29%0A%20%20%20%20%0A%20%20%20%20%23%2 0%E5%9C%A8%E5%B0%BE%E9%83%A8%E6%B7%BB%E5%8A%A0%E5%85%83%E7%B4%A0%0A%20%20% 20%20nums.append%281%29%0A%20%20%20%20nums.append%283%29%0A%20%20%20%20num s.append%282%29%0A%20%20%20%20nums.append%285%29%0A%20%20%20%20nums.append %284%29%0A%20%20%20%20%0A%20%20%20%20%23%20%E5%9C%A8%E4%B8%AD%E9%97%B4%E6 %8F%92%E5%85%A5%E5%85%83%E7%B4%A0%0A%20%20%20%20nums.insert%283,%206%29%20 %20%23%20%E5%9C%A8%E7%B4%A2%E5%BC%95%203%20%E5%A4%84%E6%8F%92%E5%85%A5%E6% 95%B0%E5%AD%97%206%0A%20%20%20%20%0A%20%20%20%20%23%20%E5%88%A0%E9%99%A4%E 5%85%83%E7%B4%A0%0A%20%20%20%20nums.pop%283%29%20%20%20%20%20%20%20%20%23 %20%E5%88%A0%E9%99%A4%E7%B4%A2%E5%BC%95%203%20%E5%A4%84%E7%9A%84%E5%85%83% E7%B4%A0&cumulative=false&curInstr=3&heapPrimitives=nvernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

### Duyệt qua danh sách

Giống như mảng, danh sách có thể được duyệt theo chỉ mục hoặc bằng cách duyệt trực tiếp qua các phần tử.

=== "Trăn"

    ```python title="list.py"
    # Traverse the list by index
    count = 0
    for i in range(len(nums)):
        count += nums[i]

    # Traverse list elements directly
    for num in nums:
        count += num
    ```

=== "C++"

    ```cpp title="list.cpp"
    /* Traverse the list by index */
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        count += nums[i];
    }

    /* Traverse list elements directly */
    count = 0;
    for (int num : nums) {
        count += num;
    }
    ```

=== "Java"

    ```java title="list.java"
    /* Traverse the list by index */
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        count += nums.get(i);
    }

    /* Traverse list elements directly */
    for (int num : nums) {
        count += num;
    }
    ```

=== "C#"

    ```csharp title="list.cs"
    /* Traverse the list by index */
    int count = 0;
    for (int i = 0; i < nums.Count; i++) {
        count += nums[i];
    }

    /* Traverse list elements directly */
    count = 0;
    foreach (int num in nums) {
        count += num;
    }
    ```

=== "Đi"

    ```go title="list_test.go"
    /* Traverse the list by index */
    count := 0
    for i := 0; i < len(nums); i++ {
        count += nums[i]
    }

    /* Traverse list elements directly */
    count = 0
    for _, num := range nums {
        count += num
    }
    ```

=== "Nhanh chóng"

    ```swift title="list.swift"
    /* Traverse the list by index */
    var count = 0
    for i in nums.indices {
        count += nums[i]
    }

    /* Traverse list elements directly */
    count = 0
    for num in nums {
        count += num
    }
    ```

=== "JS"

    ```javascript title="list.js"
    /* Traverse the list by index */
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        count += nums[i];
    }

    /* Traverse list elements directly */
    count = 0;
    for (const num of nums) {
        count += num;
    }
    ```

=== "TS"

    ```typescript title="list.ts"
    /* Traverse the list by index */
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        count += nums[i];
    }

    /* Traverse list elements directly */
    count = 0;
    for (const num of nums) {
        count += num;
    }
    ```

=== "Phi tiêu"

    ```dart title="list.dart"
    /* Traverse the list by index */
    int count = 0;
    for (var i = 0; i < nums.length; i++) {
        count += nums[i];
    }

    /* Traverse list elements directly */
    count = 0;
    for (var num in nums) {
        count += num;
    }
    ```

=== "Rỉ sét"

    ```rust title="list.rs"
    // Traverse the list by index
    let mut _count = 0;
    for i in 0..nums.len() {
        _count += nums[i];
    }

    // Traverse list elements directly
    _count = 0;
    for num in &nums {
        _count += num;
    }
    ```

=== "C"

    ```c title="list.c"
    // C does not provide built-in dynamic arrays
    ```

=== "Kotlin"

    ```kotlin title="list.kt"
    /* Traverse the list by index */
    var count = 0
    for (i in nums.indices) {
        count += nums[i]
    }

    /* Traverse list elements directly */
    for (num in nums) {
        count += num
    }
    ```

=== "Ruby"

    ```ruby title="list.rb"
    # Traverse the list by index
    count = 0
    for i in 0...nums.length
        count += nums[i]
    end

    # Traverse list elements directly
    count = 0
    for num in nums
        count += num
    end
    ```

??? pythontutor "Trực quan hóa mã"

https://pythontutor.com/render.html#code=%22%22%22Driver%20Code%22%22%22%0Aif%20__name__%20%3D%3D%20% 22__main__%22%3A%0A%20%20%20%20%23%20%E5%88%9D%E5%A7%8B%E5%8C%96%E5%88%97%E8%A1%A8%0A%20%20%20%20nums %20%3D%20%5B1,%203,%202,%205,%204%5D%0A%20%20%20%20%0A%20%20%20%20%23%20%E9%80%9A%E8%BF%87%E7%B4%A2%E 5%BC%95%E9%81%8D%E5%8E%86%E5%88%97%E8%A1%A8%0A%20%20%20%20count%20%3D%200%0A%20%20%20%20for%20i%20in%2 0phạm vi%28len%28nums%29%29%3A%0A%20%20%20%20%20%20%20%20count%20%2B%3D%20nums%5Bi%5D%0A%0A%20%20%20%20 %23%20%E7%9B%B4%E6%8E%A5%E9%81%8D%E5%8E%86%E5%88%97%E8%A1%A8%E5%85%83%E7%B4%A0%0A%20%20%20%20for%20nu m%20in%20nums%3A%0A%20%20%20%20%20%20%20%20count%20%2B%3D%20num&cumulative=false&curInstr=3&heapPrimi tives=nvernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

### Nối danh sách

Đưa ra một danh sách mới `nums1`, chúng ta có thể nối nó vào cuối danh sách ban đầu.

=== "Trăn"

    ```python title="list.py"
    # Concatenate two lists
    nums1: list[int] = [6, 8, 7, 10, 9]
    nums += nums1  # Concatenate list nums1 to the end of nums
    ```

=== "C++"

    ```cpp title="list.cpp"
    /* Concatenate two lists */
    vector<int> nums1 = { 6, 8, 7, 10, 9 };
    // Concatenate list nums1 to the end of nums
    nums.insert(nums.end(), nums1.begin(), nums1.end());
    ```

=== "Java"

    ```java title="list.java"
    /* Concatenate two lists */
    List<Integer> nums1 = new ArrayList<>(Arrays.asList(new Integer[] { 6, 8, 7, 10, 9 }));
    nums.addAll(nums1);  // Concatenate list nums1 to the end of nums
    ```

=== "C#"

    ```csharp title="list.cs"
    /* Concatenate two lists */
    List<int> nums1 = [6, 8, 7, 10, 9];
    nums.AddRange(nums1);  // Concatenate list nums1 to the end of nums
    ```

=== "Đi"

    ```go title="list_test.go"
    /* Concatenate two lists */
    nums1 := []int{6, 8, 7, 10, 9}
    nums = append(nums, nums1...)  // Concatenate list nums1 to the end of nums
    ```

=== "Nhanh chóng"

    ```swift title="list.swift"
    /* Concatenate two lists */
    let nums1 = [6, 8, 7, 10, 9]
    nums.append(contentsOf: nums1) // Concatenate list nums1 to the end of nums
    ```

=== "JS"

    ```javascript title="list.js"
    /* Concatenate two lists */
    const nums1 = [6, 8, 7, 10, 9];
    nums.push(...nums1);  // Concatenate list nums1 to the end of nums
    ```

=== "TS"

    ```typescript title="list.ts"
    /* Concatenate two lists */
    const nums1: number[] = [6, 8, 7, 10, 9];
    nums.push(...nums1);  // Concatenate list nums1 to the end of nums
    ```

=== "Phi tiêu"

    ```dart title="list.dart"
    /* Concatenate two lists */
    List<int> nums1 = [6, 8, 7, 10, 9];
    nums.addAll(nums1);  // Concatenate list nums1 to the end of nums
    ```

=== "Rỉ sét"

    ```rust title="list.rs"
    /* Concatenate two lists */
    let nums1: Vec<i32> = vec![6, 8, 7, 10, 9];
    nums.extend(nums1);
    ```

=== "C"

    ```c title="list.c"
    // C does not provide built-in dynamic arrays
    ```

=== "Kotlin"

    ```kotlin title="list.kt"
    /* Concatenate two lists */
    val nums1 = intArrayOf(6, 8, 7, 10, 9).toMutableList()
    nums.addAll(nums1)  // Concatenate list nums1 to the end of nums
    ```

=== "Ruby"

    ```ruby title="list.rb"
    # Concatenate two lists
    nums1 = [6, 8, 7, 10, 9]
    nums += nums1
    ```

??? pythontutor "Trực quan hóa mã"

https://pythontutor.com/render.html#code=%22%22%22Driver%20Code%22%22%22%0Aif%20__n ame__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20%23%20%E5%88%9D%E5%A7%8B%E5%8C%96% E5%88%97%E8%A1%A8%0A%20%20%20%20nums%20%3D%20%5B1,%203,%202,%205,%204%5D%0A%20%20%2 0%20%0A%20%20%20%20%23%20%E6%8B%BC%E6%8E%A5%E4%B8%A4%E4%B8%AA%E5%88%97%E8%A1%A8%0A%2 0%20%20%20nums1%20%3D%20%5B6,%208,%207,%2010,%209%5D%0A%20%20%20%20nums%20%2B%3D%20 số1%20%20%23%20%E5%B0%86%E5%88%97%E8%A1%A8%20nums1%20%E6%8B%BC%E6%8E%A5%E5%88%B0% 20nums%20%E4%B9%8B%E5%90%8E&cumulative=false&curInstr=3&heapPrimitives=nvernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

### Sắp xếp danh sách

Sau khi sắp xếp danh sách, chúng ta có thể sử dụng thuật toán "tìm kiếm nhị phân" và "hai con trỏ", những thuật toán này thường được kiểm tra trong các bài toán thuật toán mảng.

=== "Trăn"

    ```python title="list.py"
    # Sort a list
    nums.sort()  # After sorting, list elements are arranged from smallest to largest
    ```

=== "C++"

    ```cpp title="list.cpp"
    /* Sort a list */
    sort(nums.begin(), nums.end());  // After sorting, list elements are arranged from smallest to largest
    ```

=== "Java"

    ```java title="list.java"
    /* Sort a list */
    Collections.sort(nums);  // After sorting, list elements are arranged from smallest to largest
    ```

=== "C#"

    ```csharp title="list.cs"
    /* Sort a list */
    nums.Sort(); // After sorting, list elements are arranged from smallest to largest
    ```

=== "Đi"

    ```go title="list_test.go"
    /* Sort a list */
    sort.Ints(nums)  // After sorting, list elements are arranged from smallest to largest
    ```

=== "Nhanh chóng"

    ```swift title="list.swift"
    /* Sort a list */
    nums.sort() // After sorting, list elements are arranged from smallest to largest
    ```

=== "JS"

    ```javascript title="list.js"
    /* Sort a list */
    nums.sort((a, b) => a - b);  // After sorting, list elements are arranged from smallest to largest
    ```

=== "TS"

    ```typescript title="list.ts"
    /* Sort a list */
    nums.sort((a, b) => a - b);  // After sorting, list elements are arranged from smallest to largest
    ```

=== "Phi tiêu"

    ```dart title="list.dart"
    /* Sort a list */
    nums.sort(); // After sorting, list elements are arranged from smallest to largest
    ```

=== "Rỉ sét"

    ```rust title="list.rs"
    /* Sort a list */
    nums.sort(); // After sorting, list elements are arranged from smallest to largest
    ```

=== "C"

    ```c title="list.c"
    // C does not provide built-in dynamic arrays
    ```

=== "Kotlin"

    ```kotlin title="list.kt"
    /* Sort a list */
    nums.sort() // After sorting, list elements are arranged from smallest to largest
    ```

=== "Ruby"

    ```ruby title="list.rb"
    # Sort a list
    nums = nums.sort { |a, b| a <=> b } # After sorting, list elements are arranged from smallest to largest
    ```

??? pythontutor "Trực quan hóa mã"

https://pythontutor.com/render.html#code=%22%22%22Driver%20Code%22%22%22%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20%23%20%E5%88%9D%E5%A7% 8B%E5%8C%96%E5%88%97%E8%A1%A8%0A%20%20%20%20nums%20%3D%20%5B1,%203,%202,%205, %204%5D%0A%20%20%20%20%0A%20%20%20%20%23%20%E6%8E%92%E5%BA%8F%E5%88%97%E8%A1%A 8%0A%20%20%20%20nums.sort%28%29%20%20%23%20%E6%8E%92%E5%BA%8F%E5%90%8E%EF%BC% 8C%E5%88%97%E8%A1%A8%E5%85%83%E7%B4%A0%E4%BB%8E%E5%B0%8F%E5%88%B0%E5%A4%A7%E6 %8E%92%E5%88%97&cumulative=false&curInstr=3&heapPrimitives=nvernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false

## Triển khai danh sách

Nhiều ngôn ngữ lập trình có sẵn danh sách, chẳng hạn như Java, C++ và Python. Việc triển khai chúng khá phức tạp và các tham số được xem xét cẩn thận, chẳng hạn như công suất ban đầu, bội số mở rộng, v.v. Bạn đọc quan tâm có thể tham khảo mã nguồn để tìm hiểu thêm.

Để hiểu sâu hơn về cách hoạt động của danh sách, chúng tôi cố gắng triển khai một danh sách đơn giản với ba cân nhắc thiết kế chính:

- **Dung lượng ban đầu**: Chọn dung lượng ban đầu hợp lý cho mảng cơ bản. Trong ví dụ này, chúng tôi chọn 10 làm công suất ban đầu.
- **Theo dõi kích thước**: Khai báo biến `size` để ghi lại số phần tử hiện tại trong danh sách và cập nhật nó theo thời gian thực khi các phần tử được chèn và xóa. Dựa trên biến này, chúng tôi có thể xác định vị trí cuối danh sách và xác định xem có cần mở rộng hay không.
- **Cơ chế mở rộng**: Khi chèn một phần tử vào đã đầy dung lượng danh sách, chúng ta cần mở rộng. Chúng tôi tạo một mảng lớn hơn dựa trên bội số mở rộng và sau đó di chuyển tất cả các phần tử từ mảng hiện tại sang mảng mới theo thứ tự. Trong ví dụ này, chúng tôi chỉ định rằng mảng sẽ được mở rộng gấp 2 lần kích thước trước đó của nó mỗi lần.

=== "Python"
    ```python title="my_list.py"
    class MyList:
        """List class"""
    
        def __init__(self):
            """Constructor"""
            self._capacity: int = 10  # List capacity
            self._arr: list[int] = [0] * self._capacity  # Array (stores list elements)
            self._size: int = 0  # List length (current number of elements)
            self._extend_ratio: int = 2  # Multiple by which the list capacity is extended each time
    
        def size(self) -> int:
            """Get list length (current number of elements)"""
            return self._size
    
        def capacity(self) -> int:
            """Get list capacity"""
            return self._capacity
    
        def get(self, index: int) -> int:
            """Access element"""
            # If the index is out of bounds, throw an exception, as below
            if index < 0 or index >= self._size:
                raise IndexError("Index out of bounds")
            return self._arr[index]
    
        def set(self, num: int, index: int):
            """Update element"""
            if index < 0 or index >= self._size:
                raise IndexError("Index out of bounds")
            self._arr[index] = num
    
        def add(self, num: int):
            """Add element at the end"""
            # When the number of elements exceeds capacity, trigger the extension mechanism
            if self.size() == self.capacity():
                self.extend_capacity()
            self._arr[self._size] = num
            self._size += 1
    
        def insert(self, num: int, index: int):
            """Insert element in the middle"""
            if index < 0 or index >= self._size:
                raise IndexError("Index out of bounds")
            # When the number of elements exceeds capacity, trigger the extension mechanism
            if self._size == self.capacity():
                self.extend_capacity()
            # Move all elements at and after index index backward by one position
            for j in range(self._size - 1, index - 1, -1):
                self._arr[j + 1] = self._arr[j]
            self._arr[index] = num
            # Update the number of elements
            self._size += 1
    
        def remove(self, index: int) -> int:
            """Remove element"""
            if index < 0 or index >= self._size:
                raise IndexError("Index out of bounds")
            num = self._arr[index]
            # Move all elements after index index forward by one position
            for j in range(index, self._size - 1):
                self._arr[j] = self._arr[j + 1]
            # Update the number of elements
            self._size -= 1
            # Return the removed element
            return num
    
        def extend_capacity(self):
            """Extend list capacity"""
            # Create a new array with length _extend_ratio times the original array, and copy the original array to the new array
            self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
            # Update list capacity
            self._capacity = len(self._arr)
    
        def to_array(self) -> list[int]:
            """Return list with valid length"""
            return self._arr[: self._size]
    ```
=== "C++"
    ```cpp title="my_list.cpp"
    class MyList {
      private:
        int *arr;             // Array (stores list elements)
        int arrCapacity = 10; // List capacity
        int arrSize = 0;      // List length (current number of elements)
        int extendRatio = 2;   // Multiple by which the list capacity is extended each time
    
      public:
        /* Constructor */
        MyList() {
            arr = new int[arrCapacity];
        }
    
        /* Destructor */
        ~MyList() {
            delete[] arr;
        }
    
        /* Get list length (current number of elements)*/
        int size() {
            return arrSize;
        }
    
        /* Get list capacity */
        int capacity() {
            return arrCapacity;
        }
    
        /* Update element */
        int get(int index) {
            // If the index is out of bounds, throw an exception, as below
            if (index < 0 || index >= size())
                throw out_of_range("Index out of bounds");
            return arr[index];
        }
    
        /* Add elements at the end */
        void set(int index, int num) {
            if (index < 0 || index >= size())
                throw out_of_range("Index out of bounds");
            arr[index] = num;
        }
    
        /* Direct traversal of list elements */
        void add(int num) {
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (size() == capacity())
                extendCapacity();
            arr[size()] = num;
            // Update the number of elements
            arrSize++;
        }
    
        /* Sort list */
        void insert(int index, int num) {
            if (index < 0 || index >= size())
                throw out_of_range("Index out of bounds");
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (size() == capacity())
                extendCapacity();
            // Move all elements after index index forward by one position
            for (int j = size() - 1; j >= index; j--) {
                arr[j + 1] = arr[j];
            }
            arr[index] = num;
            // Update the number of elements
            arrSize++;
        }
    
        /* Remove element */
        int remove(int index) {
            if (index < 0 || index >= size())
                throw out_of_range("Index out of bounds");
            int num = arr[index];
            // Create a new array with length _extend_ratio times the original array, and copy the original array to the new array
            for (int j = index; j < size() - 1; j++) {
                arr[j] = arr[j + 1];
            }
            // Update the number of elements
            arrSize--;
            // Return the removed element
            return num;
        }
    
        /* Driver Code */
        void extendCapacity() {
            // Create a new array with length extendRatio times the original array
            int newCapacity = capacity() * extendRatio;
            int *tmp = arr;
            arr = new int[newCapacity];
            // Copy all elements from the original array to the new array
            for (int i = 0; i < size(); i++) {
                arr[i] = tmp[i];
            }
            // Free memory
            delete[] tmp;
            arrCapacity = newCapacity;
        }
    
        /* Convert list to Vector for printing */
        vector<int> toVector() {
            // Elements enqueue
            vector<int> vec(size());
            for (int i = 0; i < size(); i++) {
                vec[i] = arr[i];
            }
            return vec;
        }
    };
    ```
=== "Java"
    ```java title="my_list.java"
    class MyList {
        private int[] arr; // Array (stores list elements)
        private int capacity = 10; // List capacity
        private int size = 0; // List length (current number of elements)
        private int extendRatio = 2; // Multiple by which the list capacity is extended each time
    
        /* Constructor */
        public MyList() {
            arr = new int[capacity];
        }
    
        /* Get list length (current number of elements) */
        public int size() {
            return size;
        }
    
        /* Get list capacity */
        public int capacity() {
            return capacity;
        }
    
        /* Update element */
        public int get(int index) {
            // If the index is out of bounds, throw an exception, as below
            if (index < 0 || index >= size)
                throw new IndexOutOfBoundsException("Index out of bounds");
            return arr[index];
        }
    
        /* Add elements at the end */
        public void set(int index, int num) {
            if (index < 0 || index >= size)
                throw new IndexOutOfBoundsException("Index out of bounds");
            arr[index] = num;
        }
    
        /* Direct traversal of list elements */
        public void add(int num) {
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (size == capacity())
                extendCapacity();
            arr[size] = num;
            // Update the number of elements
            size++;
        }
    
        /* Sort list */
        public void insert(int index, int num) {
            if (index < 0 || index >= size)
                throw new IndexOutOfBoundsException("Index out of bounds");
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (size == capacity())
                extendCapacity();
            // Move all elements after index index forward by one position
            for (int j = size - 1; j >= index; j--) {
                arr[j + 1] = arr[j];
            }
            arr[index] = num;
            // Update the number of elements
            size++;
        }
    
        /* Remove element */
        public int remove(int index) {
            if (index < 0 || index >= size)
                throw new IndexOutOfBoundsException("Index out of bounds");
            int num = arr[index];
            // Move all elements after index forward by one position
            for (int j = index; j < size - 1; j++) {
                arr[j] = arr[j + 1];
            }
            // Update the number of elements
            size--;
            // Return the removed element
            return num;
        }
    
        /* Driver Code */
        public void extendCapacity() {
            // Create a new array with length extendRatio times the original array and copy the original array to the new array
            arr = Arrays.copyOf(arr, capacity() * extendRatio);
            // Add elements at the end
            capacity = arr.length;
        }
    
        /* Convert list to array */
        public int[] toArray() {
            int size = size();
            // Elements enqueue
            int[] arr = new int[size];
            for (int i = 0; i < size; i++) {
                arr[i] = get(i);
            }
            return arr;
        }
    }
    ```
=== "C#"
    ```csharp title="my_list.cs"
    class MyList {
        private int[] arr;           // Array (stores list elements)
        private int arrCapacity = 10;    // List capacity
        private int arrSize = 0;         // List length (current number of elements)
        private readonly int extendRatio = 2;  // Multiple by which the list capacity is extended each time
    
        /* Constructor */
        public MyList() {
            arr = new int[arrCapacity];
        }
    
        /* Get list length (current number of elements) */
        public int Size() {
            return arrSize;
        }
    
        /* Get list capacity */
        public int Capacity() {
            return arrCapacity;
        }
    
        /* Update element */
        public int Get(int index) {
            // If the index is out of bounds, throw an exception, as below
            if (index < 0 || index >= arrSize)
                throw new IndexOutOfRangeException("Index out of bounds");
            return arr[index];
        }
    
        /* Add elements at the end */
        public void Set(int index, int num) {
            if (index < 0 || index >= arrSize)
                throw new IndexOutOfRangeException("Index out of bounds");
            arr[index] = num;
        }
    
        /* Direct traversal of list elements */
        public void Add(int num) {
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (arrSize == arrCapacity)
                ExtendCapacity();
            arr[arrSize] = num;
            // Update the number of elements
            arrSize++;
        }
    
        /* Sort list */
        public void Insert(int index, int num) {
            if (index < 0 || index >= arrSize)
                throw new IndexOutOfRangeException("Index out of bounds");
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (arrSize == arrCapacity)
                ExtendCapacity();
            // Move all elements after index index forward by one position
            for (int j = arrSize - 1; j >= index; j--) {
                arr[j + 1] = arr[j];
            }
            arr[index] = num;
            // Update the number of elements
            arrSize++;
        }
    
        /* Remove element */
        public int Remove(int index) {
            if (index < 0 || index >= arrSize)
                throw new IndexOutOfRangeException("Index out of bounds");
            int num = arr[index];
            // Move all elements after index forward by one position
            for (int j = index; j < arrSize - 1; j++) {
                arr[j] = arr[j + 1];
            }
            // Update the number of elements
            arrSize--;
            // Return the removed element
            return num;
        }
    
        /* Driver Code */
        public void ExtendCapacity() {
            // Create new array of length arrCapacity * extendRatio and copy original array to new array
            Array.Resize(ref arr, arrCapacity * extendRatio);
            // Add elements at the end
            arrCapacity = arr.Length;
        }
    
        /* Convert list to array */
        public int[] ToArray() {
            // Elements enqueue
            int[] arr = new int[arrSize];
            for (int i = 0; i < arrSize; i++) {
                arr[i] = Get(i);
            }
            return arr;
        }
    }
    ```
=== "Go"
    ```go title="my_list.go"
    type myList struct {
    	arrCapacity int
    	arr         []int
    	arrSize     int
    	extendRatio int
    }
    ```
=== "Swift"
    ```swift title="my_list.swift"
    class MyList {
        private var arr: [Int] // Array (stores list elements)
        private var _capacity: Int // List capacity
        private var _size: Int // List length (current number of elements)
        private let extendRatio: Int // Multiple by which the list capacity is extended each time
    
        /* Constructor */
        init() {
            _capacity = 10
            _size = 0
            extendRatio = 2
            arr = Array(repeating: 0, count: _capacity)
        }
    
        /* Get list length (current number of elements) */
        func size() -> Int {
            _size
        }
    
        /* Get list capacity */
        func capacity() -> Int {
            _capacity
        }
    
        /* Update element */
        func get(index: Int) -> Int {
            // Throw error if index out of bounds, same below
            if index < 0 || index >= size() {
                fatalError("Index out of bounds")
            }
            return arr[index]
        }
    
        /* Add elements at the end */
        func set(index: Int, num: Int) {
            if index < 0 || index >= size() {
                fatalError("Index out of bounds")
            }
            arr[index] = num
        }
    
        /* Direct traversal of list elements */
        func add(num: Int) {
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if size() == capacity() {
                extendCapacity()
            }
            arr[size()] = num
            // Update the number of elements
            _size += 1
        }
    
        /* Sort list */
        func insert(index: Int, num: Int) {
            if index < 0 || index >= size() {
                fatalError("Index out of bounds")
            }
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if size() == capacity() {
                extendCapacity()
            }
            // Move all elements after index index forward by one position
            for j in (index ..< size()).reversed() {
                arr[j + 1] = arr[j]
            }
            arr[index] = num
            // Update the number of elements
            _size += 1
        }
    
        /* Remove element */
        @discardableResult
        func remove(index: Int) -> Int {
            if index < 0 || index >= size() {
                fatalError("Index out of bounds")
            }
            let num = arr[index]
            // Move all elements after index forward by one position
            for j in index ..< (size() - 1) {
                arr[j] = arr[j + 1]
            }
            // Update the number of elements
            _size -= 1
            // Return the removed element
            return num
        }
    
        /* Driver Code */
        func extendCapacity() {
            // Create a new array with length extendRatio times the original array and copy the original array to the new array
            arr = arr + Array(repeating: 0, count: capacity() * (extendRatio - 1))
            // Add elements at the end
            _capacity = arr.count
        }
    
        /* Convert list to array */
        func toArray() -> [Int] {
            Array(arr.prefix(size()))
        }
    }
    ```
=== "JS"
    ```javascript title="my_list.js"
    class MyList {
        #arr = new Array(); // Array (stores list elements)
        #capacity = 10; // List capacity
        #size = 0; // List length (current number of elements)
        #extendRatio = 2; // Multiple by which the list capacity is extended each time
    
        /* Constructor */
        constructor() {
            this.#arr = new Array(this.#capacity);
        }
    
        /* Get list length (current number of elements) */
        size() {
            return this.#size;
        }
    
        /* Get list capacity */
        capacity() {
            return this.#capacity;
        }
    
        /* Update element */
        get(index) {
            // If the index is out of bounds, throw an exception, as below
            if (index < 0 || index >= this.#size) throw new Error('Index out of bounds');
            return this.#arr[index];
        }
    
        /* Add elements at the end */
        set(index, num) {
            if (index < 0 || index >= this.#size) throw new Error('Index out of bounds');
            this.#arr[index] = num;
        }
    
        /* Direct traversal of list elements */
        add(num) {
            // If length equals capacity, need to expand
            if (this.#size === this.#capacity) {
                this.extendCapacity();
            }
            // Add new element to end of list
            this.#arr[this.#size] = num;
            this.#size++;
        }
    
        /* Sort list */
        insert(index, num) {
            if (index < 0 || index >= this.#size) throw new Error('Index out of bounds');
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (this.#size === this.#capacity) {
                this.extendCapacity();
            }
            // Move all elements after index index forward by one position
            for (let j = this.#size - 1; j >= index; j--) {
                this.#arr[j + 1] = this.#arr[j];
            }
            // Update the number of elements
            this.#arr[index] = num;
            this.#size++;
        }
    
        /* Remove element */
        remove(index) {
            if (index < 0 || index >= this.#size) throw new Error('Index out of bounds');
            let num = this.#arr[index];
            // Create a new array with length _extend_ratio times the original array, and copy the original array to the new array
            for (let j = index; j < this.#size - 1; j++) {
                this.#arr[j] = this.#arr[j + 1];
            }
            // Update the number of elements
            this.#size--;
            // Return the removed element
            return num;
        }
    
        /* Driver Code */
        extendCapacity() {
            // Create a new array with length extendRatio times the original array and copy the original array to the new array
            this.#arr = this.#arr.concat(
                new Array(this.capacity() * (this.#extendRatio - 1))
            );
            // Add elements at the end
            this.#capacity = this.#arr.length;
        }
    
        /* Convert list to array */
        toArray() {
            let size = this.size();
            // Elements enqueue
            const arr = new Array(size);
            for (let i = 0; i < size; i++) {
                arr[i] = this.get(i);
            }
            return arr;
        }
    }
    ```
=== "TS"
    ```typescript title="my_list.ts"
    class MyList {
        private arr: Array<number>; // Array (stores list elements)
        private _capacity: number = 10; // List capacity
        private _size: number = 0; // List length (current number of elements)
        private extendRatio: number = 2; // Multiple by which the list capacity is extended each time
    
        /* Constructor */
        constructor() {
            this.arr = new Array(this._capacity);
        }
    
        /* Get list length (current number of elements) */
        public size(): number {
            return this._size;
        }
    
        /* Get list capacity */
        public capacity(): number {
            return this._capacity;
        }
    
        /* Update element */
        public get(index: number): number {
            // If the index is out of bounds, throw an exception, as below
            if (index < 0 || index >= this._size) throw new Error('Index out of bounds');
            return this.arr[index];
        }
    
        /* Add elements at the end */
        public set(index: number, num: number): void {
            if (index < 0 || index >= this._size) throw new Error('Index out of bounds');
            this.arr[index] = num;
        }
    
        /* Direct traversal of list elements */
        public add(num: number): void {
            // If length equals capacity, need to expand
            if (this._size === this._capacity) this.extendCapacity();
            // Add new element to end of list
            this.arr[this._size] = num;
            this._size++;
        }
    
        /* Sort list */
        public insert(index: number, num: number): void {
            if (index < 0 || index >= this._size) throw new Error('Index out of bounds');
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (this._size === this._capacity) {
                this.extendCapacity();
            }
            // Move all elements after index index forward by one position
            for (let j = this._size - 1; j >= index; j--) {
                this.arr[j + 1] = this.arr[j];
            }
            // Update the number of elements
            this.arr[index] = num;
            this._size++;
        }
    
        /* Remove element */
        public remove(index: number): number {
            if (index < 0 || index >= this._size) throw new Error('Index out of bounds');
            let num = this.arr[index];
            // Move all elements after index forward by one position
            for (let j = index; j < this._size - 1; j++) {
                this.arr[j] = this.arr[j + 1];
            }
            // Update the number of elements
            this._size--;
            // Return the removed element
            return num;
        }
    
        /* Driver Code */
        public extendCapacity(): void {
            // Create new array of length size and copy original array to new array
            this.arr = this.arr.concat(
                new Array(this.capacity() * (this.extendRatio - 1))
            );
            // Add elements at the end
            this._capacity = this.arr.length;
        }
    
        /* Convert list to array */
        public toArray(): number[] {
            let size = this.size();
            // Elements enqueue
            const arr = new Array(size);
            for (let i = 0; i < size; i++) {
                arr[i] = this.get(i);
            }
            return arr;
        }
    }
    ```
=== "Dart"
    ```dart title="my_list.dart"
    class MyList {
      late List<int> _arr; // Array (stores list elements)
      int _capacity = 10; // List capacity
      int _size = 0; // List length (current number of elements)
      int _extendRatio = 2; // Multiple by which the list capacity is extended each time
    
      /* Constructor */
      MyList() {
        _arr = List.filled(_capacity, 0);
      }
    
      /* Get list length (current number of elements) */
      int size() => _size;
    
      /* Get list capacity */
      int capacity() => _capacity;
    
      /* Update element */
      int get(int index) {
        if (index >= _size) throw RangeError('Index out of bounds');
        return _arr[index];
      }
    
      /* Add elements at the end */
      void set(int index, int _num) {
        if (index >= _size) throw RangeError('Index out of bounds');
        _arr[index] = _num;
      }
    
      /* Direct traversal of list elements */
      void add(int _num) {
        // When the number of elements exceeds capacity, trigger the extension mechanism
        if (_size == _capacity) extendCapacity();
        _arr[_size] = _num;
        // Update the number of elements
        _size++;
      }
    
      /* Sort list */
      void insert(int index, int _num) {
        if (index >= _size) throw RangeError('Index out of bounds');
        // When the number of elements exceeds capacity, trigger the extension mechanism
        if (_size == _capacity) extendCapacity();
        // Move all elements after index index forward by one position
        for (var j = _size - 1; j >= index; j--) {
          _arr[j + 1] = _arr[j];
        }
        _arr[index] = _num;
        // Update the number of elements
        _size++;
      }
    
      /* Remove element */
      int remove(int index) {
        if (index >= _size) throw RangeError('Index out of bounds');
        int _num = _arr[index];
        // Move all elements after index forward by one position
        for (var j = index; j < _size - 1; j++) {
          _arr[j] = _arr[j + 1];
        }
        // Update the number of elements
        _size--;
        // Return the removed element
        return _num;
      }
    
      /* Driver Code */
      void extendCapacity() {
        // Create new array with length _extendRatio times original array
        final _newNums = List.filled(_capacity * _extendRatio, 0);
        // Copy original array to new array
        List.copyRange(_newNums, 0, _arr);
        // Update _arr reference
        _arr = _newNums;
        // Add elements at the end
        _capacity = _arr.length;
      }
    
      /* Convert list to array */
      List<int> toArray() {
        List<int> arr = [];
        for (var i = 0; i < _size; i++) {
          arr.add(get(i));
        }
        return arr;
      }
    }
    ```
=== "Rust"
    ```rust title="my_list.rs"
    #[allow(dead_code)]
    struct MyList {
        arr: Vec<i32>,       // Array (stores list elements)
        capacity: usize,     // List capacity
        size: usize,         // List length (current number of elements)
        extend_ratio: usize, // Multiple by which the list capacity is extended each time
    }
    ```
=== "C"
    ```c title="my_list.c"
    void extendCapacity(MyList *nums);
    
    /* Constructor */
    MyList *newMyList() {
        MyList *nums = malloc(sizeof(MyList));
        nums->capacity = 10;
        nums->arr = malloc(sizeof(int) * nums->capacity);
        nums->size = 0;
        nums->extendRatio = 2;
        return nums;
    }
    ```
=== "Kotlin"
    ```kotlin title="my_list.kt"
    class MyList {
        private var arr: IntArray = intArrayOf() // Array (stores list elements)
        private var capacity: Int = 10 // List capacity
        private var size: Int = 0 // List length (current number of elements)
        private var extendRatio: Int = 2 // Multiple by which the list capacity is extended each time
    
        /* Constructor */
        init {
            arr = IntArray(capacity)
        }
    
        /* Get list length (current number of elements) */
        fun size(): Int {
            return size
        }
    
        /* Get list capacity */
        fun capacity(): Int {
            return capacity
        }
    
        /* Update element */
        fun get(index: Int): Int {
            // If the index is out of bounds, throw an exception, as below
            if (index < 0 || index >= size)
                throw IndexOutOfBoundsException("Index out of bounds")
            return arr[index]
        }
    
        /* Add elements at the end */
        fun set(index: Int, num: Int) {
            if (index < 0 || index >= size)
                throw IndexOutOfBoundsException("Index out of bounds")
            arr[index] = num
        }
    
        /* Direct traversal of list elements */
        fun add(num: Int) {
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (size == capacity())
                extendCapacity()
            arr[size] = num
            // Update the number of elements
            size++
        }
    
        /* Sort list */
        fun insert(index: Int, num: Int) {
            if (index < 0 || index >= size)
                throw IndexOutOfBoundsException("Index out of bounds")
            // When the number of elements exceeds capacity, trigger the extension mechanism
            if (size == capacity())
                extendCapacity()
            // Move all elements after index index forward by one position
            for (j in size - 1 downTo index)
                arr[j + 1] = arr[j]
            arr[index] = num
            // Update the number of elements
            size++
        }
    
        /* Remove element */
        fun remove(index: Int): Int {
            if (index < 0 || index >= size)
                throw IndexOutOfBoundsException("Index out of bounds")
            val num = arr[index]
            // Move all elements after index forward by one position
            for (j in index..<size - 1)
                arr[j] = arr[j + 1]
            // Update the number of elements
            size--
            // Return the removed element
            return num
        }
    
        /* Driver Code */
        fun extendCapacity() {
            // Create a new array with length extendRatio times the original array and copy the original array to the new array
            arr = arr.copyOf(capacity() * extendRatio)
            // Add elements at the end
            capacity = arr.size
        }
    
        /* Convert list to array */
        fun toArray(): IntArray {
            val size = size()
            // Elements enqueue
            val arr = IntArray(size)
            for (i in 0..<size) {
                arr[i] = get(i)
            }
            return arr
        }
    }
    ```
=== "Ruby"
    ```ruby title="my_list.rb"
    ### List class ###
    class MyList
      attr_reader :size       # Get list length (current number of elements)
      attr_reader :capacity   # Get list capacity
    
      ### Constructor ###
      def initialize
        @capacity = 10
        @size = 0
        @extend_ratio = 2
        @arr = Array.new(capacity)
      end
    
      ### Access element ###
      def get(index)
        # If the index is out of bounds, throw an exception, as below
        raise IndexError, "Index out of bounds" if index < 0 || index >= size
        @arr[index]
      end
    
      ### Access element ###
      def set(index, num)
        raise IndexError, "Index out of bounds" if index < 0 || index >= size
        @arr[index] = num
      end
    
      ### Add element at end ###
      def add(num)
        # When the number of elements exceeds capacity, trigger the extension mechanism
        extend_capacity if size == capacity
        @arr[size] = num
    
        # Update the number of elements
        @size += 1
      end
    
      ### Insert element in middle ###
      def insert(index, num)
        raise IndexError, "Index out of bounds" if index < 0 || index >= size
    
        # When the number of elements exceeds capacity, trigger the extension mechanism
        extend_capacity if size == capacity
    
        # Move all elements after index index forward by one position
        for j in (size - 1).downto(index)
          @arr[j + 1] = @arr[j]
        end
        @arr[index] = num
    
        # Update the number of elements
        @size += 1
      end
    
      ### Delete element ###
      def remove(index)
        raise IndexError, "Index out of bounds" if index < 0 || index >= size
        num = @arr[index]
    
        # Move all elements after index forward by one position
        for j in index...size
          @arr[j] = @arr[j + 1]
        end
    
        # Update the number of elements
        @size -= 1
    
        # Return the removed element
        num
      end
    
      ### Expand list capacity ###
      def extend_capacity
        # Create new array with length extend_ratio times original, copy original array to new array
        arr = @arr.dup + Array.new(capacity * (@extend_ratio - 1))
        # Add elements at the end
        @capacity = arr.length
      end
    
      ### Convert list to array ###
      def to_array
        sz = size
        # Elements enqueue
        arr = Array.new(sz)
        for i in 0...sz
          arr[i] = get(i)
        end
        arr
      end
    ```

