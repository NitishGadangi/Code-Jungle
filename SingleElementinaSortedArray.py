#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/
#12May2020

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
        	return nums[0]
        i=0
        j=1
        while i<n-1:
        	if nums[i]!=nums[j]:
        		return nums[i]
        	i+=2
        	j+=2
        return nums[n-1]