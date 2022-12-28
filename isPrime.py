def prime_checker(num):
    isPrime = True
    for i in range (2,num):
        result = num % i
        if(result == 0):
            isPrime = False
    
    return isPrime


number = int(input("Check this number: "))
isP = prime_checker(number)
print(f"{number} is prime? {isP}")
