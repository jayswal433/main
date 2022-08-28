N = int(input("Enter the first positive integer: "))
M = int(input("Enter the second positive integer: "))
n = N
m = M

Nsum = 0
while N != 0:

    a = N % 10
    Nsum = Nsum + a
    N = N // 10
Msum = 0
while M != 0:

    b = M %10
    Msum = Msum + b
    M = M // 10

if Nsum > Msum:
    print(n)
elif Msum > Nsum:
    print(m)
elif Nsum == Msum:
    print("-1")
else:
    pass




