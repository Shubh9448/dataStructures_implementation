
class Algorithm(object):
    HAS_CYCLE = False

    def calculateShortestPath(self, vertexList, edgeList, startVertex):
        startVertex.minDistance = 0

        for i in range(0, len(vertexList) - 1):
            for edge in edgeList:

                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

            for edge in edgeList:
                if self.hasCycle(edge):
                print("Negative cycle detected...")
                Algorithm.HAS_CYCLE = True
                return

    def getShortestPathTo(self, targetVertex):

        print("Shortest path to target vertex:", targetVertex.minDistance)

        node = targetVertex

        while node is not None:
            print("%s ->"% node.name)
            node = node.predecessor


