#https://codeforces.com/problemset/problem/1220/A
#10Apr2020
main1=int(input())
main2=input()
zeros=int(main2.count('z'))
ones=int(main2.count('n'))
res=""
for x in range(0,ones):
	res=res+"1 "
for x in range(0,zeros):
	res=res+"0 "
print(res.strip())	