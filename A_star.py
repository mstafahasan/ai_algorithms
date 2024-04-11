#NAME:MOSTAFA HASSAN MOHAMED 
#ID:21P0349
#GROUP:2
#SEC:3

import heapq

# Define directions: South, East, North, West
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Define heuristic function (Manhattan distance)
def heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

# python A* algorithm 
def astar_search(maze, start, goal):
    frontier = [(0, start)]  # Priority queue (cost, state)
    came_from = {}  # Parent pointers
    cost_so_far = {start: 0}  # Cost to reach each state

    while frontier:
        current_cost, current_state = heapq.heappop(frontier)

        if current_state == goal:
            break

        for dx, dy in directions:
            next_state = (current_state[0] + dx, current_state[1] + dy)
            if 0 <= next_state[0] < len(maze) and 0 <= next_state[1] < len(maze[0]) and maze[next_state[0]][next_state[1]] != 1:
                new_cost = cost_so_far[current_state] + 1
                if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                    cost_so_far[next_state] = new_cost
                    priority = new_cost + heuristic(next_state, goal)
                    heapq.heappush(frontier, (priority, next_state))
                    came_from[next_state] = current_state

    
    path = []
    current_state = goal
    while current_state != start:
        path.append(current_state)
        current_state = came_from[current_state]
    path.append(start)
    path.reverse()

    return path
"""
0 -> empty state 
1 -> wall
2-> start state 
3-> goal state 
"""
#Here is the question three in sheet 4
# Define the maze
maze = [
    [0 , 0, 1, 1, 0, 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0, 0, 0, 0, 0 , 0 , 3 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 0, 1, 1, 0, 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 0],
    [1 , 1, 1, 1, 0, 1 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0],
    [0 , 1, 1, 1, 0, 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 0],
    [0 , 0, 0, 2, 0, 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0]
    
]

start_state = (5, 3)  # Start state
goal_state = (1, 7)   # Goal state

# Find the path using A* search
path = astar_search(maze, start_state, goal_state)

# Print the solution path
print("A* Search Path :")
for state in path:
    print(state)
#Now run and get a solution 