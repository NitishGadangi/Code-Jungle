#leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/
#13May2020

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
	    n=len(num)
	    if n==k:
	    	return "0"
	    ans=num
	    while k>0:
	    	i=0
	    	while i<len(ans)-1:
	    		if int(ans[i])>int(ans[i+1]):
	    			ans=ans[:i]+ans[i+1:]
	    			break
	    		i+=1
	    		if i == len(ans)-1:
	    			ans=ans[:i]
	    	k-=1
	    j=0
	    while j<len(ans):
	    	if ans[j] is not '0':
	    		return ans[j:]
	    	j+=1
	    return '0'

print(Solution.removeKdigits(self,"112",1))