#Vấn đề Hanota

Trong việc sắp xếp hợp nhất và xây dựng cây nhị phân, chúng ta phân tách bài toán ban đầu thành hai bài toán con, mỗi bài toán có kích thước bằng một nửa bài toán ban đầu. Tuy nhiên, đối với bài toán haota, chúng tôi áp dụng một chiến lược phân rã khác.

!!! câu hỏi

Cho ba trụ cột, ký hiệu là `A`, `B` và `C`. Ban đầu cột `A` có $n$ đĩa xếp chồng lên nhau, xếp từ trên xuống dưới theo thứ tự kích thước tăng dần. Nhiệm vụ của chúng ta là di chuyển các đĩa $n$ này sang cột `C` trong khi vẫn giữ nguyên thứ tự ban đầu của chúng (như trong hình bên dưới). Phải tuân thủ các quy tắc sau đây khi di chuyển đĩa.

1. Đĩa chỉ được lấy từ đầu cột này và đặt lên trên cột khác.
    2. Mỗi lần chỉ có thể di chuyển một đĩa.
    3. Đĩa nhỏ hơn phải luôn nằm trên đĩa lớn hơn.

![Example of the hanota problem](hanota_problem.assets/hanota_example.png)

**Chúng ta ký hiệu bài toán haota có kích thước $i$ là $f(i)$**. Ví dụ: $f(3)$ thể hiện việc di chuyển các đĩa $3$ từ `A` sang `C`.

### Xét các trường hợp cơ bản

Như trong hình bên dưới, đối với bài toán $f(1)$, khi chỉ có một đĩa, chúng ta có thể di chuyển nó trực tiếp từ `A` sang `C`.

=== "<1>"
    ![Solution for a problem of size 1](hanota_problem.assets/hanota_f1_step1.png)

=== "<2>"
    ![hanota_f1_step2](hanota_problem.assets/hanota_f1_step2.png)

Như minh họa trong hình bên dưới, đối với bài toán $f(2)$, khi có hai đĩa, **vì chúng ta phải luôn giữ đĩa nhỏ hơn ở trên đĩa lớn hơn, nên chúng ta cần sử dụng `B` để hỗ trợ di chuyển**.

1. Đầu tiên, di chuyển đĩa nhỏ hơn từ `A` sang `B`.
2. Sau đó di chuyển đĩa lớn hơn từ `A` sang `C`.
3. Cuối cùng, di chuyển đĩa nhỏ hơn từ `B` sang `C`.

=== "<1>"
    ![Solution for a problem of size 2](hanota_problem.assets/hanota_f2_step1.png)

=== "<2>"
    ![hanota_f2_step2](hanota_problem.assets/hanota_f2_step2.png)

=== "<3>"
    ![hanota_f2_step3](hanota_problem.assets/hanota_f2_step3.png)

=== "<4>"
    ![hanota_f2_step4](hanota_problem.assets/hanota_f2_step4.png)

Quá trình giải bài toán $f(2)$ có thể tóm tắt như sau: **di chuyển hai đĩa từ `A` sang `C` với sự trợ giúp của `B`**. Ở đây, `C` được gọi là trụ mục tiêu và `B` được gọi là trụ đệm.

### Phân tách bài toán con

Đối với bài toán $f(3)$, khi có ba đĩa, tình huống trở nên phức tạp hơn một chút.

Vì chúng ta đã biết các giải pháp cho $f(1)$ và $f(2)$, nên chúng ta có thể suy nghĩ từ góc độ phân chia và chinh phục, **xử lý toàn bộ hai đĩa trên cùng trên `A`** và thực hiện các bước được hiển thị trong hình bên dưới. Thao tác này đã di chuyển thành công ba đĩa từ `A` sang `C`.

1. Đặt `B` là trụ mục tiêu và `C` là trụ đệm và di chuyển hai đĩa từ `A` sang `B`.
2. Di chuyển đĩa còn lại từ `A` trực tiếp sang `C`.
3. Đặt `C` là trụ mục tiêu và `A` là trụ đệm và di chuyển hai đĩa từ `B` sang `C`.

=== "<1>"
    ![Solution for a problem of size 3](hanota_problem.assets/hanota_f3_step1.png)

=== "<2>"
    ![hanota_f3_step2](hanota_problem.assets/hanota_f3_step2.png)

=== "<3>"
    ![hanota_f3_step3](hanota_problem.assets/hanota_f3_step3.png)

=== "<4>"
    ![hanota_f3_step4](hanota_problem.assets/hanota_f3_step4.png)

Về cơ bản, **chúng ta chia bài toán $f(3)$ thành hai bài toán con $f(2)$ và một bài toán con $f(1)$**. Bằng cách giải quyết ba bài toán con này theo thứ tự, bài toán ban đầu sẽ được giải. Điều này cho thấy các bài toán con là độc lập và lời giải của chúng có thể được hợp nhất.

Từ đó, chúng ta có thể tóm tắt chiến lược chia để trị để giải bài toán hanota như trong hình bên dưới: chia bài toán ban đầu $f(n)$ thành hai bài toán con $f(n-1)$ và một bài toán con $f(1)$, và giải ba bài toán con này theo thứ tự sau.

1. Di chuyển các đĩa $n-1$ từ `A` sang `B` với sự trợ giúp của `C`.
2. Di chuyển trực tiếp đĩa $1$ còn lại từ `A` sang `C`.
3. Di chuyển các đĩa $n-1$ từ `B` sang `C` với sự trợ giúp của `A`.

