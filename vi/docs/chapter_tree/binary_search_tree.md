# Cây tìm kiếm nhị phân

Như minh họa trong hình bên dưới, <u>cây tìm kiếm nhị phân</u> thỏa mãn các điều kiện sau.

1. Đối với nút gốc, giá trị của tất cả các nút trong cây con bên trái $<$ giá trị của nút gốc $<$ giá trị của tất cả các nút trong cây con bên phải.
2. Cây con bên trái và bên phải của bất kỳ nút nào cũng là cây tìm kiếm nhị phân, tức là chúng cũng thỏa mãn điều kiện `1.`.

![Binary search tree](binary_search_tree.assets/binary_search_tree.png)

## Các thao tác trên cây tìm kiếm nhị phân

Chúng tôi đóng gói cây tìm kiếm nhị phân dưới dạng lớp `BinarySearchTree` và khai báo một biến thành viên `root` trỏ đến nút gốc của cây.

### Tìm kiếm nút

Cho trước giá trị nút đích `num`, chúng ta có thể tìm kiếm theo các thuộc tính của cây tìm kiếm nhị phân. Như được hiển thị trong hình bên dưới, chúng ta khai báo một nút `cur` và bắt đầu từ nút `root` của cây tìm kiếm nhị phân, lặp để so sánh `cur.val` với `num`.

- Nếu `cur.val < num`, nghĩa là nút đích nằm trong cây con bên phải của `cur`, do đó thực thi `cur = cur.right`.
- Nếu `cur.val > num`, nghĩa là nút đích nằm trong cây con bên trái của `cur`, do đó thực thi `cur = cur.left`.
- Nếu `cur.val = num` nghĩa là đã tìm thấy nút đích, thoát khỏi vòng lặp và trả về nút.

=== "<1>"
    ![Example of searching for a node in a binary search tree](binary_search_tree.assets/bst_search_step1.png)

=== "<2>"
    ![bst_search_step2](binary_search_tree.assets/bst_search_step2.png)

=== "<3>"
    ![bst_search_step3](binary_search_tree.assets/bst_search_step3.png)

=== "<4>"
    ![bst_search_step4](binary_search_tree.assets/bst_search_step4.png)

Hoạt động tìm kiếm trong cây tìm kiếm nhị phân tuân theo nguyên tắc tương tự như tìm kiếm nhị phân: mỗi vòng loại trừ một nửa số trường hợp còn lại. Số lần lặp vòng lặp tối đa bằng chiều cao của cây. Khi cây được cân bằng, việc tìm kiếm mất $O(\log n)$ thời gian. Mã ví dụ như sau:

=== "Python"
    ```python title="binary_search_tree.py"
    class BinarySearchTree:
        """Binary search tree"""
    
        def __init__(self):
            """Constructor"""
            # Initialize empty tree
            self._root = None
    
        def get_root(self) -> TreeNode | None:
            """Get binary tree root node"""
            return self._root
    
        def search(self, num: int) -> TreeNode | None:
            """Search node"""
            cur = self._root
            # Loop search, exit after passing leaf node
            while cur is not None:
                # Target node is in cur's right subtree
                if cur.val < num:
                    cur = cur.right
                # Target node is in cur's left subtree
                elif cur.val > num:
                    cur = cur.left
                # Found target node, exit loop
                else:
                    break
            return cur
    
        def insert(self, num: int):
            """Insert node"""
            # If tree is empty, initialize root node
            if self._root is None:
                self._root = TreeNode(num)
                return
            # Loop search, exit after passing leaf node
            cur, pre = self._root, None
            while cur is not None:
                # Found duplicate node, return directly
                if cur.val == num:
                    return
                pre = cur
                # Insertion position is in cur's right subtree
                if cur.val < num:
                    cur = cur.right
                # Insertion position is in cur's left subtree
                else:
                    cur = cur.left
            # Insert node
            node = TreeNode(num)
            if pre.val < num:
                pre.right = node
            else:
                pre.left = node
    
        def remove(self, num: int):
            """Delete node"""
            # If tree is empty, return directly
            if self._root is None:
                return
            # Loop search, exit after passing leaf node
            cur, pre = self._root, None
            while cur is not None:
                # Found node to delete, exit loop
                if cur.val == num:
                    break
                pre = cur
                # Node to delete is in cur's right subtree
                if cur.val < num:
                    cur = cur.right
                # Node to delete is in cur's left subtree
                else:
                    cur = cur.left
            # If no node to delete, return directly
            if cur is None:
                return
    
            # Number of child nodes = 0 or 1
            if cur.left is None or cur.right is None:
                # When number of child nodes = 0 / 1, child = null / that child node
                child = cur.left or cur.right
                # Delete node cur
                if cur != self._root:
                    if pre.left == cur:
                        pre.left = child
                    else:
                        pre.right = child
                else:
                    # If deleted node is root node, reassign root node
                    self._root = child
            # Number of child nodes = 2
            else:
                # Get next node of cur in inorder traversal
                tmp: TreeNode = cur.right
                while tmp.left is not None:
                    tmp = tmp.left
                # Recursively delete node tmp
                self.remove(tmp.val)
                # Replace cur with tmp
                cur.val = tmp.val
    ```
=== "C++"
    ```cpp title="binary_search_tree.cpp"
    class BinarySearchTree {
      private:
        TreeNode *root;
    
      public:
        /* Constructor */
        BinarySearchTree() {
            // Initialize empty tree
            root = nullptr;
        }
    
        /* Destructor */
        ~BinarySearchTree() {
            freeMemoryTree(root);
        }
    
        /* Get binary tree root node */
        TreeNode *getRoot() {
            return root;
        }
    
        /* Search node */
        TreeNode *search(int num) {
            TreeNode *cur = root;
            // Loop search, exit after passing leaf node
            while (cur != nullptr) {
                // Target node is in cur's right subtree
                if (cur->val < num)
                    cur = cur->right;
                // Target node is in cur's left subtree
                else if (cur->val > num)
                    cur = cur->left;
                // Found target node, exit loop
                else
                    break;
            }
            // Return target node
            return cur;
        }
    
        /* Insert node */
        void insert(int num) {
            // If tree is empty, initialize root node
            if (root == nullptr) {
                root = new TreeNode(num);
                return;
            }
            TreeNode *cur = root, *pre = nullptr;
            // Loop search, exit after passing leaf node
            while (cur != nullptr) {
                // Found duplicate node, return directly
                if (cur->val == num)
                    return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur->val < num)
                    cur = cur->right;
                // Insertion position is in cur's left subtree
                else
                    cur = cur->left;
            }
            // Insert node
            TreeNode *node = new TreeNode(num);
            if (pre->val < num)
                pre->right = node;
            else
                pre->left = node;
        }
    
        /* Remove node */
        void remove(int num) {
            // If tree is empty, return directly
            if (root == nullptr)
                return;
            TreeNode *cur = root, *pre = nullptr;
            // Loop search, exit after passing leaf node
            while (cur != nullptr) {
                // Found node to delete, exit loop
                if (cur->val == num)
                    break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur->val < num)
                    cur = cur->right;
                // Node to delete is in cur's left subtree
                else
                    cur = cur->left;
            }
            // If no node to delete, return directly
            if (cur == nullptr)
                return;
            // Number of child nodes = 0 or 1
            if (cur->left == nullptr || cur->right == nullptr) {
                // When number of child nodes = 0 / 1, child = nullptr / that child node
                TreeNode *child = cur->left != nullptr ? cur->left : cur->right;
                // Delete node cur
                if (cur != root) {
                    if (pre->left == cur)
                        pre->left = child;
                    else
                        pre->right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    root = child;
                }
                // Free memory
                delete cur;
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                TreeNode *tmp = cur->right;
                while (tmp->left != nullptr) {
                    tmp = tmp->left;
                }
                int tmpVal = tmp->val;
                // Recursively delete node tmp
                remove(tmp->val);
                // Replace cur with tmp
                cur->val = tmpVal;
            }
        }
    };
    ```
