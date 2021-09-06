from math import factorial as f
diagonal = lambda n, p: f(n+1)//f(p+1)//f(n-p)