def is_prime(x):
    
    prime = True
    
    if x == 1 or x == 0:
        prime = False
    
    else:
        for i in range (2, x):
            if x % i == 0:
                prime = False

    return prime

x = int(input("How many numbers should the program check?: "))
primesList = []

for i in range(x):
    if is_prime(i):
        primesList.append(i)

print(primesList)