=== "Java"
    ```java title="binary_search_tree.java"
    class BinarySearchTree {
        private TreeNode root;
    
        /* Constructor */
        public BinarySearchTree() {
            // Initialize empty tree
            root = null;
        }
    
        /* Get binary tree root node */
        public TreeNode getRoot() {
            return root;
        }
    
        /* Search node */
        public TreeNode search(int num) {
            TreeNode cur = root;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Target node is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Target node is in cur's left subtree
                else if (cur.val > num)
                    cur = cur.left;
                // Found target node, exit loop
                else
                    break;
            }
            // Return target node
            return cur;
        }
    
        /* Insert node */
        public void insert(int num) {
            // If tree is empty, initialize root node
            if (root == null) {
                root = new TreeNode(num);
                return;
            }
            TreeNode cur = root, pre = null;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found duplicate node, return directly
                if (cur.val == num)
                    return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Insertion position is in cur's left subtree
                else
                    cur = cur.left;
            }
            // Insert node
            TreeNode node = new TreeNode(num);
            if (pre.val < num)
                pre.right = node;
            else
                pre.left = node;
        }
    
        /* Remove node */
        public void remove(int num) {
            // If tree is empty, return directly
            if (root == null)
                return;
            TreeNode cur = root, pre = null;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found node to delete, exit loop
                if (cur.val == num)
                    break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Node to delete is in cur's left subtree
                else
                    cur = cur.left;
            }
            // If no node to delete, return directly
            if (cur == null)
                return;
            // Number of child nodes = 0 or 1
            if (cur.left == null || cur.right == null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                TreeNode child = cur.left != null ? cur.left : cur.right;
                // Delete node cur
                if (cur != root) {
                    if (pre.left == cur)
                        pre.left = child;
                    else
                        pre.right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    root = child;
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                TreeNode tmp = cur.right;
                while (tmp.left != null) {
                    tmp = tmp.left;
                }
                // Recursively delete node tmp
                remove(tmp.val);
                // Replace cur with tmp
                cur.val = tmp.val;
            }
        }
    }
    ```
=== "C#"
    ```csharp title="binary_search_tree.cs"
    class BinarySearchTree {
        TreeNode? root;
    
        public BinarySearchTree() {
            // Initialize empty tree
            root = null;
        }
    
        /* Get binary tree root node */
        public TreeNode? GetRoot() {
            return root;
        }
    
        /* Search node */
        public TreeNode? Search(int num) {
            TreeNode? cur = root;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Target node is in cur's right subtree
                if (cur.val < num) cur =
                    cur.right;
                // Target node is in cur's left subtree
                else if (cur.val > num)
                    cur = cur.left;
                // Found target node, exit loop
                else
                    break;
            }
            // Return target node
            return cur;
        }
    
        /* Insert node */
        public void Insert(int num) {
            // If tree is empty, initialize root node
            if (root == null) {
                root = new TreeNode(num);
                return;
            }
            TreeNode? cur = root, pre = null;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found duplicate node, return directly
                if (cur.val == num)
                    return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Insertion position is in cur's left subtree
                else
                    cur = cur.left;
            }
    
            // Insert node
            TreeNode node = new(num);
            if (pre != null) {
                if (pre.val < num)
                    pre.right = node;
                else
                    pre.left = node;
            }
        }
    
    
        /* Remove node */
        public void Remove(int num) {
            // If tree is empty, return directly
            if (root == null)
                return;
            TreeNode? cur = root, pre = null;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found node to delete, exit loop
                if (cur.val == num)
                    break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Node to delete is in cur's left subtree
                else
                    cur = cur.left;
            }
            // If no node to delete, return directly
            if (cur == null)
                return;
            // Number of child nodes = 0 or 1
            if (cur.left == null || cur.right == null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                TreeNode? child = cur.left ?? cur.right;
                // Delete node cur
                if (cur != root) {
                    if (pre!.left == cur)
                        pre.left = child;
                    else
                        pre.right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    root = child;
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                TreeNode? tmp = cur.right;
                while (tmp.left != null) {
                    tmp = tmp.left;
                }
                // Recursively delete node tmp
                Remove(tmp.val!.Value);
                // Replace cur with tmp
                cur.val = tmp.val;
            }
        }
    }
    ```
=== "Go"
    ```go title="binary_search_tree.go"
    type binarySearchTree struct {
    	root *TreeNode
    }
    ```
=== "Swift"
    ```swift title="binary_search_tree.swift"
    class BinarySearchTree {
        private var root: TreeNode?
    
        /* Constructor */
        init() {
            // Initialize empty tree
            root = nil
        }
    
        /* Get binary tree root node */
        func getRoot() -> TreeNode? {
            root
        }
    
        /* Search node */
        func search(num: Int) -> TreeNode? {
            var cur = root
            // Loop search, exit after passing leaf node
            while cur != nil {
                // Target node is in cur's right subtree
                if cur!.val < num {
                    cur = cur?.right
                }
                // Target node is in cur's left subtree
                else if cur!.val > num {
                    cur = cur?.left
                }
                // Found target node, exit loop
                else {
                    break
                }
            }
            // Return target node
            return cur
        }
    
        /* Insert node */
        func insert(num: Int) {
            // If tree is empty, initialize root node
            if root == nil {
                root = TreeNode(x: num)
                return
            }
            var cur = root
            var pre: TreeNode?
            // Loop search, exit after passing leaf node
            while cur != nil {
                // Found duplicate node, return directly
                if cur!.val == num {
                    return
                }
                pre = cur
                // Insertion position is in cur's right subtree
                if cur!.val < num {
                    cur = cur?.right
                }
                // Insertion position is in cur's left subtree
                else {
                    cur = cur?.left
                }
            }
            // Insert node
            let node = TreeNode(x: num)
            if pre!.val < num {
                pre?.right = node
            } else {
                pre?.left = node
            }
        }
    
        /* Remove node */
        func remove(num: Int) {
            // If tree is empty, return directly
            if root == nil {
                return
            }
            var cur = root
            var pre: TreeNode?
            // Loop search, exit after passing leaf node
            while cur != nil {
                // Found node to delete, exit loop
                if cur!.val == num {
                    break
                }
                pre = cur
                // Node to delete is in cur's right subtree
                if cur!.val < num {
                    cur = cur?.right
                }
                // Node to delete is in cur's left subtree
                else {
                    cur = cur?.left
                }
            }
            // If no node to delete, return directly
            if cur == nil {
                return
            }
            // Number of child nodes = 0 or 1
            if cur?.left == nil || cur?.right == nil {
                // When number of child nodes = 0 / 1, child = null / that child node
                let child = cur?.left ?? cur?.right
                // Delete node cur
                if cur !== root {
                    if pre?.left === cur {
                        pre?.left = child
                    } else {
                        pre?.right = child
                    }
                } else {
                    // If deleted node is root node, reassign root node
                    root = child
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                var tmp = cur?.right
                while tmp?.left != nil {
                    tmp = tmp?.left
                }
                // Recursively delete node tmp
                remove(num: tmp!.val)
                // Replace cur with tmp
                cur?.val = tmp!.val
            }
        }
    }
    ```
