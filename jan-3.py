'''
Leetle #3 2/6 1:06
[5 lines]

⚠️⚠️⚠️⚠️⚠️⚠️
🟩🟩🟩🟩🟩🟩
leetle.app
'''

def solve(nums):
  for num in nums:
    amount = nums.count(num)
    if amount > len(nums)/2:
      return num
