# Cây AVL *

Trong phần "Cây tìm kiếm nhị phân", chúng tôi đã đề cập rằng sau nhiều thao tác chèn và xóa, cây tìm kiếm nhị phân có thể thoái hóa thành danh sách liên kết. Trong trường hợp này, độ phức tạp về thời gian của tất cả các thao tác giảm từ $O(\log n)$ xuống $O(n)$.

Như thể hiện trong hình bên dưới, sau hai thao tác loại bỏ nút, cây tìm kiếm nhị phân này sẽ chuyển thành danh sách liên kết.

![Degradation of an AVL tree after removing nodes](avl_tree.assets/avltree_degradation_from_removing_node.png)

Ví dụ, trong cây nhị phân hoàn hảo như trong hình bên dưới, sau khi chèn hai nút, cây sẽ nghiêng nhiều về bên trái và độ phức tạp về thời gian của các thao tác tìm kiếm cũng sẽ giảm đi.

![Degradation of an AVL tree after inserting nodes](avl_tree.assets/avltree_degradation_from_inserting_node.png)

Năm 1962, G. M. Adelson-Velsky và E. M. Landis đã đề xuất <u>cây AVL</u> trong bài báo "Một thuật toán tổ chức thông tin". Bài viết mô tả một loạt các thao tác ngăn chặn cây AVL bị thoái hóa khi các nút được chèn và xóa, do đó giữ độ phức tạp về thời gian của các thao tác khác nhau ở mức $O(\log n)$. Nói cách khác, trong các tình huống yêu cầu các hoạt động chèn, xóa, tra cứu và cập nhật thường xuyên, cây AVL có thể duy trì hiệu suất ổn định và do đó có giá trị thực tế cao.

## Thuật ngữ thông dụng trong cây AVL

Cây AVL vừa là cây tìm kiếm nhị phân vừa là cây nhị phân cân bằng, đồng thời thỏa mãn tất cả các thuộc tính của hai loại cây nhị phân này nên là <u>cây tìm kiếm nhị phân cân bằng</u>.

### Chiều cao nút

Vì các hoạt động liên quan đến cây AVL yêu cầu lấy chiều cao nút, nên chúng ta cần thêm biến `height` vào lớp nút:

=== "Trăn"

    ```python title=""
    class TreeNode:
        """AVL tree node"""
        def __init__(self, val: int):
            self.val: int = val                 # Node value
            self.height: int = 0                # Node height
            self.left: TreeNode | None = None   # Left child reference
            self.right: TreeNode | None = None  # Right child reference
    ```

=== "C++"

    ```cpp title=""
    /* AVL tree node */
    struct TreeNode {
        int val{};          // Node value
        int height = 0;     // Node height
        TreeNode *left{};   // Left child
        TreeNode *right{};  // Right child
        TreeNode() = default;
        explicit TreeNode(int x) : val(x){}
    };
    ```

=== "Java"

    ```java title=""
    /* AVL tree node */
    class TreeNode {
        public int val;        // Node value
        public int height;     // Node height
        public TreeNode left;  // Left child
        public TreeNode right; // Right child
        public TreeNode(int x) { val = x; }
    }
    ```

=== "C#"

    ```csharp title=""
    /* AVL tree node */
    class TreeNode(int? x) {
        public int? val = x;    // Node value
        public int height;      // Node height
        public TreeNode? left;  // Left child reference
        public TreeNode? right; // Right child reference
    }
    ```

=== "Đi"

    ```go title=""
    /* AVL tree node */
    type TreeNode struct {
        Val    int       // Node value
        Height int       // Node height
        Left   *TreeNode // Left child reference
        Right  *TreeNode // Right child reference
    }
    ```

=== "Nhanh chóng"

    ```swift title=""
    /* AVL tree node */
    class TreeNode {
        var val: Int // Node value
        var height: Int // Node height
        var left: TreeNode? // Left child
        var right: TreeNode? // Right child

        init(x: Int) {
            val = x
            height = 0
        }
    }
    ```

=== "JS"

    ```javascript title=""
    /* AVL tree node */
    class TreeNode {
        val; // Node value
        height; // Node height
        left; // Left child pointer
        right; // Right child pointer
        constructor(val, left, right, height) {
            this.val = val === undefined ? 0 : val;
            this.height = height === undefined ? 0 : height;
            this.left = left === undefined ? null : left;
            this.right = right === undefined ? null : right;
        }
    }
    ```

=== "TS"

    ```typescript title=""
    /* AVL tree node */
    class TreeNode {
        val: number;            // Node value
        height: number;         // Node height
        left: TreeNode | null;  // Left child pointer
        right: TreeNode | null; // Right child pointer
        constructor(val?: number, height?: number, left?: TreeNode | null, right?: TreeNode | null) {
            this.val = val === undefined ? 0 : val;
            this.height = height === undefined ? 0 : height; 
            this.left = left === undefined ? null : left; 
            this.right = right === undefined ? null : right; 
        }
    }
    ```

=== "Phi tiêu"

    ```dart title=""
    /* AVL tree node */
    class TreeNode {
      int val;         // Node value
      int height;      // Node height
      TreeNode? left;  // Left child
      TreeNode? right; // Right child
      TreeNode(this.val, [this.height = 0, this.left, this.right]);
    }
    ```

=== "Rỉ sét"

    ```rust title=""
    use std::rc::Rc;
    use std::cell::RefCell;

    /* AVL tree node */
    struct TreeNode {
        val: i32,                               // Node value
        height: i32,                            // Node height
        left: Option<Rc<RefCell<TreeNode>>>,    // Left child
        right: Option<Rc<RefCell<TreeNode>>>,   // Right child
    }

    impl TreeNode {
        /* Constructor */
        fn new(val: i32) -> Rc<RefCell<Self>> {
            Rc::new(RefCell::new(Self {
                val,
                height: 0,
                left: None,
                right: None
            }))
        }
    }
    ```

