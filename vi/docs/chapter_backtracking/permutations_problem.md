#Vấn đề về hoán vị

Bài toán hoán vị là một ứng dụng cổ điển của thuật toán quay lui. Nó được định nghĩa là tìm tất cả các cách sắp xếp có thể có của các phần tử trong một bộ sưu tập nhất định (chẳng hạn như một mảng hoặc chuỗi).

Bảng bên dưới hiển thị một số tập dữ liệu mẫu, bao gồm mảng đầu vào và hoán vị tương ứng của chúng.

<p align="center"> Table <id> &nbsp; Permutations Examples </p>

| Mảng đầu vào | Tất cả các hoán vị |
| :---------- | :-------------------------------------------------------------------------------- |
| $[1]$ | $[1]$ |
| $[1, 2]$ | $[1, 2], [2, 1]$ |
| $[1, 2, 3]$ | $[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]$ |

## Trường hợp có các phần tử riêng biệt

!!! câu hỏi

Cho một mảng số nguyên không có phần tử trùng lặp, trả về tất cả các hoán vị có thể có.

Từ góc độ của thuật toán quay lui, **chúng ta có thể tưởng tượng quá trình tạo ra các hoán vị là kết quả của một loạt các lựa chọn**. Giả sử mảng đầu vào là $[1, 2, 3]$. Nếu trước tiên chúng ta chọn $1$, sau đó chọn $3$ và cuối cùng chọn $2$, chúng ta sẽ nhận được hoán vị $[1, 3, 2]$. Quay lại có nghĩa là hoàn tác một lựa chọn và sau đó thử các lựa chọn khác.

Từ góc độ của mã quay lui, tập ứng cử viên `lựa chọn` bao gồm tất cả các phần tử trong mảng đầu vào và trạng thái `trạng thái` là các phần tử đã được chọn cho đến nay. Lưu ý rằng mỗi phần tử chỉ có thể được chọn một lần, **do đó tất cả các phần tử ở `state` phải là duy nhất**.

