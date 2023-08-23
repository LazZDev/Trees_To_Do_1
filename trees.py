class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Method to add a new value to the Binary Search Tree
    def add(self, value):
        if self.root:
            runner = self.root
            while runner:
                if value > runner.value:
                    if runner.right:
                        runner = runner.right
                    else:
                        runner.right = Node(
                            value
                        )  # Create a new node on the right if no node exists
                        return self
                else:
                    if runner.left:
                        runner = runner.left
                    else:
                        runner.left = Node(
                            value
                        )  # Create a new node on the left if no node exists
                        return self
        self.root = Node(value)  # If the tree is empty, set the new value as the root
        return self

    # Method to check if a given value exists in the Binary Search Tree
    def contains(self, value):
        runner = self.root
        while runner:
            if value == runner.value:
                return True  # Value found
            if value < runner.value:
                if not runner.left:
                    return False  # Value not found since there's no more left to search
                runner = runner.left  # Move to the left child
            else:
                if not runner.right:
                    return (
                        False  # Value not found since there's no more right to search
                    )
                runner = runner.right  # Move to the right child
        return False

    # Method to find the minimum value in the Binary Search Tree
    def min(self):
        runner = self.root
        min_value = self.root.value
        while runner.left:
            if runner.left.value < min_value:
                min_value = (
                    runner.left.value
                )  # Update the minimum value if a smaller value is found
            runner = runner.left  # Move to the left child
        return min_value

    # Method to find the maximum value in the Binary Search Tree
    def max(self):
        runner = self.root
        max_value = self.root.value
        while runner.right:
            if runner.right.value > max_value:
                max_value = (
                    runner.right.value
                )  # Update the maximum value if a larger value is found
            runner = runner.right  # Move to the right child
        return max_value

    # Method to calculate the size (number of nodes) of the Binary Search Tree
    def size(self):
        if self.root == None:
            return 0

        # Helper function to calculate size recursively
        def sizeHelp(runner):
            if not runner:
                return 0
            return 1 + sizeHelp(runner.left) + sizeHelp(runner.right)

        return sizeHelp(self.root)

    # Method to check if the Binary Search Tree is empty
    def isEmpty(self):
        if self.root:
            return False  # Tree is not empty
        return True  # Tree is empty
