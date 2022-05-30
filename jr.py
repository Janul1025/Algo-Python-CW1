step_count = 0
paths_in_line = 1
paths_in_next_line = 0
grid = []
r_list = []
c_list = []
visted = []
cell_list = []
dir_list = []
steps_list = []

import time

def input_rows(n):
    for i in range(n):
        grid.append(input().strip())
    return


def find_location(symbol):
    global grid, m, n
    for i in range(m):
        for j in range(n):
            if grid[i][j] == symbol:
                return i, j


def find_shortest_path():
    global step_count, r_list, c_list, paths_in_line, paths_in_next_line

    while len(r_list) > 0:
        cr = r_list[0]
        cc = c_list[0]
        if er == cr and ec == cc:
            break
        paths_in_line -= 1
        r_list, c_list = r_list[1:], c_list[1:]

        next_cells(cr, cc)

        if paths_in_line == 0:
            paths_in_line = paths_in_next_line
            paths_in_next_line = 0
            # print(r_list)
            # print(c_list)
            step_count += 1
    return


def next_cells(r, c):
    global paths_in_next_line
    rf = [0, 1, 0, -1]
    cf = [-1, 0, 1, 0]
    for i in range(4):
        # print(i, "#", r, c, rf[i], cf[i])
        if rf[i] == 0:
            if cf[i] == 1:
                # print(1,r,c,r_list,c_list)
                for step in range(1, n):
                    # print(c+step ,grid[r][c+step])
                    if c + step >= n or grid[r][c + step] == '0' or grid[r][c + step - 1] == "F":
                        if not visted[r][c + step - 1]:
                            visted[r][c + step - 1] = True
                            paths_in_next_line += 1
                            r_list.append(r)
                            c_list.append(c + step - 1)
                            cell_list.append((r, c + step - 1))
                            dir_list.append((rf[i], cf[i]))
                            steps_list.append(step - 1)
                            # print(r, c+step-1, (rf[i], cf[i]),cell_list,dir_list)
                        break
            else:
                # print(2,r,c,r_list,c_list)
                for step in range(1, n):
                    # print(c-step, grid[r][c-step])
                    if c - step < 0 or grid[r][c - step] == '0' or grid[r][c - step + 1] == "F":
                        if not visted[r][c - step + 1]:
                            visted[r][c - step + 1] = True
                            paths_in_next_line += 1
                            r_list.append(r)
                            c_list.append(c - step + 1)
                            cell_list.append((r, c - step + 1))
                            dir_list.append((rf[i], cf[i]))

                            steps_list.append(step - 1)
                            # print(r, c-step+1, (rf[i], cf[i]),cell_list,dir_list)
                        break
        elif rf[i] == 1:
            # print(3,r,c,r_list,c_list)
            for step in range(1, m):
                # print(r + step, grid[r+step][c])
                if r + step >= m or grid[r + step][c] == '0' or grid[r + step - 1][c] == "F":
                    if not visted[r + step - 1][c]:
                        visted[r + step - 1][c] = True
                        paths_in_next_line += 1
                        r_list.append(r + step - 1)
                        c_list.append(c)
                        cell_list.append((r + step - 1, c))
                        dir_list.append((rf[i], cf[i]))
                        steps_list.append(step - 1)
                        # print(r+step-1, c, (rf[i], cf[i]),cell_list,dir_list)
                    break
        else:
            # print(4,r,c,r_list,c_list)
            for step in range(1, m):
                # print(r - step, grid[r-step][c])
                if r - step < 0 or grid[r - step][c] == '0' or grid[r - step + 1][c] == "F":
                    if not visted[r - step + 1][c]:
                        visted[r - step + 1][c] = True
                        paths_in_next_line += 1
                        r_list.append(r - step + 1)
                        c_list.append(c)
                        cell_list.append((r - step + 1, c))
                        dir_list.append((rf[i], cf[i]))
                        steps_list.append(step - 1)
                        # print(r-step+1, c, (rf[i], cf[i]),cell_list,dir_list)
                    break

            '''if ccr < 0 or ccc >= n or ccc < 0 or ccr >= m or grid[ccr][ccc] == "0" or visted[ccr][ccc]:
                continue
            else:
                # print(ccr, ccc,step_count,"!")
                visted[ccr][ccc] = True
                paths_in_next_line += 1
                r_list.append(ccr)
                c_list.append(ccc)
                cell_list.append((ccr, ccc))
                dir_list.append((rf[i], cf[i]))
                print(ccr,ccc,(rf[i], cf[i]))'''

    # print(r_list,c_list,cell_list,paths_in_next_line,paths_in_line)
    return

t1=time.time()


m = int(input("Map Height"))
input_rows(m)
n = len(grid[0])


# creating visited matrix
for i in range(m):
    visted.append([False] * n)

# to find starting location
sr, sc = find_location("S")

# to find finishing location
er, ec = find_location("F")
# print(er,ec)
r_list.append(sr)
c_list.append(sc)
visted[sr][sc] = True

find_shortest_path()

print("Distance :",step_count)
print()

# print(cell_list)
# print(dir_list,steps_list)

path = []
directions = []

while er != sr or ec != sc:
    path.append((ec + 1, er + 1))
    index = cell_list.index((er, ec))
    r_factor, c_factor = dir_list[index]
    step_factor = steps_list[index]
    if r_factor == 0:
        if c_factor == 1:
            directions.append("right")
        else:
            directions.append("left")
    elif r_factor == 1:
        directions.append("down")
    else:
        directions.append("up")

    er, ec = er - r_factor * step_factor, ec - c_factor * step_factor
    # print(path,directions,er,ec)

# print(path)
# print(directions)

l = len(directions)
print("Start at", (sc + 1, sr + 1))
for i in range(l - 1, 0, -1):
    print("Move", directions[i], "to", path[i])
print("Move", directions[0], "to", path[0])
print("Done!")

t2=time.time()
# t=t2-t1
print()
print("Time Taken =",t2 -t1,"seconds")