Như được hiển thị trong hình bên dưới, chúng ta có thể triển khai quá trình tìm kiếm thành một cây đệ quy, trong đó mỗi nút trong cây biểu thị trạng thái hiện tại ``trạng thái`. Bắt đầu từ nút gốc, sau ba vòng lựa chọn, chúng ta đến được một nút lá và mỗi nút lá tương ứng với một hoán vị.

![Recursion tree of permutations](permutations_problem.assets/permutations_i.png)

### Cắt bớt các lựa chọn trùng lặp

Để đảm bảo rằng mỗi phần tử chỉ được chọn một lần, chúng tôi xem xét việc giới thiệu một mảng boolean `selected`, trong đó `selected[i]` cho biết liệu `lựa chọn[i]` đã được chọn hay chưa. Chúng tôi thực hiện thao tác cắt tỉa sau dựa trên nó.

- Sau khi thực hiện lựa chọn `choices[i]`, chúng ta đặt `selected[i]` thành $\text{True}$, cho biết rằng nó đã được chọn.
- Khi duyệt qua danh sách ứng cử viên `lựa chọn`, chúng ta bỏ qua tất cả các nút đã được chọn đó là việc cắt tỉa.

Như minh họa trong hình bên dưới, giả sử chúng ta chọn $1$ ở vòng đầu tiên, $3$ ở vòng thứ hai và $2$ ở vòng thứ ba. Sau đó, chúng ta cần tỉa nhánh của phần tử $1$ ở vòng thứ hai và tỉa nhánh của phần tử $1$ và $3$ ở vòng thứ ba.

![Pruning example of permutations](permutations_problem.assets/permutations_i_pruning.png)

Quan sát hình trên, chúng ta thấy rằng thao tác cắt tỉa này làm giảm kích thước không gian tìm kiếm từ $O(n^n)$ xuống $O(n!)$.

### Triển khai mã

Sau khi hiểu rõ những thông tin trên, chúng ta có thể điền vào chỗ trống trong mã mẫu. Để rút ngắn mã tổng thể, chúng tôi không triển khai từng hàm trong mẫu một cách riêng biệt mà thay vào đó mở rộng chúng trong hàm `backtrack()`:

=== "Python"
    ```python title="permutations_i.py"
    def permutations_i(nums: list[int]) -> list[list[int]]:
        """Permutations I"""
        res = []
        backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
        return res
    ```
=== "C++"
    ```cpp title="permutations_i.cpp"
    vector<vector<int>> permutationsI(vector<int> nums) {
        vector<int> state;
        vector<bool> selected(nums.size(), false);
        vector<vector<int>> res;
        backtrack(state, nums, selected, res);
        return res;
    }
    ```
=== "Java"
    ```java title="permutations_i.java"
    public class permutations_i {
        /* Backtracking algorithm: Permutations I */
        public static void backtrack(List<Integer> state, int[] choices, boolean[] selected, List<List<Integer>> res) {
            // When the state length equals the number of elements, record the solution
            if (state.size() == choices.length) {
                res.add(new ArrayList<Integer>(state));
                return;
            }
            // Traverse all choices
            for (int i = 0; i < choices.length; i++) {
                int choice = choices[i];
                // Pruning: do not allow repeated selection of elements
                if (!selected[i]) {
                    // Attempt: make choice, update state
                    selected[i] = true;
                    state.add(choice);
                    // Proceed to the next round of selection
                    backtrack(state, choices, selected, res);
                    // Backtrack: undo choice, restore to previous state
                    selected[i] = false;
                    state.remove(state.size() - 1);
                }
            }
        }
    
        /* Permutations I */
        static List<List<Integer>> permutationsI(int[] nums) {
            List<List<Integer>> res = new ArrayList<List<Integer>>();
            backtrack(new ArrayList<Integer>(), nums, new boolean[nums.length], res);
            return res;
        }
    
        public static void main(String[] args) {
            int[] nums = { 1, 2, 3 };
    
            List<List<Integer>> res = permutationsI(nums);
    
            System.out.println("Input array nums = " + Arrays.toString(nums));
            System.out.println("All permutations res = " + res);
        }
    }
    ```
=== "C#"
    ```csharp title="permutations_i.cs"
    public class permutations_i {
        /* Backtracking algorithm: Permutations I */
        void Backtrack(List<int> state, int[] choices, bool[] selected, List<List<int>> res) {
            // When the state length equals the number of elements, record the solution
            if (state.Count == choices.Length) {
                res.Add(new List<int>(state));
                return;
            }
            // Traverse all choices
            for (int i = 0; i < choices.Length; i++) {
                int choice = choices[i];
                // Pruning: do not allow repeated selection of elements
                if (!selected[i]) {
                    // Attempt: make choice, update state
                    selected[i] = true;
                    state.Add(choice);
                    // Proceed to the next round of selection
                    Backtrack(state, choices, selected, res);
                    // Backtrack: undo choice, restore to previous state
                    selected[i] = false;
                    state.RemoveAt(state.Count - 1);
                }
            }
        }
    
        /* Permutations I */
        List<List<int>> PermutationsI(int[] nums) {
            List<List<int>> res = [];
            Backtrack([], nums, new bool[nums.Length], res);
            return res;
        }
    
        [Test]
        public void Test() {
            int[] nums = [1, 2, 3];
    
            List<List<int>> res = PermutationsI(nums);
    
            Console.WriteLine("Input array nums = " + string.Join(", ", nums));
            Console.WriteLine("All permutations res = ");
            foreach (List<int> permutation in res) {
                PrintUtil.PrintList(permutation);
            }
        }
    }
    ```
=== "Go"
    ```go title="permutations_i.go"
    func permutationsI(nums []int) [][]int {
    	res := make([][]int, 0)
    	state := make([]int, 0)
    	selected := make([]bool, len(nums))
    	backtrackI(&state, &nums, &selected, &res)
    	return res
    }
    ```
=== "Swift"
    ```swift title="permutations_i.swift"
    func permutationsI(nums: [Int]) -> [[Int]] {
        var state: [Int] = []
        var selected = Array(repeating: false, count: nums.count)
        var res: [[Int]] = []
        backtrack(state: &state, choices: nums, selected: &selected, res: &res)
        return res
    }
    ```
=== "JS"
    ```javascript title="permutations_i.js"
    function permutationsI(nums) {
        const res = [];
        backtrack([], nums, Array(nums.length).fill(false), res);
        return res;
    }
    ```
=== "TS"
    ```typescript title="permutations_i.ts"
    function permutationsI(nums: number[]): number[][] {
        const res: number[][] = [];
        backtrack([], nums, Array(nums.length).fill(false), res);
        return res;
    }
    ```
=== "Dart"
    ```dart title="permutations_i.dart"
    List<List<int>> permutationsI(List<int> nums) {
      List<List<int>> res = [];
      backtrack([], nums, List.filled(nums.length, false), res);
      return res;
    }
    ```
=== "Rust"
    ```rust title="permutations_i.rs"
    fn permutations_i(nums: &mut [i32]) -> Vec<Vec<i32>> {
        let mut res = Vec::new(); // State (subset)
        backtrack(Vec::new(), nums, &mut vec![false; nums.len()], &mut res);
        res
    }
    ```
=== "C"
    ```c title="permutations_i.c"
    int **permutationsI(int *nums, int numsSize, int *returnSize) {
        int *state = (int *)malloc(numsSize * sizeof(int));
        bool *selected = (bool *)malloc(numsSize * sizeof(bool));
        for (int i = 0; i < numsSize; i++) {
            selected[i] = false;
        }
        int **res = (int **)malloc(MAX_SIZE * sizeof(int *));
        *returnSize = 0;
    
        backtrack(state, 0, nums, numsSize, selected, res, returnSize);
    
        free(state);
        free(selected);
    
        return res;
    }
    ```
=== "Kotlin"
    ```kotlin title="permutations_i.kt"
    fun permutationsI(nums: IntArray): MutableList<MutableList<Int>?> {
        val res = mutableListOf<MutableList<Int>?>()
        backtrack(mutableListOf(), nums, BooleanArray(nums.size), res)
        return res
    }
    ```
=== "Ruby"
    ```ruby title="permutations_i.rb"
    ### Permutations I ###
    def permutations_i(nums)
      res = []
      backtrack([], nums, Array.new(nums.length, false), res)
      res
    ```


## Trường hợp có phần tử trùng lặp

!!! câu hỏi

Cho một mảng số nguyên **có thể chứa các phần tử trùng lặp**, trả về tất cả các hoán vị duy nhất.

Giả sử mảng đầu vào là $[1, 1, 2]$. Để phân biệt hai phần tử trùng lặp $1$, chúng tôi biểu thị $1$ thứ hai là $\hat{1}$.

Như thể hiện trong hình bên dưới, một nửa số hoán vị được tạo bởi phương pháp trên là trùng lặp.

![Duplicate permutations](permutations_problem.assets/permutations_ii.png)

Vậy làm cách nào để loại bỏ các hoán vị trùng lặp? Cách tiếp cận trực tiếp nhất là sử dụng bộ băm để loại bỏ trực tiếp các kết quả hoán vị. Tuy nhiên, điều này không tinh tế vì **các nhánh tìm kiếm tạo ra hoán vị trùng lặp là không cần thiết và cần được xác định và cắt bớt sớm**, điều này có thể cải thiện hơn nữa hiệu quả của thuật toán.

### Cắt tỉa các phần tử bằng nhau

Quan sát hình dưới đây. Ở vòng đầu tiên, chọn $1$ hoặc chọn $\hat{1}$ là tương đương. Tất cả các hoán vị được tạo ra theo hai lựa chọn này đều là trùng lặp. Vì vậy, chúng ta nên tỉa bớt $\hat{1}$.

Tương tự, sau khi chọn $2$ ở vòng đầu tiên, $1$ và $\hat{1}$ ở vòng thứ hai cũng tạo ra các nhánh trùng lặp, do đó $\hat{1}$ của vòng thứ hai cũng nên được cắt tỉa.

Về cơ bản, **mục tiêu của chúng tôi là đảm bảo rằng nhiều phần tử bằng nhau chỉ được chọn một lần trong một vòng lựa chọn nhất định**.

![Pruning duplicate permutations](permutations_problem.assets/permutations_ii_pruning.png)

### Triển khai mã

Dựa trên mã từ bài toán trước, chúng ta khởi tạo một bộ băm `trùng lặp` trong mỗi vòng lựa chọn để ghi lại những phần tử nào đã được thử trong vòng đó và lược bỏ các phần tử bằng nhau:

=== "Python"
    ```python title="permutations_ii.py"
    def permutations_ii(nums: list[int]) -> list[list[int]]:
        """Permutations II"""
        res = []
        backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
        return res
    ```
=== "C++"
    ```cpp title="permutations_ii.cpp"
    * File: permutations_ii.cpp
     * Created Time: 2023-04-24
     * Author: krahets (krahets@163.com)
     */
    
    #include "../utils/common.hpp"
    
    /* Backtracking algorithm: Permutations II */
    void backtrack(vector<int> &state, const vector<int> &choices, vector<bool> &selected, vector<vector<int>> &res) {
        // When the state length equals the number of elements, record the solution
        if (state.size() == choices.size()) {
            res.push_back(state);
            return;
        }
        // Traverse all choices
        unordered_set<int> duplicated;
        for (int i = 0; i < choices.size(); i++) {
            int choice = choices[i];
            // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
            if (!selected[i] && duplicated.find(choice) == duplicated.end()) {
                // Attempt: make choice, update state
                duplicated.emplace(choice); // Record the selected element value
                selected[i] = true;
                state.push_back(choice);
                // Proceed to the next round of selection
                backtrack(state, choices, selected, res);
                // Backtrack: undo choice, restore to previous state
                selected[i] = false;
                state.pop_back();
            }
        }
    }
    ```
=== "Java"
    ```java title="permutations_ii.java"
    public class permutations_ii {
        /* Backtracking algorithm: Permutations II */
        static void backtrack(List<Integer> state, int[] choices, boolean[] selected, List<List<Integer>> res) {
            // When the state length equals the number of elements, record the solution
            if (state.size() == choices.length) {
                res.add(new ArrayList<Integer>(state));
                return;
            }
            // Traverse all choices
            Set<Integer> duplicated = new HashSet<Integer>();
            for (int i = 0; i < choices.length; i++) {
                int choice = choices[i];
                // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
                if (!selected[i] && !duplicated.contains(choice)) {
                    // Attempt: make choice, update state
                    duplicated.add(choice); // Record the selected element value
                    selected[i] = true;
                    state.add(choice);
                    // Proceed to the next round of selection
                    backtrack(state, choices, selected, res);
                    // Backtrack: undo choice, restore to previous state
                    selected[i] = false;
                    state.remove(state.size() - 1);
                }
            }
        }
    
        /* Permutations II */
        static List<List<Integer>> permutationsII(int[] nums) {
            List<List<Integer>> res = new ArrayList<List<Integer>>();
            backtrack(new ArrayList<Integer>(), nums, new boolean[nums.length], res);
            return res;
        }
    
        public static void main(String[] args) {
            int[] nums = { 1, 2, 2 };
    
            List<List<Integer>> res = permutationsII(nums);
    
            System.out.println("Input array nums = " + Arrays.toString(nums));
            System.out.println("All permutations res = " + res);
        }
    }
    ```
=== "C#"
    ```csharp title="permutations_ii.cs"
    public class permutations_ii {
        /* Backtracking algorithm: Permutations II */
        void Backtrack(List<int> state, int[] choices, bool[] selected, List<List<int>> res) {
            // When the state length equals the number of elements, record the solution
            if (state.Count == choices.Length) {
                res.Add(new List<int>(state));
                return;
            }
            // Traverse all choices
            HashSet<int> duplicated = [];
            for (int i = 0; i < choices.Length; i++) {
                int choice = choices[i];
                // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
                if (!selected[i] && !duplicated.Contains(choice)) {
                    // Attempt: make choice, update state
                    duplicated.Add(choice); // Record the selected element value
                    selected[i] = true;
                    state.Add(choice);
                    // Proceed to the next round of selection
                    Backtrack(state, choices, selected, res);
                    // Backtrack: undo choice, restore to previous state
                    selected[i] = false;
                    state.RemoveAt(state.Count - 1);
                }
            }
        }
    
        /* Permutations II */
        List<List<int>> PermutationsII(int[] nums) {
            List<List<int>> res = [];
            Backtrack([], nums, new bool[nums.Length], res);
            return res;
        }
    
        [Test]
        public void Test() {
            int[] nums = [1, 2, 2];
    
            List<List<int>> res = PermutationsII(nums);
    
            Console.WriteLine("Input array nums = " + string.Join(", ", nums));
            Console.WriteLine("All permutations res = ");
            foreach (List<int> permutation in res) {
                PrintUtil.PrintList(permutation);
            }
        }
    }
    ```
=== "Go"
    ```go title="permutations_ii.go"
    // File: permutations_ii.go
    // Created Time: 2023-05-14
    // Author: Reanon (793584285@qq.com)
    
    package chapter_backtracking
    
    /* Backtracking algorithm: Permutations II */
    func backtrackII(state *[]int, choices *[]int, selected *[]bool, res *[][]int) {
    	// When the state length equals the number of elements, record the solution
    	if len(*state) == len(*choices) {
    		newState := append([]int{}, *state...)
    		*res = append(*res, newState)
    	}
    	// Traverse all choices
    	duplicated := make(map[int]struct{}, 0)
    	for i := 0; i < len(*choices); i++ {
    		choice := (*choices)[i]
    		// Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
    		if _, ok := duplicated[choice]; !ok && !(*selected)[i] {
    			// Attempt: make choice, update state
    			// Record the selected element value
    			duplicated[choice] = struct{}{}
    			(*selected)[i] = true
    			*state = append(*state, choice)
    			// Proceed to the next round of selection
    			backtrackII(state, choices, selected, res)
    			// Backtrack: undo choice, restore to previous state
    			(*selected)[i] = false
    			*state = (*state)[:len(*state)-1]
    		}
    	}
    }
    ```
=== "Swift"
    ```swift title="permutations_ii.swift"
    * File: permutations_ii.swift
     * Created Time: 2023-04-30
     * Author: nuomi1 (nuomi1@qq.com)
     */
    
    /* Backtracking algorithm: Permutations II */
    func backtrack(state: inout [Int], choices: [Int], selected: inout [Bool], res: inout [[Int]]) {
        // When the state length equals the number of elements, record the solution
        if state.count == choices.count {
            res.append(state)
            return
        }
        // Traverse all choices
        var duplicated: Set<Int> = []
        for (i, choice) in choices.enumerated() {
            // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
            if !selected[i], !duplicated.contains(choice) {
                // Attempt: make choice, update state
                duplicated.insert(choice) // Record the selected element value
                selected[i] = true
                state.append(choice)
                // Proceed to the next round of selection
                backtrack(state: &state, choices: choices, selected: &selected, res: &res)
                // Backtrack: undo choice, restore to previous state
                selected[i] = false
                state.removeLast()
            }
        }
    }
    ```
=== "JS"
    ```javascript title="permutations_ii.js"
    * File: permutations_ii.js
     * Created Time: 2023-05-13
     * Author: Justin (xiefahit@gmail.com)
     */
    
    /* Backtracking algorithm: Permutations II */
    function backtrack(state, choices, selected, res) {
        // When the state length equals the number of elements, record the solution
        if (state.length === choices.length) {
            res.push([...state]);
            return;
        }
        // Traverse all choices
        const duplicated = new Set();
        choices.forEach((choice, i) => {
            // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
            if (!selected[i] && !duplicated.has(choice)) {
                // Attempt: make choice, update state
                duplicated.add(choice); // Record the selected element value
                selected[i] = true;
                state.push(choice);
                // Proceed to the next round of selection
                backtrack(state, choices, selected, res);
                // Backtrack: undo choice, restore to previous state
                selected[i] = false;
                state.pop();
            }
        });
    }
    ```
=== "TS"
    ```typescript title="permutations_ii.ts"
    * File: permutations_ii.ts
     * Created Time: 2023-05-13
     * Author: Justin (xiefahit@gmail.com)
     */
    
    /* Backtracking algorithm: Permutations II */
    function backtrack(
        state: number[],
        choices: number[],
        selected: boolean[],
        res: number[][]
    ): void {
        // When the state length equals the number of elements, record the solution
        if (state.length === choices.length) {
            res.push([...state]);
            return;
        }
        // Traverse all choices
        const duplicated = new Set();
        choices.forEach((choice, i) => {
            // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
            if (!selected[i] && !duplicated.has(choice)) {
                // Attempt: make choice, update state
                duplicated.add(choice); // Record the selected element value
                selected[i] = true;
                state.push(choice);
                // Proceed to the next round of selection
                backtrack(state, choices, selected, res);
                // Backtrack: undo choice, restore to previous state
                selected[i] = false;
                state.pop();
            }
        });
    }
    ```
=== "Dart"
    ```dart title="permutations_ii.dart"
    * File: permutations_ii.dart
     * Created Time: 2023-08-10
     * Author: liuyuxin (gvenusleo@gmail.com)
     */
    
    /* Backtracking algorithm: Permutations II */
    void backtrack(
      List<int> state,
      List<int> choices,
      List<bool> selected,
      List<List<int>> res,
    ) {
      // When the state length equals the number of elements, record the solution
      if (state.length == choices.length) {
        res.add(List.from(state));
        return;
      }
      // Traverse all choices
      Set<int> duplicated = {};
      for (int i = 0; i < choices.length; i++) {
        int choice = choices[i];
        // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
        if (!selected[i] && !duplicated.contains(choice)) {
          // Attempt: make choice, update state
          duplicated.add(choice); // Record the selected element value
          selected[i] = true;
          state.add(choice);
          // Proceed to the next round of selection
          backtrack(state, choices, selected, res);
          // Backtrack: undo choice, restore to previous state
          selected[i] = false;
          state.removeLast();
        }
      }
    }
    ```
=== "Rust"
    ```rust title="permutations_ii.rs"
    fn permutations_ii(nums: &mut [i32]) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        backtrack(Vec::new(), nums, &mut vec![false; nums.len()], &mut res);
        res
    }
    ```
=== "C"
    ```c title="permutations_ii.c"
    * File: permutations_ii.c
     * Created Time: 2023-10-17
     * Author: krahets (krahets@163.com)
     */
    
    #include "../utils/common.h"
    
    // Assume at most 1000 permutations, max element value 1000
    #define MAX_SIZE 1000
    
    /* Backtracking algorithm: Permutations II */
    void backtrack(int *state, int stateSize, int *choices, int choicesSize, bool *selected, int **res, int *resSize) {
        // When the state length equals the number of elements, record the solution
        if (stateSize == choicesSize) {
            res[*resSize] = (int *)malloc(choicesSize * sizeof(int));
            for (int i = 0; i < choicesSize; i++) {
                res[*resSize][i] = state[i];
            }
            (*resSize)++;
            return;
        }
        // Traverse all choices
        bool duplicated[MAX_SIZE] = {false};
        for (int i = 0; i < choicesSize; i++) {
            int choice = choices[i];
            // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
            if (!selected[i] && !duplicated[choice]) {
                // Attempt: make choice, update state
                duplicated[choice] = true; // Record the selected element value
                selected[i] = true;
                state[stateSize] = choice;
                // Proceed to the next round of selection
                backtrack(state, stateSize + 1, choices, choicesSize, selected, res, resSize);
                // Backtrack: undo choice, restore to previous state
                selected[i] = false;
            }
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="permutations_ii.kt"
    * File: permutations_ii.kt
     * Created Time: 2024-01-25
     * Author: curtishd (1023632660@qq.com)
     */
    
    package chapter_backtracking.permutations_ii
    
    /* Backtracking algorithm: Permutations II */
    fun backtrack(
        state: MutableList<Int>,
        choices: IntArray,
        selected: BooleanArray,
        res: MutableList<MutableList<Int>?>
    ) {
        // When the state length equals the number of elements, record the solution
        if (state.size == choices.size) {
            res.add(state.toMutableList())
            return
        }
        // Traverse all choices
        val duplicated = HashSet<Int>()
        for (i in choices.indices) {
            val choice = choices[i]
            // Pruning: do not allow repeated selection of elements and do not allow repeated selection of equal elements
            if (!selected[i] && !duplicated.contains(choice)) {
                // Attempt: make choice, update state
                duplicated.add(choice) // Record the selected element value
                selected[i] = true
                state.add(choice)
                // Proceed to the next round of selection
                backtrack(state, choices, selected, res)
                // Backtrack: undo choice, restore to previous state
                selected[i] = false
                state.removeAt(state.size - 1)
            }
        }
    }
    ```
=== "Ruby"
    ```ruby title="permutations_ii.rb"
    ### Permutations II ###
    def permutations_ii(nums)
      res = []
      backtrack([], nums, Array.new(nums.length, false), res)
      res
    ```


Giả sử các phần tử là riêng biệt theo từng cặp, thì có các hoán vị $n!$ (giai thừa) của các phần tử $n$. Khi ghi kết quả, chúng ta cần sao chép danh sách có độ dài $n$, sử dụng thời gian $O(n)$. **Do đó, độ phức tạp về thời gian là $O(n! \cdot n)$**.

Độ sâu đệ quy tối đa là $n$, sử dụng không gian khung ngăn xếp $O(n)$. `được chọn` sử dụng không gian $O(n)$. Nhiều nhất $n$ các bộ trùng lặp` tồn tại đồng thời, sử dụng không gian $O(n^2)$. **Do đó, độ phức tạp của không gian là $O(n^2)$**.

###So Sánh Hai Phương Pháp Cắt Tỉa

Lưu ý rằng mặc dù cả `được chọn` và `duplicate` đều được sử dụng để cắt tỉa nhưng chúng có các mục tiêu khác nhau.

- **Cắt bớt các lựa chọn trùng lặp**: Chỉ có một `được chọn` trong toàn bộ quá trình tìm kiếm. Nó ghi lại những phần tử nào được bao gồm trong trạng thái hiện tại và mục đích của nó là ngăn chặn một phần tử xuất hiện lặp đi lặp lại trong `state`.
- **Cắt bớt các phần tử bằng nhau**: Mỗi vòng lựa chọn (mỗi lệnh gọi hàm `backtrack`) chứa một tập hợp `trùng lặp`. Nó ghi lại những phần tử nào đã được chọn trong lần lặp của vòng này (vòng lặp `for`) và mục đích của nó là đảm bảo rằng các phần tử bằng nhau chỉ được chọn một lần.

Hình dưới đây cho thấy phạm vi hiệu quả của hai điều kiện cắt tỉa. Lưu ý rằng mỗi nút trong cây đại diện cho một lựa chọn và các nút trên đường đi từ nút gốc đến nút lá tạo thành một hoán vị.

![Effective scope of two pruning conditions](permutations_problem.assets/permutations_ii_pruning_summary.png)
