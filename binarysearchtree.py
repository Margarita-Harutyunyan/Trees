class BinaryNode:
    def __init__(self):
        self.__item = None
        self.__left = None
        self.__right = None
    
    def setItem(self, item) -> None:
        self.__item = item

    def getItem(self):
        return self.__item
    
    def setLeft(self, item) -> None:
        self.__left = item
    
    def getLeft(self):
        return self.__left
    
    def setRight(self, item) -> None:
        self.__right = item

    def getRight(self):
        return self.__right
    
    def isLeaf(self) -> bool:
        return not(self.__left) and not(self.__right)
    

class BinarySearchTree:
    def __init__(self) -> None:
        self.__root = None
    
    # Public methods

    def isEmpty(self) -> bool:
        return self.__root is None

    def getHeight(self) -> int:
        return self._getHeightHelper(self.__root)

    def getNumberOfNodes(self) -> int:
        return self._getNumberOdNodesHelper(self.__root)

    def getRootData(self) -> BinaryNode:
        return self.__root
    
    def add(self, newEntry):
        node = BinaryNode()
        node.setItem(newEntry)
        self.__root = self._insertInorder(self.__root, node)
    
    def remove(self, anEntry):
        node = BinaryNode()
        node.setItem(anEntry)
        self.__root = self._removeHelper(self.__root, node)

    def clear(self) -> None:
        self.__root = None

    def contains(self, data) -> bool:
        return self._contains(self.getRoot(), data)

    def preorderTraverse(self, visit) -> None:
        return self._preorder(self.__root, visit)

    def inorderTraverse(self, visit) -> None:
        return self._inorder(self.__root, visit)

    def postorderTraverse(self, visit) -> None:
        return self._postorderTraverse(self.__root, visit)

    # Protected helper methods

    def _getHeightHelper(self, node) -> int:
        if node is None:
            return 0
        
        leftHeight = self._getHeightHelper(node.getLeft())
        rightHeight = self._getHeightHelper(node.getRight())

        return max(leftHeight, rightHeight)

    def _getNumberOdNodesHelper(self, node) -> int:
        if node is None:
            return 0
        else:
            leftNodes = self._getNumberOdNodesHelper(node.getLeft())
            rightNodes = self._getNumberOdNodesHelper(node.getRight())
            return leftNodes + rightNodes + 1

    def _preorder(self, root, visit) -> None:
        if root is not None:
            visit(root.getItem())
            self._preorderTraverse(root.getLeft())
            self._preorderTraverse(root.getRight())

    def _inorder(self, root, visit) -> None:
        if root is not None:
            self._inorder(root.getLeft())
            visit(root.getItem())
            self._inorder(root.getRight())

    def _postorder(self, root, visit) -> None:
        if root is not None:
            self._postorder(root.getLeft())
            self._postorder(root.getRight())
            visit(root.getItem())
        
    def _insertInorder(self, node : BinaryNode, newNode : BinaryNode) -> BinaryNode:
        if node is None:
            return newNode
        elif newNode.getItem() < node.getItem():
            node.setLeft(self._insertInorder(node.getLeft(), newNode))
        else:
            node.setRight(self._insertInorder(node.getRight(), newNode))
        return node  

    def _removeHelper(self, root : BinaryNode, node : BinaryNode):
        if root is None:
            return root
        if node < root.getItem():
            root.setLeft(self._removeHelper(root.getLeft(), node))
        elif node.getItem() > root.getItem():
            root.setRight(self._removeHelper(root.getRight(), node))
        else:
            if root.getLeft() is None:
                return root.getRight()
            elif root.getRight() is None:
                return root.getLeft()
            else:
                minValue = self._findMinValue(root.getRight())
                root.setItem(minValue)
                root.setRight(self._removeHelper(root.getRight(), minValue))
        return root

    def _findMinValue(self, node):
        while node.getLeft() is not None:
            node = node.getLeft()
        return node.getItem()

    def _contains(self, node, data):
        if node is None:
            return False
        elif data == node.getItem():
            return True
        elif data < node.getItem():
            return self._contains(node.getLeft(), data)
        else:
            return self._contains(node.getRight(), data)