Đối với hai bài toán con $f(n-1)$ này, **chúng ta có thể chia chúng theo cách tương tự** cho đến khi đạt đến bài toán con nhỏ nhất $f(1)$. Lời giải của $f(1)$ đã được biết và chỉ cần một thao tác di chuyển.

![Divide and conquer strategy for solving the hanota problem](hanota_problem.assets/hanota_divide_and_conquer.png)

### Triển khai mã

Trong mã, chúng ta khai báo một hàm đệ quy `dfs(i, src, buf, tar)`, với mục đích là di chuyển các đĩa $i$ trên cùng từ cột `src` sang cột đích `tar` với sự trợ giúp của cột đệm `buf`:

=== "Python"
    ```python title="hanota.py"
    def solve_hanota(A: list[int], B: list[int], C: list[int]):
        """Solve the Tower of Hanoi problem"""
        n = len(A)
        # Move the top n disks from A to C using B
        dfs(n, A, B, C)
    ```
=== "C++"
    ```cpp title="hanota.cpp"
    void solveHanota(vector<int> &A, vector<int> &B, vector<int> &C) {
        int n = A.size();
        // Move the top n disks from A to C using B
        dfs(n, A, B, C);
    }
    ```
=== "Java"
    ```java title="hanota.java"
    static void solveHanota(List<Integer> A, List<Integer> B, List<Integer> C) {
            int n = A.size();
            // Move the top n disks from A to C using B
            dfs(n, A, B, C);
        }
    ```
=== "C#"
    ```csharp title="hanota.cs"
    void SolveHanota(List<int> A, List<int> B, List<int> C) {
            int n = A.Count;
            // Move the top n disks from A to C using B
            DFS(n, A, B, C);
        }
    ```
=== "Go"
    ```go title="hanota.go"
    func solveHanota(A, B, C *list.List) {
    	n := A.Len()
    	// Move the top n disks from A to C using B
    	dfsHanota(n, A, B, C)
    }
    ```
=== "Swift"
    ```swift title="hanota.swift"
    func solveHanota(A: inout [Int], B: inout [Int], C: inout [Int]) {
        let n = A.count
        // The tail of the list is the top of the rod
        // Move top n disks from src to C using B
        dfs(i: n, src: &A, buf: &B, tar: &C)
    }
    ```
=== "JS"
    ```javascript title="hanota.js"
    function solveHanota(A, B, C) {
        const n = A.length;
        // Move the top n disks from A to C using B
        dfs(n, A, B, C);
    }
    ```
=== "TS"
    ```typescript title="hanota.ts"
    function solveHanota(A: number[], B: number[], C: number[]): void {
        const n = A.length;
        // Move the top n disks from A to C using B
        dfs(n, A, B, C);
    }
    ```
=== "Dart"
    ```dart title="hanota.dart"
    void solveHanota(List<int> A, List<int> B, List<int> C) {
      int n = A.length;
      // Move the top n disks from A to C using B
      dfs(n, A, B, C);
    }
    ```
=== "Rust"
    ```rust title="hanota.rs"
    fn solve_hanota(A: &mut Vec<i32>, B: &mut Vec<i32>, C: &mut Vec<i32>) {
        let n = A.len() as i32;
        // Move the top n disks from A to C using B
        dfs(n, A, B, C);
    }
    ```
=== "C"
    ```c title="hanota.c"
    void solveHanota(int *A, int *ASize, int *B, int *BSize, int *C, int *CSize) {
        // Move the top n disks from A to C using B
        dfs(*ASize, A, ASize, B, BSize, C, CSize);
    }
    ```
=== "Kotlin"
    ```kotlin title="hanota.kt"
    fun solveHanota(A: MutableList<Int>, B: MutableList<Int>, C: MutableList<Int>) {
        val n = A.size
        // Move the top n disks from A to C using B
        dfs(n, A, B, C)
    }
    ```
=== "Ruby"
    ```ruby title="hanota.rb"
    ### Solve Tower of Hanoi ###
    def solve_hanota(_A, _B, _C)
      n = _A.length
      # Move the top n disks from A to C using B
      dfs(n, _A, _B, _C)
    ```


Như được hiển thị trong hình bên dưới, bài toán hanota tạo thành một cây đệ quy có chiều cao $n$, trong đó mỗi nút biểu thị một bài toán con tương ứng với một lệnh gọi hàm `dfs()`, **do đó độ phức tạp về thời gian là $O(2^n)$ và độ phức tạp về không gian là $O(n)$**.

![Recursion tree of the hanota problem](hanota_problem.assets/hanota_recursive_tree.png)

!!! trích dẫn

Vấn đề hanota bắt nguồn từ một truyền thuyết cổ xưa. Trong một ngôi chùa ở Ấn Độ cổ đại, các nhà sư có ba cột kim cương cao và những chiếc đĩa vàng trị giá 64 đô la với nhiều kích cỡ khác nhau. Các nhà sư liên tục di chuyển những chiếc đĩa vì tin rằng khi chiếc đĩa cuối cùng được đặt đúng chỗ, thế giới sẽ kết thúc.

Tuy nhiên, ngay cả khi các nhà sư di chuyển một đĩa mỗi giây, thì cũng sẽ mất khoảng $2^{64} \approx 1,84×10^{19}$ giây, tức là khoảng $585$ tỷ năm, vượt xa ước tính hiện tại về tuổi của vũ trụ. Vì vậy, nếu truyền thuyết này là sự thật thì chúng ta không cần phải lo lắng về ngày tận thế.
