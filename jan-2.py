'''
Leetle #2 2/6 1:00

⚠️⚠️⚠️⚠️⚠️⚠️
🟩🟩🟩🟩🟩🟩
'''
def solve(nums):
  for i in nums:
    if nums.count(i) == 1:
      return i
