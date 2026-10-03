class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, num):
        current = self

        while True:
            if num < current.val:
                if current.left is None:
                    current.left = BST(num)
                    return

                current = current.left

            elif num > current.val:
                if current.right is None:
                    current.right = BST(num)
                    return

                current = current.right

            else:
                return

    def search(self, num):
        current = self

        while current is not None:
            if current.val == num:
                return current

            if num < current.val:
                current = current.left
            else:
                current = current.right

        return None