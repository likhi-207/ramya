from collections import deque

people=["Alice","Bob","charlie","David","Eve"]

leave_times=[4,2,5,6,3]

queue=deque(people)
leave_queue=deque(leave_times)
time=1

while len(queue)!=0:
    guy=queue.popleft()
    if leave_queue.popleft()>time:
        print(f"{guy} got the ticket:",time)
    else:
        print(f"{guy} left angrily:",time)
    time+=1
