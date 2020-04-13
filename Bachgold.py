#https://codeforces.com/problemset/problem/749/A
#13Apr2020

def primes(n): # simple Sieve of Eratosthenes 
   odds = range(3, n+1, 2)
   sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds],[]))
   return [2] + [p for p in odds if p not in sieve]

main=int(input())
list_of_primes=primes(main)
res=[]
if main in list_of_primes:
	res.append(str(main))
else:
	for prime in list_of_primes:
		temp=int(main/prime)
		main=main%prime
		for x in range(temp):
			res.append(str(prime))
		if main==0:
			break
print(len(res))
print(" ".join(res))