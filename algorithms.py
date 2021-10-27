from collections import defaultdict

#define constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

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
    while cur and cur != start:
        cur.color = WHITE
        cur = prev[cur]