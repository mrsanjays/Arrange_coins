class Solution:

    def arrangecoins(self,n):
        l,r,res=1,n,0
        while l<=r:
            mid=(l+r)//2
            coins=mid*(mid+1)/2
            if coins>n:
                r=mid-1
            else:
                l=mid+1
                res=max(res,mid)
        return res
"""
Arranging Coins
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.
"""
if __name__ == '__main__':
    n=int(input())
    print(Solution().arrangecoins(n))
