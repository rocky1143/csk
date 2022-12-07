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
for i in range(0,n):
    b=[0]*n
    a.append(b)
print("Enter no of edgs : ")
edgs=int(input())
print("Enter edges from src to dest with cost (src,dst,cost)")
for i in range(0,edgs):
    src,dest,cost=map(int,input().split(' '))
    a[src][dest]=cost
    a[dest][src]=cost
print("Enter src and dest to search : ")
src,dest=map(int,input().split(' '))
vis=[0]*n
stk=[0]*n
cost=[0]*n
top=0
stk[top]=src
vis[src]=1
while(stk[top]!=dest):
    ele=stk[top]
    print(stk[top],end=" ")
    top-=1
    for i in range(0,n):
        if(a[ele][i]>0 and vis[i]==0):
            top+=1
            stk[top]=i;
            cost[top]=a[ele][i];
            vis[i]=1
    if(stk[top]!=ele):
        sort(stk,cost,top)
print(dest)

//output :
Enter no of vertices : 
10
Enter no of edgs : 
9
Enter edges from src to dest with cost (src,dst,cost)
0 1 3
0 2 2
1 3 4
1 4 1
2 5 3
2 6 1
5 7 5
6 8 2
6 9 3
Enter src and dest to search : 
0 9
0 2 6 8 9
