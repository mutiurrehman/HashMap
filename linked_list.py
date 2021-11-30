class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def pop_head(self):
        if not self.head:
            return None

        next_node = self.head.next
        if next_node != None:
            next_node.prev = None

        item = self.head.data
        self.head = next_node
        return item


    def __str__(self):
        temp = self.head
        sol = "[ "

        while temp != None:
            sol += temp.data.key
            sol += " "
            temp = temp.next
        sol += " ]"
        return sol

    def get_node(self, node, key):
        if not node:
            return None

        return node if node.data.key == key else self.get_node(node.next, key)

    def find_node(self, key):
         return self.get_node(self.head, key)

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return new_node

        def get_last_node(node):
            return get_last_node(node.next) if node.next != None else node

        last_node = get_last_node(self.head)
        new_node.prev = last_node
        last_node.next = new_node
        return new_node

    def delete_node(self, key):
        node = self.get_node(self.head, key)
        if not node:
            raise ValueError("Node not present")

        if not node.prev:
            self.head = node.next
            return node

        prev_node = node.prev
        prev_node.next  = node.next
        if node.next:
            node.next.prev = prev_node

        return node