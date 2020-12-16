# Course: CS261 - Data Structures
# Assignment: 5
# Student: Amin Malik
# Description: This is an implementation of a hash map within Python


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        This method clears the content of the hash map. It does not change underlying hash table
        capacity.
        """
        # Clear the content of the hash map
        self.buckets = DynamicArray()
        # Maintain the same capacity for the hash map by replacing each index with an empty bucket
        for _ in range(self.capacity):
            self.buckets.append(LinkedList())
        # Reset the size of the hash map to 0
        self.size = 0

    def get(self, key: str) -> object:
        """
        This method returns the value associated with the given key. If the key is not in the hash
        map, the method returns None.
        """
        # Calculate the hash_key and resulting index
        hash_key = self.hash_function(key)
        index = hash_key % self.capacity

        buckets = self.buckets

        # Find the correct bucket to search for the key in
        bucket = (buckets.get_at_index(index))
        if bucket.contains(key):
            for i in bucket:
                # Find the given key in the bucket and return its value
                if i.key == key:
                    return i.value
        else:
            # If the key is not in the hash map, return None
            return None

    def put(self, key: str, value: object) -> None:
        """
        This method updates the key / value pair in the hash map. If a given key already exists in
        the hash map, its associated value should be replaced with the new value. If a given key is
        not in the hash map, a key / value pair should be added.
        """
        # Calculate the hash_key and resulting index
        hash_key = self.hash_function(key)
        index = hash_key % self.capacity

        buckets = self.buckets

        # Find the correct bucket
        bucket = (buckets.get_at_index(index))

        if bucket.contains(key):
            # If the given key already exists, find the key and update the associated value
            for node in bucket:
                if node.key == key:
                    node.value = value
        else:
            # If the given key does not already exist, insert the new key value pair in the bucket and increase the
            # hash map size by 1
            bucket.insert(key, value)
            self.size += 1

    def remove(self, key: str) -> None:
        """
        This method removes the given key and its associated value from the hash map. If a given
        key is not in the hash map, the method does nothing (no exception needs to be raised).
        """
        # Calculate the correct position to look for the key in
        hash_key = self.hash_function(key)
        index = hash_key % self.capacity

        buckets = self.buckets
        # Access the correct bucket to remove the key from
        bucket = (buckets.get_at_index(index))
        # If the key is in the hash map, remove the given key and its associated value and decrement the size by 1
        if bucket.contains(key):
            bucket.remove(key)
            self.size -= 1
        else:
            pass

    def contains_key(self, key: str) -> bool:
        """
        This method returns True if the given key is in the hash map, otherwise it returns False. An
        empty hash map does not contain any keys.
        """
        # Calculate the correct bucket to look for the key in
        hash_key = self.hash_function(key)
        index = hash_key % self.capacity

        buckets = self.buckets

        # Access the correct bucket to look for the key in
        bucket = (buckets.get_at_index(index))
        # If the given key is in the hash map, return True. Else, return False.
        if bucket.contains(key):
            return True
        else:
            return False

    def empty_buckets(self) -> int:
        """
        This method returns a number of empty buckets in the hash table.
        """
        # Initialize the count at 0
        count = 0
        buckets = self.buckets
        for bucket in buckets:
            # For each empty bucket within the table, increase the count by 1
            if bucket.length() == 0:
                count += 1
        # Return the count
        return count

    def table_load(self) -> float:
        """
        This method returns the current hash table load factor.
        """
        # The load factor of a hash table is the average number of elements in each bucket, calculated by dividing
        # the number of elements in the hash map by the number of buckets in the hash map
        return self.size / self.capacity

    def resize_table(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the internal hash table. All existing key / value pairs
        must remain in the new hash map and all hash table links must be rehashed. If
        new_capacity is less than 1, this method should do nothing.
        """
        # If new capacity is less than 1, this method should return without doing anything
        if new_capacity < 1:
            return
        # Store the old hash table in a variable
        old_hash_table = self.buckets
        # Set the hash map table to a new dynamic array
        self.buckets = DynamicArray()
        # Give the new dynamic array the new capacity
        for _ in range(new_capacity):
            self.buckets.append(LinkedList())
        self.capacity = new_capacity

        # Access each bucket within the old hash table
        for bucket in old_hash_table:
            # For each pair in the bucket, access the key and the value
            for pair in bucket:
                key = pair.key
                value = pair.value
                # Use the new capacity to recalculate the correct index to place each key value pair into
                # within the resized table
                index = self.hash_function(key) % self.capacity
                # Access the correct bucket within the resized table
                bucket = self.buckets.get_at_index(index)
                # Insert the key value pair into the correct bucket in the resized table
                bucket.insert(key, value)

    def get_keys(self) -> DynamicArray:
        """
        This method returns a DynamicArray that contains all keys stored in your hash map. The
        order of the keys in the DA does not matter.
        """
        # Create a new array to place the key values into
        keys = DynamicArray()

        buckets = self.buckets

        # For each bucket, access each pair within the bucket
        for bucket in buckets:
            for pair in bucket:
                # Access the key value in each pair and append it to the keys array
                key = pair.key
                keys.append(key)
        # Return the dynamic array containing all the keys
        return keys

    hf_1 = HashMap(20, hash_function_1)
    hf_2 = HashMap(20, hash_function_2)
    hf_1.put('bat', 10)
    hf_1.put('tab', 10)
    hf_2.put('bat', 10)
    hf_1.put('tab', 10)
    hf_1.empty_buckets()
    hf_2.empty_buckets()
    hf_1.table_load()
    hf_2.table_load()



# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    hf_1 = HashMap(20, hash_function_1)
    hf_2 = HashMap(20, hash_function_2)
    hf_1.put('bat', 10)
    hf_1.put('tab', 10)
    hf_2.put('bat', 10)
    hf_1.put('tab', 10)
    hf_1.empty_buckets()
    hf_2.empty_buckets()
    hf_1.table_load()
    hf_2.table_load()
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
