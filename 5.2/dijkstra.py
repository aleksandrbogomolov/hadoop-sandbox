#!/usr/bin/env python3

import sys

edges = {}
vertex_weight = {}

(vertex_count, edge_count) = sys.stdin.readline().strip().split(' ')

count = 0

while count < int(edge_count):
    (from_vertex, in_vertex, edge_weigth) = sys.stdin.readline().strip().split(' ')
    if from_vertex in edges:
        edges[from_vertex].append((in_vertex, int(edge_weigth)))
    else:
        edges[from_vertex] = [(in_vertex, int(edge_weigth))]
    vertex_weight[from_vertex] = 0
    vertex_weight[in_vertex] = 0
    count = count + 1

(init_vertex, end_vertex) = sys.stdin.readline().strip().split(' ')

print('init_vertex = %s, end_vertex = %s' % (init_vertex, end_vertex))

excluded_list = []

def apply(start_vertex_list, start_vertex):
    print(start_vertex_list)
    for vertex, weight in start_vertex_list:
        print('vertex = %s' % (vertex))
        edge_dist = vertex_weight[start_vertex] + weight
        print('%i = %i + %i' % (edge_dist, vertex_weight[start_vertex], weight))
        if vertex != init_vertex and (vertex_weight[vertex] == 0 or vertex_weight[vertex] > edge_dist):
            vertex_weight[vertex] = edge_dist
    excluded_list.append(start_vertex)

    start_vertex_list.sort(key = lambda x: x[1])
    for vertex, weight in start_vertex_list:
        print('vertex: %s, excluded_list: %s' % (vertex, excluded_list))
        if vertex not in excluded_list and vertex in edges:
            apply(edges[vertex], vertex)
    
result = 0
if init_vertex in edges:
    apply(edges[init_vertex], init_vertex)
    result = vertex_weight[end_vertex]
else:
    result = -1

print(-1 if result == 0 else result)
