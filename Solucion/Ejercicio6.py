def get_max(nums: str):
  nums = nums.split()
  max = int(nums[0])

  for index in range(1, len(nums)):
    num = int(nums[index])
    if num > max:
      max = num

  return max

def get_min(nums: str):
  nums = nums.split()
  min = int(nums[0])

  for index in range(1, len(nums)):
    num = int(nums[index])
    if num < min:
      min = num

  return min

def main():
  nums = input()
  print(get_max(nums), get_min(nums))

main()