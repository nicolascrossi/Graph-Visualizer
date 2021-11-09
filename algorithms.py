from collections import defaultdict
import math

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (221,160,221)

def dfs(node, goal):
    s = [node]
    while len(s) > 0:
        node = s.pop()
        if node is None or node.color == BLACK:
            continue
        if node == goal:
            return True
        
        node.color = BLACK

        for adj in node:
            s.append(adj)

def bfs(start, goal):
    prev = defaultdict(lambda : None)

    q = [start]
    while len(q) > 0:
        node = q.pop(0)
        if node == goal:
            break

        node.color = BLACK

        for adj in node:
            if adj and prev[adj] is None:
                prev[adj] = node
                q.append(adj)

    cur = prev[goal]
    while cur and cur != start:
        cur.color = WHITE
        cur = prev[cur]
    return True

def bfs_step_setup(start):
    return  [start], defaultdict(lambda : None)

def bfs_step(q, prev, goal):
    node = q.pop(0)
    if node == goal:
        return True

    node.color = BLACK

    for adj in node:
        if adj and prev[adj] is None:
            prev[adj] = node
            q.append(adj)
    return False

def trail(prev, goal, start):
    cur = prev[goal]
    cost = 0
    while cur and cur != start:
        cost += cur.weight
        cur.color = PURPLE
        cur = prev[cur]
    print(cost)

def dijkstra(start, goal):
    dist, prev = {}, {}
    adj = [start]
    dist[start] = 0
    prev[start] = None

    while len(adj) > 0:
        min_node = adj[0]
        min_dist = dist[min_node]
        
        for node in adj:
            if dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node

        adj.remove(min_node)

        if min_node == goal:
            trail(prev, goal, start)
            return True
        
        for n in min_node:
            if n:
                n_d = dist.get(n, -1)
                d = dist[min_node]
                if d < n_d:
                    dist[n] = d + n.weight
                    prev[n] = min_node
                elif n_d == -1:
                    dist[n] = d + n.weight
                    prev[n] = min_node
                    adj.append(n)

        min_node.color = BLACK
    
    return False
            

def a_star(start, goal):
    dist, prev = {}, {}
    adj = [start]
    dist[start] = 0
    prev[start] = None

    while len(adj) > 0:
        min_node = adj[0]
        min_dist = dist[min_node] + dist_cart(min_node.pos, goal.pos) * 10
        
        for node in adj:
            if dist[node] + dist_cart(node.pos, goal.pos) * 10 < min_dist:
                min_dist = dist[node]
                min_node = node

        adj.remove(min_node)

        if min_node == goal:
            trail(prev, goal, start)
            return True
        
        for n in min_node:
            if n:
                n_d = dist.get(n, -1)
                d = dist[min_node]
                if d < n_d:
                    dist[n] = d + n.weight
                    prev[n] = min_node
                elif n_d == -1:
                    dist[n] = d + n.weight
                    prev[n] = min_node
                    adj.append(n)

        min_node.color = BLACK
    
    return False

def a_star_setup(start):
    dist, prev = {}, {}
    adj = [start]
    dist[start] = 0
    prev[start] = None
    return dist, prev, adj

def a_star_step(start, goal, dist, prev, adj):
    min_node = adj[0]
    min_dist = dist[min_node] + dist_cart(min_node.pos, goal.pos) * 10
    
    for node in adj:
        if dist[node] + dist_cart(node.pos, goal.pos) * 10 < min_dist:
            min_dist = dist[node]
            min_node = node

    adj.remove(min_node)

    if min_node == goal:
        trail(prev, goal, start)
        return True
    
    for n in min_node:
        if n:
            n_d = dist.get(n, -1)
            d = dist[min_node]
            if d < n_d:
                dist[n] = d + n.weight
                prev[n] = min_node
            elif n_d == -1:
                dist[n] = d + n.weight
                prev[n] = min_node
                adj.append(n)

    min_node.color = BLACK
    return False

def dist_cart(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)