class Stack:
    def __init__(self):
        self.myStack = []

    def isEmpty(self):
        return self.myStack == []

    def insert(self, item):
        self.myStack.append(item)

    def takeOut(self):
        self.myStack.pop()

    def Size(self):
        return len(self.myStack)

    def printStack(self):
        for items in reversed(self.myStack):
            print(items)




s = Stack()
s.isEmpty()
print(" ")
s.insert("my name is shubham patial and i want to be a very good programmer")
s.insert(4)
s.insert("shubham")
s.insert("patial")
s.insert("is 23")
print(s.Size())
print(" ")
s.printStack()
print(" ")
print("*" * 40)
s.takeOut()
s.printStack()

print('')
s.takeOut()

print("Element has been pooped out from the stack")

print("*" * 40)
s.printStack()
