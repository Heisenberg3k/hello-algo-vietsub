# Bài toán về chiếc ba lô phân số

!!! câu hỏi

Cho $n$ vật phẩm, trong đó trọng lượng của vật phẩm thứ $i$ là $wgt[i-1]$ và giá trị của nó là $val[i-1]$, và một chiếc ba lô có sức chứa $cap$. Mỗi mục chỉ có thể được chọn một lần, **nhưng có thể chọn một phần của mục, với giá trị của nó tỷ lệ thuận với trọng lượng đã chọn**. Tổng giá trị tối đa có thể được đặt trong ba lô dưới giới hạn dung lượng là bao nhiêu? Một ví dụ được hiển thị trong hình dưới đây.

![Example data for the fractional knapsack problem](fractional_knapsack_problem.assets/fractional_knapsack_example.png)

Bài toán chiếc ba lô phân số nhìn chung rất giống với bài toán chiếc ba lô 0-1, với các trạng thái bao gồm vật phẩm hiện tại $i$ và sức chứa $c$, và mục tiêu là tối đa hóa giá trị trong sức chứa giới hạn của chiếc ba lô.

Sự khác biệt là bài toán này chỉ cho phép chọn một phần của một mục. Như minh họa trong hình bên dưới, **chúng ta có thể chia một mục tùy ý và tính giá trị của nó theo tỷ lệ với trọng lượng đã chọn**.

1. Đối với mặt hàng $i$, giá trị trên mỗi đơn vị trọng lượng của nó là $val[i-1] / wgt[i-1]$, được gọi là giá trị đơn vị.
2. Giả sử chúng ta cho một phần vật phẩm $i$ có trọng lượng $w$ vào trong ba lô thì giá trị cộng thêm vào ba lô là $w \times val[i-1] / wgt[i-1]$.

![Value of items per unit weight](fractional_knapsack_problem.assets/fractional_knapsack_unit_value.png)

### Quyết định chiến lược tham lam

Tối đa hóa tổng giá trị trong ba lô **về cơ bản có nghĩa là ưu tiên các mặt hàng có giá trị cao hơn trên mỗi đơn vị trọng lượng**. Từ quan sát này, chúng ta có thể rút ra chiến lược tham lam được thể hiện trong hình bên dưới.

1. Sắp xếp các mục theo giá trị đơn vị từ cao xuống thấp.
2. Lặp lại qua tất cả các mục, **tham lam chọn mục có giá trị đơn vị cao nhất trong mỗi vòng**.
3. Nếu sức chứa ba lô còn lại không đủ, hãy sử dụng một phần vật phẩm hiện tại để đổ vào ba lô.

![Greedy strategy for the fractional knapsack problem](fractional_knapsack_problem.assets/fractional_knapsack_greedy_strategy.png)

### Triển khai mã

Chúng tôi định nghĩa một lớp `Item` để các mục có thể được sắp xếp theo giá trị đơn vị. Sau đó, chúng ta lặp lại các mục được sắp xếp một cách tham lam, dừng lại khi ba lô đầy và trả về kết quả:

=== "Python"
    ```python title="fractional_knapsack.py"
    def fractional_knapsack(wgt: list[int], val: list[int], cap: int) -> int:
        """Fractional knapsack: Greedy algorithm"""
        # Create item list with two attributes: weight, value
        items = [Item(w, v) for w, v in zip(wgt, val)]
        # Sort by unit value item.v / item.w from high to low
        items.sort(key=lambda item: item.v / item.w, reverse=True)
        # Loop for greedy selection
        res = 0
        for item in items:
            if item.w <= cap:
                # If remaining capacity is sufficient, put the entire current item into the knapsack
                res += item.v
                cap -= item.w
            else:
                # If remaining capacity is insufficient, put part of the current item into the knapsack
                res += (item.v / item.w) * cap
                # No remaining capacity, so break out of the loop
                break
        return res
    ```
=== "C++"
    ```cpp title="fractional_knapsack.cpp"
    double fractionalKnapsack(vector<int> &wgt, vector<int> &val, int cap) {
        // Create item list with two attributes: weight, value
        vector<Item> items;
        for (int i = 0; i < wgt.size(); i++) {
            items.push_back(Item(wgt[i], val[i]));
        }
        // Sort by unit value item.v / item.w from high to low
        sort(items.begin(), items.end(), [](Item &a, Item &b) { return (double)a.v / a.w > (double)b.v / b.w; });
        // Loop for greedy selection
        double res = 0;
        for (auto &item : items) {
            if (item.w <= cap) {
                // If remaining capacity is sufficient, put the entire current item into the knapsack
                res += item.v;
                cap -= item.w;
            } else {
                // If remaining capacity is insufficient, put part of the current item into the knapsack
                res += (double)item.v / item.w * cap;
                // No remaining capacity, so break out of the loop
                break;
            }
        }
        return res;
    }
    ```
