'''
Leetle #1 4/6 3:43

🟥🟥🟥🟥🟥🟥
🟥🟩🟩🟩🟩🟥
🟩🟩🟩🟩🟩🟩
'''

def solve(n):
  sol = []
  for i in range (1, n+1):
    add = ""
    if i % 3 == 0:
      add += "Fizz"
    if i % 5 == 0:
      add += "Buzz"
    sol.append(add or i)
  return sol
