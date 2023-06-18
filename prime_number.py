def is_prime_number(n: int):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(100):
        print(f"{i} is {'' if is_prime_number(i) else 'not '}prime number")
