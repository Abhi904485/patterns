import queue
import sys
sys.path.append(".")

from tree.tree import Tree
from collections import deque


class BinaryTree(Tree):
    queue = deque()

    def size(self, root):
        if not root:
            return 0
        left_size = self.size(root.left)
        right_size = self.size(root.right)
        return left_size + right_size + 1

    def height(self, root):
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1

    def recursive_preorder(self, root, result):
        if root:
            result.append(root.data)
            self.recursive_preorder(root.left, result)
            self.recursive_preorder(root.right, result)
        return result

    def iterative_preorder(self, node, result):
        stack = deque()
        if not node:
            return
        if node:
            stack.appendleft(node)
        while stack:
            temp = stack.pop()
            result.append(temp.data)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return result

    def recursive_inorder(self, root, result):
        if root:
            self.recursive_inorder(root.left, result)
            result.append(root.data)
            self.recursive_inorder(root.right, result)
        return result

    def iterative_inorder(self, root, result):
        stack = deque()
        if not root:
            return
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.data)
                root = root.right
        return result

    def recursive_postorder(self, root, result):
        if root:
            self.recursive_postorder(root.left, result)
            self.recursive_postorder(root.right, result)
            result.append(root.data)

        return result

    def iterative_postorder(self, root, result):
        stack = deque()
        visited = []
        if not root:
            return
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.right and root.right.data not in visited:
                    stack.append(root)
                    root = root.right
                else:
                    result.append(root.data)
                    visited.append(root.data)
                    root = None
        return result

    def iterative_levelorder(self, root, result):
        if not root:
            return
        if root:
            self.queue.append(root)
        while len(self.queue) > 0:
            node = self.queue.popleft()
            result.append(node.data)
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)

        return result

    def print_current_level(self, node, level, result):
        if not node:
            return
        if level == 0:
            return result.append(node.data)
        else:
            self.print_current_level(node.left, level - 1, result)
            self.print_current_level(node.right, level - 1, result)
        return result

    def recursive_levelorder(self, root, result):
        result1 = []
        if not root:
            return
        tree_height = self.height(root)
        for i in range(tree_height):
            result1 = self.print_current_level(root, i, result)
        return result1


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7]
    bt = BinaryTree(nodes=nodes)
    print("Recursive Preorder {}".format(
        bt.recursive_preorder(bt.root, result=[])))
    print("Iterative Preorder {}".format(
        bt.iterative_preorder(bt.root, result=[])))
    print("Recursive Inorder  {}".format(
        bt.recursive_inorder(bt.root, result=[])))
    print("Iterative Inorder {}".format(
        bt.iterative_inorder(bt.root, result=[])))
    print("Recursive Postorder {}".format(
        bt.recursive_postorder(bt.root, result=[])))
    print("Iterative Postorder {}".format(
        bt.iterative_postorder(bt.root, result=[])))
    print("Iterative Levelorder {}".format(
        bt.iterative_levelorder(bt.root, result=[])))
    print("Recursive Levelorder {}".format(
        bt.recursive_levelorder(bt.root, result=[])))