=== "C"

    ```c title=""
    /* AVL tree node */
    typedef struct TreeNode {
        int val;
        int height;
        struct TreeNode *left;
        struct TreeNode *right;
    } TreeNode;

    /* Constructor */
    TreeNode *newTreeNode(int val) {
        TreeNode *node;

        node = (TreeNode *)malloc(sizeof(TreeNode));
        node->val = val;
        node->height = 0;
        node->left = NULL;
        node->right = NULL;
        return node;
    }
    ```

=== "Kotlin"

    ```kotlin title=""
    /* AVL tree node */
    class TreeNode(val _val: Int) {  // Node value
        val height: Int = 0          // Node height
        val left: TreeNode? = null   // Left child
        val right: TreeNode? = null  // Right child
    }
    ```

=== "Ruby"

    ```ruby title=""
    ### AVL tree node class ###
    class TreeNode
      attr_accessor :val    # Node value
      attr_accessor :height # Node height
      attr_accessor :left   # Left child reference
      attr_accessor :right  # Right child reference

      def initialize(val)
        @val = val
        @height = 0
      end
    end
    ```

"Chiều cao nút" đề cập đến khoảng cách từ nút đó đến nút lá xa nhất của nó, tức là số cạnh trên đường dẫn. Điều quan trọng cần lưu ý là chiều cao của nút lá là $0$ và chiều cao của nút null là $-1$. Chúng ta sẽ tạo hai hàm tiện ích để lấy và cập nhật chiều cao của nút:

=== "Python"
    ```python title="avl_tree.py"
    def update_height(self, node: TreeNode | None):
            """Update node height"""
            # Node height equals the height of the tallest subtree + 1
            node.height = max([self.height(node.left), self.height(node.right)]) + 1
    ```
=== "C++"
    ```cpp title="avl_tree.cpp"
    void updateHeight(TreeNode *node) {
            // Node height equals the height of the tallest subtree + 1
            node->height = max(height(node->left), height(node->right)) + 1;
        }
    ```
=== "Java"
    ```java title="avl_tree.java"
    private void updateHeight(TreeNode node) {
            // Node height equals the height of the tallest subtree + 1
            node.height = Math.max(height(node.left), height(node.right)) + 1;
        }
    ```
=== "C#"
    ```csharp title="avl_tree.cs"
    void UpdateHeight(TreeNode node) {
            // Node height equals the height of the tallest subtree + 1
            node.height = Math.Max(Height(node.left), Height(node.right)) + 1;
        }
    ```
=== "Go"
    ```go title="avl_tree.go"
    func (t *aVLTree) updateHeight(node *TreeNode) {
    	lh := t.height(node.Left)
    	rh := t.height(node.Right)
    	// Node height equals the height of the tallest subtree + 1
    	if lh > rh {
    		node.Height = lh + 1
    	} else {
    		node.Height = rh + 1
    	}
    }
    ```
=== "Swift"
    ```swift title="avl_tree.swift"
    private func updateHeight(node: TreeNode?) {
            // Node height equals the height of the tallest subtree + 1
            node?.height = max(height(node: node?.left), height(node: node?.right)) + 1
        }
    ```
=== "JS"
    ```javascript title="avl_tree.js"
    #updateHeight(node) {
            // Node height equals the height of the tallest subtree + 1
            node.height =
                Math.max(this.height(node.left), this.height(node.right)) + 1;
        }
    ```
=== "TS"
    ```typescript title="avl_tree.ts"
    private updateHeight(node: TreeNode): void {
            // Node height equals the height of the tallest subtree + 1
            node.height =
                Math.max(this.height(node.left), this.height(node.right)) + 1;
        }
    ```
=== "Dart"
    ```dart title="avl_tree.dart"
    void updateHeight(TreeNode? node) {
        // Node height equals the height of the tallest subtree + 1
        node!.height = max(height(node.left), height(node.right)) + 1;
      }
    ```
=== "Rust"
    ```rust title="avl_tree.rs"
    fn update_height(node: OptionTreeNodeRc) {
            if let Some(node) = node {
                let left = node.borrow().left.clone();
                let right = node.borrow().right.clone();
                // Node height equals the height of the tallest subtree + 1
                node.borrow_mut().height = std::cmp::max(Self::height(left), Self::height(right)) + 1;
            }
        }
    ```
=== "C"
    ```c title="avl_tree.c"
    void updateHeight(TreeNode *node) {
        int lh = height(node->left);
        int rh = height(node->right);
        // Node height equals the height of the tallest subtree + 1
        if (lh > rh) {
            node->height = lh + 1;
        } else {
            node->height = rh + 1;
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="avl_tree.kt"
    private fun updateHeight(node: TreeNode?) {
            // Node height equals the height of the tallest subtree + 1
            node?.height = max(height(node?.left), height(node?.right)) + 1
        }
    ```
=== "Ruby"
    ```ruby title="avl_tree.rb"
    ### Update node height ###
      def update_height(node)
        # Node height equals the height of the tallest subtree + 1
        node.height = [height(node.left), height(node.right)].max + 1
    ```


### Hệ số cân bằng nút

<u>Hệ số cân bằng</u> của một nút được xác định bằng chiều cao của cây con bên trái của nút trừ đi chiều cao của cây con bên phải của nó và hệ số cân bằng của nút rỗng được xác định là $0$. Chúng tôi cũng gói gọn hàm để lấy hệ số cân bằng của nút để thuận tiện cho việc sử dụng sau này:

=== "Python"
    ```python title="avl_tree.py"
    def balance_factor(self, node: TreeNode | None) -> int:
            """Get balance factor"""
            # Empty node balance factor is 0
            if node is None:
                return 0
            # Node balance factor = left subtree height - right subtree height
            return self.height(node.left) - self.height(node.right)
    ```
=== "C++"
    ```cpp title="avl_tree.cpp"
    // Get balance factor of node
            int _balanceFactor = balanceFactor(node);
            // Left-leaning tree
            if (_balanceFactor > 1) {
                if (balanceFactor(node->left) >= 0) {
                    // Right rotation
                    return rightRotate(node);
                } else {
                    // First left rotation then right rotation
                    node->left = leftRotate(node->left);
                    return rightRotate(node);
                }
            }
    ```
