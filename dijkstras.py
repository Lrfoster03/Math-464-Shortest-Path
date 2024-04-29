import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def convert2Vertex(vertex):
    if(type(vertex) == int):
        return chr(vertex + 65)
    elif(type(vertex) == list):
        return [chr(i + 65) for i in vertex]

def make_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[j][i] = matrix[i][j]
    return matrix

def check_symmetric(matrix):
    symmetric = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] != matrix[j][i]):
                symmetric = False
                print(matrix[i][j])
                break
    print(symmetric)

# Load the CSV file into a numpy array
distanceData = np.genfromtxt('Distance Data.csv', delimiter=',')
delayData = np.genfromtxt('Delay Data.csv', delimiter=',')
num_vertices = len(distanceData)

# Create an undirected graph
G = nx.Graph()


# Take the ratio between length / delay and then average them all 

# Check 7761.08
omega = 7761.08 / 30
# omega = 260
# print("Omega:", omega)

# Add edges from the data sets
for i in range(num_vertices):
    for j in range(i+1, num_vertices):
        if distanceData[i][j] != 0:
            G.add_edge(i, j, weight= distanceData[i][j] + (omega * delayData[i][j]))

# Draw the graph (optional)
# nx.draw(G, with_labels=True)
# plt.show()

# Find the shortest path between two vertices
# start_vertex = 0
# end_vertex = 13
# shortest_path = nx.shortest_path(G, source=start_vertex, target=end_vertex)

# Print the shortest path
# print("Shortest Path from", convert2Vertex(start_vertex), "to", convert2Vertex(end_vertex), ":", convert2Vertex(shortest_path))

# Calculate the shortest path length
# shortest_path_length = nx.shortest_path_length(G, source=start_vertex, target=end_vertex, weight='weight')
# print("Shortest Path Length:", shortest_path_length)

# total_length = sum(G.edges[shortest_path[i], shortest_path[i+1]]['weight'] for i in range(len(shortest_path)-1))
# print("Total Length of the Path:", total_length)

shortestPaths =[[0 for _ in range(15)] for _ in range(15)]
shortestDistances =[[0 for _ in range(15)] for _ in range(15)]

for i in range(num_vertices):
    for j in range(num_vertices):
        temp_list = nx.shortest_path(G, source=i, target=j, weight='weight')
        shortestPaths[i][j] = convert2Vertex(temp_list)
        shortestDistances[i][j] = sum(G.edges[temp_list[m], temp_list[m+1]]['weight'] for m in range(len(temp_list)-1))

for i in range(num_vertices):
    print(shortestPaths[i])

print()

# Truncate integer after 6th decimal place
for i in range(num_vertices):
    for j in range(num_vertices):
        shortestDistances[i][j] = round(shortestDistances[i][j], 8)

for i in range(num_vertices):
    print(shortestDistances[i])