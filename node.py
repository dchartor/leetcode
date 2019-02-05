class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data:
            if self.data < data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data > data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

def preorder(root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = [root]
        output = []

        while stack:
            root = stack.pop()
            output.append(root.data)
            stack.extend(root.children[::-1])
        return output

print(preorder(root))
