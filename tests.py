import factorial_ns

for i in range(0, 20):
    tmp = factorial_ns.convert(i)
    print(i, "|", tmp)
    print(tmp, "|", factorial_ns.convert_to_dec(tmp))
    print("\n")
