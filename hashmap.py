from typing import List
from linked_list import LinkedList

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Hashmap:

    def __init__(self, size = 10):
        self.size = 0
        self.bucket: List[LinkedList] = [LinkedList() for _ in range(size)]


    def hash_function(self, key):
        return abs(hash(key))

    def increase_size(self):

        new_bucket = [LinkedList() for _ in range(self.size * 2)]

        self.bucket = new_bucket
        for llist in self.bucket:
            while llist.head:
                pair = llist.pop_head()
                new_position = self.hash_function(pair.key) % len(new_bucket)
                new_bucket[new_position].insert_at_end(pair)

        self.bucket = new_bucket


    def put(self, key, value):
        position_in_bucket = self.hash_function(key) % len(self.bucket)
        node = self.bucket[position_in_bucket].find_node(key)
        if node:
            node.data.value = value
        else:
            pair = Pair(key,value)
            self.bucket[position_in_bucket].insert_at_end(pair)
            self.size += 1

        if self.size / len(self.bucket) > 0.75:
            self.increase_size()


    def get(self, key):
        position_in_bucket = self.hash_function(key) % len(self.bucket)
        node = self.bucket[position_in_bucket].find_node(key)
        if not node:
            raise ValueError("key not found")

        return node.data.value

    def delete_key(self, key):

        position_in_bucket = self.hash_function(key) % len(self.bucket)
        self.bucket[position_in_bucket].delete_node(key)

    def print_hash_map(self):
        for llist in self.bucket:
            print(llist)