#Các thao tác cơ bản trên đồ thị

Các thao tác cơ bản trên đồ thị có thể được chia thành các thao tác trên “cạnh” và các thao tác trên “đỉnh”. Việc triển khai của chúng khác nhau tùy thuộc vào việc biểu đồ được biểu diễn dưới dạng "ma trận kề" hay "danh sách kề".

## Triển khai dựa trên Ma trận kề

Cho một đồ thị vô hướng có các đỉnh $n$, các phép toán khác nhau được thực hiện như trong hình bên dưới.

- **Thêm hoặc xóa một cạnh**: Sửa đổi trực tiếp cạnh được chỉ định trong ma trận kề, sử dụng thời gian $O(1)$. Vì là đồ thị vô hướng nên cả hai hướng của cạnh cần được cập nhật đồng thời.
- **Thêm một đỉnh**: Thêm một hàng và một cột vào cuối ma trận kề và điền tất cả chúng bằng $0$s, sử dụng thời gian $O(n)$.
- **Xóa một đỉnh**: Xóa một hàng và một cột trong ma trận kề. Trường hợp xấu nhất xảy ra khi xóa hàng và cột đầu tiên, yêu cầu các phần tử $(n-1)^2$ phải được "di chuyển lên và sang trái", do đó sử dụng $O(n^2)$ thời gian.
- **Khởi tạo**: Cho $n$ đỉnh, khởi tạo danh sách đỉnh `đỉnh` có độ dài $n$, sử dụng $O(n)$ thời gian; khởi tạo một ma trận kề `adjMat` có kích thước $n \times n$, sử dụng $O(n^2)$ time.

=== "<1>"
    ![Initialization, adding and removing edges, adding and removing vertices in adjacency matrix](graph_operations.assets/adjacency_matrix_step1_initialization.png)

=== "<2>"
    ![adjacency_matrix_add_edge](graph_operations.assets/adjacency_matrix_step2_add_edge.png)

=== "<3>"
    ![adjacency_matrix_remove_edge](graph_operations.assets/adjacency_matrix_step3_remove_edge.png)

=== "<4>"
    ![adjacency_matrix_add_vertex](graph_operations.assets/adjacency_matrix_step4_add_vertex.png)

=== "<5>"
    ![adjacency_matrix_remove_vertex](graph_operations.assets/adjacency_matrix_step5_remove_vertex.png)

Sau đây là mã triển khai cho các biểu đồ được biểu diễn bằng ma trận kề:

=== "Python"
    ```python title="graph_adjacency_matrix.py"
    class GraphAdjMat:
        """Undirected graph class based on adjacency matrix"""
    
        def __init__(self, vertices: list[int], edges: list[list[int]]):
            """Constructor"""
            # Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
            self.vertices: list[int] = []
            # Adjacency matrix, where the row and column indices correspond to the "vertex index"
            self.adj_mat: list[list[int]] = []
            # Add vertices
            for val in vertices:
                self.add_vertex(val)
            # Add edges
            # Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
            for e in edges:
                self.add_edge(e[0], e[1])
    
        def size(self) -> int:
            """Get the number of vertices"""
            return len(self.vertices)
    
        def add_vertex(self, val: int):
            """Add vertex"""
            n = self.size()
            # Add the value of the new vertex to the vertex list
            self.vertices.append(val)
            # Add a row to the adjacency matrix
            new_row = [0] * n
            self.adj_mat.append(new_row)
            # Add a column to the adjacency matrix
            for row in self.adj_mat:
                row.append(0)
    
        def remove_vertex(self, index: int):
            """Remove vertex"""
            if index >= self.size():
                raise IndexError()
            # Remove the vertex at index from the vertex list
            self.vertices.pop(index)
            # Remove the row at index from the adjacency matrix
            self.adj_mat.pop(index)
            # Remove the column at index from the adjacency matrix
            for row in self.adj_mat:
                row.pop(index)
    
        def add_edge(self, i: int, j: int):
            """Add edge"""
            # Parameters i, j correspond to the vertices element indices
            # Handle index out of bounds and equality
            if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
                raise IndexError()
            # In an undirected graph, the adjacency matrix is symmetric about the main diagonal, i.e., (i, j) == (j, i)
            self.adj_mat[i][j] = 1
            self.adj_mat[j][i] = 1
    
        def remove_edge(self, i: int, j: int):
            """Remove edge"""
            # Parameters i, j correspond to the vertices element indices
            # Handle index out of bounds and equality
            if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
                raise IndexError()
            self.adj_mat[i][j] = 0
            self.adj_mat[j][i] = 0
    
        def print(self):
            """Print adjacency matrix"""
            print("Vertex list =", self.vertices)
            print("Adjacency matrix =")
            print_matrix(self.adj_mat)
    ```
=== "C++"
    ```cpp title="graph_adjacency_matrix.cpp"
    class GraphAdjMat {
        vector<int> vertices;       // Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        vector<vector<int>> adjMat; // Adjacency matrix, where the row and column indices correspond to the "vertex index"
    
      public:
        /* Constructor */
        GraphAdjMat(const vector<int> &vertices, const vector<vector<int>> &edges) {
            // Add vertex
            for (int val : vertices) {
                addVertex(val);
            }
            // Add edge
            // Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
            for (const vector<int> &edge : edges) {
                addEdge(edge[0], edge[1]);
            }
        }
    
        /* Get the number of vertices */
        int size() const {
            return vertices.size();
        }
    
        /* Add vertex */
        void addVertex(int val) {
            int n = size();
            // Add the value of the new vertex to the vertex list
            vertices.push_back(val);
            // Add a row to the adjacency matrix
            adjMat.emplace_back(vector<int>(n, 0));
            // Add a column to the adjacency matrix
            for (vector<int> &row : adjMat) {
                row.push_back(0);
            }
        }
    
        /* Remove vertex */
        void removeVertex(int index) {
            if (index >= size()) {
                throw out_of_range("Vertex does not exist");
            }
            // Remove the vertex at index from the vertex list
            vertices.erase(vertices.begin() + index);
            // Remove the row at index from the adjacency matrix
            adjMat.erase(adjMat.begin() + index);
            // Remove the column at index from the adjacency matrix
            for (vector<int> &row : adjMat) {
                row.erase(row.begin() + index);
            }
        }
    
        /* Add edge */
        // Parameters i, j correspond to the vertices element indices
        void addEdge(int i, int j) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= size() || j >= size() || i == j) {
                throw out_of_range("Vertex does not exist");
            }
            // In an undirected graph, the adjacency matrix is symmetric about the main diagonal, i.e., (i, j) == (j, i)
            adjMat[i][j] = 1;
            adjMat[j][i] = 1;
        }
    
        /* Remove edge */
        // Parameters i, j correspond to the vertices element indices
        void removeEdge(int i, int j) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= size() || j >= size() || i == j) {
                throw out_of_range("Vertex does not exist");
            }
            adjMat[i][j] = 0;
            adjMat[j][i] = 0;
        }
    
        /* Print adjacency matrix */
        void print() {
            cout << "Vertex list = ";
            printVector(vertices);
            cout << "Adjacency matrix =" << endl;
            printVectorMatrix(adjMat);
        }
    };
    ```
