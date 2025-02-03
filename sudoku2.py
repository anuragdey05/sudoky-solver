def is_valid(grid, r, c, k):
    not_in_row = k not in grid[r]
    not_in_column = k not in [grid[i][c] for i in range(9)]
    not_in_box = k not in [grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
    return not_in_row and not_in_column and not_in_box


def solve(grid, r=0, c=0, count=0):
    if r == 9:
        return count + 1
    elif c == 9:
        return solve(grid, r+1, 0, count)
    elif grid[r][c] != 0:
        return solve(grid, r, c+1, count)
    else:
        for k in range(1, 10):
            if is_valid(grid, r, c, k):
                grid[r][c] = k
                count = solve(grid, r, c+1, count)
                if count > 1:
                    return count
                grid[r][c] = 0
        return count
    
grid = [
     [9,0,6,0,7,0,4,0,3],
     [0,0,0,4,0,0,2,0,0],
     [0,7,0,0,2,3,0,1,0],
     [5,0,0,0,0,0,1,0,0],
     [0,4,0,2,0,8,0,6,0],
     [0,0,3,0,0,0,0,0,5],
     [0,3,0,7,0,0,0,5,0],
     [0,0,7,0,0,5,0,0,0],
     [4,0,5,0,1,0,7,0,8],
 ]
solutions = solve(grid)
if(solutions > 1):
    print("Not Unique")
else:
    print("Unique")
