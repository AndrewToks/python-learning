#Write a recursive function to compute factorial of a given number

def recursiveFunction(n):
    if (n == 0):
        return 1
    else:
        return recursiveFunction(n-1) * n
print(recursiveFunction(3))
