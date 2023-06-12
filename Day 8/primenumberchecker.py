def prime_checker(n):
    prime = True
    count = n - 1
    while count > 1:
        if n % count == 0:
            prime = False
            break
        
        count-= 1

    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(n)