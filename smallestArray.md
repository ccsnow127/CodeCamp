# Rearrange the strings in list to form the smallest

### reload the sort function
```python
import functools
class Solution:
    def PrintMinNumber(self , numbers: List[int]) -> str:
        # write code here
        if not numbers:
            return ""
        #transform integer to string
        nums = list(map(str, numbers))
        #compare
        cmp = lambda a, b: 1 if a + b > b + a else -1
        nums.sort(key = functools.cmp_to_key(cmp))
        return "".join(nums)
```
### bubble sort
```python
class Solution:
    def PrintMinNumber(self , numbers: List[int]) -> str:
        # write code here
        # empty array
        if not numbers:
            return ""
        # trun integer into string
        nums = list(map(str, numbers))
        #bubble sort
        for i in range(len(nums)-1):
            for j in range(len(nums) - i - 1):
                s1 = nums[j] + nums[j+1]
                s2 = nums[j+1] + nums[j]
                if s1 > s2:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        return "".join(nums)
```