=== "Java"
    ```java title="fractional_knapsack.java"
    public class fractional_knapsack {
        /* Fractional knapsack: Greedy algorithm */
        static double fractionalKnapsack(int[] wgt, int[] val, int cap) {
            // Create item list with two attributes: weight, value
            Item[] items = new Item[wgt.length];
            for (int i = 0; i < wgt.length; i++) {
                items[i] = new Item(wgt[i], val[i]);
            }
            // Sort by unit value item.v / item.w from high to low
            Arrays.sort(items, Comparator.comparingDouble(item -> -((double) item.v / item.w)));
            // Loop for greedy selection
            double res = 0;
            for (Item item : items) {
                if (item.w <= cap) {
                    // If remaining capacity is sufficient, put the entire current item into the knapsack
                    res += item.v;
                    cap -= item.w;
                } else {
                    // If remaining capacity is insufficient, put part of the current item into the knapsack
                    res += (double) item.v / item.w * cap;
                    // No remaining capacity, so break out of the loop
                    break;
                }
            }
            return res;
        }
    
        public static void main(String[] args) {
            int[] wgt = { 10, 20, 30, 40, 50 };
            int[] val = { 50, 120, 150, 210, 240 };
            int cap = 50;
    
            // Greedy algorithm
            double res = fractionalKnapsack(wgt, val, cap);
            System.out.println("Maximum item value not exceeding knapsack capacity is " + res);
        }
    }
    ```
=== "C#"
    ```csharp title="fractional_knapsack.cs"
    public class fractional_knapsack {
        /* Fractional knapsack: Greedy algorithm */
        double FractionalKnapsack(int[] wgt, int[] val, int cap) {
            // Create item list with two attributes: weight, value
            Item[] items = new Item[wgt.Length];
            for (int i = 0; i < wgt.Length; i++) {
                items[i] = new Item(wgt[i], val[i]);
            }
            // Sort by unit value item.v / item.w from high to low
            Array.Sort(items, (x, y) => (y.v / y.w).CompareTo(x.v / x.w));
            // Loop for greedy selection
            double res = 0;
            foreach (Item item in items) {
                if (item.w <= cap) {
                    // If remaining capacity is sufficient, put the entire current item into the knapsack
                    res += item.v;
                    cap -= item.w;
                } else {
                    // If remaining capacity is insufficient, put part of the current item into the knapsack
                    res += (double)item.v / item.w * cap;
                    // No remaining capacity, so break out of the loop
                    break;
                }
            }
            return res;
        }
    
        [Test]
        public void Test() {
            int[] wgt = [10, 20, 30, 40, 50];
            int[] val = [50, 120, 150, 210, 240];
            int cap = 50;
    
            // Greedy algorithm
            double res = FractionalKnapsack(wgt, val, cap);
            Console.WriteLine("Maximum item value not exceeding knapsack capacity is " + res);
        }
    }
    ```
=== "Go"
    ```go title="fractional_knapsack.go"
    func fractionalKnapsack(wgt []int, val []int, cap int) float64 {
    	// Create item list with two attributes: weight, value
    	items := make([]Item, len(wgt))
    	for i := 0; i < len(wgt); i++ {
    		items[i] = Item{wgt[i], val[i]}
    	}
    	// Sort by unit value item.v / item.w from high to low
    	sort.Slice(items, func(i, j int) bool {
    		return float64(items[i].v)/float64(items[i].w) > float64(items[j].v)/float64(items[j].w)
    	})
    	// Loop for greedy selection
    	res := 0.0
    	for _, item := range items {
    		if item.w <= cap {
    			// If remaining capacity is sufficient, put the entire current item into the knapsack
    			res += float64(item.v)
    			cap -= item.w
    		} else {
    			// If remaining capacity is insufficient, put part of the current item into the knapsack
    			res += float64(item.v) / float64(item.w) * float64(cap)
    			// No remaining capacity, so break out of the loop
    			break
    		}
    	}
    	return res
    }
    ```
