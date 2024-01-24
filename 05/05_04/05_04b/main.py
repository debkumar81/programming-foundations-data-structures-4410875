from collections import deque
def create_binary_nums(n):
  if n<=0:
    return
  queue=deque()
  queue.append(1)
  for _ in range(n):
    binary=queue.popleft()
    print(binary)
    queue.append(binary*10)
    queue.append(binary*10+1)
create_binary_nums(2)
print( )
create_binary_nums(4)
print( )
create_binary_nums(-1)
print( )
create_binary_nums(5)
print()
