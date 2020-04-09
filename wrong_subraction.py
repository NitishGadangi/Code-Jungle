#httpscodeforces.comproblemsetproblem977A
#09 April 2020

temp=input()
temp=temp.split(" ")
n=temp[0]
k=int(temp[1])
final=int(n)
for i in range(k):
	if len(n)>1 and (n[len(n)-1] == '0'):
		final=final/10
	else:
		final=final-1
	n=str(int(final))
print(int(final))
		