=== "Java"
    ```java title="graph_adjacency_matrix.java"
    class GraphAdjMat {
        List<Integer> vertices; // Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        List<List<Integer>> adjMat; // Adjacency matrix, where the row and column indices correspond to the "vertex index"
    
        /* Constructor */
        public GraphAdjMat(int[] vertices, int[][] edges) {
            this.vertices = new ArrayList<>();
            this.adjMat = new ArrayList<>();
            // Add vertex
            for (int val : vertices) {
                addVertex(val);
            }
            // Add edge
            // Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
            for (int[] e : edges) {
                addEdge(e[0], e[1]);
            }
        }
    
        /* Get the number of vertices */
        public int size() {
            return vertices.size();
        }
    
        /* Add vertex */
        public void addVertex(int val) {
            int n = size();
            // Add the value of the new vertex to the vertex list
            vertices.add(val);
            // Add a row to the adjacency matrix
            List<Integer> newRow = new ArrayList<>(n);
            for (int j = 0; j < n; j++) {
                newRow.add(0);
            }
            adjMat.add(newRow);
            // Add a column to the adjacency matrix
            for (List<Integer> row : adjMat) {
                row.add(0);
            }
        }
    
        /* Remove vertex */
        public void removeVertex(int index) {
            if (index >= size())
                throw new IndexOutOfBoundsException();
            // Remove the vertex at index from the vertex list
            vertices.remove(index);
            // Remove the row at index from the adjacency matrix
            adjMat.remove(index);
            // Remove the column at index from the adjacency matrix
            for (List<Integer> row : adjMat) {
                row.remove(index);
            }
        }
    
        /* Add edge */
        // Parameters i, j correspond to the vertices element indices
        public void addEdge(int i, int j) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= size() || j >= size() || i == j)
                throw new IndexOutOfBoundsException();
            // In an undirected graph, the adjacency matrix is symmetric about the main diagonal, i.e., (i, j) == (j, i)
            adjMat.get(i).set(j, 1);
            adjMat.get(j).set(i, 1);
        }
    
        /* Remove edge */
        // Parameters i, j correspond to the vertices element indices
        public void removeEdge(int i, int j) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= size() || j >= size() || i == j)
                throw new IndexOutOfBoundsException();
            adjMat.get(i).set(j, 0);
            adjMat.get(j).set(i, 0);
        }
    
        /* Print adjacency matrix */
        public void print() {
            System.out.print("Vertex list = ");
            System.out.println(vertices);
            System.out.println("Adjacency matrix =");
            PrintUtil.printMatrix(adjMat);
        }
    }
    ```
=== "C#"
    ```csharp title="graph_adjacency_matrix.cs"
    class GraphAdjMat {
        List<int> vertices;     // Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        List<List<int>> adjMat; // Adjacency matrix, where the row and column indices correspond to the "vertex index"
    
        /* Constructor */
        public GraphAdjMat(int[] vertices, int[][] edges) {
            this.vertices = [];
            this.adjMat = [];
            // Add vertex
            foreach (int val in vertices) {
                AddVertex(val);
            }
            // Add edge
            // Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
            foreach (int[] e in edges) {
                AddEdge(e[0], e[1]);
            }
        }
    
        /* Get the number of vertices */
        int Size() {
            return vertices.Count;
        }
    
        /* Add vertex */
        public void AddVertex(int val) {
            int n = Size();
            // Add the value of the new vertex to the vertex list
            vertices.Add(val);
            // Add a row to the adjacency matrix
            List<int> newRow = new(n);
            for (int j = 0; j < n; j++) {
                newRow.Add(0);
            }
            adjMat.Add(newRow);
            // Add a column to the adjacency matrix
            foreach (List<int> row in adjMat) {
                row.Add(0);
            }
        }
    
        /* Remove vertex */
        public void RemoveVertex(int index) {
            if (index >= Size())
                throw new IndexOutOfRangeException();
            // Remove the vertex at index from the vertex list
            vertices.RemoveAt(index);
            // Remove the row at index from the adjacency matrix
            adjMat.RemoveAt(index);
            // Remove the column at index from the adjacency matrix
            foreach (List<int> row in adjMat) {
                row.RemoveAt(index);
            }
        }
    
        /* Add edge */
        // Parameters i, j correspond to the vertices element indices
        public void AddEdge(int i, int j) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= Size() || j >= Size() || i == j)
                throw new IndexOutOfRangeException();
            // In an undirected graph, the adjacency matrix is symmetric about the main diagonal, i.e., (i, j) == (j, i)
            adjMat[i][j] = 1;
            adjMat[j][i] = 1;
        }
    
        /* Remove edge */
        // Parameters i, j correspond to the vertices element indices
        public void RemoveEdge(int i, int j) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= Size() || j >= Size() || i == j)
                throw new IndexOutOfRangeException();
            adjMat[i][j] = 0;
            adjMat[j][i] = 0;
        }
    
        /* Print adjacency matrix */
        public void Print() {
            Console.Write("Vertex list = ");
            PrintUtil.PrintList(vertices);
            Console.WriteLine("Adjacency matrix =");
            PrintUtil.PrintMatrix(adjMat);
        }
    }
    ```
=== "Go"
    ```go title="graph_adjacency_matrix.go"
    type graphAdjMat struct {
    	// Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
    	vertices []int
    	// Adjacency matrix, where the row and column indices correspond to the "vertex index"
    	adjMat [][]int
    }
    ```
=== "Swift"
    ```swift title="graph_adjacency_matrix.swift"
    class GraphAdjMat {
        private var vertices: [Int] // Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        private var adjMat: [[Int]] // Adjacency matrix, where the row and column indices correspond to the "vertex index"
    
        /* Constructor */
        init(vertices: [Int], edges: [[Int]]) {
            self.vertices = []
            adjMat = []
            // Add vertex
            for val in vertices {
                addVertex(val: val)
            }
            // Add edge
            // Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
            for e in edges {
                addEdge(i: e[0], j: e[1])
            }
        }
    
        /* Get the number of vertices */
        func size() -> Int {
            vertices.count
        }
    
        /* Add vertex */
        func addVertex(val: Int) {
            let n = size()
            // Add the value of the new vertex to the vertex list
            vertices.append(val)
            // Add a row to the adjacency matrix
            let newRow = Array(repeating: 0, count: n)
            adjMat.append(newRow)
            // Add a column to the adjacency matrix
            for i in adjMat.indices {
                adjMat[i].append(0)
            }
        }
    
        /* Remove vertex */
        func removeVertex(index: Int) {
            if index >= size() {
                fatalError("Out of bounds")
            }
            // Remove the vertex at index from the vertex list
            vertices.remove(at: index)
            // Remove the row at index from the adjacency matrix
            adjMat.remove(at: index)
            // Remove the column at index from the adjacency matrix
            for i in adjMat.indices {
                adjMat[i].remove(at: index)
            }
        }
    
        /* Add edge */
        // Parameters i, j correspond to the vertices element indices
        func addEdge(i: Int, j: Int) {
            // Handle index out of bounds and equality
            if i < 0 || j < 0 || i >= size() || j >= size() || i == j {
                fatalError("Out of bounds")
            }
            // In an undirected graph, the adjacency matrix is symmetric about the main diagonal, i.e., (i, j) == (j, i)
            adjMat[i][j] = 1
            adjMat[j][i] = 1
        }
    
        /* Remove edge */
        // Parameters i, j correspond to the vertices element indices
        func removeEdge(i: Int, j: Int) {
            // Handle index out of bounds and equality
            if i < 0 || j < 0 || i >= size() || j >= size() || i == j {
                fatalError("Out of bounds")
            }
            adjMat[i][j] = 0
            adjMat[j][i] = 0
        }
    
        /* Print adjacency matrix */
        func print() {
            Swift.print("Vertex list = ", terminator: "")
            Swift.print(vertices)
            Swift.print("Adjacency matrix =")
            PrintUtil.printMatrix(matrix: adjMat)
        }
    }
    ```
