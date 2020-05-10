#https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/
#09May2020

# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         if num is  0 or num is 1 or num is 4:
#         	return True
#         left = 1
#         right = int(num/2)

#         while left<right:
#         	mid = int((left+right)/2)
#         	if mid*mid is num:
#         		return True
#         	if mid*mid < num:
#         		left=mid+1
#         	if mid*mid > num:
#         		right=mid-1
#         return False

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    	guess=num
    	while guess*guess>num:
    		guess=int((guess+int(num/guess))/2)
    	return guess*guess is num