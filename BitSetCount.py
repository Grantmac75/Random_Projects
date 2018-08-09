# Count the number of bit values that are 1 in a number

# With Recursion
def countSetBits(n):

    if n==0:
        return 0
    else:
        return (n & 1) + countSetBits(n >> 1)

n = 20
print(countSetBits(n))
#print(4 >> 1)


# With While Loop
def countSetBits_while(n):

    count = 0
    while(n):
        count += n & 1
        n >>= 1
    return count


print(countSetBits_while(n))

#Print Binary Number in Python
print(bin(n))