=== "JS"
    ```javascript title="binary_search_tree.js"
    class BinarySearchTree {
        /* Constructor */
        constructor() {
            // Initialize empty tree
            this.root = null;
        }
    
        /* Get binary tree root node */
        getRoot() {
            return this.root;
        }
    
        /* Search node */
        search(num) {
            let cur = this.root;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Target node is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Target node is in cur's left subtree
                else if (cur.val > num) cur = cur.left;
                // Found target node, exit loop
                else break;
            }
            // Return target node
            return cur;
        }
    
        /* Insert node */
        insert(num) {
            // If tree is empty, initialize root node
            if (this.root === null) {
                this.root = new TreeNode(num);
                return;
            }
            let cur = this.root,
                pre = null;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Found duplicate node, return directly
                if (cur.val === num) return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Insertion position is in cur's left subtree
                else cur = cur.left;
            }
            // Insert node
            const node = new TreeNode(num);
            if (pre.val < num) pre.right = node;
            else pre.left = node;
        }
    
        /* Remove node */
        remove(num) {
            // If tree is empty, return directly
            if (this.root === null) return;
            let cur = this.root,
                pre = null;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Found node to delete, exit loop
                if (cur.val === num) break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Node to delete is in cur's left subtree
                else cur = cur.left;
            }
            // If no node to delete, return directly
            if (cur === null) return;
            // Number of child nodes = 0 or 1
            if (cur.left === null || cur.right === null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                const child = cur.left !== null ? cur.left : cur.right;
                // Delete node cur
                if (cur !== this.root) {
                    if (pre.left === cur) pre.left = child;
                    else pre.right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    this.root = child;
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                let tmp = cur.right;
                while (tmp.left !== null) {
                    tmp = tmp.left;
                }
                // Recursively delete node tmp
                this.remove(tmp.val);
                // Replace cur with tmp
                cur.val = tmp.val;
            }
        }
    }
    ```
=== "TS"
    ```typescript title="binary_search_tree.ts"
    class BinarySearchTree {
        private root: TreeNode | null;
    
        /* Constructor */
        constructor() {
            // Initialize empty tree
            this.root = null;
        }
    
        /* Get binary tree root node */
        getRoot(): TreeNode | null {
            return this.root;
        }
    
        /* Search node */
        search(num: number): TreeNode | null {
            let cur = this.root;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Target node is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Target node is in cur's left subtree
                else if (cur.val > num) cur = cur.left;
                // Found target node, exit loop
                else break;
            }
            // Return target node
            return cur;
        }
    
        /* Insert node */
        insert(num: number): void {
            // If tree is empty, initialize root node
            if (this.root === null) {
                this.root = new TreeNode(num);
                return;
            }
            let cur: TreeNode | null = this.root,
                pre: TreeNode | null = null;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Found duplicate node, return directly
                if (cur.val === num) return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Insertion position is in cur's left subtree
                else cur = cur.left;
            }
            // Insert node
            const node = new TreeNode(num);
            if (pre!.val < num) pre!.right = node;
            else pre!.left = node;
        }
    
        /* Remove node */
        remove(num: number): void {
            // If tree is empty, return directly
            if (this.root === null) return;
            let cur: TreeNode | null = this.root,
                pre: TreeNode | null = null;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Found node to delete, exit loop
                if (cur.val === num) break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Node to delete is in cur's left subtree
                else cur = cur.left;
            }
            // If no node to delete, return directly
            if (cur === null) return;
            // Number of child nodes = 0 or 1
            if (cur.left === null || cur.right === null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                const child: TreeNode | null =
                    cur.left !== null ? cur.left : cur.right;
                // Delete node cur
                if (cur !== this.root) {
                    if (pre!.left === cur) pre!.left = child;
                    else pre!.right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    this.root = child;
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                let tmp: TreeNode | null = cur.right;
                while (tmp!.left !== null) {
                    tmp = tmp!.left;
                }
                // Recursively delete node tmp
                this.remove(tmp!.val);
                // Replace cur with tmp
                cur.val = tmp!.val;
            }
        }
    }
    ```
=== "Dart"
    ```dart title="binary_search_tree.dart"
    class BinarySearchTree {
      late TreeNode? _root;
    
      /* Constructor */
      BinarySearchTree() {
        // Initialize empty tree
        _root = null;
      }
    
      /* Get root node of binary tree */
      TreeNode? getRoot() {
        return _root;
      }
    
      /* Search node */
      TreeNode? search(int _num) {
        TreeNode? cur = _root;
        // Loop search, exit after passing leaf node
        while (cur != null) {
          // Target node is in cur's right subtree
          if (cur.val < _num)
            cur = cur.right;
          // Target node is in cur's left subtree
          else if (cur.val > _num)
            cur = cur.left;
          // Found target node, exit loop
          else
            break;
        }
        // Return target node
        return cur;
      }
    
      /* Insert node */
      void insert(int _num) {
        // If tree is empty, initialize root node
        if (_root == null) {
          _root = TreeNode(_num);
          return;
        }
        TreeNode? cur = _root;
        TreeNode? pre = null;
        // Loop search, exit after passing leaf node
        while (cur != null) {
          // Found duplicate node, return directly
          if (cur.val == _num) return;
          pre = cur;
          // Insertion position is in cur's right subtree
          if (cur.val < _num)
            cur = cur.right;
          // Insertion position is in cur's left subtree
          else
            cur = cur.left;
        }
        // Insert node
        TreeNode? node = TreeNode(_num);
        if (pre!.val < _num)
          pre.right = node;
        else
          pre.left = node;
      }
    
      /* Remove node */
      void remove(int _num) {
        // If tree is empty, return directly
        if (_root == null) return;
        TreeNode? cur = _root;
        TreeNode? pre = null;
        // Loop search, exit after passing leaf node
        while (cur != null) {
          // Found node to delete, exit loop
          if (cur.val == _num) break;
          pre = cur;
          // Node to delete is in cur's right subtree
          if (cur.val < _num)
            cur = cur.right;
          // Node to delete is in cur's left subtree
          else
            cur = cur.left;
        }
        // If no node to delete, return directly
        if (cur == null) return;
        // Number of child nodes = 0 or 1
        if (cur.left == null || cur.right == null) {
          // When number of child nodes = 0 / 1, child = null / that child node
          TreeNode? child = cur.left ?? cur.right;
          // Delete node cur
          if (cur != _root) {
            if (pre!.left == cur)
              pre.left = child;
            else
              pre.right = child;
          } else {
            // If deleted node is root node, reassign root node
            _root = child;
          }
        } else {
          // Number of child nodes = 2
          // Get next node of cur in inorder traversal
          TreeNode? tmp = cur.right;
          while (tmp!.left != null) {
            tmp = tmp.left;
          }
          // Recursively delete node tmp
          remove(tmp.val);
          // Replace cur with tmp
          cur.val = tmp.val;
        }
      }
    }
    ```
=== "Rust"
    ```rust title="binary_search_tree.rs"
    pub struct BinarySearchTree {
        root: OptionTreeNodeRc,
    }
    ```
=== "C"
    ```c title="binary_search_tree.c"
    void delBinarySearchTree(BinarySearchTree *bst) {
        freeMemoryTree(bst->root);
        free(bst);
    }
    ```