=== "JS"
    ```javascript title="graph_adjacency_matrix.js"
    class GraphAdjMat {
        vertices; // Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        adjMat; // Adjacency matrix, where the row and column indices correspond to the "vertex index"
    
        /* Constructor */
        constructor(vertices, edges) {
            this.vertices = [];
            this.adjMat = [];
            // Add vertex
            for (const val of vertices) {
                this.addVertex(val);
            }
            // Add edge
            // Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
            for (const e of edges) {
                this.addEdge(e[0], e[1]);
            }
        }
    
        /* Get the number of vertices */
        size() {
            return this.vertices.length;
        }
    
        /* Add vertex */
        addVertex(val) {
            const n = this.size();
            // Add the value of the new vertex to the vertex list
            this.vertices.push(val);
            // Add a row to the adjacency matrix
            const newRow = [];
            for (let j = 0; j < n; j++) {
                newRow.push(0);
            }
            this.adjMat.push(newRow);
            // Add a column to the adjacency matrix
            for (const row of this.adjMat) {
                row.push(0);
            }
        }
    
        /* Remove vertex */
        removeVertex(index) {
            if (index >= this.size()) {
                throw new RangeError('Index Out Of Bounds Exception');
            }
            // Remove the vertex at index from the vertex list
            this.vertices.splice(index, 1);
    
            // Remove the row at index from the adjacency matrix
            this.adjMat.splice(index, 1);
            // Remove the column at index from the adjacency matrix
            for (const row of this.adjMat) {
                row.splice(index, 1);
            }
        }
    
        /* Add edge */
        // Parameters i, j correspond to the vertices element indices
        addEdge(i, j) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= this.size() || j >= this.size() || i === j) {
                throw new RangeError('Index Out Of Bounds Exception');
            }
            // In undirected graph, adjacency matrix is symmetric about main diagonal, i.e., satisfies (i, j) === (j, i)
            this.adjMat[i][j] = 1;
            this.adjMat[j][i] = 1;
        }
    
        /* Remove edge */
        // Parameters i, j correspond to the vertices element indices
        removeEdge(i, j) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= this.size() || j >= this.size() || i === j) {
                throw new RangeError('Index Out Of Bounds Exception');
            }
            this.adjMat[i][j] = 0;
            this.adjMat[j][i] = 0;
        }
    
        /* Print adjacency matrix */
        print() {
            console.log('Vertex list = ', this.vertices);
            console.log('Adjacency matrix =', this.adjMat);
        }
    }
    ```
=== "TS"
    ```typescript title="graph_adjacency_matrix.ts"
    class GraphAdjMat {
        vertices: number[]; // Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        adjMat: number[][]; // Adjacency matrix, where the row and column indices correspond to the "vertex index"
    
        /* Constructor */
        constructor(vertices: number[], edges: number[][]) {
            this.vertices = [];
            this.adjMat = [];
            // Add vertex
            for (const val of vertices) {
                this.addVertex(val);
            }
            // Add edge
            // Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
            for (const e of edges) {
                this.addEdge(e[0], e[1]);
            }
        }
    
        /* Get the number of vertices */
        size(): number {
            return this.vertices.length;
        }
    
        /* Add vertex */
        addVertex(val: number): void {
            const n: number = this.size();
            // Add the value of the new vertex to the vertex list
            this.vertices.push(val);
            // Add a row to the adjacency matrix
            const newRow: number[] = [];
            for (let j: number = 0; j < n; j++) {
                newRow.push(0);
            }
            this.adjMat.push(newRow);
            // Add a column to the adjacency matrix
            for (const row of this.adjMat) {
                row.push(0);
            }
        }
    
        /* Remove vertex */
        removeVertex(index: number): void {
            if (index >= this.size()) {
                throw new RangeError('Index Out Of Bounds Exception');
            }
            // Remove the vertex at index from the vertex list
            this.vertices.splice(index, 1);
    
            // Remove the row at index from the adjacency matrix
            this.adjMat.splice(index, 1);
            // Remove the column at index from the adjacency matrix
            for (const row of this.adjMat) {
                row.splice(index, 1);
            }
        }
    
        /* Add edge */
        // Parameters i, j correspond to the vertices element indices
        addEdge(i: number, j: number): void {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= this.size() || j >= this.size() || i === j) {
                throw new RangeError('Index Out Of Bounds Exception');
            }
            // In undirected graph, adjacency matrix is symmetric about main diagonal, i.e., satisfies (i, j) === (j, i)
            this.adjMat[i][j] = 1;
            this.adjMat[j][i] = 1;
        }
    
        /* Remove edge */
        // Parameters i, j correspond to the vertices element indices
        removeEdge(i: number, j: number): void {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= this.size() || j >= this.size() || i === j) {
                throw new RangeError('Index Out Of Bounds Exception');
            }
            this.adjMat[i][j] = 0;
            this.adjMat[j][i] = 0;
        }
    
        /* Print adjacency matrix */
        print(): void {
            console.log('Vertex list = ', this.vertices);
            console.log('Adjacency matrix =', this.adjMat);
        }
    }
    ```
=== "Dart"
    ```dart title="graph_adjacency_matrix.dart"
    class GraphAdjMat {
      List<int> vertices = []; // Vertex elements, elements represent "vertex values", indices represent "vertex indices"
      List<List<int>> adjMat = []; // Adjacency matrix, where the row and column indices correspond to the "vertex index"
    
      /* Constructor */
      GraphAdjMat(List<int> vertices, List<List<int>> edges) {
        this.vertices = [];
        this.adjMat = [];
        // Add vertex
        for (int val in vertices) {
          addVertex(val);
        }
        // Add edge
        // Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
        for (List<int> e in edges) {
          addEdge(e[0], e[1]);
        }
      }
    
      /* Get the number of vertices */
      int size() {
        return vertices.length;
      }
    
      /* Add vertex */
      void addVertex(int val) {
        int n = size();
        // Add the value of the new vertex to the vertex list
        vertices.add(val);
        // Add a row to the adjacency matrix
        List<int> newRow = List.filled(n, 0, growable: true);
        adjMat.add(newRow);
        // Add a column to the adjacency matrix
        for (List<int> row in adjMat) {
          row.add(0);
        }
      }
    
      /* Remove vertex */
      void removeVertex(int index) {
        if (index >= size()) {
          throw IndexError;
        }
        // Remove the vertex at index from the vertex list
        vertices.removeAt(index);
        // Remove the row at index from the adjacency matrix
        adjMat.removeAt(index);
        // Remove the column at index from the adjacency matrix
        for (List<int> row in adjMat) {
          row.removeAt(index);
        }
      }
    
      /* Add edge */
      // Parameters i, j correspond to the vertices element indices
      void addEdge(int i, int j) {
        // Handle index out of bounds and equality
        if (i < 0 || j < 0 || i >= size() || j >= size() || i == j) {
          throw IndexError;
        }
        // In an undirected graph, the adjacency matrix is symmetric about the main diagonal, i.e., (i, j) == (j, i)
        adjMat[i][j] = 1;
        adjMat[j][i] = 1;
      }
    
      /* Remove edge */
      // Parameters i, j correspond to the vertices element indices
      void removeEdge(int i, int j) {
        // Handle index out of bounds and equality
        if (i < 0 || j < 0 || i >= size() || j >= size() || i == j) {
          throw IndexError;
        }
        adjMat[i][j] = 0;
        adjMat[j][i] = 0;
      }
    
      /* Print adjacency matrix */
      void printAdjMat() {
        print("Vertex list = $vertices");
        print("Adjacency matrix = ");
        printMatrix(adjMat);
      }
    }
    ```
