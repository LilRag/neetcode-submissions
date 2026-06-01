class MyHashMap:

    def __init__(self):
        # Choose a size (preferably a prime number to reduce collisions)
        self.size = 1000 
        self.hash_table = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.size
        bucket = self.hash_table[hash_key]

        # Check if key exists to update it
        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, value)
                return
        
        # If key doesn't exist, append new pair
        bucket.append((key, value))

    def get(self, key: int) -> int:
        hash_key = key % self.size
        bucket = self.hash_table[hash_key]

        for record_key, record_value in bucket:
            if record_key == key:
                return record_value
        
        # Standard return for "not found" in integer hashmaps is often -1
        return -1 

    def remove(self, key: int) -> None:
        hash_key = key % self.size
        bucket = self.hash_table[hash_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                del bucket[index]
                return