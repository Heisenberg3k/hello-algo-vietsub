#Thuật toán quay lui

<u>The backtracking algorithm</u> is a method for solving problems through exhaustive search. Its core idea is to start from an initial state and exhaustively search all possible solutions. When a correct solution is found, it is recorded. This process continues until a solution is found or all possible choices have been tried without finding a solution.

Thuật toán quay lui thường sử dụng "tìm kiếm theo chiều sâu" để duyệt qua không gian lời giải. Trong chương "Cây nhị phân", chúng tôi đã đề cập rằng việc duyệt thứ tự trước, thứ tự thứ tự và thứ tự sau đều thuộc về tìm kiếm theo chiều sâu. Tiếp theo, chúng ta sẽ xây dựng bài toán quay lui bằng cách sử dụng phương pháp duyệt theo thứ tự trước để hiểu dần cách hoạt động của thuật toán quay lui.

!!! Câu hỏi “Ví dụ 1”

Cho một cây nhị phân, tìm kiếm và ghi lại tất cả các nút có giá trị $7$ và trả về danh sách các nút này.

Đối với vấn đề này, chúng tôi thực hiện duyệt cây theo thứ tự trước và kiểm tra xem giá trị của nút hiện tại có phải là $7$ hay không. Nếu đúng như vậy, chúng tôi thêm nút vào danh sách kết quả `res`. Việc triển khai có liên quan được thể hiện trong hình và mã sau:

=== "Python"
    ```python title="preorder_traversal_i_compact.py"
    def pre_order(root: TreeNode):
        """Preorder traversal: Example 1"""
        if root is None:
            return
        if root.val == 7:
            # Record solution
            res.append(root)
        pre_order(root.left)
        pre_order(root.right)
    ```
=== "C++"
    ```cpp title="preorder_traversal_i_compact.cpp"
    void preOrder(TreeNode *root) {
        if (root == nullptr) {
            return;
        }
        if (root->val == 7) {
            // Record solution
            res.push_back(root);
        }
        preOrder(root->left);
        preOrder(root->right);
    }
    ```
=== "Java"
    ```java title="preorder_traversal_i_compact.java"
    static void preOrder(TreeNode root) {
            if (root == null) {
                return;
            }
            if (root.val == 7) {
                // Record solution
                res.add(root);
            }
            preOrder(root.left);
            preOrder(root.right);
        }
    ```
=== "C#"
    ```csharp title="preorder_traversal_i_compact.cs"
    void PreOrder(TreeNode? root) {
            if (root == null) {
                return;
            }
            if (root.val == 7) {
                // Record solution
                res.Add(root);
            }
            PreOrder(root.left);
            PreOrder(root.right);
        }
    ```
=== "Go"
    ```go title="preorder_traversal_i_compact.go"
    func preOrderI(root *TreeNode, res *[]*TreeNode) {
    	if root == nil {
    		return
    	}
    	if (root.Val).(int) == 7 {
    		// Record solution
    		*res = append(*res, root)
    	}
    	preOrderI(root.Left, res)
    	preOrderI(root.Right, res)
    }
    ```
=== "Swift"
    ```swift title="preorder_traversal_i_compact.swift"
    func preOrder(root: TreeNode?) {
        guard let root = root else {
            return
        }
        if root.val == 7 {
            // Record solution
            res.append(root)
        }
        preOrder(root: root.left)
        preOrder(root: root.right)
    }
    ```
=== "JS"
    ```javascript title="preorder_traversal_i_compact.js"
    function preOrder(root, res) {
        if (root === null) {
            return;
        }
        if (root.val === 7) {
            // Record solution
            res.push(root);
        }
        preOrder(root.left, res);
        preOrder(root.right, res);
    }
    ```
=== "TS"
    ```typescript title="preorder_traversal_i_compact.ts"
    function preOrder(root: TreeNode | null, res: TreeNode[]): void {
        if (root === null) {
            return;
        }
        if (root.val === 7) {
            // Record solution
            res.push(root);
        }
        preOrder(root.left, res);
        preOrder(root.right, res);
    }
    ```
=== "Dart"
    ```dart title="preorder_traversal_i_compact.dart"
    void preOrder(TreeNode? root, List<TreeNode> res) {
      if (root == null) {
        return;
      }
      if (root.val == 7) {
        // Record solution
        res.add(root);
      }
      preOrder(root.left, res);
      preOrder(root.right, res);
    }
    ```
=== "Rust"
    ```rust title="preorder_traversal_i_compact.rs"
    fn pre_order(res: &mut Vec<Rc<RefCell<TreeNode>>>, root: Option<&Rc<RefCell<TreeNode>>>) {
        if root.is_none() {
            return;
        }
        if let Some(node) = root {
            if node.borrow().val == 7 {
                // Record solution
                res.push(node.clone());
            }
            pre_order(res, node.borrow().left.as_ref());
            pre_order(res, node.borrow().right.as_ref());
        }
    }
    ```
=== "C"
    ```c title="preorder_traversal_i_compact.c"
    void preOrder(TreeNode *root) {
        if (root == NULL) {
            return;
        }
        if (root->val == 7) {
            // Record solution
            res[resSize++] = root;
        }
        preOrder(root->left);
        preOrder(root->right);
    }
    ```
=== "Kotlin"
    ```kotlin title="preorder_traversal_i_compact.kt"
    fun preOrder(root: TreeNode?) {
        if (root == null) {
            return
        }
        if (root._val == 7) {
            // Record solution
            res!!.add(root)
        }
        preOrder(root.left)
        preOrder(root.right)
    }
    ```
=== "Ruby"
    ```ruby title="preorder_traversal_i_compact.rb"
    ### Pre-order traversal: example 1 ###
    def pre_order(root)
      return unless root
    
      # Record solution
      $res << root if root.val == 7
    
      pre_order(root.left)
      pre_order(root.right)
    ```


![Search for nodes in preorder traversal](backtracking_algorithm.assets/preorder_find_nodes.png)

## Cố gắng và quay lại

