# DAY 2 TASK

class SimpleHashMap:
    def __init__(self, n=10):
        # Step 1: Initialise an array of N empty lists (buckets).
        self.bucketArray = [[] for _ in range(n)]

    def generateHash(self, key):
        # Step 2: Hash Function converting a string to an integer index.
        # It sums the ASCII values of each character and uses modulo N to ensure it fits in the array.
        return sum(ord(char) for char in key) % len(self.bucketArray)

    def putItem(self, key, value):
        # Step 3: Insert item.
        targetIndex = self.generateHash(key)
        targetBucket = self.bucketArray[targetIndex]
        
        # If the key already exists, update its value.
        for index, (existingKey, existingValue) in enumerate(targetBucket):
            if existingKey == key:
                targetBucket[index] = (key, value)
                return
                
        # Handle collisions by appending to the bucket list (chaining)[cite: 2].
        targetBucket.append((key, value))

    def getItem(self, key):
        # Step 3: Get item[cite: 2].
        targetIndex = self.generateHash(key)
        targetBucket = self.bucketArray[targetIndex]
        
        # Search through the specific bucket's list in case of chained collisions.
        for existingKey, existingValue in targetBucket:
            if existingKey == key:
                return existingValue
        return None

# Step 4: Observe Collisions[cite: 2].
if __name__ == "__main__":
    myMap = SimpleHashMap()
    
    # Inserting normal keys
    myMap.putItem("Bet9ja", "Shop 1")
    myMap.putItem("Nordics", "Table Water")
    
    # Deliberately inserting keys that collide (Anagrams have the same ASCII sum)[cite: 2].
    myMap.putItem("ACT", "First Collision Item")
    myMap.putItem("CAT", "Second Collision Item")
    
    # Print the raw internal bucket array to observe the chaining[cite: 2].
    for i, bucket in enumerate(myMap.bucketArray):
        if bucket:
            print(f"Bucket {i}: {bucket}")