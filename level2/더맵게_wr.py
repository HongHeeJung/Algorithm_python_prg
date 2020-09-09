# 38.1점

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        scoville.sort()
        mix = scoville[0] + scoville[1]*2
        del scoville[0]
        del scoville[0]
        answer += 1
        if mix < K:
            scoville.append(mix)
        scoville.sort()
        check = 0
        for num in scoville:
            if num >= K:
                check += 1
            else:
                break
        if len(scoville) == check:
            return answer
        elif len(scoville) == 1 and (scovile[0] < K):
            return -1
