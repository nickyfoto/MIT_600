import string
from graph import * 

def load_map(mapFilename):
    lst = []
    g = WeightedDigraph()
    dataFile = open(mapFilename, 'r')
    for line in dataFile:
        dataLine = string.split(line[:-1], ' ')
        lst.append(dataLine)
    for e in lst:
        for i in range(2):
            try:
                g.addNode(Node(e[i]))
            except ValueError:
                pass
    for e in lst:
        g.addEdge(WeightedEdge(Node(e[0]), Node(e[1]), float(e[2]), float(e[3])))
    return g
        
# mitMap = load_map("mit_map.txt")

def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result



# def DFSShortest(graph, start, end, path = [], shortest = None):
#     path = path + [start]
#     # print 'Current dfs path:', printPath(path)
#     if start == end:
#         print path
#         return path
#     for node in graph.childrenOf(start):
#         if node not in path: #avoid cycles
#             if shortest == None or len(path)<len(shortest):
#                 newPath = DFSShortest(graph,node,end,path,shortest)
#                 if newPath != None:
#                     shortest = newPath
#     return shortest

def pairs(sp):
    res = []
    if sp != None:
        for i in range(len(sp)-1):
            res.append([sp[i], sp[i+1]])
        return res
    else:
        return res

def totalD(lst, graph):
    TD = 0
    TOD = 0
    for p in lst:
        for n in graph.edges[p[0]]:
            if n[0] == p[1]:
                TD += n[1][0]
                TOD += n[1][1]
    return TD, TOD

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    allPath = []
    def DFSShortest(graph, start, end, path = [], shortest = None):
        path = path + [start]
        if start == end:
            allPath.append((path, totalD(pairs(path), graph)))
            return path
        for node in graph.childrenOf(start):
            if node not in path: #avoid cycles
                # if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
        return shortest
    
    sp = DFSShortest(digraph, Node(start), Node(end), path = [], shortest = None)
    # print allPath
    f1 = []
    for p in allPath:
        if p[1][0] <= maxTotalDist:
            f1.append(p)
    if f1 == []:
        raise ValueError
    f2 = []
    for p in f1:
        if p[1][1] <= maxDistOutdoors:
            f2.append(p)
    if f2 == []:
        raise ValueError
    sm = []
    for p in f2:
        sm.append(p[1][0])
    res = []
    for n in f2[sm.index(min(sm))][0]:
        res.append(str(n))
    return res

# n1 = Node('1')
# n2 = Node('2')
# n3 = Node('3')
# n4 = Node('4')
# n5 = Node('5')
# e1 = WeightedEdge(n1, n2, 5, 2)
# e2 = WeightedEdge(n3, n5, 6, 3)
# e3 = WeightedEdge(n2, n3, 20, 10)
# e4 = WeightedEdge(n2, n4, 10, 5)
# e5 = WeightedEdge(n4, n3, 2, 1)
# e6 = WeightedEdge(n4, n5, 20, 10)
# g = WeightedDigraph()
# g.addNode(n1)
# g.addNode(n2)
# g.addNode(n3)
# g.addNode(n4)
# g.addNode(n5)
# g.addEdge(e1)
# g.addEdge(e2)
# g.addEdge(e3)
# g.addEdge(e4)
# g.addEdge(e5)
# g.addEdge(e6)

# print g

# print bruteForceSearch(g, "1", "3", 100, 100)
# print bruteForceSearch(g, "1", "5", 100, 100)
# print bruteForceSearch(g, "1", "3", 17, 8)
# print type(bruteForceSearch(g, "1", "3", 18, 18)[0])



# print bruteForceSearch(mitMap, 56, 13, 300, 100)


#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    allPath = []
    minD = [maxTotalDist]
    minOutDoor = [maxDistOutdoors]
    def DFSShortest(graph, start, end, path = [], shortest = None):
        path = path + [start]
        if start == end:
            D = totalD(pairs(path), graph)
            if D[0] <= minD[0] and D[1] <= minOutDoor[0]:
                allPath.append((path, D))
                minD[0] = D[0]
            return path
        for node in graph.childrenOf(start):
            if node not in path: #avoid cycles
                if totalD(pairs(shortest), graph)[0] == 0 or totalD(pairs(path), graph)[0] < totalD(pairs(shortest), graph)[0]:
                    newPath = DFSShortest(graph,node,end,path,shortest)
                    if newPath != None:
                        shortest = newPath
        return shortest
    
    sp = DFSShortest(digraph, Node(start), Node(end), path = [], shortest = None)
    # print len(allPath)
    # for p in allPath:
    #     print p
    if allPath == []:
        raise ValueError
    else:
        return [str(x) for x in allPath[-1][0]]

# print directedDFS(g, "1", "3", 17, 8)
# print directedDFS(mitMap, 56, 13, 300, 100)

# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
#     Test cases
    mitMap = load_map("mit_map.txt")
    # print isinstance(mitMap, Digraph)
    # print isinstance(mitMap, WeightedDigraph)
    # print 'nodes', mitMap.nodes
    # print 'edges', mitMap.edges


    LARGE_DIST = 1000000

#     Test case 1
    # print "---------------"
    # print "Test case 1:"
    # print "Find the shortest-path from Building 32 to 56"
    # expectedPath1 = ['32', '56']
    # brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    # dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    # print "Expected: ", expectedPath1
    # print "Brute-force: ", brutePath1
    # print "DFS: ", dfsPath1
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
    # print "---------------"
    # print "Test case 2:"
    # print "Find the shortest-path from Building 32 to 56 without going outdoors"
    # expectedPath2 = ['32', '36', '26', '16', '56']
    # brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    # dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    # print dfsPath2
    # print "Expected: ", expectedPath2
    # print "Brute-force: ", brutePath2
    # print "DFS: ", dfsPath2
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
    # print "---------------"
    # print "Test case 3:"
    # print "Find the shortest-path from Building 2 to 9"
    # expectedPath3 = ['2', '3', '7', '9']
    # brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    # dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    # print "Expected: ", expectedPath3
    # print "Brute-force: ", brutePath3
    # print "DFS: ", dfsPath3
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

    # Test case 4
    # print "---------------"
    # print "Test case 4:"
    # print "Find the shortest-path from Building 2 to 9 without going outdoors"
    # expectedPath4 = ['2', '4', '10', '13', '9']
    # brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    # dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    # print "Expected: ", expectedPath4
    # print "Brute-force: ", brutePath4
    # print "DFS: ", dfsPath4
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
    # print "---------------"
    # print "Test case 5:"
    # print "Find the shortest-path from Building 1 to 32"
    # expectedPath5 = ['1', '4', '12', '32']
    # brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    # dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    # print "Expected: ", expectedPath5
    # print "Brute-force: ", brutePath5
    # print "DFS: ", dfsPath5
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
    # print "---------------"
    # print "Test case 6:"
    # print "Find the shortest-path from Building 1 to 32 without going outdoors"
    # expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    # brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    # dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    # print "Expected: ", expectedPath6
    # print "Brute-force: ", brutePath6
    # print "DFS: ", dfsPath6
    # print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
    # print "---------------"
    # print "Test case 7:"
    # print "Find the shortest-path from Building 8 to 50 without going outdoors"
    # bruteRaisedErr = 'No'
    # dfsRaisedErr = 'No'
    # try:
    #     bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    # except ValueError:
    #     bruteRaisedErr = 'Yes'
    
    # try:
    #     directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    # except ValueError:
    #     dfsRaisedErr = 'Yes'
    
    # print "Expected: No such path! Should throw a value error."
    # print "Did brute force search raise an error?", bruteRaisedErr
    # print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
