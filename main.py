class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    '''
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    '''

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    letters = ["I", "R", "I", "S", "H", "A", "P", "A", "N", "I", "Z", "A"]
    letters_tree = build_tree(letters)
    print("Building the tree:")
    print("In order traversal:", letters_tree.in_order_traversal())
    print("Pre order traversal:", letters_tree.pre_order_traversal())
    print("Post order traversal:", letters_tree.post_order_traversal(), '\n')

    print("Min, Max, and Sum Functions:")
    print("Min:", letters_tree.find_min())
    print("Max:", letters_tree.find_max())
    #print("Sum:", letters_tree.calculate_sum(), '\n')

    print("Searching for letters:")
    print('Is letter "z" on the tree?', letters_tree.search("z"))
    print('Is letter "H" on the tree?', letters_tree.search("H"), '\n')


    print("Deletion Examples:")
    letters_tree = build_tree(letters)
    letters_tree.delete("S")
    print('After deleting "S"', letters_tree.in_order_traversal())

    letters_tree = build_tree(letters)
    letters_tree.delete("H")
    print('After deleting "H"', letters_tree.in_order_traversal())

    letters_tree = build_tree(letters)
    letters_tree.delete("j")
    print('After deleting "j"', letters_tree.in_order_traversal())