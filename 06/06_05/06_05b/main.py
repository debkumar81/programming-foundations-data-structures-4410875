from collections import deque
def check_parentheses(chars):
  stack=deque()
  for char in chars:
    if char=='(':
      stack.append(char)
    elif char==')':
      if len(stack)==0:
        return False
      stack.pop()
  return len(stack)==0
print(check_parentheses("()"))
print(check_parentheses("(hi there)"))
print(check_parentheses("(hell)o"))
print(check_parentheses("((linkedin)) learning"))

print(check_parentheses("(hi(there"))
print(check_parentheses("()ok)"))
print(check_parentheses("((increment)"))
print(check_parentheses(")linkedin()"))