=== "Kotlin"
    ```kotlin title="binary_search_tree.kt"
    class BinarySearchTree {
        // Initialize empty tree
        private var root: TreeNode? = null
    
        /* Get binary tree root node */
        fun getRoot(): TreeNode? {
            return root
        }
    
        /* Search node */
        fun search(num: Int): TreeNode? {
            var cur = root
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Target node is in cur's right subtree
                cur = if (cur._val < num)
                    cur.right
                // Target node is in cur's left subtree
                else if (cur._val > num)
                    cur.left
                // Found target node, exit loop
                else
                    break
            }
            // Return target node
            return cur
        }
    
        /* Insert node */
        fun insert(num: Int) {
            // If tree is empty, initialize root node
            if (root == null) {
                root = TreeNode(num)
                return
            }
            var cur = root
            var pre: TreeNode? = null
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found duplicate node, return directly
                if (cur._val == num)
                    return
                pre = cur
                // Insertion position is in cur's right subtree
                cur = if (cur._val < num)
                    cur.right
                // Insertion position is in cur's left subtree
                else
                    cur.left
            }
            // Insert node
            val node = TreeNode(num)
            if (pre?._val!! < num)
                pre.right = node
            else
                pre.left = node
        }
    
        /* Remove node */
        fun remove(num: Int) {
            // If tree is empty, return directly
            if (root == null)
                return
            var cur = root
            var pre: TreeNode? = null
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found node to delete, exit loop
                if (cur._val == num)
                    break
                pre = cur
                // Node to delete is in cur's right subtree
                cur = if (cur._val < num)
                    cur.right
                // Node to delete is in cur's left subtree
                else
                    cur.left
            }
            // If no node to delete, return directly
            if (cur == null)
                return
            // Number of child nodes = 0 or 1
            if (cur.left == null || cur.right == null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                val child = if (cur.left != null)
                    cur.left
                else
                    cur.right
                // Delete node cur
                if (cur != root) {
                    if (pre!!.left == cur)
                        pre.left = child
                    else
                        pre.right = child
                } else {
                    // If deleted node is root node, reassign root node
                    root = child
                }
                // Number of child nodes = 2
            } else {
                // Get next node of cur in inorder traversal
                var tmp = cur.right
                while (tmp!!.left != null) {
                    tmp = tmp.left
                }
                // Recursively delete node tmp
                remove(tmp._val)
                // Replace cur with tmp
                cur._val = tmp._val
            }
        }
    }
    ```
=== "Ruby"
    ```ruby title="binary_search_tree.rb"
    ### Binary search tree ###
    class BinarySearchTree
      ### Constructor ###
      def initialize
        # Initialize empty tree
        @root = nil
      end
    
      ### Get binary tree root node ###
      def get_root
        @root
      end
    
      ### Search node ###
      def search(num)
        cur = @root
    
        # Loop search, exit after passing leaf node
        while !cur.nil?
          # Target node is in cur's right subtree
          if cur.val < num
            cur = cur.right
          # Target node is in cur's left subtree
          elsif cur.val > num
            cur = cur.left
          # Found target node, exit loop
          else
            break
          end
        end
    
        cur
      end
    
      ### Insert node ###
      def insert(num)
        # If tree is empty, initialize root node
        if @root.nil?
          @root = TreeNode.new(num)
          return
        end
    
        # Loop search, exit after passing leaf node
        cur, pre = @root, nil
        while !cur.nil?
          # Found duplicate node, return directly
          return if cur.val == num
    
          pre = cur
          # Insertion position is in cur's right subtree
          if cur.val < num
            cur = cur.right
          # Insertion position is in cur's left subtree
          else
            cur = cur.left
          end
        end
    
        # Insert node
        node = TreeNode.new(num)
        if pre.val < num
          pre.right = node
        else
          pre.left = node
        end
      end
    
      ### Delete node ###
      def remove(num)
        # If tree is empty, return directly
        return if @root.nil?
    
        # Loop search, exit after passing leaf node
        cur, pre = @root, nil
        while !cur.nil?
          # Found node to delete, exit loop
          break if cur.val == num
    
          pre = cur
          # Node to delete is in cur's right subtree
          if cur.val < num
            cur = cur.right
          # Node to delete is in cur's left subtree
          else
            cur = cur.left
          end
        end
        # If no node to delete, return directly
        return if cur.nil?
    
        # Number of child nodes = 0 or 1
        if cur.left.nil? || cur.right.nil?
          # When number of child nodes = 0 / 1, child = null / that child node
          child = cur.left || cur.right
          # Delete node cur
          if cur != @root
            if pre.left == cur
              pre.left = child
            else
              pre.right = child
            end
          else
            # If deleted node is root node, reassign root node
            @root = child
          end
        # Number of child nodes = 2
        else
          # Get next node of cur in inorder traversal
          tmp = cur.right
          while !tmp.left.nil?
            tmp = tmp.left
          end
          # Recursively delete node tmp
          remove(tmp.val)
          # Replace cur with tmp
          cur.val = tmp.val
        end
      end
    ```


### Chèn một nút

Cho một phần tử `num` được chèn vào, để duy trì thuộc tính của cây tìm kiếm nhị phân "cây con trái < nút gốc < cây con phải", quá trình chèn như thể hiện trong hình bên dưới.

1. **Tìm vị trí chèn**: Tương tự như thao tác tìm kiếm, bắt đầu từ nút gốc và lặp tìm kiếm xuống theo mối quan hệ kích thước giữa giá trị nút hiện tại và `num`, cho đến khi đi qua nút lá (duyệt tới `None`) rồi thoát khỏi vòng lặp.
2. **Chèn nút vào vị trí đó**: Tạo một nút cho `num` và đặt nó ở vị trí `None`.

![Inserting a node into a binary search tree](binary_search_tree.assets/bst_insert.png)

Trong quá trình triển khai mã, hãy lưu ý hai điểm sau:

- Cây tìm kiếm nhị phân không cho phép trùng lặp nút; nếu không thì cây sẽ không còn thỏa mãn định nghĩa của nó nữa. Do đó, nếu nút được chèn đã tồn tại trong cây thì thao tác chèn sẽ bị bỏ qua và hàm sẽ trả về trực tiếp.
- Để thực hiện việc chèn nút, chúng ta cần sử dụng nút `pre` để lưu nút khỏi vòng lặp trước đó. Bằng cách này, khi duyệt tới `None`, chúng ta có thể lấy được nút cha của nó, từ đó hoàn thành thao tác chèn nút.

=== "Python"
    ```python title="binary_search_tree.py"
    def insert(self, num: int):
            """Insert node"""
            # If tree is empty, initialize root node
            if self._root is None:
                self._root = TreeNode(num)
                return
            # Loop search, exit after passing leaf node
            cur, pre = self._root, None
            while cur is not None:
                # Found duplicate node, return directly
                if cur.val == num:
                    return
                pre = cur
                # Insertion position is in cur's right subtree
                if cur.val < num:
                    cur = cur.right
                # Insertion position is in cur's left subtree
                else:
                    cur = cur.left
            # Insert node
            node = TreeNode(num)
            if pre.val < num:
                pre.right = node
            else:
                pre.left = node
    ```
=== "C++"
    ```cpp title="binary_search_tree.cpp"
    void insert(int num) {
            // If tree is empty, initialize root node
            if (root == nullptr) {
                root = new TreeNode(num);
                return;
            }
            TreeNode *cur = root, *pre = nullptr;
            // Loop search, exit after passing leaf node
            while (cur != nullptr) {
                // Found duplicate node, return directly
                if (cur->val == num)
                    return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur->val < num)
                    cur = cur->right;
                // Insertion position is in cur's left subtree
                else
                    cur = cur->left;
            }
            // Insert node
            TreeNode *node = new TreeNode(num);
            if (pre->val < num)
                pre->right = node;
            else
                pre->left = node;
        }
    ```
=== "Java"
    ```java title="binary_search_tree.java"
    public void insert(int num) {
            // If tree is empty, initialize root node
            if (root == null) {
                root = new TreeNode(num);
                return;
            }
            TreeNode cur = root, pre = null;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found duplicate node, return directly
                if (cur.val == num)
                    return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Insertion position is in cur's left subtree
                else
                    cur = cur.left;
            }
            // Insert node
            TreeNode node = new TreeNode(num);
            if (pre.val < num)
                pre.right = node;
            else
                pre.left = node;
        }
    ```
=== "C#"
    ```csharp title="binary_search_tree.cs"
    public void Insert(int num) {
            // If tree is empty, initialize root node
            if (root == null) {
                root = new TreeNode(num);
                return;
            }
            TreeNode? cur = root, pre = null;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found duplicate node, return directly
                if (cur.val == num)
                    return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Insertion position is in cur's left subtree
                else
                    cur = cur.left;
            }
    
            // Insert node
            TreeNode node = new(num);
            if (pre != null) {
                if (pre.val < num)
                    pre.right = node;
                else
                    pre.left = node;
            }
        }
    ```