**Lý do nó được gọi là thuật toán quay lui là vì nó sử dụng các chiến lược "cố gắng" và "quay lại" khi tìm kiếm không gian lời giải**. Khi thuật toán gặp trạng thái không thể tiếp tục chuyển tiếp hoặc không thể tìm ra giải pháp thỏa mãn các ràng buộc, nó sẽ hoàn tác lựa chọn trước đó, quay lại trạng thái trước đó và thử các lựa chọn khả thi khác.

Đối với Ví dụ 1, việc truy cập từng nút biểu thị một "lần thử", trong khi việc bỏ qua một nút lá hoặc `return` đưa quá trình truyền tải trở lại nút cha biểu thị một "quay ngược".

Điều đáng lưu ý là **quay lại không chỉ giới hạn ở hàm trả về**. Để minh họa điều này, hãy mở rộng Ví dụ 1 một chút.

!!! Câu hỏi “Ví dụ 2”

Trong cây nhị phân, tìm kiếm tất cả các nút có giá trị $7$, **và trả về đường dẫn từ nút gốc đến các nút này**.

Dựa trên mã từ Ví dụ 1, chúng ta cần sử dụng danh sách `path` để ghi lại đường dẫn của các nút đã truy cập. Khi chúng tôi đến một nút có giá trị $7$, chúng tôi sao chép `path` và thêm nó vào danh sách kết quả `res`. Sau khi quá trình truyền tải hoàn tất, `res` chứa tất cả các giải pháp. Mã này như sau:

=== "Python"
    ```python title="preorder_traversal_ii_compact.py"
    def pre_order(root: TreeNode):
        """Preorder traversal: Example 2"""
        if root is None:
            return
        # Attempt
        path.append(root)
        if root.val == 7:
            # Record solution
            res.append(list(path))
        pre_order(root.left)
        pre_order(root.right)
        # Backtrack
        path.pop()
    ```
=== "C++"
    ```cpp title="preorder_traversal_ii_compact.cpp"
    void preOrder(TreeNode *root) {
        if (root == nullptr) {
            return;
        }
        // Attempt
        path.push_back(root);
        if (root->val == 7) {
            // Record solution
            res.push_back(path);
        }
        preOrder(root->left);
        preOrder(root->right);
        // Backtrack
        path.pop_back();
    }
    ```
=== "Java"
    ```java title="preorder_traversal_ii_compact.java"
    static void preOrder(TreeNode root) {
            if (root == null) {
                return;
            }
            // Attempt
            path.add(root);
            if (root.val == 7) {
                // Record solution
                res.add(new ArrayList<>(path));
            }
            preOrder(root.left);
            preOrder(root.right);
            // Backtrack
            path.remove(path.size() - 1);
        }
    ```
=== "C#"
    ```csharp title="preorder_traversal_ii_compact.cs"
    void PreOrder(TreeNode? root) {
            if (root == null) {
                return;
            }
            // Attempt
            path.Add(root);
            if (root.val == 7) {
                // Record solution
                res.Add(new List<TreeNode>(path));
            }
            PreOrder(root.left);
            PreOrder(root.right);
            // Backtrack
            path.RemoveAt(path.Count - 1);
        }
    ```
=== "Go"
    ```go title="preorder_traversal_ii_compact.go"
    func preOrderII(root *TreeNode, res *[][]*TreeNode, path *[]*TreeNode) {
    	if root == nil {
    		return
    	}
    	// Attempt
    	*path = append(*path, root)
    	if root.Val.(int) == 7 {
    		// Record solution
    		*res = append(*res, append([]*TreeNode{}, *path...))
    	}
    	preOrderII(root.Left, res, path)
    	preOrderII(root.Right, res, path)
    	// Backtrack
    	*path = (*path)[:len(*path)-1]
    }
    ```
=== "Swift"
    ```swift title="preorder_traversal_ii_compact.swift"
    func preOrder(root: TreeNode?) {
        guard let root = root else {
            return
        }
        // Attempt
        path.append(root)
        if root.val == 7 {
            // Record solution
            res.append(path)
        }
        preOrder(root: root.left)
        preOrder(root: root.right)
        // Backtrack
        path.removeLast()
    }
    ```
=== "JS"
    ```javascript title="preorder_traversal_ii_compact.js"
    function preOrder(root, path, res) {
        if (root === null) {
            return;
        }
        // Attempt
        path.push(root);
        if (root.val === 7) {
            // Record solution
            res.push([...path]);
        }
        preOrder(root.left, path, res);
        preOrder(root.right, path, res);
        // Backtrack
        path.pop();
    }
    ```
=== "TS"
    ```typescript title="preorder_traversal_ii_compact.ts"
    function preOrder(
        root: TreeNode | null,
        path: TreeNode[],
        res: TreeNode[][]
    ): void {
        if (root === null) {
            return;
        }
        // Attempt
        path.push(root);
        if (root.val === 7) {
            // Record solution
            res.push([...path]);
        }
        preOrder(root.left, path, res);
        preOrder(root.right, path, res);
        // Backtrack
        path.pop();
    }
    ```
=== "Dart"
    ```dart title="preorder_traversal_ii_compact.dart"
    void preOrder(
      TreeNode? root,
      List<TreeNode> path,
      List<List<TreeNode>> res,
    ) {
      if (root == null) {
        return;
      }
    
      // Attempt
      path.add(root);
      if (root.val == 7) {
        // Record solution
        res.add(List.from(path));
      }
      preOrder(root.left, path, res);
      preOrder(root.right, path, res);
      // Backtrack
      path.removeLast();
    }
    ```
=== "Rust"
    ```rust title="preorder_traversal_ii_compact.rs"
    fn pre_order(
        res: &mut Vec<Vec<Rc<RefCell<TreeNode>>>>,
        path: &mut Vec<Rc<RefCell<TreeNode>>>,
        root: Option<&Rc<RefCell<TreeNode>>>,
    ) {
        if root.is_none() {
            return;
        }
        if let Some(node) = root {
            // Attempt
            path.push(node.clone());
            if node.borrow().val == 7 {
                // Record solution
                res.push(path.clone());
            }
            pre_order(res, path, node.borrow().left.as_ref());
            pre_order(res, path, node.borrow().right.as_ref());
            // Backtrack
            path.pop();
        }
    }
    ```
