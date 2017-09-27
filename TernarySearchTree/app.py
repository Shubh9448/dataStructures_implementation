from TernarySearchTree.TST import TST

tree = TST()

tree.put("apple",100)
tree.put("orange",200)
tree.put("guava",300)
tree.put("pineapple",400)
tree.put("grapes",500)
tree.put("watermelon",600)
tree.put("strawberry",700)
tree.put("blueberry",800)
tree.put("muskmelon",900)
tree.put("lemon",950)
tree.put("banana",850)

print(tree.get("orange"))
print(tree.get("banana"))
print(tree.get("blueberry"))
print(tree.get("guava"))
print(tree.get("grapes"))