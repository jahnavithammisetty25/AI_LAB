def find_blank(state):
    return state.index(0)

def get_neighbors(state):
    neighbors = []
    blank_idx = find_blank(state)
    row, col = blank_idx // 3, blank_idx % 3
    
    moves = [
        (-1, 0, 'Up'),
        (1, 0, 'Down'),
        (0, -1, 'Left'),
        (0, 1, 'Right')
    ]
    
    for dr, dc, move in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[blank_idx]
            neighbors.append((tuple(new_state), move))
            
    return neighbors

def dfs_8_puzzle(start_state, goal_state, max_depth=50):
    stack = [(start_state, [(start_state, "Initial State")], 0)]
    visited = set()
    
    while stack:
        current_state, path, depth = stack.pop()
        
        if current_state == goal_state:
            return path
            
        if current_state in visited or depth > max_depth:
            continue
            
        visited.add(current_state)
        for neighbor, move in get_neighbors(current_state):
            if neighbor not in visited:
                stack.append((neighbor, path + [(neighbor, move)], depth + 1))
                
    return None 

def print_board(state):
    for i in range(0, 9, 3):
        print(f" {state[i] if state[i] != 0 else ' '} | {state[i+1] if state[i+1] != 0 else ' '} | {state[i+2] if state[i+2] != 0 else ' '} ")
        if i < 6:
            print("---|---|---")
    print()

if __name__ == "__main__":
   
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    start = (1, 2, 3, 4, 0, 6, 7, 5, 8)    
    print("Searching for a solution using DFS...\n")
    history_path = dfs_8_puzzle(start, goal)
    
    if history_path:
        print(f"Success! Goal reached in {len(history_path) - 1} moves.\n")
        print("=" * 30)
        print("        STAGE-BY-STAGE PATH      ")
        print("=" * 30 + "\n")
        
        for index, (state, move) in enumerate(history_path):
            if index == 0:
                print(f"Step {index}: {move}")
            else:
                print(f"Step {index}: Move Blank '{move}'")
            print("-" * 15)
            print_board(state)
            
        print("=" * 30)
        print("Target goal state successfully achieved!")
    else:
        print("No solution found within the depth limit.")


OUTPUT:

Searching for a solution using DFS...

Success! Goal reached in 2 moves.

==============================
        STAGE-BY-STAGE PATH      
==============================

Step 0: Initial State
---------------
 1 | 2 | 3 
---|---|---
 4 |   | 6 
---|---|---
 7 | 5 | 8 

Step 1: Move Blank 'Down'
---------------
 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 |   | 8 

Step 2: Move Blank 'Right'
---------------
 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 |   

==============================
Target goal state successfully achieved!
