def sort(stk,cost,top):
    for i in range(0,top):
        for j in range(0,top):
            if(cost[j]<cost[j+1]):
                temp=cost[j]
                cost[j]=cost[j+1]
                cost[j+1]=temp
                temp=stk[j]
                stk[j]=stk[j+1]
                stk[j+1]=temp
print("Enter no of vertices : ")
n=int(input())
a=[]
par=[0]*100
for i in range(0,n):
    b=[0]*n
    a.append(b)
print("enter heuristic value fr every node(node,heuristic value)")
h=[0]*100
for i in range(0,n):
    src,h1=map(int,input().split(' '))
    h[src]=h1
print("enter no of edges : ")
edgs=int(input())
print("Enter edges from src to dest with cost: ")
for i in range(0,edgs):
    src,dest,cost=map(int,input().split(' '))
    a[src][dest]=cost
top=0
stk=[0]*n
cost=[0]*n
print("Enter src and dest : ")
src,dest=map(int,input().split(' '))
stk[top]=src
while(stk[top]!=dest):
    print(stk[top],end=" ")
    ele=stk[top]
    top-=1
    for i in range(0,n):
        if(a[ele][i]>0):
            top+=1;
            stk.insert(0,i)
            cost.insert(0,a[ele][i]+h[i]+par[ele])
            par[i]=par[ele]+a[ele][i]
    if(ele!=stk[top]):
        sort(stk,cost,top)
print(dest)



//output:
    Enter no of vertices : 
10
enter heuristic value fr every node(node,heuristic value)
1 13
2 12
3 4
4 7
5 3
6 8
7 2
8 4
9 9
10 0
enter no of edges : 
9
Enter edges from src to dest with cost: 
0 1 3
0 2 2
1 3 4
1 4 1
2 5 3
2 6 1
5 7 5
6 8 2
6 9 3
Enter src and dest : 
0 7
0 2 5 6 8 7