=== "Rust"
    ```rust title="graph_adjacency_matrix.rs"
    pub struct GraphAdjMat {
        // Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        pub vertices: Vec<i32>,
        // Adjacency matrix, where the row and column indices correspond to the "vertex index"
        pub adj_mat: Vec<Vec<i32>>,
    }
    ```
=== "C"
    ```c title="graph_adjacency_matrix.c"
    GraphAdjMat *newGraphAdjMat() {
        GraphAdjMat *graph = (GraphAdjMat *)malloc(sizeof(GraphAdjMat));
        graph->size = 0;
        for (int i = 0; i < MAX_SIZE; i++) {
            for (int j = 0; j < MAX_SIZE; j++) {
                graph->adjMat[i][j] = 0;
            }
        }
        return graph;
    }
    ```
=== "Kotlin"
    ```kotlin title="graph_adjacency_matrix.kt"
    class GraphAdjMat(vertices: IntArray, edges: Array<IntArray>) {
        val vertices = mutableListOf<Int>() // Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        val adjMat = mutableListOf<MutableList<Int>>() // Adjacency matrix, where the row and column indices correspond to the "vertex index"
    
        /* Constructor */
        init {
            // Add vertex
            for (vertex in vertices) {
                addVertex(vertex)
            }
            // Add edge
            // Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
            for (edge in edges) {
                addEdge(edge[0], edge[1])
            }
        }
    
        /* Get the number of vertices */
        fun size(): Int {
            return vertices.size
        }
    
        /* Add vertex */
        fun addVertex(_val: Int) {
            val n = size()
            // Add the value of the new vertex to the vertex list
            vertices.add(_val)
            // Add a row to the adjacency matrix
            val newRow = mutableListOf<Int>()
            for (j in 0..<n) {
                newRow.add(0)
            }
            adjMat.add(newRow)
            // Add a column to the adjacency matrix
            for (row in adjMat) {
                row.add(0)
            }
        }
    
        /* Remove vertex */
        fun removeVertex(index: Int) {
            if (index >= size())
                throw IndexOutOfBoundsException()
            // Remove the vertex at index from the vertex list
            vertices.removeAt(index)
            // Remove the row at index from the adjacency matrix
            adjMat.removeAt(index)
            // Remove the column at index from the adjacency matrix
            for (row in adjMat) {
                row.removeAt(index)
            }
        }
    
        /* Add edge */
        // Parameters i, j correspond to the vertices element indices
        fun addEdge(i: Int, j: Int) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= size() || j >= size() || i == j)
                throw IndexOutOfBoundsException()
            // In an undirected graph, the adjacency matrix is symmetric about the main diagonal, i.e., (i, j) == (j, i)
            adjMat[i][j] = 1
            adjMat[j][i] = 1
        }
    
        /* Remove edge */
        // Parameters i, j correspond to the vertices element indices
        fun removeEdge(i: Int, j: Int) {
            // Handle index out of bounds and equality
            if (i < 0 || j < 0 || i >= size() || j >= size() || i == j)
                throw IndexOutOfBoundsException()
            adjMat[i][j] = 0
            adjMat[j][i] = 0
        }
    
        /* Print adjacency matrix */
        fun print() {
            print("Vertex list = ")
            println(vertices)
            println("Adjacency matrix =")
            printMatrix(adjMat)
        }
    }
    ```
=== "Ruby"
    ```ruby title="graph_adjacency_matrix.rb"
    ### Undirected graph class based on adjacency matrix ###
    class GraphAdjMat
      def initialize(vertices, edges)
        ### Constructor ###
        # Vertex list, where the element represents the "vertex value" and the index represents the "vertex index"
        @vertices = []
        # Adjacency matrix, where the row and column indices correspond to the "vertex index"
        @adj_mat = []
        # Add vertex
        vertices.each { |val| add_vertex(val) }
        # Add edge
        # Note that the edges elements represent vertex indices, i.e., corresponding to the vertices element indices
        edges.each { |e| add_edge(e[0], e[1]) }
      end
    
      ### Get number of vertices ###
      def size
        @vertices.length
      end
    
      ### Add vertex ###
      def add_vertex(val)
        n = size
        # Add the value of the new vertex to the vertex list
        @vertices << val
        # Add a row to the adjacency matrix
        new_row = Array.new(n, 0)
        @adj_mat << new_row
        # Add a column to the adjacency matrix
        @adj_mat.each { |row| row << 0 }
      end
    
      ### Delete vertex ###
      def remove_vertex(index)
        raise IndexError if index >= size
    
        # Remove the vertex at index from the vertex list
        @vertices.delete_at(index)
        # Remove the row at index from the adjacency matrix
        @adj_mat.delete_at(index)
        # Remove the column at index from the adjacency matrix
        @adj_mat.each { |row| row.delete_at(index) }
      end
    
      ### Add edge ###
      def add_edge(i, j)
        # Parameters i, j correspond to the vertices element indices
        # Handle index out of bounds and equality
        if i < 0 || j < 0 || i >= size || j >= size || i == j
          raise IndexError
        end
        # In an undirected graph, the adjacency matrix is symmetric about the main diagonal, i.e., (i, j) == (j, i)
        @adj_mat[i][j] = 1
        @adj_mat[j][i] = 1
      end
    
      ### Delete edge ###
      def remove_edge(i, j)
        # Parameters i, j correspond to the vertices element indices
        # Handle index out of bounds and equality
        if i < 0 || j < 0 || i >= size || j >= size || i == j
          raise IndexError
        end
        @adj_mat[i][j] = 0
        @adj_mat[j][i] = 0
      end
    
      ### Print adjacency matrix ###
      def __print__
        puts "Vertex list = #{@vertices}"
        puts 'Adjacency matrix ='
        print_matrix(@adj_mat)
      end
    ```


## Triển khai dựa trên danh sách lân cận

Cho một đồ thị vô hướng có tổng số $n$ đỉnh và $m$ cạnh, các phép toán khác nhau có thể được thực hiện như trong hình bên dưới.

