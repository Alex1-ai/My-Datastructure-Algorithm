def path_traverse(grid, start_row, start_col):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (-1, 0), # UP
        (1, 0), # DOWN
        (0, -1), # LEFT
        (0, 1)  # RIGHT
    ]
    visited = [grid[start_row][start_col]]

    while True:
        curr_max = -1
        for dir in directions:
            new_row = start_row + dir[0]
            new_col = start_col + dir[1]
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue
            if grid[new_row][new_col] > curr_max:
                next_row, next_col, curr_max = new_row, new_col, grid[new_row][new_col]
        if curr_max <= grid[start_row][start_col]:
            break
        start_row, start_col = next_row, next_col
        visited.append(curr_max)

    return visited
