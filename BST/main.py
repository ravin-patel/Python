
# initilize node class


class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class binary_search_tree:
    def __init__(self):
        self.root = None

# NODE INSERTION
    def insert(self, value):
        # check if root is empty, if so add the value as the root node using the Node class
        if self.root == None:
            self.root = node(value)
        else:
            # private recursive insert function represented by the _
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        # check if the past value is less than the current node
        if value < current_node.value:
            # If the current node doesnt have a left child (lesser node),create a new node and insert the value
            if current_node.left_child == None:
                current_node.left_child = node(value)
            else:
                self._insert(value, current_node.left_child)  # recursive call

        elif value > current_node.value:
             # If the current node doesnt have a right child (lesser node),create a new node and insert the value
            if current_node.right_child == None:
                current_node.right_child = node(value)
            else:
                # call private recrusive function
                self._insert(value, current_node.right_child)
        else:
            # if the value = curr node
            print("value is already in the tree!")
# TREE HEIGHT

    def height(self):
        if self.root != None:
            # call private recrusive function
            return self._height(self.root, 0)
        else:
            return 0  # if root is none then tree height is 0

    def _height(self, current_node, current_height):
        # if node is none dont increment
        if current_node == None:
            return current_height
        # get height from left and right subtree
        left_subtree_height = self._height(
            current_node.left_child, current_height+1)
        right_subtree_height = self._height(
            current_node.right_child, current_height+1)
        # whichever subtree is higher, is the height of the tree
        return max(left_subtree_height, right_subtree_height)

# TREE PRINT
     def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)  # call private recrusive function

    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self._print_tree(current_node.right_child)

# fill trees with random number_of_elements with values upto max_int
def fill_tree(tree, number_of_elements=100, max_int=1000):
    from random import randint
    for _ in range(number_of_elements):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree

tree = binary_search_tree()
tree = fill_tree(tree)
tree.print_tree()
print("Tree height: " + str(tree.height()))
