# 8 Puzzle using Depth First Search (DFS)

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    # Up
    if row > 0:
        new_state = list(state)
        new_state[zero], new_state[zero - 3] = \
            new_state[zero - 3], new_state[zero]
        neighbors.append(tuple(new_state))

    # Down
    if row < 2:
        new_state = list(state)
        new_state[zero], new_state[zero + 3] = \
            new_state[zero + 3], new_state[zero]
        neighbors.append(tuple(new_state))

    # Left
    if col > 0:
        new_state = list(state)
        new_state[zero], new_state[zero - 1] = \
            new_state[zero - 1], new_state[zero]
        neighbors.append(tuple(new_state))

    # Right
    if col < 2:
        new_state = list(state)
        new_state[zero], new_state[zero + 1] = \
            new_state[zero + 1], new_state[zero]
        neighbors.append(tuple(new_state))

    return neighbors


def dfs(start, goal, max_depth):
    stack = [(start, [start])]

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if len(path) - 1 >= max_depth:
            continue

        for neighbor in get_neighbors(state):
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return None


# Initial state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Perform DFS
solution = dfs(start, goal, 20)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for state in solution:
        print_puzzle(state)
else:
    print("No solution found within the depth limit.")