=== "Go"
    ```go title="binary_search_tree.go"
    func (bst *binarySearchTree) insert(num int) {
    	cur := bst.root
    	// If tree is empty, initialize root node
    	if cur == nil {
    		bst.root = NewTreeNode(num)
    		return
    	}
    	// Node position before the node to be inserted
    	var pre *TreeNode = nil
    	// Loop search, exit after passing leaf node
    	for cur != nil {
    		if cur.Val == num {
    			return
    		}
    		pre = cur
    		if cur.Val.(int) < num {
    			cur = cur.Right
    		} else {
    			cur = cur.Left
    		}
    	}
    	// Insert node
    	node := NewTreeNode(num)
    	if pre.Val.(int) < num {
    		pre.Right = node
    	} else {
    		pre.Left = node
    	}
    }
    ```
=== "Swift"
    ```swift title="binary_search_tree.swift"
    func insert(num: Int) {
            // If tree is empty, initialize root node
            if root == nil {
                root = TreeNode(x: num)
                return
            }
            var cur = root
            var pre: TreeNode?
            // Loop search, exit after passing leaf node
            while cur != nil {
                // Found duplicate node, return directly
                if cur!.val == num {
                    return
                }
                pre = cur
                // Insertion position is in cur's right subtree
                if cur!.val < num {
                    cur = cur?.right
                }
                // Insertion position is in cur's left subtree
                else {
                    cur = cur?.left
                }
            }
            // Insert node
            let node = TreeNode(x: num)
            if pre!.val < num {
                pre?.right = node
            } else {
                pre?.left = node
            }
        }
    ```
=== "JS"
    ```javascript title="binary_search_tree.js"
    insert(num) {
            // If tree is empty, initialize root node
            if (this.root === null) {
                this.root = new TreeNode(num);
                return;
            }
            let cur = this.root,
                pre = null;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Found duplicate node, return directly
                if (cur.val === num) return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Insertion position is in cur's left subtree
                else cur = cur.left;
            }
            // Insert node
            const node = new TreeNode(num);
            if (pre.val < num) pre.right = node;
            else pre.left = node;
        }
    ```
=== "TS"
    ```typescript title="binary_search_tree.ts"
    insert(num: number): void {
            // If tree is empty, initialize root node
            if (this.root === null) {
                this.root = new TreeNode(num);
                return;
            }
            let cur: TreeNode | null = this.root,
                pre: TreeNode | null = null;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Found duplicate node, return directly
                if (cur.val === num) return;
                pre = cur;
                // Insertion position is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Insertion position is in cur's left subtree
                else cur = cur.left;
            }
            // Insert node
            const node = new TreeNode(num);
            if (pre!.val < num) pre!.right = node;
            else pre!.left = node;
        }
    ```
=== "Dart"
    ```dart title="binary_search_tree.dart"
    void insert(int _num) {
        // If tree is empty, initialize root node
        if (_root == null) {
          _root = TreeNode(_num);
          return;
        }
        TreeNode? cur = _root;
        TreeNode? pre = null;
        // Loop search, exit after passing leaf node
        while (cur != null) {
          // Found duplicate node, return directly
          if (cur.val == _num) return;
          pre = cur;
          // Insertion position is in cur's right subtree
          if (cur.val < _num)
            cur = cur.right;
          // Insertion position is in cur's left subtree
          else
            cur = cur.left;
        }
        // Insert node
        TreeNode? node = TreeNode(_num);
        if (pre!.val < _num)
          pre.right = node;
        else
          pre.left = node;
      }
    ```
=== "Rust"
    ```rust title="binary_search_tree.rs"
    pub fn insert(&mut self, num: i32) {
            // If tree is empty, initialize root node
            if self.root.is_none() {
                self.root = Some(TreeNode::new(num));
                return;
            }
            let mut cur = self.root.clone();
            let mut pre = None;
            // Loop search, exit after passing leaf node
            while let Some(node) = cur.clone() {
                match num.cmp(&node.borrow().val) {
                    // Found duplicate node, return directly
                    Ordering::Equal => return,
                    // Insertion position is in cur's right subtree
                    Ordering::Greater => {
                        pre = cur.clone();
                        cur = node.borrow().right.clone();
                    }
                    // Insertion position is in cur's left subtree
                    Ordering::Less => {
                        pre = cur.clone();
                        cur = node.borrow().left.clone();
                    }
                }
            }
            // Insert node
            let pre = pre.unwrap();
            let node = Some(TreeNode::new(num));
            if num > pre.borrow().val {
                pre.borrow_mut().right = node;
            } else {
                pre.borrow_mut().left = node;
            }
        }
    ```
=== "C"
    ```c title="binary_search_tree.c"
    void insert(BinarySearchTree *bst, int num) {
        // If tree is empty, initialize root node
        if (bst->root == NULL) {
            bst->root = newTreeNode(num);
            return;
        }
        TreeNode *cur = bst->root, *pre = NULL;
        // Loop search, exit after passing leaf node
        while (cur != NULL) {
            // Found duplicate node, return directly
            if (cur->val == num) {
                return;
            }
            pre = cur;
            if (cur->val < num) {
                // Insertion position is in cur's right subtree
                cur = cur->right;
            } else {
                // Insertion position is in cur's left subtree
                cur = cur->left;
            }
        }
        // Insert node
        TreeNode *node = newTreeNode(num);
        if (pre->val < num) {
            pre->right = node;
        } else {
            pre->left = node;
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="binary_search_tree.kt"
    fun insert(num: Int) {
            // If tree is empty, initialize root node
            if (root == null) {
                root = TreeNode(num)
                return
            }
            var cur = root
            var pre: TreeNode? = null
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found duplicate node, return directly
                if (cur._val == num)
                    return
                pre = cur
                // Insertion position is in cur's right subtree
                cur = if (cur._val < num)
                    cur.right
                // Insertion position is in cur's left subtree
                else
                    cur.left
            }
            // Insert node
            val node = TreeNode(num)
            if (pre?._val!! < num)
                pre.right = node
            else
                pre.left = node
        }
    ```
=== "Ruby"
    ```ruby title="binary_search_tree.rb"
    ### Insert node ###
      def insert(num)
        # If tree is empty, initialize root node
        if @root.nil?
          @root = TreeNode.new(num)
          return
        end
    
        # Loop search, exit after passing leaf node
        cur, pre = @root, nil
        while !cur.nil?
          # Found duplicate node, return directly
          return if cur.val == num
    
          pre = cur
          # Insertion position is in cur's right subtree
          if cur.val < num
            cur = cur.right
          # Insertion position is in cur's left subtree
          else
            cur = cur.left
          end
        end
    
        # Insert node
        node = TreeNode.new(num)
        if pre.val < num
          pre.right = node
        else
          pre.left = node
        end
    ```


Tương tự như tìm kiếm một nút, việc chèn một nút sử dụng thời gian $O(\log n)$.

### Xóa nút

Đầu tiên, tìm nút đích trong cây tìm kiếm nhị phân, sau đó loại bỏ nó. Tương tự như chèn nút, chúng ta cần đảm bảo rằng sau khi hoàn thành thao tác loại bỏ, thuộc tính của cây tìm kiếm nhị phân là "cây con trái $<$ nút gốc $<$ cây con phải" vẫn được duy trì. Do đó, tùy thuộc vào số lượng nút con mà nút mục tiêu có, chúng tôi xem xét ba trường hợp: độ $0$, độ $1$ và độ $2$ và thực hiện thao tác loại bỏ tương ứng.

Như được hiển thị trong hình bên dưới, khi mức độ của nút bị xóa là $0$, điều đó có nghĩa là nút đó là nút lá và có thể bị xóa trực tiếp.

