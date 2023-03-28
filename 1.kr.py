from collections import deque

chet = deque()
nechet = deque()

l = list(map(int, input().split()))
for i in l:
    if i % 2 == 1:
        nechet.append(i)

    if i % 2 == 0:
        chet.append(i)

res = []

for i in range(min(len(chet), len(nechet))):
    res.append(chet.pop())
    res.append(nechet.pop())
if len(chet) > len(nechet):
    for i in range(len(chet)):
        res.append(chet.pop())

if len(chet) < len(nechet):
    for i in range(len(nechet)):
        res.append(nechet.pop())

print(*res, end = '\n')