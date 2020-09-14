# 29.0점

# key 90도씩 회전
def rotate(key):
    n = len(key)
    new_key = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            new_key[c][n-1-r] = key[r][c]
    return new_key

# key를 (x,y)만큼 이동시키면서 대입
def move(wide, key, N_key, x, y):
    for i in range(N_key):
        for j in range(N_key):
            wide[x+i][y+j] = key[i][j]
    return wide
    
# lock이 모두 1인지 확인
def check(wide, N_lock, N_key):
    for i in range (N_lock):
        for j in range(N_lock):
            if wide[N_key - 1 + i][N_key - 1 + j] == 1:
                continue
            else:
                return False
    return True

def solution(key, lock):
    answer = True
    N_lock = len(lock[0])
    N_key = len(lock[0])
    N_wide = N_lock + 2 * N_key - 2
    wide = [[0]*N_wide for _ in range(N_wide)]
    for i in range (N_lock):
        for j in range(N_lock):
            wide[N_key - 1 + i][N_key - 1 + j] = lock[i][j]
            
    for _ in range(4):
        for y in range(N_wide - N_key + 1):
            for x in range(N_wide - N_key + 1):
                new_wide = move(wide, key, N_key, x, y)
                if check(new_wide, N_lock, N_key) == True:
                    answer = True
                    return answer
                else:
                    continue
                
        # 이동했을 때 없으면 90도 회전
        key = rotate(key)
        
    answer = False
    return answer
