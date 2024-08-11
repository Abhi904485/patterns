from typing import List


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, nodes: List) -> None:
        self.root = None
        self.nodes_list = [Node(data=n)for n in nodes]
        for node in self.nodes_list:
            if not self.root:
                self.root = node
            elif not self.root.left:
                self.root.left = node  # type: ignore
            elif not self.root.right:
                self.root.right = node  # type: ignore
            elif not self.root.left.left:
                self.root.left.left = node  # type: ignore
            elif not self.root.left.right:
                self.root.left.right = node  # type: ignore
            elif not self.root.right.left:
                self.root.right.left = node  # type: ignore
            elif not self.root.right.right:
                self.root.right.right = node  # type: ignore