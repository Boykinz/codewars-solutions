from scipy.special import zeta, zetac

def doubles(k, n):
    return sum((zetac(2*i) - zeta(2*i, 2+n))/i for i in range(1, k+1))