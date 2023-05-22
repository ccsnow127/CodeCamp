### Dynamic programming
```python
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        #start from 0, fib(0)=0, fib(1)=1, fib(2)=fib(0)+fib(1)=1
        if n <= 1:
            return n
        res = 0
        a = 0
        b = 1
        for i in range(2, n+1):
            res = (a+b)
            a = b
            b = res
        return res
```