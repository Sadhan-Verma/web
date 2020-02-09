def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        print(n, "is divisible by 2")
        return False
    if n < 2:
        return False
    prime = True
    m = n // 2 + 1
    for x in range(3, m, 2):
        if n % x == 0:
            print(n, "is divisible by", x)
            prime = False
            return False
    return prime

while True:
    number = int(input("Enter a number (0 to exit): "))
    if number == 0:
        break
    primetest = isprime(number)
    if primetest is True:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
