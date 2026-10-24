# DAY 1 PRACTICAL TASK

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.rootNode = None

    def insertValue(self, value):
        if self.rootNode is None:
            self.rootNode = Node(value)
        else:
            self._insertRecursive(self.rootNode, value)

    def _insertRecursive(self, currentNode, value):
        if value < currentNode.value:
            if currentNode.left is None:
                currentNode.left = Node(value)
            else:
                self._insertRecursive(currentNode.left, value)
        elif value > currentNode.value:
            if currentNode.right is None:
                currentNode.right = Node(value)
            else:
                self._insertRecursive(currentNode.right, value)
    def searchValue(self, value):
        return self._searchRecursive(self.rootNode, value)

    def _searchRecursive(self, currentNode, value):
        if currentNode is None:
            return False
        if currentNode.value == value:
            return True
        if value < currentNode.value:
            return self._searchRecursive(currentNode.left, value)
        return self._searchRecursive(currentNode.right, value)

    def inOrderTraversal(self):
        self._inOrderRecursive(self.rootNode)
        print()

    def _inOrderRecursive(self, currentNode):
        if currentNode is not None:
            self._inOrderRecursive(currentNode.left)
            print(currentNode.value, end=" ")
            self._inOrderRecursive(currentNode.right)



# To see the Code OutPuts

if __name__ == "__main__":

    # 1. Create a new empty filing system
    myTree = binarySearchTree()

    # 2. Insert Out-of-order receipt numbers
    print("Inserting receipts: 60, 35, 85, 20, 40... ")
    myTree.insertValue(60)
    myTree.insertValue(35)
    myTree.insertValue(85)
    myTree.insertValue(20)
    myTree.insertValue(40)

    # 3. Print the numbers (This will automatically print them sorted!)
    print("\nPrinting In-Order Traversal:")
    myTree.inOrderTraversal()

    # 4. Search for specific records
    print("\nDid we file receipt #35?")
    print(myTree.searchValue(35))

    print("Did we file receipt #99?")
    print(myTree.searchValue(99)) # This will print False