from collections import defaultdict
class Graph:
    def __init__(self, vertices):

        self.V = vertices

        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DLS(self,src,target,maxDepth,):
        if src == target:
            return True

        if maxDepth <= 0:
            return False

        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth - 1):
                return True
        return False
    def IDDFS(self,src,target,maxDepth,):

        for i in range(maxDepth):
            if self.DLS(src, target, i):
                return True
        return False
n=int(input('Enter number of edges :'))
g = Graph(n)
print('Enter Edges : ')

#x,y=map(int,input().split())

for i in range(n-1):
  x,y=map(int,input().split()[:2])
  g.addEdge(x,y)
target = int(input('Enter target node :'))
maxDepth =int(input('Enter max depth :'))
src = int(input('Enter source :'))

if g.IDDFS(src, target, maxDepth) == True:
    print('Target is reachable from source ' ,'within max depth')
else:
    print('Target is NOT reachable from source ' ,'within max depth')
    
'''Output
 Enter number of edges :4
Enter Edges : 
1 2
2 3
3  4
Enter target node :2
Enter max depth :2
Enter source :1
Target is reachable from source  within max depth'''
