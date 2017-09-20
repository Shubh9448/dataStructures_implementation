class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not  None:
                self.nextNode.remove(data, self)
# class Node(object):
#
#     def __init__(self, data, next):
#         self.data = data
#         self.next = next