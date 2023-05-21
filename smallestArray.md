# Rearrange the strings in list to form the smallest

reload the sort function
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

