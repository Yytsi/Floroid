# This is a module containing functions for the language Floroid.
# Some code taken from the internet and the rest written by me.
# Not by any means meant to be readable.

from math import*

# Prime functions
def isPrime(n):
    """Returns True if n is prime."""

    if n == 2:return True
    if n == 3:return True
    if n % 2 == 0:return False
    if n % 3 == 0:return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True
def getPrime(n):
    # Generate a list enough large.
    # Best possible values for those ranges.
    # Tested with mathematica.
    size = 0

    if n <= 100: size = 547
    elif n <= 1000: size = 7927
    elif n <= 10000: size = 104743
    elif n <= 100000: size = 1299721
    elif n <= 1000000: size = 15485867
    elif n <= 10000000: size = 179424691
    elif n <= 100000000: size = 2038074751
    elif n <= 1000000000: size = 22801763513

    return sieveOfAtkin(size)[n]
def getPrimeIndex(prime):
    if not isPrime(prime): return False # Discard if it's not a prime.
    return sieveOfAtkin(prime).index(prime) # Generate a list of primes up to (<prime> + 1) and return the index of <prime>.
def sieveOfAtkin(end):
    end += 1
    """sieveOfAtkin(end): return a list of all the prime numbers <= end
    using the Sieve of Atkin."""
    # Code by Steve Krenzel, <Sgk284@gmail.com>, improved
    # Code: https://web.archive.org/web/20080324064651/http://krenzel.info/?p=83
    # Info: http://en.wikipedia.org/wiki/Sieve_of_Atkin
    assert end > 0
    lng = ((end-1) // 2)
    sieve = [False] * (lng + 1)

    x_max, x2, xd = int(sqrt((end-1)/4.0)), 0, 4
    for xd in range(4, 8*x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, x2, xd = int(sqrt((end-1) / 3.0)), 0, 3
    for xd in range(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not(n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, y_min, x2, xd = int((2 + sqrt(4-8*(1-end)))/4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end: y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x*x + x) << 1) - 1, (((x-1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d

    primes = [2, 3]
    if end <= 3:
        return primes[:max(0,end-2)]

    for n in range(5 >> 1, (int(sqrt(end))+1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in range(aux, end, 2 * aux):
                sieve[k >> 1] = False

    s  = int(sqrt(end)) + 1
    if s  % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, end, 2) if sieve[i >> 1]])

    return primes

def fibonacci(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

def int2base(x,b,alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    if isinstance(x,complex):
        return (int2base(x.real,b,alphabet) , int2base(x.imag,b,alphabet))
    if x<=0:
        if x==0:return alphabet[0]
        else:return  '-' + int2base(-x,b,alphabet)
    rets=''
    while x>0:
        x,idx = divmod(x,b)
        rets = alphabet[idx] + rets
    return rets
def lexicographic_index(p):
    """Returns the index of an permutation."""
    result = 0
    for j in range(len(p)):
        k = sum(1 for i in p[j + 1:] if i < p[j])
        result += k * factorial(len(p) - j - 1)
    return result
def getPermutationOnIndex(sequence, index):
    """Generates a permutation at index <index>."""
    S = list(sequence)
    permutation = []
    while S != []:
        f = factorial(len(S) - 1)
        i = int(floor(index / f))
        x = S[i]
        index %= f
        permutation.append(x)
        del S[i]
    return tuple(permutation)

def toASCIICodes(iterable): return [ord(char) for char in list(iterable)]
def deleteAt(lst, index): return lst[:index] + lst[index + 1:]
def first(iterable): return list(iterable)[0]
def last(iterable): return list(iterable)[::-1][0]
def highest(iterable): return max(list(iterable))
def lowest(iterable): return min(list(iterable))

def lcm(a,b): return abs(a * b) / fractions.gcd(a,b) if a and b else 0
def lcmm(args): return functools.reduce(lcm, list(args))
def gcdm(args): return functools.reduce(fractions.gcd, list(args))