=== "Java"
    ```java title="avl_tree.java"
    public int balanceFactor(TreeNode node) {
            // Empty node balance factor is 0
            if (node == null)
                return 0;
            // Node balance factor = left subtree height - right subtree height
            return height(node.left) - height(node.right);
        }
    ```
=== "C#"
    ```csharp title="avl_tree.cs"
    public int BalanceFactor(TreeNode? node) {
            // Empty node balance factor is 0
            if (node == null) return 0;
            // Node balance factor = left subtree height - right subtree height
            return Height(node.left) - Height(node.right);
        }
    ```
=== "Go"
    ```go title="avl_tree.go"
    func (t *aVLTree) balanceFactor(node *TreeNode) int {
    	// Empty node balance factor is 0
    	if node == nil {
    		return 0
    	}
    	// Node balance factor = left subtree height - right subtree height
    	return t.height(node.Left) - t.height(node.Right)
    }
    ```
=== "Swift"
    ```swift title="avl_tree.swift"
    func balanceFactor(node: TreeNode?) -> Int {
            // Empty node balance factor is 0
            guard let node = node else { return 0 }
            // Node balance factor = left subtree height - right subtree height
            return height(node: node.left) - height(node: node.right)
        }
    ```
=== "JS"
    ```javascript title="avl_tree.js"
    balanceFactor(node) {
            // Empty node balance factor is 0
            if (node === null) return 0;
            // Node balance factor = left subtree height - right subtree height
            return this.height(node.left) - this.height(node.right);
        }
    ```
=== "TS"
    ```typescript title="avl_tree.ts"
    balanceFactor(node: TreeNode): number {
            // Empty node balance factor is 0
            if (node === null) return 0;
            // Node balance factor = left subtree height - right subtree height
            return this.height(node.left) - this.height(node.right);
        }
    ```
=== "Dart"
    ```dart title="avl_tree.dart"
    int balanceFactor(TreeNode? node) {
        // Empty node balance factor is 0
        if (node == null) return 0;
        // Node balance factor = left subtree height - right subtree height
        return height(node.left) - height(node.right);
      }
    ```
=== "Rust"
    ```rust title="avl_tree.rs"
    fn balance_factor(node: OptionTreeNodeRc) -> i32 {
            match node {
                // Empty node balance factor is 0
                None => 0,
                // Node balance factor = left subtree height - right subtree height
                Some(node) => {
                    Self::height(node.borrow().left.clone()) - Self::height(node.borrow().right.clone())
                }
            }
        }
    ```
=== "C"
    ```c title="avl_tree.c"
    int balanceFactor(TreeNode *node) {
        // Empty node balance factor is 0
        if (node == NULL) {
            return 0;
        }
        // Node balance factor = left subtree height - right subtree height
        return height(node->left) - height(node->right);
    }
    ```
=== "Kotlin"
    ```kotlin title="avl_tree.kt"
    fun balanceFactor(node: TreeNode?): Int {
            // Empty node balance factor is 0
            if (node == null) return 0
            // Node balance factor = left subtree height - right subtree height
            return height(node.left) - height(node.right)
        }
    ```
=== "Ruby"
    ```ruby title="avl_tree.rb"
    ### Get balance factor ###
      def balance_factor(node)
        # Empty node balance factor is 0
        return 0 if node.nil?
    
        # Node balance factor = left subtree height - right subtree height
        height(node.left) - height(node.right)
    ```


!!! mẹo

Đặt hệ số cân bằng là $f$ thì hệ số cân bằng của bất kỳ nút nào trong cây AVL thỏa mãn $-1 \le f \le 1$.

## Phép quay trong cây AVL

Đặc điểm của cây AVL nằm ở thao tác “xoay”, có thể khôi phục lại sự cân bằng cho các nút không cân bằng mà không ảnh hưởng đến trình tự duyệt theo thứ tự của cây nhị phân. Nói cách khác, **các thao tác xoay có thể vừa duy trì thuộc tính của "cây tìm kiếm nhị phân" vừa làm cho cây trở về "cây nhị phân cân bằng"**.

Chúng tôi gọi các nút có giá trị tuyệt đối của hệ số cân bằng $> 1$ là "các nút không cân bằng". Tùy thuộc vào tình trạng mất cân bằng, các thao tác quay được chia thành 4 loại: quay phải, quay trái, quay phải rồi quay trái và quay trái rồi quay phải. Dưới đây chúng tôi mô tả chi tiết các hoạt động xoay vòng này.

### Xoay phải

Như thể hiện trong hình bên dưới, giá trị bên dưới nút là hệ số cân bằng. Từ dưới lên trên, nút không cân bằng đầu tiên trong cây nhị phân là “nút 3”. Chúng tôi tập trung vào cây con với nút không cân bằng này làm gốc, biểu thị nút là `nút` và nút con bên trái của nó là `con` và thực hiện thao tác "xoay phải". Sau khi hoàn thành phép quay bên phải, cây con lấy lại sự cân bằng và vẫn duy trì các thuộc tính của cây tìm kiếm nhị phân.

=== "<1>"
    ![Steps of right rotation](avl_tree.assets/avltree_right_rotate_step1.png)

=== "<2>"
    ![avltree_right_rotate_step2](avl_tree.assets/avltree_right_rotate_step2.png)

=== "<3>"
    ![avltree_right_rotate_step3](avl_tree.assets/avltree_right_rotate_step3.png)

=== "<4>"
    ![avltree_right_rotate_step4](avl_tree.assets/avltree_right_rotate_step4.png)

Như minh họa trong hình bên dưới, khi nút `child` có nút con bên phải (ký hiệu là `grand_child`), cần thêm một bước trong phép quay bên phải: đặt `grand_child` làm nút con bên trái của `node`.