=== "C"
    ```c title="preorder_traversal_ii_compact.c"
    void preOrder(TreeNode *root) {
        if (root == NULL) {
            return;
        }
        // Attempt
        path[pathSize++] = root;
        if (root->val == 7) {
            // Record solution
            for (int i = 0; i < pathSize; ++i) {
                res[resSize][i] = path[i];
            }
            resSize++;
        }
        preOrder(root->left);
        preOrder(root->right);
        // Backtrack
        pathSize--;
    }
    ```
=== "Kotlin"
    ```kotlin title="preorder_traversal_ii_compact.kt"
    fun preOrder(root: TreeNode?) {
        if (root == null) {
            return
        }
        // Attempt
        path!!.add(root)
        if (root._val == 7) {
            // Record solution
            res!!.add(path!!.toMutableList())
        }
        preOrder(root.left)
        preOrder(root.right)
        // Backtrack
        path!!.removeAt(path!!.size - 1)
    }
    ```
=== "Ruby"
    ```ruby title="preorder_traversal_ii_compact.rb"
    ### Pre-order traversal: example 2 ###
    def pre_order(root)
      return unless root
    
      # Attempt
      $path << root
    
      # Record solution
      $res << $path.dup if root.val == 7
    
      pre_order(root.left)
      pre_order(root.right)
    
      # Backtrack
      $path.pop
    ```


Trong mỗi lần "thử", chúng tôi ghi lại đường dẫn bằng cách thêm nút hiện tại vào `path`; trước khi "quay lại", chúng ta cần xóa nút khỏi `path`, **để khôi phục trạng thái trước lần thử này**.

Quan sát quy trình được hiển thị trong hình dưới đây, **chúng ta có thể hiểu nỗ lực và quay lại là "tiến lên" và "hoàn tác"**, hai thao tác ngược lại với nhau.

=== "<1>"
    ![Attempt and backtrack](backtracking_algorithm.assets/preorder_find_paths_step1.png)

=== "<2>"
    ![preorder_find_paths_step2](backtracking_algorithm.assets/preorder_find_paths_step2.png)

=== "<3>"
    ![preorder_find_paths_step3](backtracking_algorithm.assets/preorder_find_paths_step3.png)

=== "<4>"
    ![preorder_find_paths_step4](backtracking_algorithm.assets/preorder_find_paths_step4.png)

=== "<5>"
    ![preorder_find_paths_step5](backtracking_algorithm.assets/preorder_find_paths_step5.png)

=== "<6>"
    ![preorder_find_paths_step6](backtracking_algorithm.assets/preorder_find_paths_step6.png)

=== "<7>"
    ![preorder_find_paths_step7](backtracking_algorithm.assets/preorder_find_paths_step7.png)

=== "<8>"
    ![preorder_find_paths_step8](backtracking_algorithm.assets/preorder_find_paths_step8.png)

=== "<9>"
    ![preorder_find_paths_step9](backtracking_algorithm.assets/preorder_find_paths_step9.png)

    ![preorder_find_paths_step10](backtracking_algorithm.assets/preorder_find_paths_step10.png)

=== "<11>"
    ![preorder_find_paths_step11](backtracking_algorithm.assets/preorder_find_paths_step11.png)

## Cắt tỉa

Các vấn đề quay lui phức tạp thường chứa một hoặc nhiều ràng buộc. **Các ràng buộc thường có thể được sử dụng để "cắt tỉa"**.

!!! Câu hỏi “Ví dụ 3”

Trong cây nhị phân, tìm kiếm tất cả các nút có giá trị $7$ và trả về các đường dẫn từ nút gốc đến các nút này, **nhưng yêu cầu các đường dẫn đó không chứa các nút có giá trị $3$**.

Để thỏa mãn các ràng buộc trên, **chúng ta cần thêm các thao tác cắt tỉa**: trong quá trình tìm kiếm, nếu gặp nút có giá trị $3$, chúng ta quay lại sớm và không tiếp tục tìm kiếm. Mã này như sau:

=== "Python"
    ```python title="preorder_traversal_iii_compact.py"
    def pre_order(root: TreeNode):
        """Preorder traversal: Example 3"""
        # Pruning
        if root is None or root.val == 3:
            return
        # Attempt
        path.append(root)
        if root.val == 7:
            # Record solution
            res.append(list(path))
        pre_order(root.left)
        pre_order(root.right)
        # Backtrack
        path.pop()
    ```
=== "C++"
    ```cpp title="preorder_traversal_iii_compact.cpp"
    void preOrder(TreeNode *root) {
        // Pruning
        if (root == nullptr || root->val == 3) {
            return;
        }
        // Attempt
        path.push_back(root);
        if (root->val == 7) {
            // Record solution
            res.push_back(path);
        }
        preOrder(root->left);
        preOrder(root->right);
        // Backtrack
        path.pop_back();
    }
    ```
=== "Java"
    ```java title="preorder_traversal_iii_compact.java"
    static void preOrder(TreeNode root) {
            // Pruning
            if (root == null || root.val == 3) {
                return;
            }
            // Attempt
            path.add(root);
            if (root.val == 7) {
                // Record solution
                res.add(new ArrayList<>(path));
            }
            preOrder(root.left);
            preOrder(root.right);
            // Backtrack
            path.remove(path.size() - 1);
        }
    ```
=== "C#"
    ```csharp title="preorder_traversal_iii_compact.cs"
    void PreOrder(TreeNode? root) {
            // Pruning
            if (root == null || root.val == 3) {
                return;
            }
            // Attempt
            path.Add(root);
            if (root.val == 7) {
                // Record solution
                res.Add(new List<TreeNode>(path));
            }
            PreOrder(root.left);
            PreOrder(root.right);
            // Backtrack
            path.RemoveAt(path.Count - 1);
        }
    ```
=== "Go"
    ```go title="preorder_traversal_iii_compact.go"
    func preOrderIII(root *TreeNode, res *[][]*TreeNode, path *[]*TreeNode) {
    	// Pruning
    	if root == nil || root.Val == 3 {
    		return
    	}
    	// Attempt
    	*path = append(*path, root)
    	if root.Val.(int) == 7 {
    		// Record solution
    		*res = append(*res, append([]*TreeNode{}, *path...))
    	}
    	preOrderIII(root.Left, res, path)
    	preOrderIII(root.Right, res, path)
    	// Backtrack
    	*path = (*path)[:len(*path)-1]
    }
    ```
