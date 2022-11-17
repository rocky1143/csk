visited=set()
def Dfs(visited,graph,x):
  if x not in visited:
    print(x,end=" ")
    visited.add(x)
    for i in graph[x]:
      Dfs(visited,graph,i)

graph={
    'a':['b','c','d'],
    'b':['e','f','a'],
    'c':['f','a'],
    'd':['a'],
    'e':['b'],
    'f':['b','c']
}
print("DFS:")
Dfs(visited,graph,'b')



'''output
DFS:
b e f c a d 
'''
