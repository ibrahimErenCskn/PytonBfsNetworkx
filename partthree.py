import gym
import networkx as nx

DOWN, RIGHT, UP, LEFT = 0, 1, 2, 3



env = gym.make("CliffWalking-v0", render_mode="human")
env.reset()
graph = nx.DiGraph()

arr = [1,2,3,4,5,6,7,8,9,10]

for i in env.P:
    for j in env.P[0]:
        if i not in arr:
            graph.add_weighted_edges_from([(i, env.P[i][j][0][1], j)])



shortest_path = nx.shortest_path(graph, 0, 11, weight="weight")


path_weights = []
for i in range(len(shortest_path) - 1):
    weight = graph[shortest_path[i]][shortest_path[i + 1]]['weight']
    path_weights.append(weight)


for t in path_weights:
    if t == DOWN:
        env.step(2)
    if t == RIGHT:
        env.step(1)
    if t == UP:
        env.step(0)
    if t == LEFT:
        env.step(3)
