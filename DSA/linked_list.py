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