- **Thêm một cạnh**: Thêm cạnh vào cuối danh sách liên kết của đỉnh tương ứng, sử dụng thời gian $O(1)$. Vì là đồ thị vô hướng nên các cạnh theo cả hai hướng cần được cộng đồng thời.
- **Xóa một cạnh**: Tìm và loại bỏ cạnh được chỉ định trong danh sách liên kết của đỉnh tương ứng, sử dụng thời gian $O(m)$. Trong đồ thị vô hướng, các cạnh theo cả hai hướng cần được loại bỏ đồng thời.
- **Thêm một đỉnh**: Thêm một danh sách liên kết vào danh sách kề, với đỉnh mới làm nút đầu, sử dụng thời gian $O(1)$.
- **Xóa một đỉnh**: Duyệt toàn bộ danh sách kề và xóa tất cả các cạnh chứa đỉnh đã chỉ định, sử dụng thời gian $O(n + m)$.
- **Khởi tạo**: Tạo các đỉnh $n$ và các cạnh $2m$ trong danh sách kề, sử dụng thời gian $O(n + m)$.

=== "<1>"
    ![Initialization, adding and removing edges, adding and removing vertices in adjacency list](graph_operations.assets/adjacency_list_step1_initialization.png)

=== "<2>"
    ![adjacency_list_add_edge](graph_operations.assets/adjacency_list_step2_add_edge.png)

=== "<3>"
    ![adjacency_list_remove_edge](graph_operations.assets/adjacency_list_step3_remove_edge.png)

=== "<4>"
    ![adjacency_list_add_vertex](graph_operations.assets/adjacency_list_step4_add_vertex.png)

=== "<5>"
    ![adjacency_list_remove_vertex](graph_operations.assets/adjacency_list_step5_remove_vertex.png)

Đoạn mã sau đây hiển thị việc triển khai danh sách kề. So với hình trên, mã thực tế khác ở những điểm sau.

- Để thuận tiện trong việc thêm bớt các đỉnh và để đơn giản hóa code, chúng ta sử dụng danh sách (mảng động) thay vì danh sách liên kết.
- Bảng băm dùng để lưu trữ danh sách kề, trong đó `key` là thể hiện của đỉnh và `value` là danh sách (danh sách liên kết) các đỉnh liền kề của đỉnh đó.

Ngoài ra, chúng tôi sử dụng lớp `Vertex` để biểu thị các đỉnh trong danh sách kề vì lý do sau: nếu chúng tôi sử dụng chỉ mục danh sách để phân biệt các đỉnh khác nhau, như với ma trận kề, thì để xóa đỉnh tại chỉ mục $i$, chúng tôi sẽ cần duyệt qua toàn bộ danh sách kề và giảm tất cả các chỉ số lớn hơn $i$ x $1$, điều này rất kém hiệu quả. Tuy nhiên, nếu mỗi đỉnh là một thể hiện `Vertex` duy nhất, việc xóa một đỉnh không yêu cầu sửa đổi các đỉnh khác.

=== "Python"
    ```python title="graph_adjacency_list.py"
    class GraphAdjList:
        """Undirected graph class based on adjacency list"""
    
        def __init__(self, edges: list[list[Vertex]]):
            """Constructor"""
            # Adjacency list, key: vertex, value: all adjacent vertices of that vertex
            self.adj_list = dict[Vertex, list[Vertex]]()
            # Add all vertices and edges
            for edge in edges:
                self.add_vertex(edge[0])
                self.add_vertex(edge[1])
                self.add_edge(edge[0], edge[1])
    
        def size(self) -> int:
            """Get the number of vertices"""
            return len(self.adj_list)
    
        def add_edge(self, vet1: Vertex, vet2: Vertex):
            """Add edge"""
            if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
                raise ValueError()
            # Add edge vet1 - vet2
            self.adj_list[vet1].append(vet2)
            self.adj_list[vet2].append(vet1)
    
        def remove_edge(self, vet1: Vertex, vet2: Vertex):
            """Remove edge"""
            if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
                raise ValueError()
            # Remove edge vet1 - vet2
            self.adj_list[vet1].remove(vet2)
            self.adj_list[vet2].remove(vet1)
    
        def add_vertex(self, vet: Vertex):
            """Add vertex"""
            if vet in self.adj_list:
                return
            # Add a new linked list in the adjacency list
            self.adj_list[vet] = []
    
        def remove_vertex(self, vet: Vertex):
            """Remove vertex"""
            if vet not in self.adj_list:
                raise ValueError()
            # Remove the linked list corresponding to vertex vet in the adjacency list
            self.adj_list.pop(vet)
            # Traverse the linked lists of other vertices and remove all edges containing vet
            for vertex in self.adj_list:
                if vet in self.adj_list[vertex]:
                    self.adj_list[vertex].remove(vet)
    
        def print(self):
            """Print adjacency list"""
            print("Adjacency list =")
            for vertex in self.adj_list:
                tmp = [v.val for v in self.adj_list[vertex]]
                print(f"{vertex.val}: {tmp},")
    ```
=== "C++"
    ```cpp title="graph_adjacency_list.cpp"
    class GraphAdjList {
      public:
        // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        unordered_map<Vertex *, vector<Vertex *>> adjList;
    
        /* Remove specified node from vector */
        void remove(vector<Vertex *> &vec, Vertex *vet) {
            for (int i = 0; i < vec.size(); i++) {
                if (vec[i] == vet) {
                    vec.erase(vec.begin() + i);
                    break;
                }
            }
        }
    
        /* Constructor */
        GraphAdjList(const vector<vector<Vertex *>> &edges) {
            // Add all vertices and edges
            for (const vector<Vertex *> &edge : edges) {
                addVertex(edge[0]);
                addVertex(edge[1]);
                addEdge(edge[0], edge[1]);
            }
        }
    
        /* Get the number of vertices */
        int size() {
            return adjList.size();
        }
    
        /* Add edge */
        void addEdge(Vertex *vet1, Vertex *vet2) {
            if (!adjList.count(vet1) || !adjList.count(vet2) || vet1 == vet2)
                throw invalid_argument("Vertex does not exist");
            // Add edge vet1 - vet2
            adjList[vet1].push_back(vet2);
            adjList[vet2].push_back(vet1);
        }
    
        /* Remove edge */
        void removeEdge(Vertex *vet1, Vertex *vet2) {
            if (!adjList.count(vet1) || !adjList.count(vet2) || vet1 == vet2)
                throw invalid_argument("Vertex does not exist");
            // Remove edge vet1 - vet2
            remove(adjList[vet1], vet2);
            remove(adjList[vet2], vet1);
        }
    
        /* Add vertex */
        void addVertex(Vertex *vet) {
            if (adjList.count(vet))
                return;
            // Add a new linked list in the adjacency list
            adjList[vet] = vector<Vertex *>();
        }
    
        /* Remove vertex */
        void removeVertex(Vertex *vet) {
            if (!adjList.count(vet))
                throw invalid_argument("Vertex does not exist");
            // Remove the linked list corresponding to vertex vet in the adjacency list
            adjList.erase(vet);
            // Traverse the linked lists of other vertices and remove all edges containing vet
            for (auto &adj : adjList) {
                remove(adj.second, vet);
            }
        }
    
        /* Print adjacency list */
        void print() {
            cout << "Adjacency list =" << endl;
            for (auto &adj : adjList) {
                const auto &key = adj.first;
                const auto &vec = adj.second;
                cout << key->val << ": ";
                printVector(vetsToVals(vec));
            }
        }
    };
    ```
