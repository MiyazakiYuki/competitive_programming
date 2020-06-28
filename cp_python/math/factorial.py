## factorial library
## verify: AGC025B, ABC172E
## ref: fumiphys
## (not)ref: https://algo-logic.info/combination/
## (not)ref: https://qiita.com/derodero24/items/91b6468e66923a87f39f
## (not)ref: https://qiita.com/ofutonfuton/items/92b1a6f4a7775f00b6ae

## begin library factorial
## usage: fac = Factorial()
## usage: nCr = fac.comb(n, r)
## usage: nPr = fac.perm(n, r)
class Factorial:

    def __init__(self, N):
        self.fact = [0] * (N+1)
        self.fact_inv = [0] * (N+1)
        self.calc_factorial(N)
        self.calc_inv_factorial(N)

    def calc_factorial(self, N):
        self.fact[0] = 1
        for i in range(N):
            self.fact[i+1] = self.fact[i] * (i+1) % MOD

    def calc_inv_factorial(self, N):
        self.fact_inv[N] = pow(self.fact[N], MOD-2, MOD)
        for i in range(N, 0, -1):
            self.fact_inv[i-1] = self.fact_inv[i] * i % MOD

    def comb(self, n, r):
        if (n < 0 or r < 0 or n < r): return 0
        res = self.fact[n]
        res = res * self.fact_inv[r] % MOD
        res = res * self.fact_inv[n-r] % MOD
        return res

    def perm(self, n, r):
        if (n < 0 or r < 0 or n < r): return 0
        res = self.fact[n]
        res = res * self.fact_inv[n-r] % MOD
        return res

## end library factorial

MOD = int(1e9+7)

fac = Factorial(5)
print(fac.fact)
print(fac.fact_inv)
print(fac.comb(5, 0))
print(fac.comb(5, 1))
print(fac.comb(5, 2))
print(fac.comb(5, 3))
print(fac.comb(5, 4))
print(fac.comb(5, 5))
print(fac.perm(5, 0))
print(fac.perm(5, 1))
print(fac.perm(5, 2))
print(fac.perm(5, 3))
print(fac.perm(5, 4))
print(fac.perm(5, 5))