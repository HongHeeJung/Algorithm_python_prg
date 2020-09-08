import queue
import math

def solution(progresses, speeds):
    answer = []
    day = queue.Queue()
    for pro, spd in zip(progresses, speeds):
        day.put(math.ceil(((100-pro) / spd))) # 처리하기 위해 필요한 기간

    cnt = 1
    day.put(101) # 초과되지 않는 수
    idx_now = day.get()
    while day.empty() == False: # day가 빌 때
        idx_next = day.get()
        if idx_now >= idx_next:
            cnt += 1
        else:
            answer.append(cnt) # 배포
            cnt = 1
            idx_now = idx_next
    return answer
