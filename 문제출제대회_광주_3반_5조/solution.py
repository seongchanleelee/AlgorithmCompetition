T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    y, x = 0, 0
    ans = 0
    for i in range(1, 4): # 1,2,3
        q = []
        q.append([y, x, 0])
        visit = [[0] * N for _ in range(N)]
        visit[y][x] = 1
        while q:
            q.sort(key=lambda x:x[2]) # [0,0,2] [1,0,1]
            ny, nx, cnt = q.pop(0)
            directy = [0, 1, 0, -1]
            directx = [1, 0, -1, 0]
            if arr[ny][nx] == i:
                ans += cnt
                y = ny
                x = nx
                break
            for j in range(4):
                dy = ny + directy[j]
                dx = nx + directx[j]
                if 0 <= dy < N and 0 <= dx < N:
                    if visit[dy][dx] == 1:
                        continue
                    if arr[dy][dx] == -1:
                        continue
                    if arr[dy][dx] == 4:
                        visit[dy][dx] = 1
                        q.append([dy, dx, cnt+2])
                    else:
                        visit[dy][dx] = 1
                        q.append([dy, dx, cnt+1])

    q = []
    q.append([y, x, 0])
    visit = [[0] * N for _ in range(N)]
    visit[y][x] = 1
    while q:
        q.sort(key=lambda x: x[2])
        ny, nx, cnt = q.pop(0)
        directy = [0, 1, 0, -1]
        directx = [1, 0, -1, 0]
        if ny == 0 and nx == 0:
            ans += cnt
            break
        for j in range(4):
            dy = ny + directy[j]
            dx = nx + directx[j]
            if 0 <= dy < N and 0 <= dx < N:
                if visit[dy][dx] == 1:
                    continue
                if arr[dy][dx] == -1:
                    continue
                if arr[dy][dx] == 4:
                    visit[dy][dx] = 1
                    q.append([dy, dx, cnt + 2])
                else:
                    visit[dy][dx] = 1
                    q.append([dy, dx, cnt + 1])
    print(f'#{tc} {ans}')