=== "Swift"
    ```swift title="preorder_traversal_iii_compact.swift"
    func preOrder(root: TreeNode?) {
        // Pruning
        guard let root = root, root.val != 3 else {
            return
        }
        // Attempt
        path.append(root)
        if root.val == 7 {
            // Record solution
            res.append(path)
        }
        preOrder(root: root.left)
        preOrder(root: root.right)
        // Backtrack
        path.removeLast()
    }
    ```
=== "JS"
    ```javascript title="preorder_traversal_iii_compact.js"
    function preOrder(root, path, res) {
        // Pruning
        if (root === null || root.val === 3) {
            return;
        }
        // Attempt
        path.push(root);
        if (root.val === 7) {
            // Record solution
            res.push([...path]);
        }
        preOrder(root.left, path, res);
        preOrder(root.right, path, res);
        // Backtrack
        path.pop();
    }
    ```
=== "TS"
    ```typescript title="preorder_traversal_iii_compact.ts"
    function preOrder(
        root: TreeNode | null,
        path: TreeNode[],
        res: TreeNode[][]
    ): void {
        // Pruning
        if (root === null || root.val === 3) {
            return;
        }
        // Attempt
        path.push(root);
        if (root.val === 7) {
            // Record solution
            res.push([...path]);
        }
        preOrder(root.left, path, res);
        preOrder(root.right, path, res);
        // Backtrack
        path.pop();
    }
    ```
=== "Dart"
    ```dart title="preorder_traversal_iii_compact.dart"
    void preOrder(
      TreeNode? root,
      List<TreeNode> path,
      List<List<TreeNode>> res,
    ) {
      if (root == null || root.val == 3) {
        return;
      }
    
      // Attempt
      path.add(root);
      if (root.val == 7) {
        // Record solution
        res.add(List.from(path));
      }
      preOrder(root.left, path, res);
      preOrder(root.right, path, res);
      // Backtrack
      path.removeLast();
    }
    ```
=== "Rust"
    ```rust title="preorder_traversal_iii_compact.rs"
    fn pre_order(
        res: &mut Vec<Vec<Rc<RefCell<TreeNode>>>>,
        path: &mut Vec<Rc<RefCell<TreeNode>>>,
        root: Option<&Rc<RefCell<TreeNode>>>,
    ) {
        // Pruning
        if root.is_none() || root.as_ref().unwrap().borrow().val == 3 {
            return;
        }
        if let Some(node) = root {
            // Attempt
            path.push(node.clone());
            if node.borrow().val == 7 {
                // Record solution
                res.push(path.clone());
            }
            pre_order(res, path, node.borrow().left.as_ref());
            pre_order(res, path, node.borrow().right.as_ref());
            // Backtrack
            path.pop();
        }
    }
    ```
=== "C"
    ```c title="preorder_traversal_iii_compact.c"
    void preOrder(TreeNode *root) {
        // Pruning
        if (root == NULL || root->val == 3) {
            return;
        }
        // Attempt
        path[pathSize++] = root;
        if (root->val == 7) {
            // Record solution
            for (int i = 0; i < pathSize; i++) {
                res[resSize][i] = path[i];
            }
            resSize++;
        }
        preOrder(root->left);
        preOrder(root->right);
        // Backtrack
        pathSize--;
    }
    ```
=== "Kotlin"
    ```kotlin title="preorder_traversal_iii_compact.kt"
    fun preOrder(root: TreeNode?) {
        // Pruning
        if (root == null || root._val == 3) {
            return
        }
        // Attempt
        path!!.add(root)
        if (root._val == 7) {
            // Record solution
            res!!.add(path!!.toMutableList())
        }
        preOrder(root.left)
        preOrder(root.right)
        // Backtrack
        path!!.removeAt(path!!.size - 1)
    }
    ```
=== "Ruby"
    ```ruby title="preorder_traversal_iii_compact.rb"
    ### Pre-order traversal: example 3 ###
    def pre_order(root)
      # Pruning
      return if !root || root.val == 3
    
      # Attempt
      $path.append(root)
    
      # Record solution
      $res << $path.dup if root.val == 7
    
      pre_order(root.left)
      pre_order(root.right)
    
      # Backtrack
      $path.pop
    ```


"Cắt tỉa" là một thuật ngữ sống động. Như được hiển thị trong hình dưới đây, trong quá trình tìm kiếm, **chúng tôi "cắt tỉa" các nhánh tìm kiếm không thỏa mãn các ràng buộc**, tránh nhiều nỗ lực vô nghĩa và do đó cải thiện hiệu quả tìm kiếm.

![Pruning according to constraints](backtracking_algorithm.assets/preorder_find_constrained_paths.png)

## Mã khung

Tiếp theo, chúng tôi cố gắng trích xuất một khung chung tập trung vào "cố gắng, quay lại và cắt tỉa" của việc quay lại để cải thiện tính tổng quát của mã.

Trong mã khung sau đây, `state` thể hiện trạng thái hiện tại của vấn đề và `lựa chọn` thể hiện các lựa chọn có sẵn ở trạng thái hiện tại:

=== "Python"

    ```python title=""
    def backtrack(state: State, choices: list[choice], res: list[state]):
        """Backtracking algorithm framework"""
        # Check if it is a solution
        if is_solution(state):
            # Record the solution
            record_solution(state, res)
            # Stop searching
            return
        # Traverse all choices
        for choice in choices:
            # Pruning: check if the choice is valid
            if is_valid(state, choice):
                # Attempt: make a choice and update the state
                make_choice(state, choice)
                backtrack(state, choices, res)
                # Backtrack: undo the choice and restore to the previous state
                undo_choice(state, choice)
    ```

=== "C++"

    ```cpp title=""
    /* Backtracking algorithm framework */
    void backtrack(State *state, vector<Choice *> &choices, vector<State *> &res) {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record the solution
            recordSolution(state, res);
            // Stop searching
            return;
        }
        // Traverse all choices
        for (Choice choice : choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make a choice and update the state
                makeChoice(state, choice);
                backtrack(state, choices, res);
                // Backtrack: undo the choice and restore to the previous state
                undoChoice(state, choice);
            }
        }
    }
    ```

