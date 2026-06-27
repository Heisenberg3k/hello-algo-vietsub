# Chiến lược tối ưu hóa hàm băm

Trong các bài toán về thuật toán, **chúng tôi thường giảm độ phức tạp về thời gian của thuật toán bằng cách thay thế tìm kiếm tuyến tính bằng tìm kiếm dựa trên hàm băm**. Hãy sử dụng một vấn đề thuật toán để hiểu sâu hơn.

!!! câu hỏi

Cho một mảng số nguyên `nums` và một giá trị đích `target`, tìm hai phần tử trong mảng có tổng là `target` và trả về chỉ số của chúng. Giải pháp nào cũng được.

## Tìm kiếm tuyến tính: Đánh đổi thời gian lấy không gian

Xem xét việc duyệt trực tiếp tất cả các kết hợp có thể. Như được hiển thị trong hình bên dưới, chúng tôi sử dụng các vòng lặp lồng nhau và kiểm tra mỗi lần lặp xem tổng của hai số nguyên có phải là `target` hay không. Nếu vậy, hãy trả lại chỉ số của họ.

![Linear search solution for two sum](replace_linear_by_hashing.assets/two_sum_brute_force.png)

Mã được hiển thị dưới đây:

=== "Python"
    ```python title="two_sum.py"
    def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
        """Method 1: Brute force enumeration"""
        # Two nested loops, time complexity is O(n^2)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    ```
=== "C++"
    ```cpp title="two_sum.cpp"
    vector<int> twoSumBruteForce(vector<int> &nums, int target) {
        int size = nums.size();
        // Two nested loops, time complexity is O(n^2)
        for (int i = 0; i < size - 1; i++) {
            for (int j = i + 1; j < size; j++) {
                if (nums[i] + nums[j] == target)
                    return {i, j};
            }
        }
        return {};
    }
    ```
=== "Java"
    ```java title="two_sum.java"
    static int[] twoSumBruteForce(int[] nums, int target) {
            int size = nums.length;
            // Two nested loops, time complexity is O(n^2)
            for (int i = 0; i < size - 1; i++) {
                for (int j = i + 1; j < size; j++) {
                    if (nums[i] + nums[j] == target)
                        return new int[] { i, j };
                }
            }
            return new int[0];
        }
    ```
=== "C#"
    ```csharp title="two_sum.cs"
    int[] TwoSumBruteForce(int[] nums, int target) {
            int size = nums.Length;
            // Two nested loops, time complexity is O(n^2)
            for (int i = 0; i < size - 1; i++) {
                for (int j = i + 1; j < size; j++) {
                    if (nums[i] + nums[j] == target)
                        return [i, j];
                }
            }
            return [];
        }
    ```
=== "Go"
    ```go title="two_sum.go"
    func twoSumBruteForce(nums []int, target int) []int {
    	size := len(nums)
    	// Two nested loops, time complexity is O(n^2)
    	for i := 0; i < size-1; i++ {
    		for j := i + 1; j < size; j++ {
    			if nums[i]+nums[j] == target {
    				return []int{i, j}
    			}
    		}
    	}
    	return nil
    }
    ```
=== "Swift"
    ```swift title="two_sum.swift"
    func twoSumBruteForce(nums: [Int], target: Int) -> [Int] {
        // Two nested loops, time complexity is O(n^2)
        for i in nums.indices.dropLast() {
            for j in nums.indices.dropFirst(i + 1) {
                if nums[i] + nums[j] == target {
                    return [i, j]
                }
            }
        }
        return [0]
    }
    ```
=== "JS"
    ```javascript title="two_sum.js"
    function twoSumBruteForce(nums, target) {
        const n = nums.length;
        // Two nested loops, time complexity is O(n^2)
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] === target) {
                    return [i, j];
                }
            }
        }
        return [];
    }
    ```
=== "TS"
    ```typescript title="two_sum.ts"
    function twoSumBruteForce(nums: number[], target: number): number[] {
        const n = nums.length;
        // Two nested loops, time complexity is O(n^2)
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] === target) {
                    return [i, j];
                }
            }
        }
        return [];
    }
    ```
=== "Dart"
    ```dart title="two_sum.dart"
    List<int> twoSumBruteForce(List<int> nums, int target) {
      int size = nums.length;
      // Two nested loops, time complexity is O(n^2)
      for (var i = 0; i < size - 1; i++) {
        for (var j = i + 1; j < size; j++) {
          if (nums[i] + nums[j] == target) return [i, j];
        }
      }
      return [0];
    }
    ```
=== "Rust"
    ```rust title="two_sum.rs"
    pub fn two_sum_brute_force(nums: &Vec<i32>, target: i32) -> Option<Vec<i32>> {
        let size = nums.len();
        // Two nested loops, time complexity is O(n^2)
        for i in 0..size - 1 {
            for j in i + 1..size {
                if nums[i] + nums[j] == target {
                    return Some(vec![i as i32, j as i32]);
                }
            }
        }
        None
    }
    ```