![Removing a node in a binary search tree (degree 0)](binary_search_tree.assets/bst_remove_case1.png)

Như được hiển thị trong hình bên dưới, khi mức độ của nút bị loại bỏ là $1$, việc thay thế nút bị loại bỏ bằng nút con của nó là đủ.

![Removing a node in a binary search tree (degree 1)](binary_search_tree.assets/bst_remove_case2.png)

Khi mức độ của nút bị loại bỏ là $2$, chúng tôi không thể loại bỏ nó trực tiếp; thay vào đó, chúng ta cần sử dụng một nút để thay thế nó. Để duy trì thuộc tính của cây tìm kiếm nhị phân là "cây con bên trái $<$ nút gốc $<$ cây con bên phải," **nút này có thể là nút nhỏ nhất trong cây con bên phải hoặc nút lớn nhất trong cây con bên trái**.

Giả sử chúng ta chọn nút nhỏ nhất trong cây con bên phải, tức là nút kế tiếp theo thứ tự, quá trình loại bỏ như thể hiện trong hình bên dưới.

1. Tìm nút tiếp theo của nút cần loại bỏ trong "chuỗi truyền tải theo thứ tự", ký hiệu là `tmp`.
2. Thay thế giá trị của nút cần loại bỏ bằng giá trị của `tmp` và loại bỏ đệ quy nút `tmp` trong cây.

=== "<1>"
    ![Removing a node in a binary search tree (degree 2)](binary_search_tree.assets/bst_remove_case3_step1.png)

=== "<2>"
    ![bst_remove_case3_step2](binary_search_tree.assets/bst_remove_case3_step2.png)

=== "<3>"
    ![bst_remove_case3_step3](binary_search_tree.assets/bst_remove_case3_step3.png)

=== "<4>"
    ![bst_remove_case3_step4](binary_search_tree.assets/bst_remove_case3_step4.png)

Hoạt động loại bỏ nút cũng sử dụng thời gian $O(\log n)$, trong đó việc tìm kiếm nút cần xóa yêu cầu thời gian $O(\log n)$ và để có được nút kế tiếp theo thứ tự yêu cầu thời gian $O(\log n)$. Mã ví dụ như sau:

=== "Python"
    ```python title="binary_search_tree.py"
    def remove(self, num: int):
            """Delete node"""
            # If tree is empty, return directly
            if self._root is None:
                return
            # Loop search, exit after passing leaf node
            cur, pre = self._root, None
            while cur is not None:
                # Found node to delete, exit loop
                if cur.val == num:
                    break
                pre = cur
                # Node to delete is in cur's right subtree
                if cur.val < num:
                    cur = cur.right
                # Node to delete is in cur's left subtree
                else:
                    cur = cur.left
            # If no node to delete, return directly
            if cur is None:
                return
    
            # Number of child nodes = 0 or 1
            if cur.left is None or cur.right is None:
                # When number of child nodes = 0 / 1, child = null / that child node
                child = cur.left or cur.right
                # Delete node cur
                if cur != self._root:
                    if pre.left == cur:
                        pre.left = child
                    else:
                        pre.right = child
                else:
                    # If deleted node is root node, reassign root node
                    self._root = child
            # Number of child nodes = 2
            else:
                # Get next node of cur in inorder traversal
                tmp: TreeNode = cur.right
                while tmp.left is not None:
                    tmp = tmp.left
                # Recursively delete node tmp
                self.remove(tmp.val)
                # Replace cur with tmp
                cur.val = tmp.val
    ```
=== "C++"
    ```cpp title="binary_search_tree.cpp"
    void remove(int num) {
            // If tree is empty, return directly
            if (root == nullptr)
                return;
            TreeNode *cur = root, *pre = nullptr;
            // Loop search, exit after passing leaf node
            while (cur != nullptr) {
                // Found node to delete, exit loop
                if (cur->val == num)
                    break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur->val < num)
                    cur = cur->right;
                // Node to delete is in cur's left subtree
                else
                    cur = cur->left;
            }
            // If no node to delete, return directly
            if (cur == nullptr)
                return;
            // Number of child nodes = 0 or 1
            if (cur->left == nullptr || cur->right == nullptr) {
                // When number of child nodes = 0 / 1, child = nullptr / that child node
                TreeNode *child = cur->left != nullptr ? cur->left : cur->right;
                // Delete node cur
                if (cur != root) {
                    if (pre->left == cur)
                        pre->left = child;
                    else
                        pre->right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    root = child;
                }
                // Free memory
                delete cur;
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                TreeNode *tmp = cur->right;
                while (tmp->left != nullptr) {
                    tmp = tmp->left;
                }
                int tmpVal = tmp->val;
                // Recursively delete node tmp
                remove(tmp->val);
                // Replace cur with tmp
                cur->val = tmpVal;
            }
        }
    ```
=== "Java"
    ```java title="binary_search_tree.java"
    public void remove(int num) {
            // If tree is empty, return directly
            if (root == null)
                return;
            TreeNode cur = root, pre = null;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found node to delete, exit loop
                if (cur.val == num)
                    break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Node to delete is in cur's left subtree
                else
                    cur = cur.left;
            }
            // If no node to delete, return directly
            if (cur == null)
                return;
            // Number of child nodes = 0 or 1
            if (cur.left == null || cur.right == null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                TreeNode child = cur.left != null ? cur.left : cur.right;
                // Delete node cur
                if (cur != root) {
                    if (pre.left == cur)
                        pre.left = child;
                    else
                        pre.right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    root = child;
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                TreeNode tmp = cur.right;
                while (tmp.left != null) {
                    tmp = tmp.left;
                }
                // Recursively delete node tmp
                remove(tmp.val);
                // Replace cur with tmp
                cur.val = tmp.val;
            }
        }
    ```
=== "C#"
    ```csharp title="binary_search_tree.cs"
    public void Remove(int num) {
            // If tree is empty, return directly
            if (root == null)
                return;
            TreeNode? cur = root, pre = null;
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found node to delete, exit loop
                if (cur.val == num)
                    break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur.val < num)
                    cur = cur.right;
                // Node to delete is in cur's left subtree
                else
                    cur = cur.left;
            }
            // If no node to delete, return directly
            if (cur == null)
                return;
            // Number of child nodes = 0 or 1
            if (cur.left == null || cur.right == null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                TreeNode? child = cur.left ?? cur.right;
                // Delete node cur
                if (cur != root) {
                    if (pre!.left == cur)
                        pre.left = child;
                    else
                        pre.right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    root = child;
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                TreeNode? tmp = cur.right;
                while (tmp.left != null) {
                    tmp = tmp.left;
                }
                // Recursively delete node tmp
                Remove(tmp.val!.Value);
                // Replace cur with tmp
                cur.val = tmp.val;
            }
        }
    ```
=== "Go"
    ```go title="binary_search_tree.go"
    func (bst *binarySearchTree) remove(num int) {
    	cur := bst.root
    	// If tree is empty, return directly
    	if cur == nil {
    		return
    	}
    	// Node position before the node to be removed
    	var pre *TreeNode = nil
    	// Loop search, exit after passing leaf node
    	for cur != nil {
    		if cur.Val == num {
    			break
    		}
    		pre = cur
    		if cur.Val.(int) < num {
    			// Node to be removed is in right subtree
    			cur = cur.Right
    		} else {
    			// Node to be removed is in left subtree
    			cur = cur.Left
    		}
    	}
    	// If no node to delete, return directly
    	if cur == nil {
    		return
    	}
    	// Number of child nodes is 0 or 1
    	if cur.Left == nil || cur.Right == nil {
    		var child *TreeNode = nil
    		// Get child node of node to be removed
    		if cur.Left != nil {
    			child = cur.Left
    		} else {
    			child = cur.Right
    		}
    		// Delete node cur
    		if cur != bst.root {
    			if pre.Left == cur {
    				pre.Left = child
    			} else {
    				pre.Right = child
    			}
    		} else {
    			// If deleted node is root node, reassign root node
    			bst.root = child
    		}
    		// Number of child nodes is 2
    	} else {
    		// Get next node of node cur to be removed in in-order traversal
    		tmp := cur.Right
    		for tmp.Left != nil {
    			tmp = tmp.Left
    		}
    		// Recursively delete node tmp
    		bst.remove(tmp.Val.(int))
    		// Replace cur with tmp
    		cur.Val = tmp.Val
    	}
    }
    ```
