import heapq

visited = set()

r1 = tuple(map(int, input().split(' ')))
r2 = tuple(map(int, input().split(' ')))
initial_state = r1 + r2
r1 = tuple(map(int, input().split(' ')))
r2 = tuple(map(int, input().split(' ')))
goal_state = r1 + r2

possible_movements = [(0, 1), (1, 2), (2, 3),
                      (4, 5), (5, 6), (6, 7),
                      (0, 4), (1, 5), (2, 6), (3, 7)]

def solve(start_state):
    cnt = 0
    heap = [(0, cnt, start_state)]
    cnt += 1
    while heap:
        state_cost, _, state = heapq.heappop(heap)
        if state == goal_state:
            return state_cost
        if state not in visited:
            visited.add(state)
            for movement in possible_movements:
                p1, p2 = movement
                movement_cost = state[p1] + state[p2]
                new_state = list(state)
                new_state[p1], new_state[p2] = new_state[p2], new_state[p1]
                new_state = tuple(new_state)
                new_state_cost = state_cost + movement_cost
                heapq.heappush(heap, (new_state_cost, cnt, new_state))
                cnt += 1

print(solve(initial_state))

