#https://codeforces.com/problemset/problem/749/A
#13Apr2020

main=int(input())
res=[]
if main%2==0:
	for x in range(int(main/2)):
		res.append("2")
else:
	for x in range(int(main/2)-1):
		res.append("2")
	res.append("3")
print(len(res))
print(" ".join(res))