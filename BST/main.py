
class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # check if root is empty, if so add the value as the root node using the Node class
        if self.root == None:
            self.root = node(value)
        else:  # private insert function represented by the _
            self._insert(value, self.root)

    def _insert(self, value, current_node):  # recursive insert function
        # check is the past value is less than the current node
        if value < current_node.value:  # break this case into 2 more cases
            # Case1 : current node doesnt have a left child (lesser node),
            # if so create a new node and insert the value
            if current_node.left_child == None:
                current_node.left_child = node(value)
            else:
                self._insert(value, current_node.left_child)  # recursive call
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = node(value)
            else:
                self._insert(value, current_node.right_child)
        else:
            # value = curr node
            print("value is already in the tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left_child)
            print(str(current_node.value))
            self._print_tree(current_node.right_child)


def fill_tree(tree, num_elements=10, max_int=1000):
    from random import randint
    for _ in range(num_elements):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree


tree = binary_search_tree()
tree = fill_tree(tree)

tree.print_tree()
