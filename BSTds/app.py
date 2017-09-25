from BSTds.BinarySearchTree import BST

bst = BST()
bst.insert(12)
bst.insert(10)
bst.insert(9)
bst.insert(1)
bst.insert(18)
bst.insert(25)
bst.insert(24)
bst.insert(27)
bst.insert(29)
bst.insert(33)
bst.insert(40)
bst.insert(3)

print("Inorder")
bst.traverseInOrder()

print("*" * 40)
print("PostOrder")

bst.traversePostOrder()
print("*" * 40)
print("PreOrder")

bst.traversePreOrder()

print("*" * 40)

print("the max node is :{}".format(bst.getMax()))
print("the min node is :{}".format(bst.getMin()))