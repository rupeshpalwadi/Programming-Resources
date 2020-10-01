from collections import deque


def bfs(start_r, start_c, end_r, end_c, height, width):
    # Move count
    dist = 0

    # Keep track of visited cells
    visited = [[False]*width for _ in range(height)]

    # Queues for current (r, c) coordinate
    queue_r = deque()
    queue_c = deque()

    # Direction vector (NSEW)
    dir_r = [1, -1, 0, 0]
    dir_c = [0, 0, 1, -1]

    queue_r.append(start_r)
    queue_c.append(start_c)

    visited[start_r][start_c] = True

    # Set new position to current position (+ change)
    new_r, new_c = start_r, start_c

    while queue_r:
        for _ in range(len(queue_r)):
            # Expand on last queued item and setting to current position
            curr_r = queue_r.popleft()
            curr_c = queue_c.popleft()

            # Reached the destination
            if (curr_r, curr_c) == (end_r, end_c):
                return dist

            # New positions plus direction vectors
            for change_r, change_c in zip(dir_r, dir_c):
                new_r = curr_r + change_r
                new_c = curr_c + change_c

                # Out of bounds or visited
                if not 0 <= new_r < height or not 0 <= new_c < width:
                    continue
                elif visited[new_r][new_c]:
                    continue

                queue_r.append(new_r)
                queue_c.append(new_c)

                visited[new_r][new_c] = True

        dist += 1

    return -1


start_r, start_c = (0, 0)
end_r, end_c = (9, 9)
height, width = (10, 10)

board = [[0]*width for _ in range(height)]

print(bfs(start_r, start_c, end_r, end_c, height, width))
