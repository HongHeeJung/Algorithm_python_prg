# 23.8점

def solution(scoville, K):
    answer = 0
    scoville.sort()
    for num in scoville:
        if num < K:
            while True:
                scoville.sort()
                mix = scoville[0] + scoville[1]*2
                del scoville[0]
                del scoville[0]
                answer += 1
                if mix < K:
                    scoville.append(mix)
                else:
                    break
    return answer