![Right rotation with grand_child](avl_tree.assets/avltree_right_rotate_with_grandchild.png)

"Xoay phải" là một thuật ngữ tượng hình; trong thực tế, điều này đạt được bằng cách sửa đổi các con trỏ nút, như trong đoạn mã sau:

=== "Python"
    ```python title="avl_tree.py"
    def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
            """Right rotation operation"""
            child = node.left
            grand_child = child.right
            # Using child as pivot, rotate node to the right
            child.right = node
            node.left = grand_child
            # Update node height
            self.update_height(node)
            self.update_height(child)
            # Return root node of subtree after rotation
            return child
    ```
=== "C++"
    ```cpp title="avl_tree.cpp"
    TreeNode *rightRotate(TreeNode *node) {
            TreeNode *child = node->left;
            TreeNode *grandChild = child->right;
            // Using child as pivot, rotate node to the right
            child->right = node;
            node->left = grandChild;
            // Update node height
            updateHeight(node);
            updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Java"
    ```java title="avl_tree.java"
    private TreeNode rightRotate(TreeNode node) {
            TreeNode child = node.left;
            TreeNode grandChild = child.right;
            // Using child as pivot, rotate node to the right
            child.right = node;
            node.left = grandChild;
            // Update node height
            updateHeight(node);
            updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "C#"
    ```csharp title="avl_tree.cs"
    TreeNode? RightRotate(TreeNode? node) {
            TreeNode? child = node?.left;
            TreeNode? grandChild = child?.right;
            // Using child as pivot, rotate node to the right
            child.right = node;
            node.left = grandChild;
            // Update node height
            UpdateHeight(node);
            UpdateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Go"
    ```go title="avl_tree.go"
    func (t *aVLTree) rightRotate(node *TreeNode) *TreeNode {
    	child := node.Left
    	grandChild := child.Right
    	// Using child as pivot, rotate node to the right
    	child.Right = node
    	node.Left = grandChild
    	// Update node height
    	t.updateHeight(node)
    	t.updateHeight(child)
    	// Return root node of subtree after rotation
    	return child
    }
    ```
=== "Swift"
    ```swift title="avl_tree.swift"
    private func rightRotate(node: TreeNode?) -> TreeNode? {
            let child = node?.left
            let grandChild = child?.right
            // Using child as pivot, rotate node to the right
            child?.right = node
            node?.left = grandChild
            // Update node height
            updateHeight(node: node)
            updateHeight(node: child)
            // Return root node of subtree after rotation
            return child
        }
    ```
=== "JS"
    ```javascript title="avl_tree.js"
    #rightRotate(node) {
            const child = node.left;
            const grandChild = child.right;
            // Using child as pivot, rotate node to the right
            child.right = node;
            node.left = grandChild;
            // Update node height
            this.#updateHeight(node);
            this.#updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "TS"
    ```typescript title="avl_tree.ts"
    private rightRotate(node: TreeNode): TreeNode {
            const child = node.left;
            const grandChild = child.right;
            // Using child as pivot, rotate node to the right
            child.right = node;
            node.left = grandChild;
            // Update node height
            this.updateHeight(node);
            this.updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Dart"
    ```dart title="avl_tree.dart"
    TreeNode? rightRotate(TreeNode? node) {
        TreeNode? child = node!.left;
        TreeNode? grandChild = child!.right;
        // Using child as pivot, rotate node to the right
        child.right = node;
        node.left = grandChild;
        // Update node height
        updateHeight(node);
        updateHeight(child);
        // Return root node of subtree after rotation
        return child;
      }
    ```
=== "Rust"
    ```rust title="avl_tree.rs"
    fn right_rotate(node: OptionTreeNodeRc) -> OptionTreeNodeRc {
            match node {
                Some(node) => {
                    let child = node.borrow().left.clone().unwrap();
                    let grand_child = child.borrow().right.clone();
                    // Using child as pivot, rotate node to the right
                    child.borrow_mut().right = Some(node.clone());
                    node.borrow_mut().left = grand_child;
                    // Update node height
                    Self::update_height(Some(node));
                    Self::update_height(Some(child.clone()));
                    // Return root node of subtree after rotation
                    Some(child)
                }
                None => None,
            }
        }
    ```
=== "C"
    ```c title="avl_tree.c"
    TreeNode *rightRotate(TreeNode *node) {
        TreeNode *child, *grandChild;
        child = node->left;
        grandChild = child->right;
        // Using child as pivot, rotate node to the right
        child->right = node;
        node->left = grandChild;
        // Update node height
        updateHeight(node);
        updateHeight(child);
        // Return root node of subtree after rotation
        return child;
    }
    ```
=== "Kotlin"
    ```kotlin title="avl_tree.kt"
    private fun rightRotate(node: TreeNode?): TreeNode {
            val child = node!!.left
            val grandChild = child!!.right
            // Using child as pivot, rotate node to the right
            child.right = node
            node.left = grandChild
            // Update node height
            updateHeight(node)
            updateHeight(child)
            // Return root node of subtree after rotation
            return child
        }
    ```
=== "Ruby"
    ```ruby title="avl_tree.rb"
    ### Right rotation ###
      def right_rotate(node)
        child = node.left
        grand_child = child.right
        # Using child as pivot, rotate node to the right
        child.right = node
        node.left = grand_child
        # Update node height
        update_height(node)
        update_height(child)
        # Return root node of subtree after rotation
        child
    ```


### Xoay trái

Tương ứng, nếu xét “gương” của cây nhị phân không cân bằng trên thì cần phải thực hiện thao tác “xoay trái” như hình dưới đây.

![Left rotation operation](avl_tree.assets/avltree_left_rotate.png)

Tương tự, như trong hình bên dưới, khi nút `child` có nút con bên trái (ký hiệu là `grand_child`), cần thêm một bước trong phép quay trái: đặt `grand_child` làm nút con bên phải của `node`.

![Left rotation with grand_child](avl_tree.assets/avltree_left_rotate_with_grandchild.png)

Có thể thấy rằng **các phép toán xoay phải và xoay trái là đối xứng gương về mặt logic và hai trường hợp mất cân bằng mà chúng giải quyết cũng đối xứng**. Dựa trên tính đối xứng, chúng ta chỉ cần thay thế tất cả `left` trong mã triển khai xoay bên phải bằng `right` và tất cả `right` bằng `left`, để có được mã triển khai xoay trái:

=== "Python"
    ```python title="avl_tree.py"
    def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
            """Left rotation operation"""
            child = node.right
            grand_child = child.left
            # Using child as pivot, rotate node to the left
            child.left = node
            node.right = grand_child
            # Update node height
            self.update_height(node)
            self.update_height(child)
            # Return root node of subtree after rotation
            return child
    ```
=== "C++"
    ```cpp title="avl_tree.cpp"
    TreeNode *leftRotate(TreeNode *node) {
            TreeNode *child = node->right;
            TreeNode *grandChild = child->left;
            // Using child as pivot, rotate node to the left
            child->left = node;
            node->right = grandChild;
            // Update node height
            updateHeight(node);
            updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Java"
    ```java title="avl_tree.java"
    private TreeNode leftRotate(TreeNode node) {
            TreeNode child = node.right;
            TreeNode grandChild = child.left;
            // Using child as pivot, rotate node to the left
            child.left = node;
            node.right = grandChild;
            // Update node height
            updateHeight(node);
            updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "C#"
    ```csharp title="avl_tree.cs"
    TreeNode? LeftRotate(TreeNode? node) {
            TreeNode? child = node?.right;
            TreeNode? grandChild = child?.left;
            // Using child as pivot, rotate node to the left
            child.left = node;
            node.right = grandChild;
            // Update node height
            UpdateHeight(node);
            UpdateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Go"
    ```go title="avl_tree.go"
    func (t *aVLTree) leftRotate(node *TreeNode) *TreeNode {
    	child := node.Right
    	grandChild := child.Left
    	// Using child as pivot, rotate node to the left
    	child.Left = node
    	node.Right = grandChild
    	// Update node height
    	t.updateHeight(node)
    	t.updateHeight(child)
    	// Return root node of subtree after rotation
    	return child
    }
    ```
=== "Swift"
    ```swift title="avl_tree.swift"
    private func leftRotate(node: TreeNode?) -> TreeNode? {
            let child = node?.right
            let grandChild = child?.left
            // Using child as pivot, rotate node to the left
            child?.left = node
            node?.right = grandChild
            // Update node height
            updateHeight(node: node)
            updateHeight(node: child)
            // Return root node of subtree after rotation
            return child
        }
    ```
=== "JS"
    ```javascript title="avl_tree.js"
    #leftRotate(node) {
            const child = node.right;
            const grandChild = child.left;
            // Using child as pivot, rotate node to the left
            child.left = node;
            node.right = grandChild;
            // Update node height
            this.#updateHeight(node);
            this.#updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "TS"
    ```typescript title="avl_tree.ts"
    private leftRotate(node: TreeNode): TreeNode {
            const child = node.right;
            const grandChild = child.left;
            // Using child as pivot, rotate node to the left
            child.left = node;
            node.right = grandChild;
            // Update node height
            this.updateHeight(node);
            this.updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Dart"
    ```dart title="avl_tree.dart"
    TreeNode? leftRotate(TreeNode? node) {
        TreeNode? child = node!.right;
        TreeNode? grandChild = child!.left;
        // Using child as pivot, rotate node to the left
        child.left = node;
        node.right = grandChild;
        // Update node height
        updateHeight(node);
        updateHeight(child);
        // Return root node of subtree after rotation
        return child;
      }
    ```
=== "Rust"
    ```rust title="avl_tree.rs"
    fn left_rotate(node: OptionTreeNodeRc) -> OptionTreeNodeRc {
            match node {
                Some(node) => {
                    let child = node.borrow().right.clone().unwrap();
                    let grand_child = child.borrow().left.clone();
                    // Using child as pivot, rotate node to the left
                    child.borrow_mut().left = Some(node.clone());
                    node.borrow_mut().right = grand_child;
                    // Update node height
                    Self::update_height(Some(node));
                    Self::update_height(Some(child.clone()));
                    // Return root node of subtree after rotation
                    Some(child)
                }
                None => None,
            }
        }
    ```
=== "C"
    ```c title="avl_tree.c"
    TreeNode *leftRotate(TreeNode *node) {
        TreeNode *child, *grandChild;
        child = node->right;
        grandChild = child->left;
        // Using child as pivot, rotate node to the left
        child->left = node;
        node->right = grandChild;
        // Update node height
        updateHeight(node);
        updateHeight(child);
        // Return root node of subtree after rotation
        return child;
    }
    ```
=== "Kotlin"
    ```kotlin title="avl_tree.kt"
    private fun leftRotate(node: TreeNode?): TreeNode {
            val child = node!!.right
            val grandChild = child!!.left
            // Using child as pivot, rotate node to the left
            child.left = node
            node.right = grandChild
            // Update node height
            updateHeight(node)
            updateHeight(child)
            // Return root node of subtree after rotation
            return child
        }
    ```
=== "Ruby"
    ```ruby title="avl_tree.rb"
    ### Left rotation ###
      def left_rotate(node)
        child = node.right
        grand_child = child.left
        # Using child as pivot, rotate node to the left
        child.left = node
        node.right = grand_child
        # Update node height
        update_height(node)
        update_height(child)
        # Return root node of subtree after rotation
        child
    ```


### Xoay trái rồi xoay phải

Đối với nút 3 không cân bằng trong hình bên dưới, chỉ sử dụng phép quay trái hoặc xoay phải không thể khôi phục cây con về trạng thái cân bằng. Trong trường hợp này, trước tiên cần phải thực hiện "xoay trái" trên `con`, sau đó là "xoay phải" trên `nút`.

![Left-right rotation](avl_tree.assets/avltree_left_right_rotate.png)

### Xoay phải rồi xoay trái

Như được hiển thị trong hình bên dưới, đối với trường hợp phản chiếu của cây nhị phân không cân bằng ở trên, trước tiên cần thực hiện "xoay phải" trên `con`, sau đó là "xoay trái" trên `nút`.

![Right-left rotation](avl_tree.assets/avltree_right_left_rotate.png)

### Lựa chọn xoay

Bốn sự mất cân bằng thể hiện trong hình bên dưới tương ứng một-một với các trường hợp trên, yêu cầu các thao tác xoay phải, xoay trái rồi xoay phải, xoay phải rồi xoay trái và xoay trái tương ứng.

![The four rotation cases of AVL tree](avl_tree.assets/avltree_rotation_cases.png)

Như được hiển thị trong bảng bên dưới, chúng tôi xác định nút không cân bằng thuộc trường hợp nào bằng cách đánh giá các dấu hiệu của hệ số cân bằng của nút không cân bằng và hệ số cân bằng của nút con phía cao hơn của nó.

<p align="center"> Table <id> &nbsp; Conditions for Choosing Among the Four Rotation Cases </p>

| Hệ số cân bằng của nút không cân bằng | Hệ số cân bằng của nút con | Phương pháp luân chuyển để áp dụng |
| -------------------------------------- | --------------------------------- | --------------------------------- |
| $> 1$ (cây nghiêng trái) | $\geq 0$ | Xoay phải |
| $> 1$ (cây nghiêng trái) | $<0$ | Xoay trái rồi xoay phải |
| $< -1$ (cây nghiêng phải) | $\leq 0$ | Xoay trái |
| $< -1$ (cây nghiêng phải) | $>0$ | Xoay phải rồi xoay trái |

Để dễ sử dụng, chúng tôi gói gọn các thao tác xoay thành một hàm. **Với chức năng này, chúng ta có thể thực hiện phép quay trong các tình huống mất cân bằng khác nhau, khôi phục lại sự cân bằng cho các nút không cân bằng**. Mã này như sau:

=== "Python"
    ```python title="avl_tree.py"
    def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
            """Right rotation operation"""
            child = node.left
            grand_child = child.right
            # Using child as pivot, rotate node to the right
            child.right = node
            node.left = grand_child
            # Update node height
            self.update_height(node)
            self.update_height(child)
            # Return root node of subtree after rotation
            return child
    ```
=== "C++"
    ```cpp title="avl_tree.cpp"
    TreeNode *rightRotate(TreeNode *node) {
            TreeNode *child = node->left;
            TreeNode *grandChild = child->right;
            // Using child as pivot, rotate node to the right
            child->right = node;
            node->left = grandChild;
            // Update node height
            updateHeight(node);
            updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Java"
    ```java title="avl_tree.java"
    private TreeNode rightRotate(TreeNode node) {
            TreeNode child = node.left;
            TreeNode grandChild = child.right;
            // Using child as pivot, rotate node to the right
            child.right = node;
            node.left = grandChild;
            // Update node height
            updateHeight(node);
            updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "C#"
    ```csharp title="avl_tree.cs"
    TreeNode? RightRotate(TreeNode? node) {
            TreeNode? child = node?.left;
            TreeNode? grandChild = child?.right;
            // Using child as pivot, rotate node to the right
            child.right = node;
            node.left = grandChild;
            // Update node height
            UpdateHeight(node);
            UpdateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Go"
    ```go title="avl_tree.go"
    func (t *aVLTree) rightRotate(node *TreeNode) *TreeNode {
    	child := node.Left
    	grandChild := child.Right
    	// Using child as pivot, rotate node to the right
    	child.Right = node
    	node.Left = grandChild
    	// Update node height
    	t.updateHeight(node)
    	t.updateHeight(child)
    	// Return root node of subtree after rotation
    	return child
    }
    ```
=== "Swift"
    ```swift title="avl_tree.swift"
    private func rightRotate(node: TreeNode?) -> TreeNode? {
            let child = node?.left
            let grandChild = child?.right
            // Using child as pivot, rotate node to the right
            child?.right = node
            node?.left = grandChild
            // Update node height
            updateHeight(node: node)
            updateHeight(node: child)
            // Return root node of subtree after rotation
            return child
        }
    ```
=== "JS"
    ```javascript title="avl_tree.js"
    #rightRotate(node) {
            const child = node.left;
            const grandChild = child.right;
            // Using child as pivot, rotate node to the right
            child.right = node;
            node.left = grandChild;
            // Update node height
            this.#updateHeight(node);
            this.#updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "TS"
    ```typescript title="avl_tree.ts"
    private rightRotate(node: TreeNode): TreeNode {
            const child = node.left;
            const grandChild = child.right;
            // Using child as pivot, rotate node to the right
            child.right = node;
            node.left = grandChild;
            // Update node height
            this.updateHeight(node);
            this.updateHeight(child);
            // Return root node of subtree after rotation
            return child;
        }
    ```
=== "Dart"
    ```dart title="avl_tree.dart"
    TreeNode? rightRotate(TreeNode? node) {
        TreeNode? child = node!.left;
        TreeNode? grandChild = child!.right;
        // Using child as pivot, rotate node to the right
        child.right = node;
        node.left = grandChild;
        // Update node height
        updateHeight(node);
        updateHeight(child);
        // Return root node of subtree after rotation
        return child;
      }
    ```
=== "Rust"
    ```rust title="avl_tree.rs"
    fn right_rotate(node: OptionTreeNodeRc) -> OptionTreeNodeRc {
            match node {
                Some(node) => {
                    let child = node.borrow().left.clone().unwrap();
                    let grand_child = child.borrow().right.clone();
                    // Using child as pivot, rotate node to the right
                    child.borrow_mut().right = Some(node.clone());
                    node.borrow_mut().left = grand_child;
                    // Update node height
                    Self::update_height(Some(node));
                    Self::update_height(Some(child.clone()));
                    // Return root node of subtree after rotation
                    Some(child)
                }
                None => None,
            }
        }
    ```
=== "C"
    ```c title="avl_tree.c"
    TreeNode *rightRotate(TreeNode *node) {
        TreeNode *child, *grandChild;
        child = node->left;
        grandChild = child->right;
        // Using child as pivot, rotate node to the right
        child->right = node;
        node->left = grandChild;
        // Update node height
        updateHeight(node);
        updateHeight(child);
        // Return root node of subtree after rotation
        return child;
    }
    ```
=== "Kotlin"
    ```kotlin title="avl_tree.kt"
    private fun rightRotate(node: TreeNode?): TreeNode {
            val child = node!!.left
            val grandChild = child!!.right
            // Using child as pivot, rotate node to the right
            child.right = node
            node.left = grandChild
            // Update node height
            updateHeight(node)
            updateHeight(child)
            // Return root node of subtree after rotation
            return child
        }
    ```
=== "Ruby"
    ```ruby title="avl_tree.rb"
    ### Right rotation ###
      def right_rotate(node)
        child = node.left
        grand_child = child.right
        # Using child as pivot, rotate node to the right
        child.right = node
        node.left = grand_child
        # Update node height
        update_height(node)
        update_height(child)
        # Return root node of subtree after rotation
        child
    ```


## Các thao tác chung trong cây AVL

### Chèn nút

Hoạt động chèn nút trong cây AVL về nguyên tắc tương tự như trong cây tìm kiếm nhị phân. Điểm khác biệt duy nhất là sau khi chèn một nút vào cây AVL, một loạt nút không cân bằng có thể xuất hiện trên đường dẫn từ nút đó đến gốc. Do đó, **chúng ta cần bắt đầu từ nút này và thực hiện các thao tác xoay từ dưới lên trên, khôi phục lại sự cân bằng cho tất cả các nút không cân bằng**. Mã này như sau:

=== "Python"
    ```python title="avl_tree.py"
    self._root = self.insert_helper(self._root, val)
    ```
=== "C++"
    ```cpp title="avl_tree.cpp"
    TreeNode *insertHelper(TreeNode *node, int val) {
            if (node == nullptr)
                return new TreeNode(val);
            /* 1. Find insertion position and insert node */
            if (val < node->val)
                node->left = insertHelper(node->left, val);
            else if (val > node->val)
                node->right = insertHelper(node->right, val);
            else
                return node;    // Duplicate node not inserted, return directly
            updateHeight(node); // Update node height
            /* 2. Perform rotation operation to restore balance to this subtree */
            node = rotate(node);
            // Return root node of subtree
            return node;
        }
    ```
=== "Java"
    ```java title="avl_tree.java"
    root = insertHelper(root, val);
        }
    
        /* Recursively insert node (helper method) */
        private TreeNode insertHelper(TreeNode node, int val) {
    ```
=== "C#"
    ```csharp title="avl_tree.cs"
    root = InsertHelper(root, val);
        }
    
        /* Recursively insert node (helper method) */
        TreeNode? InsertHelper(TreeNode? node, int val) {
    ```
=== "Go"
    ```go title="avl_tree.go"
    t.root = t.insertHelper(t.root, val)
    }
    
    /* Recursively insert node (helper function) */
    func (t *aVLTree) insertHelper(node *TreeNode, val int) *TreeNode {
    ```
=== "Swift"
    ```swift title="avl_tree.swift"
    root = insertHelper(node: root, val: val)
        }
    
        /* Recursively insert node (helper method) */
        private func insertHelper(node: TreeNode?, val: Int) -> TreeNode? {
    ```
=== "JS"
    ```javascript title="avl_tree.js"
    this.root = this.#insertHelper(this.root, val);
        }
    
        /* Recursively insert node (helper method) */
        #insertHelper(node, val) {
    ```
=== "TS"
    ```typescript title="avl_tree.ts"
    this.root = this.insertHelper(this.root, val);
        }
    
        /* Recursively insert node (helper method) */
        private insertHelper(node: TreeNode, val: number): TreeNode {
    ```
=== "Dart"
    ```dart title="avl_tree.dart"
    root = insertHelper(root, val);
      }
    
      /* Recursively insert node (helper method) */
      TreeNode? insertHelper(TreeNode? node, int val) {
    ```
=== "Rust"
    ```rust title="avl_tree.rs"
    self.root = Self::insert_helper(self.root.clone(), val);
        }
    
        /* Recursively insert node (helper method) */
        fn insert_helper(node: OptionTreeNodeRc, val: i32) -> OptionTreeNodeRc {
    ```
=== "C"
    ```c title="avl_tree.c"
    TreeNode *insertHelper(TreeNode *node, int val) {
        if (node == NULL) {
            return newTreeNode(val);
        }
        /* 1. Find insertion position and insert node */
        if (val < node->val) {
            node->left = insertHelper(node->left, val);
        } else if (val > node->val) {
            node->right = insertHelper(node->right, val);
        } else {
            // Duplicate node not inserted, return directly
            return node;
        }
        // Update node height
        updateHeight(node);
        /* 2. Perform rotation operation to restore balance to this subtree */
        node = rotate(node);
        // Return root node of subtree
        return node;
    }
    ```
=== "Kotlin"
    ```kotlin title="avl_tree.kt"
    root = insertHelper(root, _val)
        }
    
        /* Recursively insert node (helper method) */
        private fun insertHelper(n: TreeNode?, _val: Int): TreeNode {
    ```
=== "Ruby"
    ```ruby title="avl_tree.rb"
    @root = insert_helper(@root, val)
      end
    
      ### Recursively insert node (helper method) ###
    ```


### Loại bỏ nút

Tương tự, trên cơ sở phương pháp loại bỏ nút của cây tìm kiếm nhị phân, các thao tác xoay cần được thực hiện từ dưới lên trên để khôi phục lại sự cân bằng cho tất cả các nút không cân bằng. Mã này như sau:

=== "Python"
    ```python title="avl_tree.py"
    self._root = self.remove_helper(self._root, val)
    ```
=== "C++"
    ```cpp title="avl_tree.cpp"
    TreeNode *removeHelper(TreeNode *node, int val) {
            if (node == nullptr)
                return nullptr;
            /* 1. Find node and delete */
            if (val < node->val)
                node->left = removeHelper(node->left, val);
            else if (val > node->val)
                node->right = removeHelper(node->right, val);
            else {
                if (node->left == nullptr || node->right == nullptr) {
                    TreeNode *child = node->left != nullptr ? node->left : node->right;
                    // Number of child nodes = 0, delete node directly and return
                    if (child == nullptr) {
                        delete node;
                        return nullptr;
                    }
                    // Number of child nodes = 1, delete node directly
                    else {
                        delete node;
                        node = child;
                    }
                } else {
                    // Number of child nodes = 2, delete the next node in inorder traversal and replace current node with it
                    TreeNode *temp = node->right;
                    while (temp->left != nullptr) {
                        temp = temp->left;
                    }
                    int tempVal = temp->val;
                    node->right = removeHelper(node->right, temp->val);
                    node->val = tempVal;
                }
            }
            updateHeight(node); // Update node height
            /* 2. Perform rotation operation to restore balance to this subtree */
            node = rotate(node);
            // Return root node of subtree
            return node;
        }
    ```
=== "Java"
    ```java title="avl_tree.java"
    root = removeHelper(root, val);
        }
    
        /* Recursively delete node (helper method) */
        private TreeNode removeHelper(TreeNode node, int val) {
    ```
=== "C#"
    ```csharp title="avl_tree.cs"
    root = RemoveHelper(root, val);
        }
    
        /* Recursively delete node (helper method) */
        TreeNode? RemoveHelper(TreeNode? node, int val) {
    ```
=== "Go"
    ```go title="avl_tree.go"
    t.root = t.removeHelper(t.root, val)
    }
    
    /* Recursively remove node (helper function) */
    func (t *aVLTree) removeHelper(node *TreeNode, val int) *TreeNode {
    ```
=== "Swift"
    ```swift title="avl_tree.swift"
    root = removeHelper(node: root, val: val)
        }
    
        /* Recursively delete node (helper method) */
        private func removeHelper(node: TreeNode?, val: Int) -> TreeNode? {
    ```
=== "JS"
    ```javascript title="avl_tree.js"
    this.root = this.#removeHelper(this.root, val);
        }
    
        /* Recursively delete node (helper method) */
        #removeHelper(node, val) {
    ```
=== "TS"
    ```typescript title="avl_tree.ts"
    this.root = this.removeHelper(this.root, val);
        }
    
        /* Recursively delete node (helper method) */
        private removeHelper(node: TreeNode, val: number): TreeNode {
    ```
=== "Dart"
    ```dart title="avl_tree.dart"
    root = removeHelper(root, val);
      }
    
      /* Recursively delete node (helper method) */
      TreeNode? removeHelper(TreeNode? node, int val) {
    ```
=== "Rust"
    ```rust title="avl_tree.rs"
    Self::remove_helper(self.root.clone(), val);
        }
    
        /* Recursively delete node (helper method) */
        fn remove_helper(node: OptionTreeNodeRc, val: i32) -> OptionTreeNodeRc {
    ```
=== "C"
    ```c title="avl_tree.c"
    TreeNode *removeHelper(TreeNode *node, int val) {
        TreeNode *child, *grandChild;
        if (node == NULL) {
            return NULL;
        }
        /* 1. Find node and delete */
        if (val < node->val) {
            node->left = removeHelper(node->left, val);
        } else if (val > node->val) {
            node->right = removeHelper(node->right, val);
        } else {
            if (node->left == NULL || node->right == NULL) {
                child = node->left;
                if (node->right != NULL) {
                    child = node->right;
                }
                // Number of child nodes = 0, delete node directly and return
                if (child == NULL) {
                    return NULL;
                } else {
                    // Number of child nodes = 1, delete node directly
                    node = child;
                }
            } else {
                // Number of child nodes = 2, delete the next node in inorder traversal and replace current node with it
                TreeNode *temp = node->right;
                while (temp->left != NULL) {
                    temp = temp->left;
                }
                int tempVal = temp->val;
                node->right = removeHelper(node->right, temp->val);
                node->val = tempVal;
            }
        }
        // Update node height
        updateHeight(node);
        /* 2. Perform rotation operation to restore balance to this subtree */
        node = rotate(node);
        // Return root node of subtree
        return node;
    }
    ```
=== "Kotlin"
    ```kotlin title="avl_tree.kt"
    root = removeHelper(root, _val)
        }
    
        /* Recursively delete node (helper method) */
        private fun removeHelper(n: TreeNode?, _val: Int): TreeNode? {
    ```
=== "Ruby"
    ```ruby title="avl_tree.rb"
    @root = remove_helper(@root, val)
      end
    
      ### Recursively delete node (helper method) ###
    ```


### Tìm kiếm nút

Hoạt động tìm kiếm nút trong cây AVL nhất quán với hoạt động tìm kiếm trong cây tìm kiếm nhị phân và sẽ không được trình bày chi tiết ở đây.

## Ứng dụng tiêu biểu của cây AVL

- Tổ chức và lưu trữ dữ liệu có quy mô lớn, phù hợp với các tình huống tìm kiếm tần suất cao và chèn, xóa tần suất thấp.
- Dùng để xây dựng hệ thống chỉ mục trong cơ sở dữ liệu.
- Cây đỏ đen cũng là một loại cây tìm kiếm nhị phân cân bằng phổ biến. So với cây AVL, cây đỏ đen có điều kiện cân bằng thoải mái hơn, yêu cầu ít thao tác xoay hơn để chèn và xóa nút và có hiệu suất trung bình cao hơn cho các thao tác thêm và xóa nút.
