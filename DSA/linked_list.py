# Creating a linked List in python

# Node class
class Node:
    # initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class contains a Node object
class LinkedList:
    # initialize the head
    def __init__(self):
        self.head = None

    def create_node(self, data):
        """
        This inserts a node at the end of the list or
        the first node if list is empty
        :param data: any ==> str, int,
        :return: None
        """
        new_node = Node(data)
        if self.head:
            # if the list ain't empty ==> there's a head, start from the head node
            current = self.head
            while current.next:  # while the current node has a reference (reference is not None)
                current = current.next  # move onto the next node in the list
            current.next = new_node  # when the reference is None, create the reference to the new_node
        else:
            self.head = new_node

    def print_list(self):
        # print list starting from the head
        # cur_node = self.head
        # while cur_node:
        #     print(cur_node.data)
        #     cur_node = cur_node.next

        cur_node = self.head
        nodes = []
        while cur_node is not None:
            nodes.append(cur_node.data)
            cur_node = cur_node.next
        nodes.append("None")
        print(" -> ".join(nodes))

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The previous node must be in the Linked List")

        new_node = Node(data)
        new_node.next = prev_node.next  # make the next node of the new node the one that came after the prev_node
        prev_node.next = new_node  # re-assign the next node of previous node to the new_node

    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in linked list
    def delete_node(self, key):
        # check if the linked list is empty
        if self.head is Node:
            print("Linked List is empty")
            return

        # check if the node to be deleted is the head
        if self.head.data == key:
            self.head = self.head.next

        # start from the head and look for the node whose reference is the one we want to delete
        prev_node = self.head
        while prev_node.next is not None:
            if prev_node.next == key:
                return
            prev_node = prev_node.next

        if prev_node.next is None:
            print("Node does not exist")
        else:
            prev_node.next = prev_node.next.next
            # prev_node.next = key.next

        # # Store head node
        # temp = self.head
        #
        # # If head node itself holds the key to be deleted
        # if temp is not None:
        #     if temp.data == key:
        #         self.head = temp.next
        #         temp = None
        #         return
        #
        # # Search for the key to be deleted, keep track of the
        # # previous node as we need to change 'prev.next'
        # while temp is not None:
        #     if temp.data == key:
        #         break
        #     prev = temp
        #     temp = temp.next
        #
        # # if key was not present in linked list
        # if temp is None:
        #     return
        #
        # # Unlink the node from linked list
        # prev.next = temp.next
        #
        # temp = None

    def delete_at_position(self, x):
        position = 1
        if position == x:
            self.head = self.head.next
        else:
            current_node = self.head  # start from the head as your current node
            prev_node = self.head  # start from the head as your prev_node
            while current_node:
                if position == x:
                    prev_node.next = current_node.next
                    break
                position += 1
                prev_node = current_node
                current_node = current_node.next

    # Enable the iteration (loop) over the linked list E.g ==> for node in linked_list: print(node.data)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


l_list = LinkedList()
l_list.create_node("One")
l_list.create_node("two")
l_list.create_node("three")
l_list.print_list()
