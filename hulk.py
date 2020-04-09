#https://codeforces.com/problemset/problem/705/A
#09 April 2020

main=input()
main=int(main)
res=""
for i in range(1,main+1):
	if i%2==0:
		res=res+" I love"
	else:
		if i!=1:
			res=res+" "
		res=res+"I hate"
	if i==main:
		res=res+" it"
	else:
		res=res+" that"
print(res)