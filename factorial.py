def factorial(n: int):
    total: int = 1
    for i in range(2, n + 1):
        total = total * i
    return total


if __name__ == "__main__":
    for i in range(10):
        print(f"Factorial of n {i} is", factorial(i))