=== "Java"
    ```java title="graph_adjacency_list.java"
    class GraphAdjList {
        // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        Map<Vertex, List<Vertex>> adjList;
    
        /* Constructor */
        public GraphAdjList(Vertex[][] edges) {
            this.adjList = new HashMap<>();
            // Add all vertices and edges
            for (Vertex[] edge : edges) {
                addVertex(edge[0]);
                addVertex(edge[1]);
                addEdge(edge[0], edge[1]);
            }
        }
    
        /* Get the number of vertices */
        public int size() {
            return adjList.size();
        }
    
        /* Add edge */
        public void addEdge(Vertex vet1, Vertex vet2) {
            if (!adjList.containsKey(vet1) || !adjList.containsKey(vet2) || vet1 == vet2)
                throw new IllegalArgumentException();
            // Add edge vet1 - vet2
            adjList.get(vet1).add(vet2);
            adjList.get(vet2).add(vet1);
        }
    
        /* Remove edge */
        public void removeEdge(Vertex vet1, Vertex vet2) {
            if (!adjList.containsKey(vet1) || !adjList.containsKey(vet2) || vet1 == vet2)
                throw new IllegalArgumentException();
            // Remove edge vet1 - vet2
            adjList.get(vet1).remove(vet2);
            adjList.get(vet2).remove(vet1);
        }
    
        /* Add vertex */
        public void addVertex(Vertex vet) {
            if (adjList.containsKey(vet))
                return;
            // Add a new linked list in the adjacency list
            adjList.put(vet, new ArrayList<>());
        }
    
        /* Remove vertex */
        public void removeVertex(Vertex vet) {
            if (!adjList.containsKey(vet))
                throw new IllegalArgumentException();
            // Remove the linked list corresponding to vertex vet in the adjacency list
            adjList.remove(vet);
            // Traverse the linked lists of other vertices and remove all edges containing vet
            for (List<Vertex> list : adjList.values()) {
                list.remove(vet);
            }
        }
    
        /* Print adjacency list */
        public void print() {
            System.out.println("Adjacency list =");
            for (Map.Entry<Vertex, List<Vertex>> pair : adjList.entrySet()) {
                List<Integer> tmp = new ArrayList<>();
                for (Vertex vertex : pair.getValue())
                    tmp.add(vertex.val);
                System.out.println(pair.getKey().val + ": " + tmp + ",");
            }
        }
    }
    ```
=== "C#"
    ```csharp title="graph_adjacency_list.cs"
    public class GraphAdjList {
        // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        public Dictionary<Vertex, List<Vertex>> adjList;
    
        /* Constructor */
        public GraphAdjList(Vertex[][] edges) {
            adjList = [];
            // Add all vertices and edges
            foreach (Vertex[] edge in edges) {
                AddVertex(edge[0]);
                AddVertex(edge[1]);
                AddEdge(edge[0], edge[1]);
            }
        }
    
        /* Get the number of vertices */
        int Size() {
            return adjList.Count;
        }
    
        /* Add edge */
        public void AddEdge(Vertex vet1, Vertex vet2) {
            if (!adjList.ContainsKey(vet1) || !adjList.ContainsKey(vet2) || vet1 == vet2)
                throw new InvalidOperationException();
            // Add edge vet1 - vet2
            adjList[vet1].Add(vet2);
            adjList[vet2].Add(vet1);
        }
    
        /* Remove edge */
        public void RemoveEdge(Vertex vet1, Vertex vet2) {
            if (!adjList.ContainsKey(vet1) || !adjList.ContainsKey(vet2) || vet1 == vet2)
                throw new InvalidOperationException();
            // Remove edge vet1 - vet2
            adjList[vet1].Remove(vet2);
            adjList[vet2].Remove(vet1);
        }
    
        /* Add vertex */
        public void AddVertex(Vertex vet) {
            if (adjList.ContainsKey(vet))
                return;
            // Add a new linked list in the adjacency list
            adjList.Add(vet, []);
        }
    
        /* Remove vertex */
        public void RemoveVertex(Vertex vet) {
            if (!adjList.ContainsKey(vet))
                throw new InvalidOperationException();
            // Remove the linked list corresponding to vertex vet in the adjacency list
            adjList.Remove(vet);
            // Traverse the linked lists of other vertices and remove all edges containing vet
            foreach (List<Vertex> list in adjList.Values) {
                list.Remove(vet);
            }
        }
    
        /* Print adjacency list */
        public void Print() {
            Console.WriteLine("Adjacency list =");
            foreach (KeyValuePair<Vertex, List<Vertex>> pair in adjList) {
                List<int> tmp = [];
                foreach (Vertex vertex in pair.Value)
                    tmp.Add(vertex.val);
                Console.WriteLine(pair.Key.val + ": [" + string.Join(", ", tmp) + "],");
            }
        }
    }
    ```
=== "Go"
    ```go title="graph_adjacency_list.go"
    type graphAdjList struct {
    	// Adjacency list, key: vertex, value: all adjacent vertices of that vertex
    	adjList map[Vertex][]Vertex
    }
    ```
=== "Swift"
    ```swift title="graph_adjacency_list.swift"
    public class GraphAdjList {
        // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        public private(set) var adjList: [Vertex: [Vertex]]
    
        /* Constructor */
        public init(edges: [[Vertex]]) {
            adjList = [:]
            // Add all vertices and edges
            for edge in edges {
                addVertex(vet: edge[0])
                addVertex(vet: edge[1])
                addEdge(vet1: edge[0], vet2: edge[1])
            }
        }
    
        /* Get the number of vertices */
        public func size() -> Int {
            adjList.count
        }
    
        /* Add edge */
        public func addEdge(vet1: Vertex, vet2: Vertex) {
            if adjList[vet1] == nil || adjList[vet2] == nil || vet1 == vet2 {
                fatalError("Invalid parameter")
            }
            // Add edge vet1 - vet2
            adjList[vet1]?.append(vet2)
            adjList[vet2]?.append(vet1)
        }
    
        /* Remove edge */
        public func removeEdge(vet1: Vertex, vet2: Vertex) {
            if adjList[vet1] == nil || adjList[vet2] == nil || vet1 == vet2 {
                fatalError("Invalid parameter")
            }
            // Remove edge vet1 - vet2
            adjList[vet1]?.removeAll { $0 == vet2 }
            adjList[vet2]?.removeAll { $0 == vet1 }
        }
    
        /* Add vertex */
        public func addVertex(vet: Vertex) {
            if adjList[vet] != nil {
                return
            }
            // Add a new linked list in the adjacency list
            adjList[vet] = []
        }
    
        /* Remove vertex */
        public func removeVertex(vet: Vertex) {
            if adjList[vet] == nil {
                fatalError("Invalid parameter")
            }
            // Remove the linked list corresponding to vertex vet in the adjacency list
            adjList.removeValue(forKey: vet)
            // Traverse the linked lists of other vertices and remove all edges containing vet
            for key in adjList.keys {
                adjList[key]?.removeAll { $0 == vet }
            }
        }
    
        /* Print adjacency list */
        public func print() {
            Swift.print("Adjacency list =")
            for (vertex, list) in adjList {
                let list = list.map { $0.val }
                Swift.print("\(vertex.val): \(list),")
            }
        }
    }
    ```
