# 二维数组建立需要如下，不要搞其他的建立法子，有些只是搞了若干个指针指向同一个数组，是有bug的
# 详见： https://www.cnblogs.com/PyLearn/p/7795552.html
# test = [[0 for i in range(m)] for j in range(n)]
def robot(grid, largest_row_index, largest_col_index, row_index, col_index):
    if grid is None or len(grid) == 0:
        return None
    pth = list()
    path(grid, largest_row_index, largest_col_index, row_index, col_index, pth)
    print(pth)


def path_wrong(grid, largest_row_index, largest_col_index, row_index, col_index, pth):
    if row_index == largest_row_index and col_index == largest_col_index:
        pth.append((row_index, col_index))
        return True

    # 这些判断条件是超前的！ 是错误的
    # out_of_right = (row_index + 1 > largest_row_index)
    # out_of_bottom = (col_index + 1 > largest_col_index)
    # right_limit = (not out_of_right) and (grid[row_index + 1][col_index] == 1)
    # bottom_limit = (not out_of_bottom) and (grid[row_index][col_index + 1] == 1)

    out_of_right = (row_index > largest_row_index)
    out_of_bottom = (col_index > largest_col_index)
    out_of_right_limit = (not out_of_right) and (grid[row_index ][col_index] == 1)
    out_of_bottom_limit = (not out_of_bottom) and (grid[row_index][col_index] == 1)

    if (out_of_right or out_of_bottom) or (out_of_right_limit or out_of_bottom_limit):
        return False

    else:
        pth.append((row_index, col_index))
        if path(grid, largest_row_index, largest_col_index, row_index + 1, col_index, pth):
            return True
        if path(grid, largest_row_index, largest_col_index, row_index, col_index + 1, pth):
            return True
        return False


def path(grid, largest_row_index, largest_col_index, row_index, col_index, pth):
    if row_index == largest_row_index and col_index == largest_col_index:
        pth.append((row_index, col_index))
        return True

    # 这些判断条件是超前的！ 是错误的
    # out_of_right = (row_index + 1 > largest_row_index)
    # out_of_bottom = (col_index + 1 > largest_col_index)
    # right_limit = (not out_of_right) and (grid[row_index + 1][col_index] == 1)
    # bottom_limit = (not out_of_bottom) and (grid[row_index][col_index + 1] == 1)

    out_of_right = (row_index > largest_row_index)
    out_of_bottom = (col_index > largest_col_index)
    out_of_right_limit = (not out_of_right) and (grid[row_index ][col_index] == 1)
    out_of_bottom_limit = (not out_of_bottom) and (grid[row_index][col_index] == 1)

    if (out_of_right or out_of_bottom) or (out_of_right_limit or out_of_bottom_limit):
        return False

    else:
        pth.append((row_index, col_index))
        if path(grid, largest_row_index, largest_col_index, row_index + 1, col_index, pth):
            return True

        # else if 要慎用
        if path(grid, largest_row_index, largest_col_index, row_index, col_index + 1, pth):
            return True

        # 以下这句必须要有。否则那些无效的连接会一直待在哪里。你可以试试看把他注释掉，就会有bug出现
        pth.pop()
        return False

grids = [[0 for i in range(5)] for j in range(6)]
grids[3][2]=1
grids[4][2]=1
grids[4][3]=1
grids[2][2]=1
grids[1][2]=1
robot(grids, 4, 5, 0, 0)
