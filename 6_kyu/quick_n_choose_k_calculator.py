from scipy.special import comb
choose = lambda n, k: comb(n, k, exact=True)