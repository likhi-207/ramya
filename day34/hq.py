import heapq
priorQ=[]

heapq.heappush(priorQ,10)
print(priorQ)

heapq.heappush(priorQ,2)
heapq.heappush(priorQ,30)
heapq.heappush(priorQ,4)
heapq.heappush(priorQ,100)
print(priorQ)
heapq.heappop(priorQ)
print(priorQ)
heapq.heappop(priorQ)
heapq.heappop(priorQ)
heapq.heappop(priorQ)
print(priorQ)
print("front element:",priorQ[0])