=== "C"
    ```c title="two_sum.c"
    int *twoSumBruteForce(int *nums, int numsSize, int target, int *returnSize) {
        for (int i = 0; i < numsSize; ++i) {
            for (int j = i + 1; j < numsSize; ++j) {
                if (nums[i] + nums[j] == target) {
                    int *res = malloc(sizeof(int) * 2);
                    res[0] = i, res[1] = j;
                    *returnSize = 2;
                    return res;
                }
            }
        }
        *returnSize = 0;
        return NULL;
    }
    ```
=== "Kotlin"
    ```kotlin title="two_sum.kt"
    fun twoSumBruteForce(nums: IntArray, target: Int): IntArray {
        val size = nums.size
        // Two nested loops, time complexity is O(n^2)
        for (i in 0..<size - 1) {
            for (j in i + 1..<size) {
                if (nums[i] + nums[j] == target) return intArrayOf(i, j)
            }
        }
        return IntArray(0)
    }
    ```
=== "Ruby"
    ```ruby title="two_sum.rb"
    ### Method 1: Brute force enumeration ###
    def two_sum_brute_force(nums, target)
      # Two nested loops, time complexity is O(n^2)
      for i in 0...(nums.length - 1)
        for j in (i + 1)...nums.length
          return [i, j] if nums[i] + nums[j] == target
        end
      end
    
      []
    ```


Phương thức này có độ phức tạp về thời gian là $O(n^2)$ và độ phức tạp về không gian là $O(1)$, khiến nó rất tốn thời gian đối với các đầu vào lớn.

## Tìm kiếm dựa trên hàm băm: Trao đổi không gian lấy thời gian

Hãy cân nhắc sử dụng bảng băm có khóa là các phần tử mảng và giá trị là chỉ mục của chúng. Duyệt mảng và thực hiện các bước được hiển thị trong hình bên dưới trong mỗi lần lặp:

1. Kiểm tra xem số `target - nums[i]` có trong bảng băm hay không. Nếu vậy, hãy trả về trực tiếp chỉ số của hai phần tử này.
2. Thêm cặp khóa-giá trị `nums[i]` và chỉ mục `i` vào bảng băm.

=== "<1>"
    ![Hash table solution for two sum](replace_linear_by_hashing.assets/two_sum_hashtable_step1.png)

=== "<2>"
    ![two_sum_hashtable_step2](replace_linear_by_hashing.assets/two_sum_hashtable_step2.png)

=== "<3>"
    ![two_sum_hashtable_step3](replace_linear_by_hashing.assets/two_sum_hashtable_step3.png)

Việc triển khai được hiển thị bên dưới và chỉ yêu cầu một vòng lặp duy nhất:

=== "Python"
    ```python title="two_sum.py"
    def two_sum_hash_table(nums: list[int], target: int) -> list[int]:
        """Method 2: Auxiliary hash table"""
        # Auxiliary hash table, space complexity is O(n)
        dic = {}
        # Single loop, time complexity is O(n)
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i
        return []
    ```
=== "C++"
    ```cpp title="two_sum.cpp"
    vector<int> twoSumHashTable(vector<int> &nums, int target) {
        int size = nums.size();
        // Auxiliary hash table, space complexity is O(n)
        unordered_map<int, int> dic;
        // Single loop, time complexity is O(n)
        for (int i = 0; i < size; i++) {
            if (dic.find(target - nums[i]) != dic.end()) {
                return {dic[target - nums[i]], i};
            }
            dic.emplace(nums[i], i);
        }
        return {};
    }
    ```
=== "Java"
    ```java title="two_sum.java"
    static int[] twoSumHashTable(int[] nums, int target) {
            int size = nums.length;
            // Auxiliary hash table, space complexity is O(n)
            Map<Integer, Integer> dic = new HashMap<>();
            // Single loop, time complexity is O(n)
            for (int i = 0; i < size; i++) {
                if (dic.containsKey(target - nums[i])) {
                    return new int[] { dic.get(target - nums[i]), i };
                }
                dic.put(nums[i], i);
            }
            return new int[0];
        }
    ```
=== "C#"
    ```csharp title="two_sum.cs"
    int[] TwoSumHashTable(int[] nums, int target) {
            int size = nums.Length;
            // Auxiliary hash table, space complexity is O(n)
            Dictionary<int, int> dic = [];
            // Single loop, time complexity is O(n)
            for (int i = 0; i < size; i++) {
                if (dic.ContainsKey(target - nums[i])) {
                    return [dic[target - nums[i]], i];
                }
                dic.Add(nums[i], i);
            }
            return [];
        }
    ```
