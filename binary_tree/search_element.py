
from collections import deque
import sys
sys.path.append(".")

from tree.tree import Tree
from collections import deque


class BinaryTree(Tree):
    def search_element_recursive(self, root, element):
        if not root:
            return False
        if root.data == element:
            return True
        if self.search_element_recursive(root.left, element) == True:
            return True
        else:
            return self.search_element_recursive(root.right, element)

    def search_element_iterative(self, root, element):
        if not root:
            return -1
        stack = deque()
        stack.append(root)
        while stack:
            temp = stack.pop()
            if temp.data == element:
                return True
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        return False


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7]
    bt = BinaryTree(nodes=nodes)
    print(bt.search_element_recursive(bt.root, 90))
    print(bt.search_element_iterative(bt.root, 7))
