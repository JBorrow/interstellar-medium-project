import numpy as np

class NFW:
    # use gen(n) to generate n random.
    def __init__(self, R, c):
        self.R = R
        self.c = c

        self.norm = R**2 * (np.log(c+1) - c/(c+1))
        self.p = np.vectorize(self.__p)


    def __p(self, r):
        # For single generations, use p for multi
        if r < (self.c*self.R):
            return r/(1+r/self.R)**2
        else:
            return 0

    
    def __gen(self):
        y = 1e100
        x = 0

        while y >= self.__p(x):  # rejection method
            x = self.c*self.R * np.random.rand()
            y = (self.R/4 + 0.001) * np.random.rand()

        return x


    def gen(self, n=1):
        op = np.empty(n)

        for i in range(n):
            op[i] = self.__gen()

        return op


class GasZ:
    # use gen(n) to generate n random.
    def __init__(self, Z):
        # Z the scale height
        self.Z = Z

        self.norm = 2*Z
        self.p = self.__p  # already works vector like
        self.gen = self.__gen  # already works vector like


    def __p(self, z):
        return 1/np.cosh(z/self.Z)**2

   
    def __gen(self, n=1):
        return self.Z*np.arctanh(2*np.random.rand(n) - 1)


class GasR:
    # use gen(n) to generate n random
    def __init__(self, R, max=10):
        # R the scale height; max is the factor of radius to stop calcing at (e.g. c above for NFW)
        self.R = R
        self.max = max

        self.norm = R**2
        self.p = np.vectorize(self.__p)


    def __p(self, r):
        if r < (self.R*self.max):
            return r*np.exp(-r/self.R)
        else:
            return 0.


    def __gen(self):
        y = 1e100
        x = 0

        while y >= self.__p(x):  # rejection method
            x = self.max*self.R * np.random.rand()
            y = (self.R + 0.001) * np.random.rand()

        return x


    def gen(self, n=1):
        op = np.empty(n)

        for i in range(n):
            op[i] = self.__gen()

        return op


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    mygas = GasZ(10)
    r = np.arange(-100, 100, 0.05)
    p = mygas.p(r)/mygas.norm
    rvs = mygas.gen(100000)

    plt.plot(r, p)
    plt.hist(rvs, bins=50, normed=True)
    plt.show()

