from typing import List
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
    
s = Solution()
data = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
print(s.InversePairs(data))
