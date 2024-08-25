def cal_median(nums):
  nums.sort()
  n = len(nums)
  m = n // 2
  if n % 2 == 0:
    return (nums[m - 1] + nums[m]) / 2
  else:
    return nums[m]


l=list(map(int,input("Enter the number in list").split()))
res=cal_median(l)
print(res)

