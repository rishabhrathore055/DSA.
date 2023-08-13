# Generate all the binary strings with n bits
def bitString(n):
    if n == 0:return []
    if n == 1:return ['0', '1']
    return [digit + bitstring for digit in bitString(1) for bitstring in bitString(n-1)]
print(bitString(4)) 