from LinkedlistDS.Node import Node


class Linkedlist(object):

    def __init__(self):
        self.head = None
        self.counter = 0

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print(" ".format(actualNode.data))
            actualNode = actualNode.nextNode



    def insertStart(self,data):

        self.counter += 1
        newNode = Node(data)


        if not self.head:
            self.head = newNode

        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size(self):
        return self.counter

    def insertEnd(self, data):
        if self.head is None:
            self.insertStart(data)
            return
        self.counter += 1

        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode


    def remove(self, data):

        self.counter -= 1
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)
#
# class SingleList(object):
#
#     head = None
#     tail = None
#
#     def show(self):
#         print("Showing list data:")
#         current_node = self.head
#         while current_node is not None:
#             print (current_node.data, " -> ",)
#             current_node = current_node.next
#         print (None)
#
#     def append(self, data):
#         node = Node(data, None)
#         if self.head is None:
#             self.head = self.tail = node
#         else:
#             self.tail.next = node
#         self.tail = node
#
#     def remove(self, node_value):
#         current_node = self.head
#         previous_node = None
#         while current_node is not None:
#             if current_node.data == node_value:
#                 # if this is the first node (head)
#                 if previous_node is not None:
#                     previous_node.next = current_node.next
#                 else:
#                     self.head = current_node.next
#
#             # needed for the next iteration
#             previous_node = current_node
#             current_node = current_node.next