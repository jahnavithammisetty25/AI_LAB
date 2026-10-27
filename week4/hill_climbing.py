import copy

def count_conflicts(state):
  
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def get_all_swap_neighbors(state):
   
    neighbors = []
    n = len(state)
   
    for i in range(n):
        for j in range(i + 1, n):
            neighbor_state = list(state)
            neighbor_state[i], neighbor_state[j] = (
                neighbor_state[j],
                neighbor_state[i],
            )
            neighbors.append((tuple(neighbor_state), (i, j)))
    return neighbors


def hill_climbing_4queens(initial_state):
    current_state = tuple(initial_state)
    current_cost = count_conflicts(current_state)

    print("==================================================")
    print("STARTING HILL-CLIMBING SEARCH")
    print("==================================================")
    print(f"Initial State: {current_state} | Cost: {current_cost}\n")

    step = 0
    while True:
        if current_cost == 0:
            print("Goal state reached! No remaining conflicts.")
            break

        step += 1
        print(f"--- Step {step}: Evaluating Neighbors ---")
        neighbors = get_all_swap_neighbors(current_state)

        best_neighbor = None
        best_cost = current_cost
        chosen_swap = None

       
        print(f"{'Swap (i, j)':<15}{'Neighbor State':<20}{'Cost':<5}")
        print("-" * 40)

        for neighbor_state, swap_pair in neighbors:
            cost = count_conflicts(neighbor_state)
            print(f"Swap {swap_pair!s:<10}{neighbor_state!s:<20}{cost:<5}")

            if cost < best_cost:
                best_cost = cost
                best_neighbor = neighbor_state
                chosen_swap = swap_pair

        print("-" * 40)

        if best_cost >= current_cost:
            print(
                f"\nNo better neighbor found. Stuck at local maximum/optimum."
            )
            print(f"Terminating at state: {current_state} with cost: {current_cost}")
            break

        print(
            f"Decision: Accept Swap {chosen_swap} -> New State: {best_neighbor} with Cost: {best_cost}\n"
        )
        current_state = best_neighbor
        current_cost = best_cost

    print("\n==================================================")
    print(f"Final State Configuration: {current_state}")
    print(f"Final Cost: {current_cost}")
    print("==================================================")

init_state = [3, 1, 2, 0]
hill_climbing_4queens(init_state)


OUTPUT:

==================================================
STARTING HILL-CLIMBING SEARCH
==================================================
Initial State: (3, 1, 2, 0) | Cost: 2

--- Step 1: Evaluating Neighbors ---
Swap (i, j)    Neighbor State      Cost 
----------------------------------------
Swap (0, 1)    (1, 3, 2, 0)        1    
Swap (0, 2)    (2, 1, 3, 0)        1    
Swap (0, 3)    (0, 1, 2, 3)        6    
Swap (1, 2)    (3, 2, 1, 0)        6    
Swap (1, 3)    (3, 0, 2, 1)        1    
Swap (2, 3)    (3, 1, 0, 2)        1    
----------------------------------------
Decision: Accept Swap (0, 1) -> New State: (1, 3, 2, 0) with Cost: 1

--- Step 2: Evaluating Neighbors ---
Swap (i, j)    Neighbor State      Cost 
----------------------------------------
Swap (0, 1)    (3, 1, 2, 0)        2    
Swap (0, 2)    (2, 3, 1, 0)        2    
Swap (0, 3)    (0, 3, 2, 1)        4    
Swap (1, 2)    (1, 2, 3, 0)        4    
Swap (1, 3)    (1, 0, 2, 3)        2    
Swap (2, 3)    (1, 3, 0, 2)        0    
----------------------------------------
Decision: Accept Swap (2, 3) -> New State: (1, 3, 0, 2) with Cost: 0

Goal state reached! No remaining conflicts.

==================================================
Final State Configuration: (1, 3, 0, 2)
Final Cost: 0
==================================================