=== "Swift"
    ```swift title="binary_search_tree.swift"
    func remove(num: Int) {
            // If tree is empty, return directly
            if root == nil {
                return
            }
            var cur = root
            var pre: TreeNode?
            // Loop search, exit after passing leaf node
            while cur != nil {
                // Found node to delete, exit loop
                if cur!.val == num {
                    break
                }
                pre = cur
                // Node to delete is in cur's right subtree
                if cur!.val < num {
                    cur = cur?.right
                }
                // Node to delete is in cur's left subtree
                else {
                    cur = cur?.left
                }
            }
            // If no node to delete, return directly
            if cur == nil {
                return
            }
            // Number of child nodes = 0 or 1
            if cur?.left == nil || cur?.right == nil {
                // When number of child nodes = 0 / 1, child = null / that child node
                let child = cur?.left ?? cur?.right
                // Delete node cur
                if cur !== root {
                    if pre?.left === cur {
                        pre?.left = child
                    } else {
                        pre?.right = child
                    }
                } else {
                    // If deleted node is root node, reassign root node
                    root = child
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                var tmp = cur?.right
                while tmp?.left != nil {
                    tmp = tmp?.left
                }
                // Recursively delete node tmp
                remove(num: tmp!.val)
                // Replace cur with tmp
                cur?.val = tmp!.val
            }
        }
    ```
=== "JS"
    ```javascript title="binary_search_tree.js"
    remove(num) {
            // If tree is empty, return directly
            if (this.root === null) return;
            let cur = this.root,
                pre = null;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Found node to delete, exit loop
                if (cur.val === num) break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Node to delete is in cur's left subtree
                else cur = cur.left;
            }
            // If no node to delete, return directly
            if (cur === null) return;
            // Number of child nodes = 0 or 1
            if (cur.left === null || cur.right === null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                const child = cur.left !== null ? cur.left : cur.right;
                // Delete node cur
                if (cur !== this.root) {
                    if (pre.left === cur) pre.left = child;
                    else pre.right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    this.root = child;
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                let tmp = cur.right;
                while (tmp.left !== null) {
                    tmp = tmp.left;
                }
                // Recursively delete node tmp
                this.remove(tmp.val);
                // Replace cur with tmp
                cur.val = tmp.val;
            }
        }
    ```
=== "TS"
    ```typescript title="binary_search_tree.ts"
    remove(num: number): void {
            // If tree is empty, return directly
            if (this.root === null) return;
            let cur: TreeNode | null = this.root,
                pre: TreeNode | null = null;
            // Loop search, exit after passing leaf node
            while (cur !== null) {
                // Found node to delete, exit loop
                if (cur.val === num) break;
                pre = cur;
                // Node to delete is in cur's right subtree
                if (cur.val < num) cur = cur.right;
                // Node to delete is in cur's left subtree
                else cur = cur.left;
            }
            // If no node to delete, return directly
            if (cur === null) return;
            // Number of child nodes = 0 or 1
            if (cur.left === null || cur.right === null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                const child: TreeNode | null =
                    cur.left !== null ? cur.left : cur.right;
                // Delete node cur
                if (cur !== this.root) {
                    if (pre!.left === cur) pre!.left = child;
                    else pre!.right = child;
                } else {
                    // If deleted node is root node, reassign root node
                    this.root = child;
                }
            }
            // Number of child nodes = 2
            else {
                // Get next node of cur in inorder traversal
                let tmp: TreeNode | null = cur.right;
                while (tmp!.left !== null) {
                    tmp = tmp!.left;
                }
                // Recursively delete node tmp
                this.remove(tmp!.val);
                // Replace cur with tmp
                cur.val = tmp!.val;
            }
        }
    ```
=== "Dart"
    ```dart title="binary_search_tree.dart"
    void remove(int _num) {
        // If tree is empty, return directly
        if (_root == null) return;
        TreeNode? cur = _root;
        TreeNode? pre = null;
        // Loop search, exit after passing leaf node
        while (cur != null) {
          // Found node to delete, exit loop
          if (cur.val == _num) break;
          pre = cur;
          // Node to delete is in cur's right subtree
          if (cur.val < _num)
            cur = cur.right;
          // Node to delete is in cur's left subtree
          else
            cur = cur.left;
        }
        // If no node to delete, return directly
        if (cur == null) return;
        // Number of child nodes = 0 or 1
        if (cur.left == null || cur.right == null) {
          // When number of child nodes = 0 / 1, child = null / that child node
          TreeNode? child = cur.left ?? cur.right;
          // Delete node cur
          if (cur != _root) {
            if (pre!.left == cur)
              pre.left = child;
            else
              pre.right = child;
          } else {
            // If deleted node is root node, reassign root node
            _root = child;
          }
        } else {
          // Number of child nodes = 2
          // Get next node of cur in inorder traversal
          TreeNode? tmp = cur.right;
          while (tmp!.left != null) {
            tmp = tmp.left;
          }
          // Recursively delete node tmp
          remove(tmp.val);
          // Replace cur with tmp
          cur.val = tmp.val;
        }
      }
    ```
=== "Rust"
    ```rust title="binary_search_tree.rs"
    pub fn remove(&mut self, num: i32) {
            // If tree is empty, return directly
            if self.root.is_none() {
                return;
            }
            let mut cur = self.root.clone();
            let mut pre = None;
            // Loop search, exit after passing leaf node
            while let Some(node) = cur.clone() {
                match num.cmp(&node.borrow().val) {
                    // Found node to delete, exit loop
                    Ordering::Equal => break,
                    // Node to delete is in cur's right subtree
                    Ordering::Greater => {
                        pre = cur.clone();
                        cur = node.borrow().right.clone();
                    }
                    // Node to delete is in cur's left subtree
                    Ordering::Less => {
                        pre = cur.clone();
                        cur = node.borrow().left.clone();
                    }
                }
            }
            // If no node to delete, return directly
            if cur.is_none() {
                return;
            }
            let cur = cur.unwrap();
            let (left_child, right_child) = (cur.borrow().left.clone(), cur.borrow().right.clone());
            match (left_child.clone(), right_child.clone()) {
                // Number of child nodes = 0 or 1
                (None, None) | (Some(_), None) | (None, Some(_)) => {
                    // When number of child nodes = 0 / 1, child = nullptr / that child node
                    let child = left_child.or(right_child);
                    let pre = pre.unwrap();
                    // Delete node cur
                    if !Rc::ptr_eq(&cur, self.root.as_ref().unwrap()) {
                        let left = pre.borrow().left.clone();
                        if left.is_some() && Rc::ptr_eq(left.as_ref().unwrap(), &cur) {
                            pre.borrow_mut().left = child;
                        } else {
                            pre.borrow_mut().right = child;
                        }
                    } else {
                        // If deleted node is root node, reassign root node
                        self.root = child;
                    }
                }
                // Number of child nodes = 2
                (Some(_), Some(_)) => {
                    // Get next node of cur in inorder traversal
                    let mut tmp = cur.borrow().right.clone();
                    while let Some(node) = tmp.clone() {
                        if node.borrow().left.is_some() {
                            tmp = node.borrow().left.clone();
                        } else {
                            break;
                        }
                    }
                    let tmp_val = tmp.unwrap().borrow().val;
                    // Recursively delete node tmp
                    self.remove(tmp_val);
                    // Replace cur with tmp
                    cur.borrow_mut().val = tmp_val;
                }
            }
        }
    ```
