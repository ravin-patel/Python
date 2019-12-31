
# initilize node class


class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # pointer to parent node in the tree


class binary_search_tree:
    def __init__(self):
        self.root = None

# NODE INSERTION

    def insert(self, value):
        # check if root is empty, if so add the value as the root node using the Node class
        if self.root == None:
            self.root = node(value)
        else:
            # private recursive insert function   by the _
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        # check if the past value is less than the current node
        if value < current_node.value:
            # If the current node doesnt have a left child (lesser node),create a new node and insert the value
            if current_node.left_child == None:
                current_node.left_child = node(value)
                current_node.parent = current_node  # setting parent node
            else:
                self._insert(value, current_node.left_child)  # recursive call

        elif value > current_node.value:
             # If the current node doesnt have a right child (lesser node),create a new node and insert the value
            if current_node.right_child == None:
                current_node.right_child = node(value)
                current_node.parent = current_node
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

# TREE SEARCH
    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            print("Found value: " + str(current_node.value))
            return True
        # recursively search the left subtree
        elif value < current_node.value and current_node.left_child != None:
            return self._search(value, current_node.left_child)

        # recursively search the right subtree
        elif value > current_node.value and current_node.right_child != None:
            return self._search(value, current_node.right_child)
        else:
            print("Value {} is not in the tree" .format(str(value)))
            return False

    # similar to search but this will return the node instead of boolean
    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child != None:
            return self._find(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child != None:
            return self._find(value, current_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        # returns the node with the min value in tree, with input node as root
        def min_value_node(n):
            current_node = n
            while current_node.left_child != None:
                current_node = current_node.left_child
            return current_node

        # return the # of childern nodes
        def number_of_childern(n):
            number_of_childern = 0
            if n.left_child != None:
                number_of_childern += 1
            if n.right_child != None:
                number_of_childern += 1
            return number_of_childern

        parent_node = node.parent  # get parent of node to be deleted
        childern_nodes = number_of_childern(node)  # get number of childern

        # break operations into different deletion cases based on
        # tree structure and the node to be deleted
        # 1: node has no children. Remove referenece to the node from parrent

        if childern_nodes == 0:
            print("Case 1:")
            if parent_node != None:
                if parent_node.left_child == node:
                    print("setting parent nodes LC to none")
                    parent_node.left_child == None
                else:
                    print("setting parent nodes RC to none")
                    parent_node.right_child == None
            else:
                self.root = None
        # 2: node has 1 child
        if childern_nodes == 1:
            # get the child node
            print("Case 2:")
            if node.left_child != None:
                print("creating child var with passed in nodes LC ")
                child = node.left_child
            else:
                print("creating child var with passed in nodes RC ")
                child = node.right_child

            # replace the node to be deleted with its child
            if parent_node.left_child == node:
                print("replacing parents LC to the child var node")
                parent_node.left_child == child
            else:
                print("replacing parents RC to the child var node")
                parent_node.right_child = child

            # update child nodes parent reference
            print("setting childs parent reference to parent node")
            child.parent = parent_node

        if childern_nodes == 2:
            # get inorder successor node
            print("Case 3: getting inorder successor node")
            successor_node = min_value_node(node.right_child)
            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            print("setting %s (node value) to %s (successor value)" %
                  (str(node.value), str(successor_node.value)))
            node.value = successor_node.value

            # delete the successor since the value was copied
            print("deleting successor node since the value has been copied")
            self.delete_node(successor_node)

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
def fill_tree(tree, number_of_elements=12, max_int=20):
    from random import randint
    for _ in range(number_of_elements):
        current_element = randint(0, max_int)
        tree.insert(current_element)
    return tree


tree = binary_search_tree()
tree = fill_tree(tree)
tree.print_tree()

if tree.search(3) == True:
    print("deleting 3")
    tree.delete_value(3)

tree.print_tree()
print("Tree height: " + str(tree.height()))
