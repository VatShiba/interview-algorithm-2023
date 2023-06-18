def fibonacci(n: int):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    n1, n2 = 0, 1
    result: int = 0
    for _ in range(2, n + 1):
        result = n1 + n2
        n1 = n2
        n2 = result
    return result


def fibonacci_recursive(n: int):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


if __name__ == "__main__":
    print("Time complexity O(n): For-Loop")
    for i in range(10):
        print(f"Fibonacci of n {i} is", fibonacci(i))

    print("Time complexity O(2^n): Recursive")
    for i in range(10):
        print(f"Fibonacci of n {i} is", fibonacci_recursive(i))
