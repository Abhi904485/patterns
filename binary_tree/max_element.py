import sys
sys.path.append(".")

from tree.tree import Tree
from collections import deque


class BinaryTree(Tree):
    MAX_ELEMENT = -sys.maxsize

    def max_element_with_recursion(self, root):
        if not root:
            return self.MAX_ELEMENT
        if root.data > self.MAX_ELEMENT:
            self.MAX_ELEMENT = root.data
        self.max_element_with_recursion(root.left)
        self.max_element_with_recursion(root.right)
        return self.MAX_ELEMENT

    def max_element_without_recursion(self, root):
        MAX_ELEMENT = -sys.maxsize
        if not root:
            return MAX_ELEMENT
        stack = deque()
        stack.append(root)
        while stack:
            temp = stack.pop()
            if temp.data > MAX_ELEMENT:
                MAX_ELEMENT = root.data
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return self.MAX_ELEMENT


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7]
    bt = BinaryTree(nodes=nodes)
    print(bt.max_element_with_recursion(bt.root))
    print(bt.max_element_without_recursion(bt.root))
