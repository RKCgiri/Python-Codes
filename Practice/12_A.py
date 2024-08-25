def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return  False
    return True
n=int(input("Enter the range"))
for i in range(2,n):
    j=i+2
    if(isPrime(i) and isPrime(j)):
        print(f"The Twines primes are {i} and {j}")