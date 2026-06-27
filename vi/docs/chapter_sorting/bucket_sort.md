# Sắp xếp nhóm

Các thuật toán sắp xếp được thảo luận trước đó đều là các thuật toán sắp xếp dựa trên so sánh, sắp xếp bằng cách so sánh thứ tự tương đối của các phần tử. Độ phức tạp về thời gian của các thuật toán như vậy không thể vượt qua $O(n \log n)$. Tiếp theo, chúng ta sẽ khám phá một số thuật toán sắp xếp không so sánh, độ phức tạp về thời gian của chúng có thể là tuyến tính.

<u>Bucket sort</u> is a typical application of the divide-and-conquer strategy. It works by creating a sequence of ordered buckets, each corresponding to a data range, and distributing the data evenly among them. The elements within each bucket are then sorted separately. Finally, all buckets are merged in order.

## Luồng thuật toán

Hãy xem xét một mảng có độ dài $n$, trong đó các phần tử của nó là các số có dấu phẩy động trong phạm vi $[0, 1)$. Luồng sắp xếp nhóm được hiển thị trong hình bên dưới.

1. Khởi tạo các nhóm $k$ và phân phối các phần tử $n$ vào các nhóm $k$.
2. Sắp xếp từng nhóm riêng biệt (ở đây chúng tôi sử dụng chức năng sắp xếp tích hợp sẵn của ngôn ngữ lập trình).
3. Hợp nhất các kết quả theo thứ tự từ nhóm nhỏ nhất đến lớn nhất.

![Bucket sort algorithm flow](bucket_sort.assets/bucket_sort_overview.png)

Mã này như sau:

=== "Python"
    ```python title="bucket_sort.py"
    def bucket_sort(nums: list[float]):
        """Bucket sort"""
        # Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
        k = len(nums) // 2
        buckets = [[] for _ in range(k)]
        # 1. Distribute array elements into various buckets
        for num in nums:
            # Input data range is [0, 1), use num * k to map to index range [0, k-1]
            i = int(num * k)
            # Add num to bucket i
            buckets[i].append(num)
        # 2. Sort each bucket
        for bucket in buckets:
            # Use built-in sorting function, can also replace with other sorting algorithms
            bucket.sort()
        # 3. Traverse buckets to merge results
        i = 0
        for bucket in buckets:
            for num in bucket:
                nums[i] = num
                i += 1
    ```
=== "C++"
    ```cpp title="bucket_sort.cpp"
    void bucketSort(vector<float> &nums) {
        // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
        int k = nums.size() / 2;
        vector<vector<float>> buckets(k);
        // 1. Distribute array elements into various buckets
        for (float num : nums) {
            // Input data range is [0, 1), use num * k to map to index range [0, k-1]
            int i = num * k;
            // Add num to bucket bucket_idx
            buckets[i].push_back(num);
        }
        // 2. Sort each bucket
        for (vector<float> &bucket : buckets) {
            // Use built-in sorting function, can also replace with other sorting algorithms
            sort(bucket.begin(), bucket.end());
        }
        // 3. Traverse buckets to merge results
        int i = 0;
        for (vector<float> &bucket : buckets) {
            for (float num : bucket) {
                nums[i++] = num;
            }
        }
    }
    ```
=== "Java"
    ```java title="bucket_sort.java"
    public class bucket_sort {
        /* Bucket sort */
        static void bucketSort(float[] nums) {
            // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
            int k = nums.length / 2;
            List<List<Float>> buckets = new ArrayList<>();
            for (int i = 0; i < k; i++) {
                buckets.add(new ArrayList<>());
            }
            // 1. Distribute array elements into various buckets
            for (float num : nums) {
                // Input data range is [0, 1), use num * k to map to index range [0, k-1]
                int i = (int) (num * k);
                // Add num to bucket i
                buckets.get(i).add(num);
            }
            // 2. Sort each bucket
            for (List<Float> bucket : buckets) {
                // Use built-in sorting function, can also replace with other sorting algorithms
                Collections.sort(bucket);
            }
            // 3. Traverse buckets to merge results
            int i = 0;
            for (List<Float> bucket : buckets) {
                for (float num : bucket) {
                    nums[i++] = num;
                }
            }
        }
    
        public static void main(String[] args) {
            // Assume input data is floating point, interval [0, 1)
            float[] nums = { 0.49f, 0.96f, 0.82f, 0.09f, 0.57f, 0.43f, 0.91f, 0.75f, 0.15f, 0.37f };
            bucketSort(nums);
            System.out.println("After bucket sort completes, nums = " + Arrays.toString(nums));
        }
    }
    ```
