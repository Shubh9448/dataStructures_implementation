
def dfs(node):
    node.visited = True
    print("{} ->".format(node.name))

    for n in node.adjacenciesList:
        if not n.visited:
            dfs(n)

