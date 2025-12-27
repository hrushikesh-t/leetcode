class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # list = [-3,6,0,3],target 0
        #creating a dictionary that can store numbers as index and its index as the values({-3:0,6:2,0:2,3:3}) 
        check = {}
        for i,num in enumerate(nums):
            #finding the complement i.e., 0-(-3) [for first number in the list]
            complement =  target - num
            #checking if complement exist in check dictionary
            if complement in check :
                return (check[complement],i)
            #if the value doesnt exist in the dictionary add the current to check dictionary
            check[num] = i
## Time Complexity for this is o(n) as we are using loooping only once
