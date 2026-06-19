from collections import deque
# append
dq = deque([1,2,3])
print(dq)
dq.append(4)
print(dq)

# appendleft
dq = deque([1,2,3])
dq.appendleft(0)
print(dq)
# pop
dq.pop()
print(dq)
# popleft
dq.popleft()
print(dq)

# rotate 
dq = deque([1,2,3,4])
dq.rotate()
print(dq)
# rotateleft
dq.rotate(-1)
print(dq)

# Problem
queue = deque([])
queue.append('A')
print(queue)
queue.append('B')
print(queue)
queue.append('C')
print(queue)
queue.popleft()
print(queue)