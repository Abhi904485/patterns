import sys
sys.path.append(".")

from tree.tree import Tree


class BinaryTree(Tree):

    def height(self, root):
        depth = 0
        q = []
        q.append(root)
        q.append(None)
        while (len(q) > 0):
            temp = q[0]
            q = q[1:]
            if (temp == None):
                depth += 1
            if (temp != None):
                if (temp.left):
                    q.append(temp.left)
                if (temp.right):
                    q.append(temp.right)
            elif (len(q) > 0):
                q.append(None)
        return depth

    def size(self, node):
        q = []
        q.append(node)
        temp = q[0]
        temp1 = q[0]
        while temp and temp.left:
            q.append(temp.left)
            temp = temp.left
        temp = temp1
        while temp and temp.right:
            q.append(temp.right)
            temp = temp.right
        return len(q)


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6]
    bt = BinaryTree(nodes=nodes)
    print(bt.height(bt.root))
    print(bt.size(bt.root))