=== "Java"

    ```java title=""
    /* Backtracking algorithm framework */
    void backtrack(State state, List<Choice> choices, List<State> res) {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record the solution
            recordSolution(state, res);
            // Stop searching
            return;
        }
        // Traverse all choices
        for (Choice choice : choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make a choice and update the state
                makeChoice(state, choice);
                backtrack(state, choices, res);
                // Backtrack: undo the choice and restore to the previous state
                undoChoice(state, choice);
            }
        }
    }
    ```

=== "C#"

    ```csharp title=""
    /* Backtracking algorithm framework */
    void Backtrack(State state, List<Choice> choices, List<State> res) {
        // Check if it is a solution
        if (IsSolution(state)) {
            // Record the solution
            RecordSolution(state, res);
            // Stop searching
            return;
        }
        // Traverse all choices
        foreach (Choice choice in choices) {
            // Pruning: check if the choice is valid
            if (IsValid(state, choice)) {
                // Attempt: make a choice and update the state
                MakeChoice(state, choice);
                Backtrack(state, choices, res);
                // Backtrack: undo the choice and restore to the previous state
                UndoChoice(state, choice);
            }
        }
    }
    ```

=== "Đi"

    ```go title=""
    /* Backtracking algorithm framework */
    func backtrack(state *State, choices []Choice, res *[]State) {
        // Check if it is a solution
        if isSolution(state) {
            // Record the solution
            recordSolution(state, res)
            // Stop searching
            return
        }
        // Traverse all choices
        for _, choice := range choices {
            // Pruning: check if the choice is valid
            if isValid(state, choice) {
                // Attempt: make a choice and update the state
                makeChoice(state, choice)
                backtrack(state, choices, res)
                // Backtrack: undo the choice and restore to the previous state
                undoChoice(state, choice)
            }
        }
    }
    ```

=== "Nhanh chóng"

    ```swift title=""
    /* Backtracking algorithm framework */
    func backtrack(state: inout State, choices: [Choice], res: inout [State]) {
        // Check if it is a solution
        if isSolution(state: state) {
            // Record the solution
            recordSolution(state: state, res: &res)
            // Stop searching
            return
        }
        // Traverse all choices
        for choice in choices {
            // Pruning: check if the choice is valid
            if isValid(state: state, choice: choice) {
                // Attempt: make a choice and update the state
                makeChoice(state: &state, choice: choice)
                backtrack(state: &state, choices: choices, res: &res)
                // Backtrack: undo the choice and restore to the previous state
                undoChoice(state: &state, choice: choice)
            }
        }
    }
    ```

=== "JS"

    ```javascript title=""
    /* Backtracking algorithm framework */
    function backtrack(state, choices, res) {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record the solution
            recordSolution(state, res);
            // Stop searching
            return;
        }
        // Traverse all choices
        for (let choice of choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make a choice and update the state
                makeChoice(state, choice);
                backtrack(state, choices, res);
                // Backtrack: undo the choice and restore to the previous state
                undoChoice(state, choice);
            }
        }
    }
    ```

=== "TS"

    ```typescript title=""
    /* Backtracking algorithm framework */
    function backtrack(state: State, choices: Choice[], res: State[]): void {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record the solution
            recordSolution(state, res);
            // Stop searching
            return;
        }
        // Traverse all choices
        for (let choice of choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make a choice and update the state
                makeChoice(state, choice);
                backtrack(state, choices, res);
                // Backtrack: undo the choice and restore to the previous state
                undoChoice(state, choice);
            }
        }
    }
    ```

=== "Phi tiêu"

    ```dart title=""
    /* Backtracking algorithm framework */
    void backtrack(State state, List<Choice>, List<State> res) {
      // Check if it is a solution
      if (isSolution(state)) {
        // Record the solution
        recordSolution(state, res);
        // Stop searching
        return;
      }
      // Traverse all choices
      for (Choice choice in choices) {
        // Pruning: check if the choice is valid
        if (isValid(state, choice)) {
          // Attempt: make a choice and update the state
          makeChoice(state, choice);
          backtrack(state, choices, res);
          // Backtrack: undo the choice and restore to the previous state
          undoChoice(state, choice);
        }
      }
    }
    ```

=== "Rỉ sét"

    ```rust title=""
    /* Backtracking algorithm framework */
    fn backtrack(state: &mut State, choices: &Vec<Choice>, res: &mut Vec<State>) {
        // Check if it is a solution
        if is_solution(state) {
            // Record the solution
            record_solution(state, res);
            // Stop searching
            return;
        }
        // Traverse all choices
        for choice in choices {
            // Pruning: check if the choice is valid
            if is_valid(state, choice) {
                // Attempt: make a choice and update the state
                make_choice(state, choice);
                backtrack(state, choices, res);
                // Backtrack: undo the choice and restore to the previous state
                undo_choice(state, choice);
            }
        }
    }
    ```

=== "C"

    ```c title=""
    /* Backtracking algorithm framework */
    void backtrack(State *state, Choice *choices, int numChoices, State *res, int numRes) {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record the solution
            recordSolution(state, res, numRes);
            // Stop searching
            return;
        }
        // Traverse all choices
        for (int i = 0; i < numChoices; i++) {
            // Pruning: check if the choice is valid
            if (isValid(state, &choices[i])) {
                // Attempt: make a choice and update the state
                makeChoice(state, &choices[i]);
                backtrack(state, choices, numChoices, res, numRes);
                // Backtrack: undo the choice and restore to the previous state
                undoChoice(state, &choices[i]);
            }
        }
    }
    ```

=== "Kotlin"

    ```kotlin title=""
    /* Backtracking algorithm framework */
    fun backtrack(state: State?, choices: List<Choice?>, res: List<State?>?) {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record the solution
            recordSolution(state, res)
            // Stop searching
            return
        }
        // Traverse all choices
        for (choice in choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make a choice and update the state
                makeChoice(state, choice)
                backtrack(state, choices, res)
                // Backtrack: undo the choice and restore to the previous state
                undoChoice(state, choice)
            }
        }
    }
    ```

