class GTreeNode:
    def __init__(self):
        self.__value = None
        self.__children = []
    
    def getValue(self):
        return self.__value
    
    def setValue(self, value):
        self.__value = value

    def getChildren(self):
        return self.__children
    
    def addChild(self, child):
        self.__children.append(child)

    def execute(self, number):
        accumulator = self.__value(number)
        for child in self.__children:
            accumulator = child.execute(accumulator)
        return accumulator
    
    def __str__(self):
        return f'{self.__value}, {self.__children}'


class GTree:
    def __init__(self):
        self.__root = None

    def getRoot(self):
        return self.__root
    
    def setRoot(self, root):
        self.__root = root

    def insert(self, value, *levels):
        current = self.__root
        for i in range(len(levels)):
            children = current.getChildren()
            current = children[levels[i] - 1]
        node = GTreeNode()
        node.setValue(value)
        current.addChild(node)

    def execute(self, number):
        return self.__root.execute(number)
       
    def __getSubtree(self, childInd):
        root = self.__root.getChildren()[childInd]
        tree = GTree()
        tree.setRoot(root)
        return tree


if __name__ == '__main__':

    # Testing insert()

    # n1 = GTreeNode()
    # n1.setValue(1)
    # n2 = GTreeNode()
    # n2.setValue(2)
    # n3 = GTreeNode()
    # n3.setValue(3)
    # n4 = GTreeNode()
    # n4.setValue(4)
    # n5 = GTreeNode()
    # n5.setValue(5)
    # n6 = GTreeNode()
    # n6.setValue(6)

    # n1.addChild(n2)
    # n1.addChild(n3)
    # n2.addChild(n4)
    # n2.addChild(n5)

    # t = GTree()
    # t.setRoot(n1)

    # t.insert(6, 2)
    # t.insert(8, 2, 1)
    # t.insert(7)
    # print(n1.getChildren())

    # Testing execute()

    f1 = lambda x: x * x
    f2 = lambda x: x / 10
    f3 = lambda x: 1 - x
    f4 = lambda x: x

    n1 = GTreeNode()
    n1.setValue(f1)
    n2 = GTreeNode()
    n2.setValue(f2)
    n1.addChild(n2)
    
    t = GTree()
    t.setRoot(n1)
    t.insert(f3, 1)
    t.insert(f4)

    print(t.execute(13))