=== "C#"
    ```csharp title="bucket_sort.cs"
    public class bucket_sort {
        /* Bucket sort */
        void BucketSort(float[] nums) {
            // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
            int k = nums.Length / 2;
            List<List<float>> buckets = [];
            for (int i = 0; i < k; i++) {
                buckets.Add([]);
            }
            // 1. Distribute array elements into various buckets
            foreach (float num in nums) {
                // Input data range is [0, 1), use num * k to map to index range [0, k-1]
                int i = (int)(num * k);
                // Add num to bucket i
                buckets[i].Add(num);
            }
            // 2. Sort each bucket
            foreach (List<float> bucket in buckets) {
                // Use built-in sorting function, can also replace with other sorting algorithms
                bucket.Sort();
            }
            // 3. Traverse buckets to merge results
            int j = 0;
            foreach (List<float> bucket in buckets) {
                foreach (float num in bucket) {
                    nums[j++] = num;
                }
            }
        }
    
        [Test]
        public void Test() {
            // Assume input data is floating point, interval [0, 1)
            float[] nums = [0.49f, 0.96f, 0.82f, 0.09f, 0.57f, 0.43f, 0.91f, 0.75f, 0.15f, 0.37f];
            BucketSort(nums);
            Console.WriteLine("After bucket sort completes, nums = " + string.Join(" ", nums));
        }
    }
    ```
=== "Go"
    ```go title="bucket_sort.go"
    func bucketSort(nums []float64) {
    	// Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
    	k := len(nums) / 2
    	buckets := make([][]float64, k)
    	for i := 0; i < k; i++ {
    		buckets[i] = make([]float64, 0)
    	}
    	// 1. Distribute array elements into various buckets
    	for _, num := range nums {
    		// Input data range is [0, 1), use num * k to map to index range [0, k-1]
    		i := int(num * float64(k))
    		// Add num to bucket i
    		buckets[i] = append(buckets[i], num)
    	}
    	// 2. Sort each bucket
    	for i := 0; i < k; i++ {
    		// Use built-in slice sorting function, can also be replaced with other sorting algorithms
    		sort.Float64s(buckets[i])
    	}
    	// 3. Traverse buckets to merge results
    	i := 0
    	for _, bucket := range buckets {
    		for _, num := range bucket {
    			nums[i] = num
    			i++
    		}
    	}
    }
    ```
=== "Swift"
    ```swift title="bucket_sort.swift"
    func bucketSort(nums: inout [Double]) {
        // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
        let k = nums.count / 2
        var buckets = (0 ..< k).map { _ in [Double]() }
        // 1. Distribute array elements into various buckets
        for num in nums {
            // Input data range is [0, 1), use num * k to map to index range [0, k-1]
            let i = Int(num * Double(k))
            // Add num to bucket i
            buckets[i].append(num)
        }
        // 2. Sort each bucket
        for i in buckets.indices {
            // Use built-in sorting function, can also replace with other sorting algorithms
            buckets[i].sort()
        }
        // 3. Traverse buckets to merge results
        var i = nums.startIndex
        for bucket in buckets {
            for num in bucket {
                nums[i] = num
                i += 1
            }
        }
    }
    ```
=== "JS"
    ```javascript title="bucket_sort.js"
    function bucketSort(nums) {
        // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
        const k = nums.length / 2;
        const buckets = [];
        for (let i = 0; i < k; i++) {
            buckets.push([]);
        }
        // 1. Distribute array elements into various buckets
        for (const num of nums) {
            // Input data range is [0, 1), use num * k to map to index range [0, k-1]
            const i = Math.floor(num * k);
            // Add num to bucket i
            buckets[i].push(num);
        }
        // 2. Sort each bucket
        for (const bucket of buckets) {
            // Use built-in sorting function, can also replace with other sorting algorithms
            bucket.sort((a, b) => a - b);
        }
        // 3. Traverse buckets to merge results
        let i = 0;
        for (const bucket of buckets) {
            for (const num of bucket) {
                nums[i++] = num;
            }
        }
    }
    ```
=== "TS"
    ```typescript title="bucket_sort.ts"
    function bucketSort(nums: number[]): void {
        // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
        const k = nums.length / 2;
        const buckets: number[][] = [];
        for (let i = 0; i < k; i++) {
            buckets.push([]);
        }
        // 1. Distribute array elements into various buckets
        for (const num of nums) {
            // Input data range is [0, 1), use num * k to map to index range [0, k-1]
            const i = Math.floor(num * k);
            // Add num to bucket i
            buckets[i].push(num);
        }
        // 2. Sort each bucket
        for (const bucket of buckets) {
            // Use built-in sorting function, can also replace with other sorting algorithms
            bucket.sort((a, b) => a - b);
        }
        // 3. Traverse buckets to merge results
        let i = 0;
        for (const bucket of buckets) {
            for (const num of bucket) {
                nums[i++] = num;
            }
        }
    }
    ```
