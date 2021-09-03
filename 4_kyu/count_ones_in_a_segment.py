import math
import numpy as np

def countOnes(n1, n2):

    n = [n1, n2]

    for index in range(len(n)):

        s, x = list(), list()
        sum1, sum2, sum3 = 0, 0, 0

        while n[1-index] > 0:
            s.append(n[1-index] % 2)
            n[1-index] = n[1-index] // 2

        s2 = np.array(s[::-1])

        for i in range(len(s2)-1):
            sum1 = 2*sum1 + 2**i
            x.append(sum1)

        x = np.array(x[::-1])

        for i in range(len(x)):
            sum2 += x[i] * s2[i]
            if (s2[::-1])[i] == 1:
                for j in range(i+1):
                    sum3 += 2**j * (s2[::-1])[j]

        n[1-index] = sum2 + sum3 + np.sum(s2)

    return(int(n[1] - n[0] + np.sum(s2)))