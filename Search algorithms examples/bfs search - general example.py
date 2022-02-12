#graph representation
adj_list ={
    0: [1,2],
    1: [3,4],
    2: [1,5],
    3: [],
    4: [5],
    5: [],
}
v = len(adj_list)
s=0

def bfs(adj_list, a, s):
    visited = [False for i in range(a)]         #set all elements to False initially
    #print(visited)
    queue = []                                  #create an empty queue
    visited[s] = True                            
    queue.append(s)                             #add starting node in queue
    while (len(queue)!=0):
        u = queue[0]                            #take the first element out
        queue.pop(0)                             
        print(u)
        for b in adj_list[u]:                   #mark the childs of first element as visited and add them to queue
            if visited[b] == False:
                visited[b] = True
                queue.append(b)
        

path = bfs(adj_list, v, s)                      #print the path travelled along nodes from start to end
print(path)