=== "Dart"
    ```dart title="bucket_sort.dart"
    void bucketSort(List<double> nums) {
      // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
      int k = nums.length ~/ 2;
      List<List<double>> buckets = List.generate(k, (index) => []);
    
      // 1. Distribute array elements into various buckets
      for (double _num in nums) {
        // Input data range is [0, 1), use _num * k to map to index range [0, k-1]
        int i = (_num * k).toInt();
        // Add _num to bucket bucket_idx
        buckets[i].add(_num);
      }
      // 2. Sort each bucket
      for (List<double> bucket in buckets) {
        bucket.sort();
      }
      // 3. Traverse buckets to merge results
      int i = 0;
      for (List<double> bucket in buckets) {
        for (double _num in bucket) {
          nums[i++] = _num;
        }
      }
    }
    ```
=== "Rust"
    ```rust title="bucket_sort.rs"
    fn bucket_sort(nums: &mut [f64]) {
        // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
        let k = nums.len() / 2;
        let mut buckets = vec![vec![]; k];
        // 1. Distribute array elements into various buckets
        for &num in nums.iter() {
            // Input data range is [0, 1), use num * k to map to index range [0, k-1]
            let i = (num * k as f64) as usize;
            // Add num to bucket i
            buckets[i].push(num);
        }
        // 2. Sort each bucket
        for bucket in &mut buckets {
            // Use built-in sorting function, can also replace with other sorting algorithms
            bucket.sort_by(|a, b| a.partial_cmp(b).unwrap());
        }
        // 3. Traverse buckets to merge results
        let mut i = 0;
        for bucket in buckets.iter() {
            for &num in bucket.iter() {
                nums[i] = num;
                i += 1;
            }
        }
    }
    ```
=== "C"
    ```c title="bucket_sort.c"
    void bucketSort(float nums[], int n) {
        int k = n / 2;                                 // Initialize k = n/2 buckets
        int *sizes = malloc(k * sizeof(int));          // Record each bucket's size
        float **buckets = malloc(k * sizeof(float *)); // Array of dynamic arrays (buckets)
        // Pre-allocate sufficient space for each bucket
        for (int i = 0; i < k; ++i) {
            buckets[i] = (float *)malloc(n * sizeof(float));
            sizes[i] = 0;
        }
        // 1. Distribute array elements into various buckets
        for (int i = 0; i < n; ++i) {
            int idx = (int)(nums[i] * k);
            buckets[idx][sizes[idx]++] = nums[i];
        }
        // 2. Sort each bucket
        for (int i = 0; i < k; ++i) {
            qsort(buckets[i], sizes[i], sizeof(float), compare);
        }
        // 3. Merge sorted buckets
        int idx = 0;
        for (int i = 0; i < k; ++i) {
            for (int j = 0; j < sizes[i]; ++j) {
                nums[idx++] = buckets[i][j];
            }
            // Free memory
            free(buckets[i]);
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="bucket_sort.kt"
    fun bucketSort(nums: FloatArray) {
        // Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
        val k = nums.size / 2
        val buckets = mutableListOf<MutableList<Float>>()
        for (i in 0..<k) {
            buckets.add(mutableListOf())
        }
        // 1. Distribute array elements into various buckets
        for (num in nums) {
            // Input data range is [0, 1), use num * k to map to index range [0, k-1]
            val i = (num * k).toInt()
            // Add num to bucket i
            buckets[i].add(num)
        }
        // 2. Sort each bucket
        for (bucket in buckets) {
            // Use built-in sorting function, can also replace with other sorting algorithms
            bucket.sort()
        }
        // 3. Traverse buckets to merge results
        var i = 0
        for (bucket in buckets) {
            for (num in bucket) {
                nums[i++] = num
            }
        }
    }
    ```
=== "Ruby"
    ```ruby title="bucket_sort.rb"
    ### Bucket sort ###
    def bucket_sort(nums)
      # Initialize k = n/2 buckets, expected to allocate 2 elements per bucket
      k = nums.length / 2
      buckets = Array.new(k) { [] }
      
      # 1. Distribute array elements into various buckets
      nums.each do |num|
        # Input data range is [0, 1), use num * k to map to index range [0, k-1]
        i = (num * k).to_i
        # Add num to bucket i
        buckets[i] << num
      end
    
      # 2. Sort each bucket
      buckets.each do |bucket|
        # Use built-in sorting function, can also replace with other sorting algorithms
        bucket.sort!
      end
    
      # 3. Traverse buckets to merge results
      i = 0
      buckets.each do |bucket|
        bucket.each do |num|
          nums[i] = num
          i += 1
        end
      end
    ```


