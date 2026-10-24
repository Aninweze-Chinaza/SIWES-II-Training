# 1. The Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 2. Insertion Function
    def insertNode(self, data):
        newNode = Node(data)
        
        # If the list is empty, make this the first node (the Head)
        if self.head is None:
            self.head = newNode
            return
            
        # Otherwise, walk to the end of the chain and attach it
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
            
        currentNode.next = newNode

    # 3. Traversal Function
    def traverseList(self):
        elements = []
        currentNode = self.head
        
        while currentNode is not None:
            elements.append(str(currentNode.data))
            currentNode = currentNode.next
            
        # Join them with an arrow to visualize the pointers
        print(" -> ".join(elements) + " -> None")

    # 4. Deletion Function
    def deleteNode(self, key):
        currentNode = self.head

        # Case A: If the node we want to delete is the very first one (Head)
        if currentNode is not None and currentNode.data == key:
            self.head = currentNode.next # Just move the Head pointer to the second node
            currentNode = None
            return

        # Case B: If the node is somewhere in the middle or end
        previousNode = None
        while currentNode is not None and currentNode.data != key:
            previousNode = currentNode
            currentNode = currentNode.next

        # If we reached the end and didn't find the key
        if currentNode is None:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node from the chain by skipping it
        previousNode.next = currentNode.next
        currentNode = None


# 5. Test Cases
if __name__ == "__main__":
    myList = SinglyLinkedList()
    
    print("--- Testing Insertion ---")
    myList.insertNode(5)
    myList.insertNode(10)
    myList.insertNode(15)
    myList.insertNode(20)
    myList.traverseList()  # Expected: 5 -> 10 -> 15 -> 20 -> None
    
    print("\n--- Testing Deletion (Middle Node) ---")
    myList.deleteNode(15)
    myList.traverseList()  # Expected: 5 -> 10 -> 20 -> None
    
    print("\n--- Testing Deletion (Head Node) ---")
    myList.deleteNode(5)
    myList.traverseList()  # Expected: 10 -> 20 -> None
    
    print("\n--- Testing Edge Case (Value Not Found) ---")
    myList.deleteNode(80)  # Expected: "Value 80 not found..."