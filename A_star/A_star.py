#Szymon Lis 

#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def load_graph_from_file(filename: str) -> nx.Graph: 
    result = [] 
    G = nx.Graph()
    
    with open(filename) as file:
        for line in file:
            if len(line.strip()) > 0:
                row=(line.split(' '))
                row[0]=int(row[0])
                row[1]=int(row[1])
                row[2]=float(row[2].strip('\n'))
                result.append(tuple(row))
            
    G.add_weighted_edges_from(result)
    return G

G1=load_graph_from_file('plik.txt')
pos = nx.spring_layout(G1)
nx.draw(G1, pos=pos, with_labels=True)
nx.draw_networkx_edge_labels(G1, pos, edge_labels=nx.get_edge_attributes(G1, 'weight'))

H={1:21.0,2:18.0,3:19.0,4:16.0,5:12.0,6:10.0,7:13.0,8:14.0,9:10.0,10:0.0}


def A_STAR(graph, start, goal,h_score):
    openset = PriorityQueue()
    openset.put(start, 0)
    came_from = {start: None}
    g_score = {start: 0}
    while not openset.empty():
        x = openset.get()

        if x == goal:
            break

        for next in graph.neighbors(x):
            new_cost = g_score[x] + graph[x][next]['weight']
            if next not in g_score or new_cost < g_score[next]:
                g_score[next] = new_cost
                priority = new_cost + h_score[next]
                openset.put(next, priority)
                came_from[next] = x

    return came_from, g_score

def reconstruct_path(came_from, start, goal):
    x = goal
    path = [x]
    while x != start:
        x = came_from[x]
        path.append(x)
    path.reverse()
    return path

came_from,g_score=A_STAR(G1,1,10,H)
path=reconstruct_path(came_from,1,10)
print(path)
print(g_score[10])
