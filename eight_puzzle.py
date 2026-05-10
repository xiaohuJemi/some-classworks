import heapq
from copy import deepcopy
def g(board):  #根据定义计算当前图的g(x)
    cnt = 0
    for di in range(3):
        for dj in range(3):
            v = board[di][dj]
            if v != 0:
                cnt += abs(di * 3 + dj + 1 - values[v])  #计算图中各点与目标位置步数差值
    return cnt
target = [[1, 2, 3], [8, 0, 4], [7, 6, 5]] #定义目标状态
s = [[1, 0, 3], [7, 2, 4], [6, 8, 5]] #定义初始状态
values = [0, 1, 2, 3, 6, 9, 8, 7, 4] #每个数的目标位置对应值
OPEN = [(g(s), s)] #定义OPEN表，用最小堆实现自动排序功能
CLOSE = []
h = 0
dr = [(0, 1), (1, 0), (0, -1), (-1, 0)] #定义操作算子，分别表示0向'右下左上'移动
while True:
    grid = heapq.heappop(OPEN)[1] #取出OPEN表中评价函数f(x)值最小的图
    CLOSE.append(grid) #并将其加入CLOSE表中
    if grid == target: #找到目标图时退出循环
        break
    h += 1 #改变深度函数h(x)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                x, y = i, j #找到grid中0的位置
                break
    for dx, dy in dr:
        new_grid = deepcopy(grid) #拷贝当前的状态图，便于操作算子的执行
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_grid[x][y], new_grid[nx][ny] = new_grid[nx][ny], new_grid[x][y] #执行操作算子
            if new_grid not in CLOSE:  #如果操作后的图没有在CLOSE表格中，加入OPEN表
                heapq.heappush(OPEN, (g(new_grid) + h, new_grid)) #将f(x) = g(x) + h(x)作为参数共同传入最小堆(OPEN表)
for i, g in enumerate(CLOSE): #遍历CLOSE表，打印搜索路径
    print(f'第{i}次移动:')
    for row in g:
        print(row)
print('得到目标状态，退出循环')