## Đặc điểm thuật toán

Sắp xếp nhóm phù hợp để xử lý các tập dữ liệu rất lớn. Ví dụ: giả sử đầu vào chứa 1 triệu phần tử và bộ nhớ hạn chế ngăn hệ thống tải tất cả chúng cùng một lúc. Trong trường hợp đó, dữ liệu có thể được chia thành 1000 nhóm, mỗi nhóm có thể được sắp xếp riêng biệt và sau đó có thể hợp nhất các kết quả.

- **Độ phức tạp về thời gian là $O(n + k)$**: Giả sử các phần tử được phân bổ đều trên các nhóm, mỗi nhóm chứa các phần tử $\frac{n}{k}$. Nếu việc sắp xếp một nhóm mất $O(\frac{n}{k} \log\frac{n}{k})$ thời gian, thì việc sắp xếp tất cả các nhóm mất $O(n \log\frac{n}{k})$ thời gian. **Khi số lượng nhóm $k$ tương đối lớn, độ phức tạp về thời gian sẽ đạt tới $O(n)$**. Việc hợp nhất các kết quả yêu cầu duyệt qua tất cả các nhóm và phần tử, việc này mất $O(n + k)$ thời gian. Trong trường hợp xấu nhất, tất cả dữ liệu được đặt vào một nhóm duy nhất và việc sắp xếp nhóm đó mất $O(n^2)$ thời gian.
- **Độ phức tạp về không gian là $O(n + k)$ và sắp xếp nhóm không đúng chỗ**: Nó yêu cầu thêm không gian cho các nhóm $k$ và tổng số phần tử $n$.
- Việc sắp xếp nhóm có ổn định hay không phụ thuộc vào việc thuật toán sắp xếp các phần tử trong nhóm có ổn định hay không.

## Làm thế nào để đạt được sự phân phối đồng đều

Về lý thuyết, sắp xếp nhóm có thể đạt được độ phức tạp về thời gian $O(n)$. **Điều quan trọng là phân phối đồng đều các phần tử trên các nhóm**, vì dữ liệu trong thế giới thực thường không được phân phối đồng đều. Ví dụ: giả sử chúng ta muốn chia đều tất cả các sản phẩm trên Taobao thành 10 nhóm theo mức giá, nhưng mức phân bổ giá không đồng đều: có nhiều sản phẩm có giá dưới 100 nhân dân tệ và rất ít sản phẩm có giá trên 1000 nhân dân tệ. Nếu khoảng giá được chia đều thành 10 khoảng thì số lượng sản phẩm trong các nhóm sẽ khác nhau rất nhiều.

Để đạt được sự phân bổ đồng đều hơn, trước tiên chúng ta có thể chọn một ranh giới thô và phân chia dữ liệu thành 3 nhóm. **Sau đó, các nhóm chứa nhiều sản phẩm hơn có thể được chia tiếp thành 3 nhóm cho đến khi số lượng phần tử trong tất cả các nhóm gần bằng nhau**.

Như thể hiện trong hình bên dưới, phương pháp này về cơ bản xây dựng một cây đệ quy với mục tiêu là làm cho các nút lá cân bằng nhất có thể. Tất nhiên, dữ liệu không nhất thiết phải chia thành 3 nhóm trong mỗi vòng; Chiến lược phân vùng cụ thể có thể được lựa chọn linh hoạt dựa trên đặc điểm của dữ liệu.

![Recursively dividing buckets](bucket_sort.assets/scatter_in_buckets_recursively.png)

Nếu chúng tôi biết trước khả năng phân phối xác suất của giá sản phẩm, **chúng tôi có thể đặt giới hạn giá cho từng nhóm theo phân bổ đó**. Đáng chú ý là việc phân bổ dữ liệu không cần phải đo lường chính xác; nó cũng có thể được tính gần đúng bằng mô hình xác suất được chọn để phù hợp với đặc điểm của dữ liệu.

Như được hiển thị trong hình bên dưới, chúng tôi giả định rằng giá sản phẩm tuân theo phân phối chuẩn, điều này cho phép chúng tôi đặt các khoảng giá hợp lý để phân phối đều sản phẩm cho từng nhóm.

![Dividing buckets based on probability distribution](bucket_sort.assets/scatter_in_buckets_distribution.png)
