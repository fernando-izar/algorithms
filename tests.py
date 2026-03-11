def test(n):
    return n


gen = [test(i) for i in range(5)]
print(gen)