=== "Ruby"

    ```ruby title=""
    ### Backtracking algorithm framework ###
    def backtrack(state, choices, res)
        # Check if it is a solution
        if is_solution?(state)
            # Record the solution
            record_solution(state, res)
            return
        end

        # Traverse all choices
        for choice in choices
            # Pruning: check if the choice is valid
            if is_valid?(state, choice)
                # Attempt: make a choice and update the state
                make_choice(state, choice)
                backtrack(state, choices, res)
                # Backtrack: undo the choice and restore to the previous state
                undo_choice(state, choice)
            end
        end
    end
    ```

Tiếp theo, chúng ta giải Ví dụ 3 dựa trên mã khung. Trạng thái `state` là đường dẫn truyền tải nút, các lựa chọn `lựa chọn` là các nút con trái và phải của nút hiện tại và kết quả `res` là danh sách các đường dẫn:

=== "Python"
    ```python title="preorder_traversal_iii_template.py"
    def backtrack(
        state: list[TreeNode], choices: list[TreeNode], res: list[list[TreeNode]]
    ```
=== "C++"
    ```cpp title="preorder_traversal_iii_template.cpp"
    void backtrack(vector<TreeNode *> &state, vector<TreeNode *> &choices, vector<vector<TreeNode *>> &res) {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record solution
            recordSolution(state, res);
        }
        // Traverse all choices
        for (TreeNode *choice : choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make choice, update state
                makeChoice(state, choice);
                // Proceed to the next round of selection
                vector<TreeNode *> nextChoices{choice->left, choice->right};
                backtrack(state, nextChoices, res);
                // Backtrack: undo choice, restore to previous state
                undoChoice(state, choice);
            }
        }
    }
    ```
=== "Java"
    ```java title="preorder_traversal_iii_template.java"
    static void backtrack(List<TreeNode> state, List<TreeNode> choices, List<List<TreeNode>> res) {
            // Check if it is a solution
            if (isSolution(state)) {
                // Record solution
                recordSolution(state, res);
            }
            // Traverse all choices
            for (TreeNode choice : choices) {
                // Pruning: check if the choice is valid
                if (isValid(state, choice)) {
                    // Attempt: make choice, update state
                    makeChoice(state, choice);
                    // Proceed to the next round of selection
                    backtrack(state, Arrays.asList(choice.left, choice.right), res);
                    // Backtrack: undo choice, restore to previous state
                    undoChoice(state, choice);
                }
            }
        }
    ```
=== "C#"
    ```csharp title="preorder_traversal_iii_template.cs"
    void Backtrack(List<TreeNode> state, List<TreeNode> choices, List<List<TreeNode>> res) {
            // Check if it is a solution
            if (IsSolution(state)) {
                // Record solution
                RecordSolution(state, res);
            }
            // Traverse all choices
            foreach (TreeNode choice in choices) {
                // Pruning: check if the choice is valid
                if (IsValid(state, choice)) {
                    // Attempt: make choice, update state
                    MakeChoice(state, choice);
                    // Proceed to the next round of selection
                    Backtrack(state, [choice.left!, choice.right!], res);
                    // Backtrack: undo choice, restore to previous state
                    UndoChoice(state, choice);
                }
            }
        }
    ```
=== "Go"
    ```go title="preorder_traversal_iii_template.go"
    func backtrackIII(state *[]*TreeNode, choices *[]*TreeNode, res *[][]*TreeNode) {
    	// Check if it is a solution
    	if isSolution(state) {
    		// Record solution
    		recordSolution(state, res)
    	}
    	// Traverse all choices
    	for _, choice := range *choices {
    		// Pruning: check if the choice is valid
    		if isValid(state, choice) {
    			// Attempt: make choice, update state
    			makeChoice(state, choice)
    			// Proceed to the next round of selection
    			temp := make([]*TreeNode, 0)
    			temp = append(temp, choice.Left, choice.Right)
    			backtrackIII(state, &temp, res)
    			// Backtrack: undo choice, restore to previous state
    			undoChoice(state, choice)
    		}
    	}
    }
    ```
=== "Swift"
    ```swift title="preorder_traversal_iii_template.swift"
    func backtrack(state: inout [TreeNode], choices: [TreeNode], res: inout [[TreeNode]]) {
        // Check if it is a solution
        if isSolution(state: state) {
            recordSolution(state: state, res: &res)
        }
        // Traverse all choices
        for choice in choices {
            // Pruning: check if the choice is valid
            if isValid(state: state, choice: choice) {
                // Attempt: make choice, update state
                makeChoice(state: &state, choice: choice)
                // Proceed to the next round of selection
                backtrack(state: &state, choices: [choice.left, choice.right].compactMap { $0 }, res: &res)
                // Backtrack: undo choice, restore to previous state
                undoChoice(state: &state, choice: choice)
            }
        }
    }
    ```
=== "JS"
    ```javascript title="preorder_traversal_iii_template.js"
    function backtrack(state, choices, res) {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record solution
            recordSolution(state, res);
        }
        // Traverse all choices
        for (const choice of choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make choice, update state
                makeChoice(state, choice);
                // Proceed to the next round of selection
                backtrack(state, [choice.left, choice.right], res);
                // Backtrack: undo choice, restore to previous state
                undoChoice(state);
            }
        }
    }
    ```
=== "TS"
    ```typescript title="preorder_traversal_iii_template.ts"
    function backtrack(
        state: TreeNode[],
        choices: TreeNode[],
        res: TreeNode[][]
    ): void {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record solution
            recordSolution(state, res);
        }
        // Traverse all choices
        for (const choice of choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make choice, update state
                makeChoice(state, choice);
                // Proceed to the next round of selection
                backtrack(state, [choice.left, choice.right], res);
                // Backtrack: undo choice, restore to previous state
                undoChoice(state);
            }
        }
    }
    ```
=== "Dart"
    ```dart title="preorder_traversal_iii_template.dart"
    void backtrack(
      List<TreeNode> state,
      List<TreeNode?> choices,
      List<List<TreeNode>> res,
    ) {
      // Check if it is a solution
      if (isSolution(state)) {
        // Record solution
        recordSolution(state, res);
      }
      // Traverse all choices
      for (TreeNode? choice in choices) {
        // Pruning: check if the choice is valid
        if (isValid(state, choice)) {
          // Attempt: make choice, update state
          makeChoice(state, choice);
          // Proceed to the next round of selection
          backtrack(state, [choice!.left, choice.right], res);
          // Backtrack: undo choice, restore to previous state
          undoChoice(state, choice);
        }
      }
    }
    ```
