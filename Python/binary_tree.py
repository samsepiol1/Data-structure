class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
    
    def insert_right_child(self, value):

        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    #Implementation of DFS Pre Order Algorithm

    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()
    
    # Implementation of DFS In Order Algotrithm

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        
        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        
        if self.right_child:
            self.right_child.post_order()
        
        print(self.value)
    

    # Implementation of BFS In Order Alghorithm

    def bfs(self):

        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)
        
        if current_node.left_child:
             queue.put(current_node.left_child)
             
        if current_node.right_child:
            queue.put(current_node.right_child)
