class COM:
    def __init__(self, MAX=51000, MOD=pow(10,9)+7):
        self.MAX = MAX
        self.MOD = MOD
        self.fac,self.finv,self.inv = [0]*self.MAX,[0]*self.MAX,[0]*self.MAX
        self.fac[0] = self.fac[1] = 1
        self.finv[0] = self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, self.MAX):
            self.fac[i] = self.fac[i-1] * i % self.MOD
            self.inv[i] = self.MOD - self.inv[MOD%i] * (self.MOD//i) % self.MOD
            self.finv[i] = self.finv[i-1] * self.inv[i] % self.MOD
    def COM(self, n, k):
        if(n < k): return 0
        if(n < 0 or k < 0): return 0
        return self.fac[n] * (self.finv[k] * self.finv[n-k] % self.MOD) % self.MOD