=== "JS"
    ```javascript title="graph_adjacency_list.js"
    class GraphAdjList {
        // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        adjList;
    
        /* Constructor */
        constructor(edges) {
            this.adjList = new Map();
            // Add all vertices and edges
            for (const edge of edges) {
                this.addVertex(edge[0]);
                this.addVertex(edge[1]);
                this.addEdge(edge[0], edge[1]);
            }
        }
    
        /* Get the number of vertices */
        size() {
            return this.adjList.size;
        }
    
        /* Add edge */
        addEdge(vet1, vet2) {
            if (
                !this.adjList.has(vet1) ||
                !this.adjList.has(vet2) ||
                vet1 === vet2
            ) {
                throw new Error('Illegal Argument Exception');
            }
            // Add edge vet1 - vet2
            this.adjList.get(vet1).push(vet2);
            this.adjList.get(vet2).push(vet1);
        }
    
        /* Remove edge */
        removeEdge(vet1, vet2) {
            if (
                !this.adjList.has(vet1) ||
                !this.adjList.has(vet2) ||
                vet1 === vet2 ||
                this.adjList.get(vet1).indexOf(vet2) === -1
            ) {
                throw new Error('Illegal Argument Exception');
            }
            // Remove edge vet1 - vet2
            this.adjList.get(vet1).splice(this.adjList.get(vet1).indexOf(vet2), 1);
            this.adjList.get(vet2).splice(this.adjList.get(vet2).indexOf(vet1), 1);
        }
    
        /* Add vertex */
        addVertex(vet) {
            if (this.adjList.has(vet)) return;
            // Add a new linked list in the adjacency list
            this.adjList.set(vet, []);
        }
    
        /* Remove vertex */
        removeVertex(vet) {
            if (!this.adjList.has(vet)) {
                throw new Error('Illegal Argument Exception');
            }
            // Remove the linked list corresponding to vertex vet in the adjacency list
            this.adjList.delete(vet);
            // Traverse the linked lists of other vertices and remove all edges containing vet
            for (const set of this.adjList.values()) {
                const index = set.indexOf(vet);
                if (index > -1) {
                    set.splice(index, 1);
                }
            }
        }
    
        /* Print adjacency list */
        print() {
            console.log('Adjacency list =');
            for (const [key, value] of this.adjList) {
                const tmp = [];
                for (const vertex of value) {
                    tmp.push(vertex.val);
                }
                console.log(key.val + ': ' + tmp.join());
            }
        }
    }
    ```
=== "TS"
    ```typescript title="graph_adjacency_list.ts"
    class GraphAdjList {
        // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        adjList: Map<Vertex, Vertex[]>;
    
        /* Constructor */
        constructor(edges: Vertex[][]) {
            this.adjList = new Map();
            // Add all vertices and edges
            for (const edge of edges) {
                this.addVertex(edge[0]);
                this.addVertex(edge[1]);
                this.addEdge(edge[0], edge[1]);
            }
        }
    
        /* Get the number of vertices */
        size(): number {
            return this.adjList.size;
        }
    
        /* Add edge */
        addEdge(vet1: Vertex, vet2: Vertex): void {
            if (
                !this.adjList.has(vet1) ||
                !this.adjList.has(vet2) ||
                vet1 === vet2
            ) {
                throw new Error('Illegal Argument Exception');
            }
            // Add edge vet1 - vet2
            this.adjList.get(vet1).push(vet2);
            this.adjList.get(vet2).push(vet1);
        }
    
        /* Remove edge */
        removeEdge(vet1: Vertex, vet2: Vertex): void {
            if (
                !this.adjList.has(vet1) ||
                !this.adjList.has(vet2) ||
                vet1 === vet2 ||
                this.adjList.get(vet1).indexOf(vet2) === -1
            ) {
                throw new Error('Illegal Argument Exception');
            }
            // Remove edge vet1 - vet2
            this.adjList.get(vet1).splice(this.adjList.get(vet1).indexOf(vet2), 1);
            this.adjList.get(vet2).splice(this.adjList.get(vet2).indexOf(vet1), 1);
        }
    
        /* Add vertex */
        addVertex(vet: Vertex): void {
            if (this.adjList.has(vet)) return;
            // Add a new linked list in the adjacency list
            this.adjList.set(vet, []);
        }
    
        /* Remove vertex */
        removeVertex(vet: Vertex): void {
            if (!this.adjList.has(vet)) {
                throw new Error('Illegal Argument Exception');
            }
            // Remove the linked list corresponding to vertex vet in the adjacency list
            this.adjList.delete(vet);
            // Traverse the linked lists of other vertices and remove all edges containing vet
            for (const set of this.adjList.values()) {
                const index: number = set.indexOf(vet);
                if (index > -1) {
                    set.splice(index, 1);
                }
            }
        }
    
        /* Print adjacency list */
        print(): void {
            console.log('Adjacency list =');
            for (const [key, value] of this.adjList.entries()) {
                const tmp = [];
                for (const vertex of value) {
                    tmp.push(vertex.val);
                }
                console.log(key.val + ': ' + tmp.join());
            }
        }
    }
    ```
=== "Dart"
    ```dart title="graph_adjacency_list.dart"
    class GraphAdjList {
      // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
      Map<Vertex, List<Vertex>> adjList = {};
    
      /* Constructor */
      GraphAdjList(List<List<Vertex>> edges) {
        for (List<Vertex> edge in edges) {
          addVertex(edge[0]);
          addVertex(edge[1]);
          addEdge(edge[0], edge[1]);
        }
      }
    
      /* Get the number of vertices */
      int size() {
        return adjList.length;
      }
    
      /* Add edge */
      void addEdge(Vertex vet1, Vertex vet2) {
        if (!adjList.containsKey(vet1) ||
            !adjList.containsKey(vet2) ||
            vet1 == vet2) {
          throw ArgumentError;
        }
        // Add edge vet1 - vet2
        adjList[vet1]!.add(vet2);
        adjList[vet2]!.add(vet1);
      }
    
      /* Remove edge */
      void removeEdge(Vertex vet1, Vertex vet2) {
        if (!adjList.containsKey(vet1) ||
            !adjList.containsKey(vet2) ||
            vet1 == vet2) {
          throw ArgumentError;
        }
        // Remove edge vet1 - vet2
        adjList[vet1]!.remove(vet2);
        adjList[vet2]!.remove(vet1);
      }
    
      /* Add vertex */
      void addVertex(Vertex vet) {
        if (adjList.containsKey(vet)) return;
        // Add a new linked list in the adjacency list
        adjList[vet] = [];
      }
    
      /* Remove vertex */
      void removeVertex(Vertex vet) {
        if (!adjList.containsKey(vet)) {
          throw ArgumentError;
        }
        // Remove the linked list corresponding to vertex vet in the adjacency list
        adjList.remove(vet);
        // Traverse the linked lists of other vertices and remove all edges containing vet
        adjList.forEach((key, value) {
          value.remove(vet);
        });
      }
    
      /* Print adjacency list */
      void printAdjList() {
        print("Adjacency list =");
        adjList.forEach((key, value) {
          List<int> tmp = [];
          for (Vertex vertex in value) {
            tmp.add(vertex.val);
          }
          print("${key.val}: $tmp,");
        });
      }
    }
    ```