=== "C"
    ```c title="binary_search_tree.c"
    // Cannot use remove keyword here due to stdio.h inclusion
    void removeItem(BinarySearchTree *bst, int num) {
        // If tree is empty, return directly
        if (bst->root == NULL)
            return;
        TreeNode *cur = bst->root, *pre = NULL;
        // Loop search, exit after passing leaf node
        while (cur != NULL) {
            // Found node to delete, exit loop
            if (cur->val == num)
                break;
            pre = cur;
            if (cur->val < num) {
                // Node to delete is in right subtree of root
                cur = cur->right;
            } else {
                // Node to delete is in left subtree of root
                cur = cur->left;
            }
        }
        // If no node to delete, return directly
        if (cur == NULL)
            return;
        // Check if node to delete has children
        if (cur->left == NULL || cur->right == NULL) {
            /* Number of child nodes = 0 or 1 */
            // When number of child nodes = 0 / 1, child = nullptr / that child node
            TreeNode *child = cur->left != NULL ? cur->left : cur->right;
            // Delete node cur
            if (pre->left == cur) {
                pre->left = child;
            } else {
                pre->right = child;
            }
            // Free memory
            free(cur);
        } else {
            /* Number of child nodes = 2 */
            // Get next node of cur in inorder traversal
            TreeNode *tmp = cur->right;
            while (tmp->left != NULL) {
                tmp = tmp->left;
            }
            int tmpVal = tmp->val;
            // Recursively delete node tmp
            removeItem(bst, tmp->val);
            // Replace cur with tmp
            cur->val = tmpVal;
        }
    }
    ```
=== "Kotlin"
    ```kotlin title="binary_search_tree.kt"
    fun remove(num: Int) {
            // If tree is empty, return directly
            if (root == null)
                return
            var cur = root
            var pre: TreeNode? = null
            // Loop search, exit after passing leaf node
            while (cur != null) {
                // Found node to delete, exit loop
                if (cur._val == num)
                    break
                pre = cur
                // Node to delete is in cur's right subtree
                cur = if (cur._val < num)
                    cur.right
                // Node to delete is in cur's left subtree
                else
                    cur.left
            }
            // If no node to delete, return directly
            if (cur == null)
                return
            // Number of child nodes = 0 or 1
            if (cur.left == null || cur.right == null) {
                // When number of child nodes = 0 / 1, child = null / that child node
                val child = if (cur.left != null)
                    cur.left
                else
                    cur.right
                // Delete node cur
                if (cur != root) {
                    if (pre!!.left == cur)
                        pre.left = child
                    else
                        pre.right = child
                } else {
                    // If deleted node is root node, reassign root node
                    root = child
                }
                // Number of child nodes = 2
            } else {
                // Get next node of cur in inorder traversal
                var tmp = cur.right
                while (tmp!!.left != null) {
                    tmp = tmp.left
                }
                // Recursively delete node tmp
                remove(tmp._val)
                // Replace cur with tmp
                cur._val = tmp._val
            }
        }
    ```
=== "Ruby"
    ```ruby title="binary_search_tree.rb"
    ### Delete node ###
      def remove(num)
        # If tree is empty, return directly
        return if @root.nil?
    
        # Loop search, exit after passing leaf node
        cur, pre = @root, nil
        while !cur.nil?
          # Found node to delete, exit loop
          break if cur.val == num
    
          pre = cur
          # Node to delete is in cur's right subtree
          if cur.val < num
            cur = cur.right
          # Node to delete is in cur's left subtree
          else
            cur = cur.left
          end
        end
        # If no node to delete, return directly
        return if cur.nil?
    
        # Number of child nodes = 0 or 1
        if cur.left.nil? || cur.right.nil?
          # When number of child nodes = 0 / 1, child = null / that child node
          child = cur.left || cur.right
          # Delete node cur
          if cur != @root
            if pre.left == cur
              pre.left = child
            else
              pre.right = child
            end
          else
            # If deleted node is root node, reassign root node
            @root = child
          end
        # Number of child nodes = 2
        else
          # Get next node of cur in inorder traversal
          tmp = cur.right
          while !tmp.left.nil?
            tmp = tmp.left
          end
          # Recursively delete node tmp
          remove(tmp.val)
          # Replace cur with tmp
          cur.val = tmp.val
        end
    ```


### Truyền tải theo thứ tự được sắp xếp

Như được hiển thị trong hình bên dưới, việc duyệt theo thứ tự của cây nhị phân tuân theo thứ tự duyệt "left $\rightarrow$ root $\rightarrow$ right", trong khi cây tìm kiếm nhị phân thỏa mãn mối quan hệ kích thước "nút con trái $<$ nút gốc $<$ nút con phải".

Điều này có nghĩa là khi thực hiện duyệt theo thứ tự trong cây tìm kiếm nhị phân, nút nhỏ nhất tiếp theo luôn được duyệt trước, do đó mang lại một thuộc tính quan trọng: **Trình tự duyệt theo thứ tự của cây tìm kiếm nhị phân đang tăng dần**.

Bằng cách sử dụng thuộc tính truyền tải theo thứ tự tăng dần, chúng ta có thể thu được dữ liệu có thứ tự trong cây tìm kiếm nhị phân chỉ trong $O(n)$ thời gian mà không cần thực hiện thêm các thao tác sắp xếp, điều này rất hiệu quả.

![Inorder traversal sequence of a binary search tree](binary_search_tree.assets/bst_inorder_traversal.png)

## Hiệu quả của cây tìm kiếm nhị phân

Đưa ra một tập hợp dữ liệu, chúng tôi xem xét sử dụng một mảng hoặc cây tìm kiếm nhị phân để lưu trữ. Quan sát bảng bên dưới, tất cả các thao tác trong cây tìm kiếm nhị phân đều có độ phức tạp thời gian logarit, mang lại hiệu suất ổn định và hiệu quả. Mảng chỉ hiệu quả hơn cây tìm kiếm nhị phân trong các trường hợp có tần suất bổ sung cao cũng như tìm kiếm và xóa tần số thấp.

<p align="center"> Table <id> &nbsp; Efficiency comparison between arrays and search trees </p>

|                | Mảng chưa sắp xếp | Cây tìm kiếm nhị phân |
| -------------- | -------------- | ------------------ |
| Phần tử tìm kiếm | $O(n)$ | $O(\log n)$ |
| Chèn phần tử | $O(1)$ | $O(\log n)$ |
| Xóa phần tử | $O(n)$ | $O(\log n)$ |

Trong trường hợp lý tưởng, cây tìm kiếm nhị phân được cân bằng, do đó, bất kỳ nút nào cũng có thể được tìm thấy trong các vòng lặp $O(\log n)$.

Tuy nhiên, nếu chúng ta liên tục chèn và xóa các nút trong cây tìm kiếm nhị phân, nó có thể thoái hóa thành danh sách liên kết như trong hình bên dưới, trong đó độ phức tạp về thời gian của các hoạt động khác nhau cũng giảm xuống $O(n)$.

![Degradation of a binary search tree](binary_search_tree.assets/bst_degradation.png)

## Ứng dụng phổ biến của cây tìm kiếm nhị phân

- Được sử dụng làm chỉ mục đa cấp trong hệ thống để thực hiện các hoạt động tìm kiếm, chèn và xóa hiệu quả.
- Phục vụ như cấu trúc dữ liệu cơ bản cho các thuật toán tìm kiếm nhất định.
- Dùng để lưu trữ các luồng dữ liệu nhằm duy trì trạng thái có trật tự của chúng.