=== "Swift"
    ```swift title="fractional_knapsack.swift"
    func fractionalKnapsack(wgt: [Int], val: [Int], cap: Int) -> Double {
        // Create item list with two attributes: weight, value
        var items = zip(wgt, val).map { Item(w: $0, v: $1) }
        // Sort by unit value item.v / item.w from high to low
        items.sort { -(Double($0.v) / Double($0.w)) < -(Double($1.v) / Double($1.w)) }
        // Loop for greedy selection
        var res = 0.0
        var cap = cap
        for item in items {
            if item.w <= cap {
                // If remaining capacity is sufficient, put the entire current item into the knapsack
                res += Double(item.v)
                cap -= item.w
            } else {
                // If remaining capacity is insufficient, put part of the current item into the knapsack
                res += Double(item.v) / Double(item.w) * Double(cap)
                // No remaining capacity, so break out of the loop
                break
            }
        }
        return res
    }
    ```
=== "JS"
    ```javascript title="fractional_knapsack.js"
    function fractionalKnapsack(wgt, val, cap) {
        // Create item list with two attributes: weight, value
        const items = wgt.map((w, i) => new Item(w, val[i]));
        // Sort by unit value item.v / item.w from high to low
        items.sort((a, b) => b.v / b.w - a.v / a.w);
        // Loop for greedy selection
        let res = 0;
        for (const item of items) {
            if (item.w <= cap) {
                // If remaining capacity is sufficient, put the entire current item into the knapsack
                res += item.v;
                cap -= item.w;
            } else {
                // If remaining capacity is insufficient, put part of the current item into the knapsack
                res += (item.v / item.w) * cap;
                // No remaining capacity, so break out of the loop
                break;
            }
        }
        return res;
    }
    ```
=== "TS"
    ```typescript title="fractional_knapsack.ts"
    function fractionalKnapsack(wgt: number[], val: number[], cap: number): number {
        // Create item list with two attributes: weight, value
        const items: Item[] = wgt.map((w, i) => new Item(w, val[i]));
        // Sort by unit value item.v / item.w from high to low
        items.sort((a, b) => b.v / b.w - a.v / a.w);
        // Loop for greedy selection
        let res = 0;
        for (const item of items) {
            if (item.w <= cap) {
                // If remaining capacity is sufficient, put the entire current item into the knapsack
                res += item.v;
                cap -= item.w;
            } else {
                // If remaining capacity is insufficient, put part of the current item into the knapsack
                res += (item.v / item.w) * cap;
                // No remaining capacity, so break out of the loop
                break;
            }
        }
        return res;
    }
    ```
=== "Dart"
    ```dart title="fractional_knapsack.dart"
    double fractionalKnapsack(List<int> wgt, List<int> val, int cap) {
      // Create item list with two attributes: weight, value
      List<Item> items = List.generate(wgt.length, (i) => Item(wgt[i], val[i]));
      // Sort by unit value item.v / item.w from high to low
      items.sort((a, b) => (b.v / b.w).compareTo(a.v / a.w));
      // Loop for greedy selection
      double res = 0;
      for (Item item in items) {
        if (item.w <= cap) {
          // If remaining capacity is sufficient, put the entire current item into the knapsack
          res += item.v;
          cap -= item.w;
        } else {
          // If remaining capacity is insufficient, put part of the current item into the knapsack
          res += item.v / item.w * cap;
          // No remaining capacity, so break out of the loop
          break;
        }
      }
      return res;
    }
    ```
=== "Rust"
    ```rust title="fractional_knapsack.rs"
    fn fractional_knapsack(wgt: &[i32], val: &[i32], mut cap: i32) -> f64 {
        // Create item list with two attributes: weight, value
        let mut items = wgt
            .iter()
            .zip(val.iter())
            .map(|(&w, &v)| Item::new(w, v))
            .collect::<Vec<Item>>();
        // Sort by unit value item.v / item.w from high to low
        items.sort_by(|a, b| {
            (b.v as f64 / b.w as f64)
                .partial_cmp(&(a.v as f64 / a.w as f64))
                .unwrap()
        });
        // Loop for greedy selection
        let mut res = 0.0;
        for item in &items {
            if item.w <= cap {
                // If remaining capacity is sufficient, put the entire current item into the knapsack
                res += item.v as f64;
                cap -= item.w;
            } else {
                // If remaining capacity is insufficient, put part of the current item into the knapsack
                res += item.v as f64 / item.w as f64 * cap as f64;
                // No remaining capacity, so break out of the loop
                break;
            }
        }
        res
    }
    ```
