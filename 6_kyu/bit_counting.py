def count_bits(n):
    return sum(1 for i in bin(n) if i == '1')