=== "Rust"
    ```rust title="graph_adjacency_list.rs"
    pub struct GraphAdjList {
        // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        pub adj_list: HashMap<Vertex, Vec<Vertex>>, // maybe HashSet<Vertex> for value part is better?
    }
    ```
=== "C"
    ```c title="graph_adjacency_list.c"
    GraphAdjList *newGraphAdjList() {
        GraphAdjList *graph = (GraphAdjList *)malloc(sizeof(GraphAdjList));
        if (!graph) {
            return NULL;
        }
        graph->size = 0;
        for (int i = 0; i < MAX_SIZE; i++) {
            graph->heads[i] = NULL;
        }
        return graph;
    }
    ```
=== "Kotlin"
    ```kotlin title="graph_adjacency_list.kt"
    class GraphAdjList(edges: Array<Array<Vertex?>>) {
        // Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        val adjList = HashMap<Vertex, MutableList<Vertex>>()
    
        /* Constructor */
        init {
            // Add all vertices and edges
            for (edge in edges) {
                addVertex(edge[0]!!)
                addVertex(edge[1]!!)
                addEdge(edge[0]!!, edge[1]!!)
            }
        }
    
        /* Get the number of vertices */
        fun size(): Int {
            return adjList.size
        }
    
        /* Add edge */
        fun addEdge(vet1: Vertex, vet2: Vertex) {
            if (!adjList.containsKey(vet1) || !adjList.containsKey(vet2) || vet1 == vet2)
                throw IllegalArgumentException()
            // Add edge vet1 - vet2
            adjList[vet1]?.add(vet2)
            adjList[vet2]?.add(vet1)
        }
    
        /* Remove edge */
        fun removeEdge(vet1: Vertex, vet2: Vertex) {
            if (!adjList.containsKey(vet1) || !adjList.containsKey(vet2) || vet1 == vet2)
                throw IllegalArgumentException()
            // Remove edge vet1 - vet2
            adjList[vet1]?.remove(vet2)
            adjList[vet2]?.remove(vet1)
        }
    
        /* Add vertex */
        fun addVertex(vet: Vertex) {
            if (adjList.containsKey(vet))
                return
            // Add a new linked list in the adjacency list
            adjList[vet] = mutableListOf()
        }
    
        /* Remove vertex */
        fun removeVertex(vet: Vertex) {
            if (!adjList.containsKey(vet))
                throw IllegalArgumentException()
            // Remove the linked list corresponding to vertex vet in the adjacency list
            adjList.remove(vet)
            // Traverse the linked lists of other vertices and remove all edges containing vet
            for (list in adjList.values) {
                list.remove(vet)
            }
        }
    
        /* Print adjacency list */
        fun print() {
            println("Adjacency list =")
            for (pair in adjList.entries) {
                val tmp = mutableListOf<Int>()
                for (vertex in pair.value) {
                    tmp.add(vertex._val)
                }
                println("${pair.key._val}: $tmp,")
            }
        }
    }
    ```
=== "Ruby"
    ```ruby title="graph_adjacency_list.rb"
    ### Undirected graph class based on adjacency list ###
    class GraphAdjList
      attr_reader :adj_list
      
      ### Constructor ###
      def initialize(edges)
        # Adjacency list, key: vertex, value: all adjacent vertices of that vertex
        @adj_list = {}
        # Add all vertices and edges
        for edge in edges
          add_vertex(edge[0])
          add_vertex(edge[1])
          add_edge(edge[0], edge[1])
        end
      end
    
      ### Get number of vertices ###
      def size
        @adj_list.length
      end
    
      ### Add edge ###
      def add_edge(vet1, vet2)
        raise ArgumentError if !@adj_list.include?(vet1) || !@adj_list.include?(vet2)
    
        @adj_list[vet1] << vet2
        @adj_list[vet2] << vet1
      end
    
      ### Delete edge ###
      def remove_edge(vet1, vet2)
        raise ArgumentError if !@adj_list.include?(vet1) || !@adj_list.include?(vet2)
    
        # Remove edge vet1 - vet2
        @adj_list[vet1].delete(vet2)
        @adj_list[vet2].delete(vet1)
      end
    
      ### Add vertex ###
      def add_vertex(vet)
        return if @adj_list.include?(vet)
    
        # Add a new linked list in the adjacency list
        @adj_list[vet] = []
      end
    
      ### Delete vertex ###
      def remove_vertex(vet)
        raise ArgumentError unless @adj_list.include?(vet)
    
        # Remove the linked list corresponding to vertex vet in the adjacency list
        @adj_list.delete(vet)
        # Traverse the linked lists of other vertices and remove all edges containing vet
        for vertex in @adj_list
          @adj_list[vertex.first].delete(vet) if @adj_list[vertex.first].include?(vet)
        end
      end
    
      ### Print adjacency list ###
      def __print__
        puts 'Adjacency list ='
        for vertex in @adj_list
          tmp = @adj_list[vertex.first].map { |v| v.val }
          puts "#{vertex.first.val}: #{tmp},"
        end
      end
    ```


## So sánh hiệu quả

Giả sử đồ thị có $n$ đỉnh và $m$ cạnh, bảng dưới đây so sánh hiệu quả về thời gian và hiệu quả về không gian của ma trận kề và danh sách kề. Lưu ý rằng danh sách kề (danh sách liên kết) tương ứng với cách triển khai được sử dụng trong phần này, trong khi danh sách kề (bảng băm) đề cập cụ thể đến cách triển khai trong đó tất cả các danh sách liên kết được thay thế bằng bảng băm.

<p align="center"> Table <id> &nbsp; Comparison of adjacency matrix and adjacency list </p>

|                        | Ma trận kề | Danh sách kề (danh sách liên kết) | Danh sách kề (bảng băm) |
| ---------------------- | ---------------- | ---------------------------- | ----------------------------- |
| Xác định lân cận | $O(1)$ | $O(n)$ | $O(1)$ |
| Thêm một cạnh | $O(1)$ | $O(1)$ | $O(1)$ |
| Xóa một cạnh | $O(1)$ | $O(n)$ | $O(1)$ |
| Thêm một đỉnh | $O(n)$ | $O(1)$ | $O(1)$ |
| Xóa một đỉnh | $O(n^2)$ | $O(n + m)$ | $O(n)$ |
| Sử dụng không gian bộ nhớ | $O(n^2)$ | $O(n + m)$ | $O(n + m)$ |

Quan sát bảng trên, có vẻ như danh sách kề (bảng băm) có hiệu quả về thời gian và không gian tốt nhất. Tuy nhiên, trong thực tế, thao tác trên các cạnh trong ma trận kề sẽ hiệu quả hơn, chỉ yêu cầu một thao tác truy cập hoặc gán mảng duy nhất. Nhìn chung, ma trận kề thể hiện nguyên tắc "đánh đổi không gian lấy thời gian", trong khi danh sách kề thể hiện "đánh đổi thời gian lấy không gian".