=== "C"
    ```c title="fractional_knapsack.c"
    float fractionalKnapsack(int wgt[], int val[], int itemCount, int cap) {
        // Create item list with two attributes: weight, value
        Item *items = malloc(sizeof(Item) * itemCount);
        for (int i = 0; i < itemCount; i++) {
            items[i] = (Item){.w = wgt[i], .v = val[i]};
        }
        // Sort by unit value item.v / item.w from high to low
        qsort(items, (size_t)itemCount, sizeof(Item), sortByValueDensity);
        // Loop for greedy selection
        float res = 0.0;
        for (int i = 0; i < itemCount; i++) {
            if (items[i].w <= cap) {
                // If remaining capacity is sufficient, put the entire current item into the knapsack
                res += items[i].v;
                cap -= items[i].w;
            } else {
                // If remaining capacity is insufficient, put part of the current item into the knapsack
                res += (float)cap / items[i].w * items[i].v;
                cap = 0;
                break;
            }
        }
        free(items);
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="fractional_knapsack.kt"
    fun fractionalKnapsack(wgt: IntArray, _val: IntArray, c: Int): Double {
        // Create item list with two attributes: weight, value
        var cap = c
        val items = arrayOfNulls<Item>(wgt.size)
        for (i in wgt.indices) {
            items[i] = Item(wgt[i], _val[i])
        }
        // Sort by unit value item.v / item.w from high to low
        items.sortBy { item: Item? -> -(item!!.v.toDouble() / item.w) }
        // Loop for greedy selection
        var res = 0.0
        for (item in items) {
            if (item!!.w <= cap) {
                // If remaining capacity is sufficient, put the entire current item into the knapsack
                res += item.v
                cap -= item.w
            } else {
                // If remaining capacity is insufficient, put part of the current item into the knapsack
                res += item.v.toDouble() / item.w * cap
                // No remaining capacity, so break out of the loop
                break
            }
        }
        return res
    }
    ```
=== "Ruby"
    ```ruby title="fractional_knapsack.rb"
    ### Fractional knapsack: greedy ###
    def fractional_knapsack(wgt, val, cap)
      # Create item list with two attributes: weight, value
      items = wgt.each_with_index.map { |w, i| Item.new(w, val[i]) }
      # Sort by unit value item.v / item.w from high to low
      items.sort! { |a, b| (b.v.to_f / b.w) <=> (a.v.to_f / a.w) }
      # Loop for greedy selection
      res = 0
      for item in items
        if item.w <= cap
          # If remaining capacity is sufficient, put the entire current item into the knapsack
          res += item.v
          cap -= item.w
        else
          # If remaining capacity is insufficient, put part of the current item into the knapsack
          res += (item.v.to_f / item.w) * cap
          # No remaining capacity, so break out of the loop
          break
        end
      end
      res
    ```


Các thuật toán sắp xếp tích hợp thường mất $O(n \log n)$ và độ phức tạp về không gian của chúng thường là $O(\log n)$ hoặc $O(n)$, tùy thuộc vào cách triển khai cụ thể của ngôn ngữ lập trình.

Ngoài việc sắp xếp, trong trường hợp xấu nhất, toàn bộ danh sách mặt hàng cần phải được duyệt qua, **do đó độ phức tạp về thời gian là $O(n)$**, trong đó $n$ là số lượng mặt hàng.

Vì danh sách đối tượng `Item` được khởi tạo, **độ phức tạp của không gian là $O(n)$**.

### Bằng chứng về tính đúng đắn

Chúng tôi sử dụng bằng chứng bằng phản chứng. Giả sử mục $x$ có giá trị đơn vị cao nhất và một số thuật toán tạo ra giá trị tối ưu `res`, nhưng giải pháp thu được không bao gồm mục $x$.

Bây giờ hãy lấy một đơn vị trọng lượng khỏi bất kỳ vật phẩm nào trong ba lô và thay thế bằng một đơn vị trọng lượng từ vật phẩm $x$. Vì mục $x$ có giá trị đơn vị cao nhất nên tổng giá trị sau khi thay thế phải lớn hơn `res`. **Điều này mâu thuẫn với giả định rằng `res` là tối ưu, chứng tỏ rằng mọi giải pháp tối ưu đều phải bao gồm mục $x$**.

Chúng ta cũng có thể xây dựng mâu thuẫn tương tự cho các hạng mục khác trong lời giải. Tóm lại, **những món đồ có giá trị đơn vị cao hơn luôn là lựa chọn tốt hơn**, điều này chứng tỏ chiến lược tham lam đang phát huy hiệu quả.

Như được hiển thị trong hình bên dưới, nếu chúng ta coi trọng lượng vật phẩm và giá trị đơn vị là trục ngang và trục dọc của biểu đồ hai chiều thì bài toán chiếc ba lô phân số có thể được xem là "tìm diện tích tối đa được bao bọc trong một khoảng giới hạn trên trục ngang." Sự tương tự này giúp giải thích tính hiệu quả của chiến lược tham lam từ góc độ hình học.

![Geometric representation of the fractional knapsack problem](fractional_knapsack_problem.assets/fractional_knapsack_area_chart.png)
