### Merge Sort
```python
class Solution:
    def merge(self, a, b, l, r):
        mid = (l + r)//2
        i = l
        j = mid + 1
        k = l#merge pointer
        ans = 0
        while i <=mid and j <= r:
            if a[i] > a[j]:
                b[k] = a[j]
                k += 1
                j += 1
                ans += mid - i + 1#other numbers in the left side are all bigger than a[j]
            else:
                b[k]=a[i]
                k += 1
                i += 1
        while i <= mid:#there are numbers in left side
            b[k] += a[i]
            k += 1
            i += 1
        while j <= r:#there are numbers in right side
            b[k] += a[j]
            k += 1
            j += 1
        a[l:r+1] = b[l:r+1]#copy to original array
        return ans




    def merge_sort(self, a, b, l, r):
        if(l >= r):
            return 0
        mid = (l + r) // 2#floor
        ans_l = self.merge_sort(a, b, l, mid)#sort left
        ans_r = self.merge_sort(a, b, mid+1, r)#sort right
        return ans_l+ans_r+self.merge(a, b, l, r)#merge left and right

    def InversePairs(self , data: List[int]) -> int:
        # write code here
        return self.merge_sort(data, [0]*len(data), 0, len(data)-1)%1000000007