import sys
sys.path.append(".")

from tree.tree import Tree


class BinaryTree(Tree):
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


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6]
    bt = BinaryTree(nodes=nodes)
    print(bt.height(bt.root))
    print(bt.size(bt.root))
