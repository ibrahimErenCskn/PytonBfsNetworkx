import gym
from collections import deque
import networkx as nx
def networkxProblem(env, start, goal):
    graph = nx.DiGraph()

    for i in env.P:
        for j in env.P[0]:
            graph.add_weighted_edges_from([(i, env.P[i][j][0][1], j)])

    shortest_path = nx.shortest_path(graph, start, goal, weight="weight")

    path_weights = []
    for i in range(len(shortest_path) - 1):
        weight = graph[shortest_path[i]][shortest_path[i + 1]]['weight']
        path_weights.append(weight)

    for t in path_weights:
        env.step(t)

    env.reset()

def bfsProblem(start, goal, env):
    states = env.observation_space.n
    actions = env.action_space.n

    stateTable = {}

    for i in range(states):
        stateTable[i] = {}
        for j in range(actions):
            stateTable[i][j] = env.P[i][j][0][1]
    print(stateTable)
    print(env.P)
    queue = deque([(start, [])])
    v = set()

    while queue:
        currentState, path = queue.popleft()
        v.add(currentState)

        if currentState == goal:
            for t in path:
                env.step(t[0])
            env.reset()
            break

        for i, j in stateTable[currentState].items():
            if j not in v:
                queue.append((j, path + [(i, j)]))

mymap = [
    "SFFFFF",
    "FFFFHF",
    "FFFHFF",
    "HFFFFF",
    "FHFFFF",
    "GFFFFF",
]

env = gym.make("FrozenLake-v1", render_mode="human", is_slippery=False, desc=mymap)
init_state = env.reset()

start = 0
goal = 30

arr1 = [1,2,3,4,5,6,7,8]



for i in range(len(arr1)):
    print(i)


#bfsProblem(start=start, goal=goal, env=env)

#networkxProblem(env=env, start=start, goal=goal)




