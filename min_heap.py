# Course: CS261 - Data Structures
# Assignment: 5
# Student: Amin Malik
# Description: This is a Python implementation of a min heap data structure.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap maintaining heap property.
        """
        # Access the dynamic array underlying the heap
        array = self.heap
        # Insert the new node at the end of the array
        array.append(node)
        # Compute the inserted element’s parent index ((i - 1) / 2).
        parent_index = ((array.length() - 1) / 2)
        # If the parent index is not valid due to being a floating decimal number, round down to nearest integer
        if type(parent_index) == float:
            parent_index = int(parent_index - 0.5)
        # Compare the value of the inserted element with the value of its parent
        i = (array.length() - 1)
        # If the value of the parent is greater than the value of the inserted element,
        # swap the elements in the array and repeat from step 2.
        while array[parent_index] > node:
            # If the parent index value is less than the inserted value, swap the two values
            array.swap(parent_index, i)
            # Recalculate the respective indexes, ensuring they are valid index position integers
            i = int(parent_index)
            parent_index = int((i - 1) / 2)
            # If the parent index number isn't a valid index position, round down to the
            if type(parent_index) == float:
                parent_index = int(parent_index - 0.5)

    def get_min(self) -> object:
        """
        This method returns an object with a minimum key without removing it from the heap. If
        the heap is empty, the method raises a MinHeapException.
        Runtime complexity of this implementation must be O(1).
        """
        # If the heap is empty, raise a MinHeapException
        if self.heap.length() == 0:
            raise MinHeapException
        # Return the object with a minimum key without removing it from the heap
        return self.heap[0]

    def remove_min(self) -> object:
        """
        This method returns an object with a minimum key and removes it from the heap. If the
        heap is empty, the method raises a MinHeapException.
        """
        # If the heap is empty, raise a MinHeapException
        if self.heap.length() == 0:
            raise MinHeapException
        # Access and store the object with the minimum key to return at the end of the function
        minimum = self.heap[0]
        # Replace the value of the first element in the array with the value of the last element
        self.heap.swap(0, self.heap.length()-1)
        # Remove the last element
        self.heap.pop()
        # If the array is empty at this point, there is nothing more to be done so the function can return
        if self.heap.length() == 0:
            return minimum
        # If the array is not empty (i.e., it started with more than one element),
        # compute the indices of the children of the replacement element (2 * i + 1 and 2 * i + 2).
        self.min_heapify()

        return minimum

    def min_heapify(self):
        """This method rearranges the elements of an array so that they obey the min heap property"""
        # Initialize the index to 0
        i = 0
        # The process should keep running as long as there is a valid left child index because if there's no left child index,
        # there is no right child)
        while self.valid_left_child_index(i):
            # First, set the minimum child index to the left child index
            min_child_index = i * 2 + 1
            # If there is a right child index and it is less than the left child, set the new minimum child index to the
            # right child index
            if self.valid_right_child_index(i) and self.heap[i * 2 + 2] < self.heap[i * 2 + 1]:
                min_child_index = i * 2 + 2
            # If the parent index value is less than its child index value, the elements are properly arranged and the
            # method should exit
            if self.heap[i] < self.heap[min_child_index]:
                break
            else:
                # If the elements should be swapped to maintain the heap order, swap them
                self.heap.swap(i, min_child_index)
            # Set the new index to the minimum child index
            i = min_child_index

    def valid_left_child_index(self, index):
        """This method checks if there is a valid left child index for a given index"""
        return 0 < index * 2 + 1 <= self.heap.length() - 1

    def valid_right_child_index(self, index):
        """This method checks if there is a valid right child index for a given index"""
        return 0 < index * 2 + 2 <= self.heap.length() - 1

    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a dynamic array with objects in any order and builds a proper
        MinHeap from them. Current content of the MinHeap is lost.
        """
        # Make a copy of the dynamic array
        array = DynamicArray()
        for i in da:
            array.append(i)

        # Set the heap's array to the copy of the given dynamic array
        self.heap = array

        # Find the position of the first non-leaf element in the array
        i = ((self.heap.length() - 1) / 2)
        if type(i) == float:
            i = int(i - 0.5)

        while self.valid_left_child_index(i):
            # First, set the minimum child index to the left child index
            min_child_index = i * 2 + 1
            # If there is a right child index and it is less than the left child, set the new minimum child index to the
            # right child index
            if self.valid_right_child_index(i) and self.heap[i * 2 + 2] <= self.heap[i * 2 + 1]:
                min_child_index = i * 2 + 2
            # If the parent index value is less than its child index value, the elements are properly arranged and the
            # method should decrement the index by 1
            if self.heap[i] < self.heap[min_child_index]:
                i = i - 1
            else:
                # If the elements should be swapped to maintain the heap order, swap them
                self.heap.swap(i, min_child_index)
                # Decrement the index by 1
                i = i - 1



# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
       print(h, end=' ')
       print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
