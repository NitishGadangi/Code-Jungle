#https://codeforces.com/problemset/problem/263/A
#11Apr2020
i1=input()
i2=input()
i3=input()
i4=input()
i5=input()
i,j=0,0
if '1' in i1:
	i=1
	j=i1.index('1')
elif '1' in i2:
	i=2
	j=i2.index('1')
elif '1' in i3:
	i=3
	j=i3.index('1')
elif '1' in i4:
	i=4
	j=i4.index('1')
elif '1' in i5:
	i=5
	j=i5.index('1')
j=j/2
res=abs(i-3)+abs(j-2)
print(int(res))