=== "Rust"
    ```rust title="preorder_traversal_iii_template.rs"
    fn backtrack(
        state: &mut Vec<Rc<RefCell<TreeNode>>>,
        choices: &Vec<Option<&Rc<RefCell<TreeNode>>>>,
        res: &mut Vec<Vec<Rc<RefCell<TreeNode>>>>,
    ) {
        // Check if it is a solution
        if is_solution(state) {
            // Record solution
            record_solution(state, res);
        }
        // Traverse all choices
        for &choice in choices.iter() {
            // Pruning: check if the choice is valid
            if is_valid(state, choice) {
                // Attempt: make choice, update state
                make_choice(state, choice.unwrap().clone());
                // Proceed to the next round of selection
                backtrack(
                    state,
                    &vec![
                        choice.unwrap().borrow().left.as_ref(),
                        choice.unwrap().borrow().right.as_ref(),
                    ],
                    res,
                );
                // Backtrack: undo choice, restore to previous state
                undo_choice(state, choice.unwrap().clone());
            }
        }
    }
    ```
=== "C"
    ```c title="preorder_traversal_iii_template.c"
    void backtrack(TreeNode *choices[2]) {
        // Check if it is a solution
        if (isSolution()) {
            // Record solution
            recordSolution();
        }
        // Traverse all choices
        for (int i = 0; i < 2; i++) {
            TreeNode *choice = choices[i];
            // Pruning: check if the choice is valid
            if (isValid(choice)) {
                // Attempt: make choice, update state
                makeChoice(choice);
                // Proceed to the next round of selection
                TreeNode *nextChoices[2] = {choice->left, choice->right};
                backtrack(nextChoices);
                // Backtrack: undo choice, restore to previous state
                undoChoice();
            }
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="preorder_traversal_iii_template.kt"
    fun backtrack(
        state: MutableList<TreeNode?>,
        choices: MutableList<TreeNode?>,
        res: MutableList<MutableList<TreeNode?>?>
    ) {
        // Check if it is a solution
        if (isSolution(state)) {
            // Record solution
            recordSolution(state, res)
        }
        // Traverse all choices
        for (choice in choices) {
            // Pruning: check if the choice is valid
            if (isValid(state, choice)) {
                // Attempt: make choice, update state
                makeChoice(state, choice)
                // Proceed to the next round of selection
                backtrack(state, mutableListOf(choice!!.left, choice.right), res)
                // Backtrack: undo choice, restore to previous state
                undoChoice(state, choice)
            }
        }
    }
    ```
=== "Ruby"
    ```ruby title="preorder_traversal_iii_template.rb"
    ### Backtracking: example 3 ###
    def backtrack(state, choices, res)
      # Check if it is a solution
      record_solution(state, res) if is_solution?(state)
    
      # Traverse all choices
      for choice in choices
        # Pruning: check if the choice is valid
        if is_valid?(state, choice)
          # Attempt: make choice, update state
          make_choice(state, choice)
          # Proceed to the next round of selection
          backtrack(state, [choice.left, choice.right], res)
          # Backtrack: undo choice, restore to previous state
          undo_choice(state, choice)
        end
      end
    ```


Theo báo cáo vấn đề, chúng ta nên tiếp tục tìm kiếm sau khi tìm thấy nút có giá trị $7$. **Vì vậy, chúng ta cần xóa câu lệnh `return` sau khi ghi lại giải pháp**. Hình dưới đây so sánh quá trình tìm kiếm có và không có câu lệnh `return`.

![Comparison of search process with and without return statement](backtracking_algorithm.assets/backtrack_remove_return_or_not.png)

So với mã dựa trên việc truyền tải theo thứ tự trước, mã dựa trên khung thuật toán quay lui có vẻ dài dòng hơn nhưng tổng quát hơn. Trên thực tế, **nhiều vấn đề quay lui có thể được giải quyết trong khuôn khổ này**. Chúng ta chỉ cần xác định `state` và `lựa chọn` cho bài toán cụ thể và triển khai từng phương thức trong framework.

## Thuật ngữ thông dụng

Để phân tích các vấn đề thuật toán rõ ràng hơn, chúng tôi tóm tắt ý nghĩa của các thuật ngữ phổ biến được sử dụng trong thuật toán quay lui và cung cấp các ví dụ tương ứng từ Ví dụ 3, như được hiển thị trong bảng sau.

<p align="center"> Table <id> &nbsp; Common Backtracking Algorithm Terminology </p>

| Kỳ hạn | Định nghĩa | Ví dụ 3 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- ------------------ |
| Giải pháp (giải pháp) | Lời giải là lời giải thỏa mãn những điều kiện cụ thể của một bài toán; có thể có một hoặc nhiều giải pháp | Tất cả các đường dẫn từ gốc tới các nút có giá trị $7$ thỏa mãn ràng buộc |
| Ràng buộc (ràng buộc) | Ràng buộc là một điều kiện trong bài toán làm hạn chế tính khả thi của các giải pháp, thường được sử dụng để cắt tỉa | Đường dẫn không chứa các nút có giá trị $3$ |
| Bang (tiểu bang) | Trạng thái thể hiện tình huống của một vấn đề tại một thời điểm nhất định, bao gồm cả những lựa chọn đã được thực hiện | Đường dẫn nút hiện đang truy cập, tức là danh sách các nút `path` |
| Cố gắng (cố gắng) | Nỗ lực là quá trình khám phá không gian giải pháp theo các lựa chọn có sẵn, bao gồm đưa ra lựa chọn, cập nhật trạng thái và kiểm tra xem đó có phải là giải pháp hay không | Truy cập đệ quy các nút con bên trái (phải), thêm các nút vào `path`, kiểm tra xem giá trị nút có phải là $7$ |
| Quay lui (backtracking) | Quay lui đề cập đến việc hoàn tác các lựa chọn trước đó và quay trở lại trạng thái trước đó khi gặp trạng thái không thỏa mãn các ràng buộc | Dừng tìm kiếm khi đi qua các nút lá, kết thúc lượt truy cập nút hoặc gặp các nút có giá trị $3$; hàm trả về |
| Cắt tỉa (cắt tỉa) | Cắt tỉa là một phương pháp tránh các đường dẫn tìm kiếm vô nghĩa theo đặc điểm và ràng buộc của vấn đề, có thể cải thiện hiệu quả tìm kiếm | Khi gặp nút có giá trị $3$, đừng tiếp tục tìm kiếm |

