import queue
import math

def solution(progresses, speeds):
    answer = []
    day = queue.Queue()
    for pro, spd in zip(progresses, speeds):
        time = math.ceil(((100-pro) / spd))
        day.put(time) # 처리하는 기간
        print(time)
    cnt = 1
    idx_now = day.get()
    while # day가 빌 때:
        idx_next = day.get()
        if idx_now <= idx_next:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            idx_now = idx_next
    return answer
