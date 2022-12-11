def count_visible_left(grid, i, j):
    ans = 0
    for k in range(i-1, -1, -1):
        if grid[i][j] > grid[k][j]:
            ans += 1
        else:
            ans += 1
            break
    return ans

def count_visible_right(grid, i, j):
    ans = 0
    for k in range(i+1, len(grid)):
        if grid[i][j] > grid[k][j]:
            ans += 1
        else:
            ans += 1
            break
    return ans

def count_visible_up(grid, i, j):
    ans = 0
    for k in range(j-1, -1, -1):
        if grid[i][j] > grid[i][k]:
            ans += 1
        else:
            ans += 1
            break
    return ans

def count_visible_down(grid, i, j):
    ans = 0
    for k in range(j+1, len(grid[i])):
        if grid[i][j] > grid[i][k]:
            ans += 1
        else:
            ans += 1
            break
    return ans

def count_visible(grid, i, j):
    return count_visible_left(grid, i, j)   * \
        count_visible_right(grid, i, j)     * \
        count_visible_up(grid, i, j)        * \
        count_visible_down(grid, i, j)