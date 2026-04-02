class TreeMap:
    
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key: int, val: int) -> None:
        if self.key is None:          # ADD: empty tree case
            self.key = key
            self.val = val
            return
        curr = self
        parent = None
        while curr:
            parent = curr
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            elif curr.key == key:
                curr.val = val
                return              # ADD: return after update
                                # REMOVE: the else block entirely
        new_node = TreeMap(key, val)
        if parent.key > key:
            parent.left = new_node
        else:
            parent.right = new_node


    def get(self, key: int) -> int:
        curr = self
        while curr and curr.key is not None:
            if curr.key == key:
                return curr.val
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right
        return -1


    def getMin(self) -> int:
        if self.key is None:
            return -1
        curr = self
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if self.key is None:
            return -1
        curr = self
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        curr = self
        parent = None

        while curr and curr.key is not None:
            if curr.key == key:
                break
            parent = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        if not curr or curr.key is None:
            return

        if curr.left and curr.right:
            suc_parent = curr
            suc = curr.right
            while suc.left:
                suc_parent = suc
                suc = suc.left
            curr.key = suc.key
            curr.val = suc.val
            curr = suc
            parent = suc_parent
        child = curr.left if curr.left else curr.right
        if parent is None:
            if child:
                curr.key = child.key
                curr.val = child.val
                curr.left = child.left
                curr.right = child.right
            else:
                curr.key = None
                curr.val = None
        elif parent.left == curr:
            parent.left = child
        else:
            parent.right = child

    def getInorderKeys(self) -> List[int]:
        result = []
        self._inorder(self, result)
        return result
    def _inorder(self, node, result):
        if not node or node.key is None:
            return
        self._inorder(node.left, result)
        result.append(node.key)
        self._inorder(node.right, result)

