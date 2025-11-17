'Create a set of prime numbers from 1–100.'

prime_set = set()

for num in range(2, 101):
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_set.add(num)

print("Prime numbers from 1 to 100:")
print(prime_set)