=== "Go"
    ```go title="two_sum.go"
    func twoSumHashTable(nums []int, target int) []int {
    	// Auxiliary hash table, space complexity is O(n)
    	hashTable := map[int]int{}
    	// Single loop, time complexity is O(n)
    	for idx, val := range nums {
    		if preIdx, ok := hashTable[target-val]; ok {
    			return []int{preIdx, idx}
    		}
    		hashTable[val] = idx
    	}
    	return nil
    }
    ```
=== "Swift"
    ```swift title="two_sum.swift"
    func twoSumHashTable(nums: [Int], target: Int) -> [Int] {
        // Auxiliary hash table, space complexity is O(n)
        var dic: [Int: Int] = [:]
        // Single loop, time complexity is O(n)
        for i in nums.indices {
            if let j = dic[target - nums[i]] {
                return [j, i]
            }
            dic[nums[i]] = i
        }
        return [0]
    }
    ```
=== "JS"
    ```javascript title="two_sum.js"
    function twoSumHashTable(nums, target) {
        // Auxiliary hash table, space complexity is O(n)
        let m = {};
        // Single loop, time complexity is O(n)
        for (let i = 0; i < nums.length; i++) {
            if (m[target - nums[i]] !== undefined) {
                return [m[target - nums[i]], i];
            } else {
                m[nums[i]] = i;
            }
        }
        return [];
    }
    ```
=== "TS"
    ```typescript title="two_sum.ts"
    function twoSumHashTable(nums: number[], target: number): number[] {
        // Auxiliary hash table, space complexity is O(n)
        let m: Map<number, number> = new Map();
        // Single loop, time complexity is O(n)
        for (let i = 0; i < nums.length; i++) {
            let index = m.get(target - nums[i]);
            if (index !== undefined) {
                return [index, i];
            } else {
                m.set(nums[i], i);
            }
        }
        return [];
    }
    ```
=== "Dart"
    ```dart title="two_sum.dart"
    List<int> twoSumHashTable(List<int> nums, int target) {
      int size = nums.length;
      // Auxiliary hash table, space complexity is O(n)
      Map<int, int> dic = HashMap();
      // Single loop, time complexity is O(n)
      for (var i = 0; i < size; i++) {
        if (dic.containsKey(target - nums[i])) {
          return [dic[target - nums[i]]!, i];
        }
        dic.putIfAbsent(nums[i], () => i);
      }
      return [0];
    }
    ```
=== "Rust"
    ```rust title="two_sum.rs"
    pub fn two_sum_hash_table(nums: &Vec<i32>, target: i32) -> Option<Vec<i32>> {
        // Auxiliary hash table, space complexity is O(n)
        let mut dic = HashMap::new();
        // Single loop, time complexity is O(n)
        for (i, num) in nums.iter().enumerate() {
            match dic.get(&(target - num)) {
                Some(v) => return Some(vec![*v as i32, i as i32]),
                None => dic.insert(num, i as i32),
            };
        }
        None
    }
    ```
=== "C"
    ```c title="two_sum.c"
    int *twoSumHashTable(int *nums, int numsSize, int target, int *returnSize) {
        HashTable *hashtable = NULL;
        for (int i = 0; i < numsSize; i++) {
            HashTable *t = find(hashtable, target - nums[i]);
            if (t != NULL) {
                int *res = malloc(sizeof(int) * 2);
                res[0] = t->val, res[1] = i;
                *returnSize = 2;
                return res;
            }
            insert(&hashtable, nums[i], i);
        }
        *returnSize = 0;
        return NULL;
    }
    ```
=== "Kotlin"
    ```kotlin title="two_sum.kt"
    fun twoSumHashTable(nums: IntArray, target: Int): IntArray {
        val size = nums.size
        // Auxiliary hash table, space complexity is O(n)
        val dic = HashMap<Int, Int>()
        // Single loop, time complexity is O(n)
        for (i in 0..<size) {
            if (dic.containsKey(target - nums[i])) {
                return intArrayOf(dic[target - nums[i]]!!, i)
            }
            dic[nums[i]] = i
        }
        return IntArray(0)
    }
    ```
=== "Ruby"
    ```ruby title="two_sum.rb"
    ### Method 2: Auxiliary hash table ###
    def two_sum_hash_table(nums, target)
      # Auxiliary hash table, space complexity is O(n)
      dic = {}
      # Single loop, time complexity is O(n)
      for i in 0...nums.length
        return [dic[target - nums[i]], i] if dic.has_key?(target - nums[i])
    
        dic[nums[i]] = i
      end
    
      []
    ```


Phương pháp này giảm độ phức tạp về thời gian từ $O(n^2)$ xuống $O(n)$ thông qua tìm kiếm dựa trên hàm băm, cải thiện đáng kể hiệu quả thời gian chạy.

Vì cần phải duy trì một bảng băm bổ sung nên độ phức tạp của không gian là $O(n)$. **Tuy nhiên, phương pháp này mang lại sự cân bằng tổng thể về không gian-thời gian cân bằng hơn, khiến nó trở thành giải pháp tối ưu cho vấn đề này**.
