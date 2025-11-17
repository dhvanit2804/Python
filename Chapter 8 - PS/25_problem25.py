'Write a function that returns all prime numbers between two numbers.'

def prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:  # Prime numbers are greater than 1
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

# Example usage:
print(prime_numbers(10, 50))