!!! mẹo

Các khái niệm về vấn đề, giải pháp, trạng thái, v.v. là phổ biến và xuất hiện trong chia để trị, quay lui, lập trình động, thuật toán tham lam, v.v.

## Ưu điểm và hạn chế

Thuật toán quay lui về cơ bản là một thuật toán tìm kiếm theo chiều sâu, thử tất cả các giải pháp có thể cho đến khi tìm thấy giải pháp thỏa mãn các điều kiện. Ưu điểm của phương pháp này là có thể tìm ra mọi giải pháp có thể và với các thao tác cắt tỉa hợp lý thì đạt hiệu quả cao.

Tuy nhiên, khi xử lý các vấn đề có quy mô lớn hoặc phức tạp, **hiệu suất chạy của thuật toán quay lui có thể không được chấp nhận**.

- **Thời gian**: Thuật toán quay lui thường cần duyệt tất cả các khả năng trong không gian trạng thái và độ phức tạp về thời gian có thể đạt tới cấp số mũ hoặc giai thừa.
- **Không gian**: Trong các cuộc gọi đệ quy, trạng thái hiện tại cần được lưu lại (chẳng hạn như đường dẫn, các biến phụ dùng để cắt tỉa, v.v.) và khi độ sâu lớn, yêu cầu về không gian có thể trở nên rất lớn.

Tuy nhiên, **thuật toán quay lui vẫn là giải pháp tốt nhất cho các vấn đề tìm kiếm nhất định và các vấn đề về sự thỏa mãn ràng buộc**. Đối với những vấn đề này, vì chúng ta không thể dự đoán những lựa chọn nào sẽ tạo ra giải pháp hợp lệ nên chúng ta phải duyệt qua tất cả các lựa chọn có thể. Trong trường hợp này, **điều quan trọng là làm thế nào để tối ưu hóa hiệu quả**. Có hai phương pháp tối ưu hóa hiệu quả phổ biến.

- **Cắt tỉa**: Tránh tìm kiếm các đường dẫn được đảm bảo không tạo ra giải pháp, từ đó tiết kiệm thời gian và không gian.
- **Tìm kiếm theo kinh nghiệm**: Đưa ra các chiến lược hoặc giá trị ước tính nhất định trong quá trình tìm kiếm để ưu tiên các đường dẫn tìm kiếm có nhiều khả năng tạo ra giải pháp hợp lệ nhất.

## Ví dụ quay lui điển hình

Thuật toán quay lui có thể được sử dụng để giải quyết nhiều vấn đề tìm kiếm, vấn đề thỏa mãn ràng buộc và vấn đề tối ưu hóa tổ hợp.

**Bài toán tìm kiếm**: Mục tiêu của những bài toán này là tìm lời giải thỏa mãn các điều kiện cụ thể.

- Bài toán hoán vị: Cho một tập hợp, tìm tất cả các hoán vị và tổ hợp có thể có.
- Bài toán tổng tập con: Cho một tập hợp và một tổng đích, tìm tất cả các tập con trong tập hợp đó có các phần tử tổng bằng đích.
- Tháp Hà Nội: Cho ba chốt và một loạt các đĩa có kích thước khác nhau, di chuyển tất cả các đĩa từ cọc này sang cọc khác, mỗi lần chỉ di chuyển một đĩa và không bao giờ đặt một đĩa lớn hơn lên một đĩa nhỏ hơn.

**Vấn đề thỏa mãn ràng buộc**: Mục tiêu của những vấn đề này là tìm giải pháp thỏa mãn mọi ràng buộc.

- N-Queens: Đặt $n$ quân hậu lên bàn cờ $n \times n$ sao cho chúng không tấn công lẫn nhau.
- Sudoku: Điền các số từ $1$ đến $9$ vào lưới $9 \times 9$ sao cho mỗi hàng, cột và lưới con $3 \times 3$ không chứa các chữ số lặp lại.
- Tô màu đồ thị: Cho một đồ thị vô hướng, tô màu mỗi đỉnh với số màu tối thiểu sao cho các đỉnh liền kề có màu khác nhau.

**Các bài toán tối ưu hóa tổ hợp**: Mục tiêu của các bài toán này là tìm ra lời giải tối ưu thỏa mãn các điều kiện nhất định trong không gian tổ hợp.

- 0-1 Ba lô: Cho một bộ vật phẩm và một chiếc ba lô, mỗi vật phẩm đều có giá trị và trọng lượng. Trong giới hạn sức chứa của ba lô, hãy chọn những món đồ để tối đa hóa tổng giá trị.
- Bài toán nhân viên bán hàng du lịch: Bắt đầu từ một điểm trên đồ thị, ghé thăm tất cả các điểm khác đúng một lần và quay lại điểm xuất phát, tìm đường đi ngắn nhất.
- Cụm tối đa: Cho một đồ thị vô hướng, tìm đồ thị con hoàn chỉnh lớn nhất, tức là đồ thị con trong đó hai đỉnh bất kỳ được nối với nhau bằng một cạnh.

Lưu ý rằng đối với nhiều bài toán tối ưu hóa tổ hợp, quay lui không phải là giải pháp tối ưu.

- Bài toán Ba lô 0-1 thường được giải bằng quy hoạch động để đạt được hiệu quả về thời gian cao hơn.
- Bài toán Người du lịch là một bài toán NP-Hard nổi tiếng; các giải pháp phổ biến bao gồm thuật toán di truyền và thuật toán đàn kiến.
- Bài toán Cụm cực đại là một bài toán kinh điển trong lý thuyết đồ thị và có thể giải bằng các thuật toán heuristic như thuật toán tham lam.
