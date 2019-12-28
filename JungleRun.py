class Graph: 
    def __init__(self, V): 
        self.V = V  
        self.adj = [[] for i in range(V)] 

    def addEdge (self, s , d ): 
        self.adj[s].append(d)  
        self.adj[d].append(s) 
    def BFS(self, s, d): 
        # Base case  
        if (s == d):  
            return 0
        level = [-1] * self.V 
      
        # Create a queue for BFS  
        queue = []  
        level[s] = 0
        queue.append(s)  
        while (len(queue) != 0): 
            s = queue.pop()  
            i = 0
            while i < len(self.adj[s]): 
                  
                # Else, continue to do BFS  
                if (level[self.adj[s][i]] < 0 or 
                    level[self.adj[s][i]] > level[s] + 1 ): 
                    level[self.adj[s][i]] = level[s] + 1
                    queue.append(self.adj[s][i]) 
                i += 1
        return level[d] 
  
def isSafe(i, j, M): 
    global N 
    if ((i < 0 or i >= N) or
        (j < 0 or j >= N ) or M[i][j] == "T"):  
        return False
    return True
 
def MinimumPath(M): 
    global N 
    s , d = None, None # source and destination  
    V = N * N + 2
    g = Graph(V)  
  
    k = 1 # Number of current vertex 
    for i in range(N): 
        for j in range(N): 
            if (M[i][j] != "T"): 
 
                if (isSafe (i , j + 1 , M)):  
                    g.addEdge (k , k + 1) 
                if (isSafe (i , j - 1 , M)): 
                    g.addEdge (k , k - 1)  
                if (j < N - 1 and isSafe (i + 1 , j , M)):  
                    g.addEdge (k , k + N)  
                if (i > 0 and isSafe (i - 1 , j , M)):  
                    g.addEdge (k , k - N) 
  
            # source index  
            if(M[i][j] == "S"): 
                s = k  
            # destination index  
            if (M[i][j] == "E"):  
                d = k  
            k += 1
    # find minimum moves  
    return g.BFS (s, d)
N=int(input())
M=[]
for _ in range(N):
    L=input().split()
    M.append(L)
print(MinimumPath(M))