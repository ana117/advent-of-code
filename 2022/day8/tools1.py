def is_visible_left(grid, i, j, dp):
    if dp[i-1][j][0] != -1 and grid[i][j] > dp[i-1][j][0]:
        dp[i][j][0] = grid[i][j]
        return True
    
    ptr = i-1
    flag = True
    while ptr >= 0:
        if grid[ptr][j] >= grid[i][j]:
            flag = False
            dp[i][j][0] = max(dp[i][j][0], grid[ptr][j])
        ptr -= 1
    
    if flag:
        dp[i][j][0] = grid[i][j]
        return True
    return False

def is_visible_right(grid, i, j, dp):
    if dp[i+1][j][1] != -1 and grid[i][j] > dp[i+1][j][1]:
        dp[i][j][1] = grid[i][j]
        return True
    
    ptr = i+1
    flag = True
    while ptr < len(grid):
        if grid[ptr][j] >= grid[i][j]:
            flag = False
            dp[i][j][1] = max(dp[i][j][1], grid[ptr][j])
        ptr += 1
    
    if flag:
        dp[i][j][1] = grid[i][j]
        return True
    return False

def is_visible_up(grid, i, j, dp):
    if dp[i][j-1][2] != -1 and grid[i][j] > dp[i][j-1][2]:
        dp[i][j][2] = grid[i][j]
        return True
    
    ptr = j-1
    flag = True
    while ptr >= 0:
        if grid[i][ptr] >= grid[i][j]:
            flag = False
            dp[i][j][2] = max(dp[i][j][2], grid[i][ptr])
        ptr -= 1
    
    if flag:
        dp[i][j][2] = grid[i][j]
        return True
    return False

def is_visible_down(grid, i, j, dp):
    if dp[i][j+1][3] != -1 and grid[i][j] > dp[i][j+1][3]:
        dp[i][j][3] = grid[i][j]
        return True
    
    ptr = j+1
    flag = True
    while ptr < len(grid[i]):
        if grid[i][ptr] >= grid[i][j]:
            flag = False
            dp[i][j][3] = max(dp[i][j][3], grid[i][ptr])
        ptr += 1
    
    if flag:
        dp[i][j][3] = grid[i][j]
        return True
    return False

def is_visible(grid, i, j, dp):
    if is_visible_left(grid, i, j, dp):
        return True
    if is_visible_right(grid, i, j, dp):
        return True
    if is_visible_up(grid, i, j, dp):
        return True
    if is_visible_down(grid, i, j, dp):
        return True
    return False