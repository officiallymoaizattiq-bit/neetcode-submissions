class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[]
        prod.append(1)
        for i in range(1,len(nums)):
            prod.append(nums[i-1]*prod[i-1])
        rProd=[1]*len(nums)
        rProd[len(nums)-1]=1
        for i in range(len(nums)-2,-1,-1):
            rProd[i]=rProd[i+1]*nums[i+1]
        for i in range(len(nums)):
            prod[i] *= rProd[i]
        return prod
        


  
        