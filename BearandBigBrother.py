#https://codeforces.com/problemset/problem/791/A
#09 April 2020
main=input()
main=main.split(" ")
a=int(main[0])
b=int(main[1])
count=0
while a<=b:
	count=count+1
	a=a*3
	b=b*2
print(count)