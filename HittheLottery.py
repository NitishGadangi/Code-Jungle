#https://codeforces.com/problemset/problem/996/A
#10Apr2020
main=int(input())
count=0
if main!=0:
	q=int(main/100)
	r=int(main%100)
	count=count+q
	main=r		
if main!=0:	
	q=int(main/20)
	r=int(main%20)
	count=count+q
	main=r
if main!=0:	
	q=int(main/10)
	r=int(main%10)
	count=count+q
	main=r
if main!=0:
	q=int(main/5)
	r=int(main%5)
	count=count+q
	main=r	
if main!=0:	
	q=int(main/1)
	r=int(main%1)
	count=count+q
	main=r
print(count)