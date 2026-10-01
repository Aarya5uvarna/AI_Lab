# 8 Puzzle using Iterative Deepening Search (IDS)

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = []

    if row > 0:
        moves.append(zero - 3)   # Up
    if row < 2:
        moves.append(zero + 3)   # Down
    if col > 0:
        moves.append(zero - 1)   # Left
    if col < 2:
        moves.append(zero + 1)   # Right

    for move in moves:
        new_state = list(state)

        new_state[zero], new_state[move] = \
            new_state[move], new_state[zero]

        neighbors.append(tuple(new_state))

    return neighbors


def depth_limited_search(state, goal, depth, path):
    if state == goal:
        return path

    if depth == 0:
        return None

    for neighbor in get_neighbors(state):

        if neighbor not in path:
            result = depth_limited_search(
                neighbor,
                goal,
                depth - 1,
                path + [neighbor]
            )

            if result:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        result = depth_limited_search(
            start,
            goal,
            depth,
            [start]
        )

        if result:
            return result

        depth += 1


# Start state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = ids(start, goal)

print("Solution found!")
print("Number of moves:", len(solution) - 1)

for state in solution:
    print_puzzle(state)